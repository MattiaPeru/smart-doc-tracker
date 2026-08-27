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
from starlette.responses import Response
from starlette.types import Scope

from ..core.file_hash import FileHashingError, calculate_file_sha256
from ..core.ocr import SUPPORTED_IMAGE_EXTENSIONS, TesseractOCR
from ..core.parser import DocumentParser, LongDocumentParser
from ..core.pdf import LocalPDFTextExtractor
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)
from ..db.vector_database import (
    ChromaDocumentVectorIndex,
    VectorDatabaseError,
    collection_name_for_embedding_model,
)
from ..infrastructure.ollama import OllamaClient, OllamaEmbeddingClient
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..models.document import DocumentData
from ..mutation_pipeline import CoordinatedMutationError, DocumentMutationPipeline
from ..pipeline import DocumentProcessingPipeline, DocumentProcessingResult
from .jobs import ProgressReporter, UploadJobService, UploadProcessor
from .pending import PendingDocumentService
from .schemas import (
    DocumentIndexedContentResponse,
    DocumentResponse,
    PendingDocumentResponse,
    UploadJobResponse,
)

RepositoryFactory = Callable[[], DocumentRepository]
_WEB_ROOT = Path(__file__).parent
_SUPPORTED_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS | {".pdf"}
_LANGUAGE_CODE = re.compile(r"^[A-Za-z][A-Za-z0-9_+-]{0,31}$")
_MAX_UPLOAD_BYTES = 25 * 1024 * 1024
_UPLOAD_CHUNK_BYTES = 1024 * 1024


class LocalStaticFiles(StaticFiles):
    """Serve local dashboard assets without retaining stale browser copies."""

    async def get_response(self, path: str, scope: Scope) -> Response:
        """Return one static asset with browser persistence disabled."""
        response = await super().get_response(path, scope)
        response.headers["Cache-Control"] = "no-store, max-age=0"
        return response


@dataclass(frozen=True, slots=True)
class WebDependencies:
    """Explicit local dependencies used by the FastAPI adapter."""

    repository_factory: RepositoryFactory
    upload_processor: UploadProcessor
    today_provider: Callable[[], date] = date.today
    vector_index: DocumentVectorIndex | None = None
    processed_path: Path = Path("data/processed")


def default_web_dependencies() -> WebDependencies:
    """Compose the production dashboard from loopback-only adapters."""
    repository_factory = MongoDocumentRepository.connect

    vector_index = ChromaDocumentVectorIndex(
        embedding_generator=OllamaEmbeddingClient(model="embeddinggemma"),
        collection_name=collection_name_for_embedding_model("embeddinggemma"),
    )

    def process_upload(
        path: Path,
        language: str,
        progress_reporter: ProgressReporter,
    ) -> DocumentProcessingResult:
        """Extract and parse one upload without persisting it."""
        generator = OllamaClient()
        return DocumentProcessingPipeline(
            ocr=TesseractOCR(),
            parser=DocumentParser(generator),
            pdf_extractor=LocalPDFTextExtractor(),
            long_document_parser=LongDocumentParser(generator),
            language=language,
            progress_reporter=progress_reporter,
        ).process(path, structured=True, store=False)

    return WebDependencies(
        repository_factory,
        process_upload,
        vector_index=vector_index,
    )


def create_app(dependencies: WebDependencies | None = None) -> FastAPI:
    """Create a testable local dashboard with injected application services."""
    resolved = dependencies or default_web_dependencies()
    data_path = resolved.processed_path.parent
    pending_documents = PendingDocumentService(
        resolved.processed_path,
        data_path / "pending_confirmation",
    )
    jobs = UploadJobService(
        resolved.upload_processor,
        pending_documents,
        data_path / "processing_queue",
    )
    mutations = (
        DocumentMutationPipeline(
            resolved.repository_factory,
            resolved.vector_index,
        )
        if resolved.vector_index is not None
        else None
    )

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        """Close the bounded worker after all accepted uploads finish."""
        yield
        jobs.close()
        pending_documents.close()

    app = FastAPI(
        title="Smart Doc Tracker",
        version="0.1.0",
        lifespan=lifespan,
    )
    app.state.upload_jobs = jobs
    templates = Jinja2Templates(directory=str(_WEB_ROOT / "templates"))
    app.mount(
        "/static",
        LocalStaticFiles(directory=str(_WEB_ROOT / "static")),
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
        response = templates.TemplateResponse(
            request=request,
            name="dashboard.html",
            context={
                "alert_days": 30,
                "max_upload_mb": 25,
                "dashboard_style": (_WEB_ROOT / "static" / "dashboard.css").read_text(
                    encoding="utf-8"
                ),
                "dashboard_script": (
                    _WEB_ROOT / "static" / "dashboard.js"
                ).read_text(encoding="utf-8"),
            },
        )
        response.headers["Cache-Control"] = "no-store, max-age=0"
        return response

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

    @app.get(
        "/api/documents/{document_id}/indexed-content",
        response_model=DocumentIndexedContentResponse,
    )
    def get_document_indexed_content(
        document_id: str,
        repository: Repository,
    ) -> DocumentIndexedContentResponse:
        """Return every local Chroma content fragment for one stored document."""
        if repository.get_document_by_id(document_id) is None:
            raise HTTPException(status_code=404, detail="Document not found.")
        if resolved.vector_index is None:
            raise HTTPException(
                status_code=503,
                detail="The local vector database is unavailable.",
            )
        try:
            fragments = resolved.vector_index.get_document_fragments(document_id)
        except (ValueError, VectorDatabaseError) as exc:
            raise HTTPException(
                status_code=503,
                detail="The indexed document content is unavailable.",
            ) from exc
        return DocumentIndexedContentResponse.from_fragments(
            document_id,
            fragments,
        )

    @app.put("/api/documents/{document_id}", response_model=DocumentResponse)
    def update_document(
        document_id: str,
        document: DocumentData,
    ) -> DocumentResponse:
        """Update one document consistently in MongoDB and ChromaDB."""
        service = _require_mutation_service(mutations)
        try:
            updated = service.update(document_id, document)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except CoordinatedMutationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        if updated is None:
            raise HTTPException(status_code=404, detail="Document not found.")
        return DocumentResponse.from_record(
            updated,
            today=resolved.today_provider(),
            alert_days=30,
        )

    @app.delete("/api/documents/{document_id}", status_code=204)
    def delete_document(document_id: str) -> None:
        """Delete one document consistently from MongoDB and ChromaDB."""
        service = _require_mutation_service(mutations)
        try:
            deleted = service.delete(document_id)
        except CoordinatedMutationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        if deleted is None:
            raise HTTPException(status_code=404, detail="Document not found.")

    @app.get("/api/pending-documents", response_model=list[PendingDocumentResponse])
    def list_pending_documents() -> list[PendingDocumentResponse]:
        """List uploads that have not yet been explicitly confirmed."""
        return [
            PendingDocumentResponse.from_pending(item)
            for item in pending_documents.list()
        ]

    @app.get(
        "/api/pending-documents/{pending_id}",
        response_model=PendingDocumentResponse,
    )
    def get_pending_document(pending_id: str) -> PendingDocumentResponse:
        """Return one editable pending upload."""
        pending = pending_documents.get(pending_id)
        if pending is None:
            raise HTTPException(status_code=404, detail="Pending document not found.")
        return PendingDocumentResponse.from_pending(pending)

    @app.post(
        "/api/pending-documents/{pending_id}/confirm",
        response_model=DocumentResponse,
    )
    def confirm_pending_document(
        pending_id: str,
        document: DocumentData,
    ) -> DocumentResponse:
        """Validate user edits before persistence, indexing, and archiving."""
        pending = pending_documents.get(pending_id)
        if pending is None:
            raise HTTPException(status_code=404, detail="Pending document not found.")
        service = _require_mutation_service(mutations)
        try:
            result = service.confirm(
                document,
                file_hash=calculate_file_sha256(pending.source_path),
                raw_text=pending.raw_text,
                sections=pending.sections,
                finalize=lambda: pending_documents.archive(pending.id),
            )
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except (CoordinatedMutationError, FileHashingError) as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        jobs.discard_for_pending(pending_id)
        return DocumentResponse.from_record(
            result.record,
            today=resolved.today_provider(),
            alert_days=30,
        )

    @app.delete("/api/pending-documents/{pending_id}", status_code=204)
    def reject_pending_document(pending_id: str) -> None:
        """Reject and securely discard one staged upload."""
        if not pending_documents.reject(pending_id):
            raise HTTPException(status_code=404, detail="Pending document not found.")
        jobs.discard_for_pending(pending_id)

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

    @app.get("/api/jobs", response_model=list[UploadJobResponse])
    def list_upload_jobs() -> list[UploadJobResponse]:
        """List documents queued, processing, or requiring attention."""
        return [UploadJobResponse.from_job(job) for job in jobs.list_processing()]

    @app.get("/api/jobs/{job_id}", response_model=UploadJobResponse)
    def get_upload_job(job_id: str) -> UploadJobResponse:
        """Return the current status of one process-local upload job."""
        job = jobs.get(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        return UploadJobResponse.from_job(job)

    @app.delete("/api/jobs/{job_id}", status_code=204)
    def discard_failed_upload_job(job_id: str) -> None:
        """Discard one failed job and its locally queued source file."""
        job = jobs.get(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        if not jobs.discard_failed(job_id):
            raise HTTPException(
                status_code=409,
                detail="Only failed upload jobs can be removed.",
            )

    return app


def _require_mutation_service(
    service: DocumentMutationPipeline | None,
) -> DocumentMutationPipeline:
    """Return configured mutation coordination or a safe service error."""
    if service is None:
        raise HTTPException(
            status_code=503,
            detail="The local vector database is unavailable.",
        )
    return service


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
