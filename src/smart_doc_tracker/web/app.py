"""FastAPI composition root for the loopback-only web dashboard."""

import argparse
import json
import os
import re
import tempfile
from collections.abc import AsyncIterator, Callable, Iterator, Sequence
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Annotated, Any

from fastapi import (
    Depends,
    FastAPI,
    File,
    Form,
    HTTPException,
    Query,
    Request,
    UploadFile,
)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ..core.ocr import SUPPORTED_IMAGE_EXTENSIONS, TesseractOCR
from ..core.parser import DocumentParser, LongDocumentParser
from ..core.pdf import LocalPDFTextExtractor
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    DocumentInsertResult,
    MongoDocumentRepository,
)
from ..db.vector_database import (
    ChromaDocumentVectorIndex,
    collection_name_for_embedding_model,
)
from ..infrastructure.ollama import OllamaClient, OllamaEmbeddingClient
from ..interfaces.document_repository import DocumentRepository
from ..pipeline import DocumentProcessingPipeline
from .jobs import ProgressReporter, UploadJobService, UploadProcessor
from .schemas import DocumentResponse, UploadJobResponse

RepositoryFactory = Callable[[], DocumentRepository]
_WEB_ROOT = Path(__file__).parent
_SUPPORTED_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS | {".pdf"}
_LANGUAGE_CODE = re.compile(r"^[A-Za-z][A-Za-z0-9_+-]{0,31}$")
_MAX_UPLOAD_BYTES = 25 * 1024 * 1024
_UPLOAD_CHUNK_BYTES = 1024 * 1024


@dataclass(frozen=True, slots=True)
class WebDependencies:
    """Explicit local dependencies used by the FastAPI adapter."""

    repository_factory: RepositoryFactory
    upload_processor: UploadProcessor
    today_provider: Callable[[], date] = date.today


def default_web_dependencies() -> WebDependencies:
    """Compose the production dashboard from loopback-only adapters."""
    repository_factory = MongoDocumentRepository.connect

    def process_upload(
        path: Path,
        language: str,
        progress_reporter: ProgressReporter,
    ) -> DocumentInsertResult:
        """Process and store one upload through local production adapters."""
        generator = OllamaClient()
        embedding_model = "embeddinggemma"
        result = DocumentProcessingPipeline(
            ocr=TesseractOCR(),
            parser=DocumentParser(generator),
            pdf_extractor=LocalPDFTextExtractor(),
            long_document_parser=LongDocumentParser(generator),
            repository_factory=repository_factory,
            vector_index=ChromaDocumentVectorIndex(
                embedding_generator=OllamaEmbeddingClient(model=embedding_model),
                collection_name=collection_name_for_embedding_model(embedding_model),
            ),
            language=language,
            progress_reporter=progress_reporter,
        ).process(path, structured=True, store=True)
        if result.insert_result is None:
            raise RuntimeError("Stored processing returned no insertion result")
        return result.insert_result

    return WebDependencies(repository_factory, process_upload)


def create_app(dependencies: WebDependencies | None = None) -> FastAPI:
    """Create a testable local dashboard with injected application services."""
    resolved = dependencies or default_web_dependencies()
    jobs = UploadJobService(resolved.upload_processor)

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        """Close the bounded worker after all accepted uploads finish."""
        yield
        jobs.close()

    app = FastAPI(
        title="Smart Doc Tracker",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.state.upload_jobs = jobs
    templates = Jinja2Templates(directory=str(_WEB_ROOT / "templates"))
    app.mount(
        "/static",
        StaticFiles(directory=str(_WEB_ROOT / "static")),
        name="static",
    )

    def repository() -> Iterator[DocumentRepository]:
        """Open and close one local repository for a request."""
        try:
            with resolved.repository_factory() as opened_repository:
                yield opened_repository
        except (DatabaseConfigurationError, DatabaseError) as exc:
            raise HTTPException(
                status_code=503,
                detail="The local document database is unavailable.",
            ) from exc

    Repository = Annotated[DocumentRepository, Depends(repository)]

    @app.get("/", response_class=HTMLResponse, include_in_schema=False)
    def dashboard(request: Request) -> HTMLResponse:
        """Render the local single-page document dashboard."""
        return templates.TemplateResponse(
            request=request,
            name="dashboard.html",
            context={"alert_days": 30, "max_upload_mb": 25},
        )

    @app.get("/api/documents", response_model=list[DocumentResponse])
    def list_documents(
        repository: Repository,
        field_key: Annotated[str | None, Query(max_length=200)] = None,
        field_value: Annotated[str | None, Query(max_length=10_000)] = None,
        alert_days: Annotated[int, Query(ge=0, le=3_650)] = 30,
    ) -> list[DocumentResponse]:
        """List documents or exactly match one validated dynamic JSON path."""
        if (field_key is None) != (field_value is None):
            raise HTTPException(
                status_code=422,
                detail="field_key and field_value must be provided together.",
            )
        try:
            records = (
                repository.search_by_dynamic_field(
                    field_key,
                    _parse_query_value(field_value),
                )
                if field_key is not None and field_value is not None
                else repository.get_all_documents()
            )
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        today = resolved.today_provider()
        return [
            DocumentResponse.from_record(
                record,
                today=today,
                alert_days=alert_days,
            )
            for record in records
        ]

    @app.get("/api/documents/{document_id}", response_model=DocumentResponse)
    def get_document(
        document_id: str,
        repository: Repository,
        alert_days: Annotated[int, Query(ge=0, le=3_650)] = 30,
    ) -> DocumentResponse:
        """Return one locally stored document."""
        record = repository.get_document_by_id(document_id)
        if record is None:
            raise HTTPException(status_code=404, detail="Document not found.")
        return DocumentResponse.from_record(
            record,
            today=resolved.today_provider(),
            alert_days=alert_days,
        )

    @app.post(
        "/api/uploads",
        response_model=UploadJobResponse,
        status_code=202,
    )
    async def upload_document(
        file: Annotated[UploadFile, File(description="A local image or PDF")],
        language: Annotated[str, Form(min_length=1, max_length=32)] = "eng",
    ) -> UploadJobResponse:
        """Validate, spool, and queue one document for local processing."""
        safe_name = Path(file.filename or "").name
        suffix = Path(safe_name).suffix.lower()
        if not safe_name or suffix not in _SUPPORTED_EXTENSIONS:
            raise HTTPException(status_code=415, detail="Unsupported document format.")
        if not _LANGUAGE_CODE.fullmatch(language):
            raise HTTPException(status_code=422, detail="Invalid OCR language code.")
        temporary_path: Path | None = None
        try:
            descriptor, raw_path = tempfile.mkstemp(
                prefix="smart-doc-upload-",
                suffix=suffix,
            )
            temporary_path = Path(raw_path)
            total = 0
            with os.fdopen(descriptor, "wb") as destination:
                while chunk := await file.read(_UPLOAD_CHUNK_BYTES):
                    total += len(chunk)
                    if total > _MAX_UPLOAD_BYTES:
                        raise HTTPException(
                            status_code=413,
                            detail="The upload exceeds the 25 MB limit.",
                        )
                    destination.write(chunk)
            if total == 0:
                raise HTTPException(status_code=422, detail="The upload is empty.")
            job = jobs.submit(
                temporary_path,
                file_name=safe_name,
                language=language,
            )
            temporary_path = None
            return UploadJobResponse.from_job(job)
        finally:
            await file.close()
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)

    @app.get("/api/jobs/{job_id}", response_model=UploadJobResponse)
    def get_upload_job(job_id: str) -> UploadJobResponse:
        """Return the current status of one process-local upload job."""
        job = jobs.get(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        return UploadJobResponse.from_job(job)

    return app


def _parse_query_value(value: str) -> Any:
    """Interpret JSON scalars and structures, falling back to a plain string."""
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def run(argv: Sequence[str] | None = None) -> None:
    """Run one local Uvicorn worker bound to loopback by default."""
    parser = argparse.ArgumentParser(description="Run the local document dashboard.")
    parser.add_argument("--host", default="127.0.0.1", choices=("127.0.0.1", "::1"))
    parser.add_argument("--port", type=int, default=8080)
    arguments = parser.parse_args(argv)
    if not 1 <= arguments.port <= 65_535:
        parser.error("--port must be between 1 and 65535")
    import uvicorn

    uvicorn.run(
        "smart_doc_tracker.web.app:create_app",
        factory=True,
        host=arguments.host,
        port=arguments.port,
        workers=1,
    )
