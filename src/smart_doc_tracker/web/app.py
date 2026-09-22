"""FastAPI composition root for the loopback-only web dashboard."""

import argparse
import json
import logging
import os
import re
import secrets
import tempfile
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Sequence
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from threading import Lock
from typing import Annotated, Any
from urllib.parse import urlsplit

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
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
from starlette.types import Scope

from ..core.file_hash import FileHashingError, calculate_file_sha256
from ..core.ocr import SUPPORTED_IMAGE_EXTENSIONS, TesseractOCR
from ..core.parser import DocumentParser, DocumentParsingError, LongDocumentParser
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
from ..infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaEmbeddingClient,
    OllamaResponseError,
)
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..interfaces.text_generator import TextGenerator
from ..models.document import DocumentData
from ..models.rag import ConversationTurn
from ..mutation_pipeline import CoordinatedMutationError, DocumentMutationPipeline
from ..pipeline import (
    DocumentProcessingPipeline,
    DocumentProcessingResult,
    DocumentQuestionPipeline,
    ExpirationYearQuestionPipeline,
    StructuredFieldQuestionPipeline,
    requested_expiry_year,
    requested_structured_field,
)
from .chat_memory import TemporaryChatMemory
from .index_jobs import DocumentIndexJobService
from .jobs import ProgressReporter, UploadJobService, UploadProcessor
from .local_services import LocalServiceStartupError, LocalWebServiceManager
from .pending import PendingDocumentService
from .schemas import (
    ChatDocumentReference,
    ChatRequest,
    ChatResponse,
    DocumentIndexedContentResponse,
    DocumentResponse,
    DocumentUpdateResponse,
    IndexUpdateJobResponse,
    PendingDocumentResponse,
    UploadJobResponse,
)

RepositoryFactory = Callable[[], DocumentRepository]
_WEB_ROOT = Path(__file__).parent
_SUPPORTED_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS | {".pdf"}
_LANGUAGE_CODE = re.compile(r"^[A-Za-z][A-Za-z0-9_+-]{0,31}$")
_MAX_UPLOAD_BYTES = 25 * 1024 * 1024
_UPLOAD_CHUNK_BYTES = 1024 * 1024
_LOOPBACK_HOSTS = frozenset({"127.0.0.1", "localhost", "::1"})
_UNSAFE_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})
_CSRF_HEADER = "X-Smart-Doc-CSRF"
_CONTENT_SECURITY_POLICY = "; ".join(
    (
        "default-src 'self'",
        "base-uri 'none'",
        "connect-src 'self'",
        "form-action 'self'",
        "frame-ancestors 'none'",
        "img-src 'self' data:",
        "object-src 'none'",
        "script-src 'self'",
        "style-src 'self'",
    )
)
_LOG_LEVELS = ("debug", "info", "warning", "error", "critical")
_LOGGER = logging.getLogger(__name__)


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
    rag_generator: TextGenerator | None = None
    processed_path: Path = Path("data/processed")
    repository_closer: Callable[[], None] | None = None
    chat_memory: TemporaryChatMemory | None = None


def default_web_dependencies() -> WebDependencies:
    """Compose the production dashboard from loopback-only adapters."""
    vector_index = ChromaDocumentVectorIndex(
        embedding_generator=OllamaEmbeddingClient(model="embeddinggemma"),
        collection_name=collection_name_for_embedding_model("embeddinggemma"),
    )
    repository = MongoDocumentRepository.connect(close_on_exit=False)

    def repository_factory() -> DocumentRepository:
        """Return the application-scoped thread-safe repository."""
        return repository

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
        rag_generator=OllamaClient(),
        repository_closer=repository.close,
    )


def create_app(dependencies: WebDependencies | None = None) -> FastAPI:
    """Create a testable local dashboard with injected application services."""
    resolved = dependencies or default_web_dependencies()
    chat_memory = resolved.chat_memory or TemporaryChatMemory()
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
    mutation_lock = Lock()
    index_jobs = (
        DocumentIndexJobService(
            resolved.repository_factory,
            resolved.vector_index,
            data_path / "index_update_queue",
            mutation_lock,
        )
        if resolved.vector_index is not None
        else None
    )

    def submit_index_update(document_id: str) -> str:
        """Durably schedule a local search refresh."""
        if index_jobs is None:
            raise RuntimeError("The local index update queue is unavailable.")
        return index_jobs.submit(document_id).id

    mutations = (
        DocumentMutationPipeline(
            resolved.repository_factory,
            resolved.vector_index,
            submit_index_update,
            mutation_lock,
        )
        if resolved.vector_index is not None
        else None
    )

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        """Close bounded workers and shared local connections cleanly."""
        yield
        jobs.close()
        if index_jobs is not None:
            index_jobs.close()
        pending_documents.close()
        chat_memory.clear_all()
        if resolved.repository_closer is not None:
            resolved.repository_closer()

    app = FastAPI(
        title="Smart Doc Tracker",
        version="0.1.0",
        lifespan=lifespan,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    csrf_token = secrets.token_urlsafe(32)
    app.state.csrf_token = csrf_token
    app.state.upload_jobs = jobs
    templates = Jinja2Templates(directory=str(_WEB_ROOT / "templates"))
    app.mount(
        "/static",
        LocalStaticFiles(directory=str(_WEB_ROOT / "static")),
        name="static",
    )

    @app.middleware("http")
    async def enforce_local_web_boundary(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        """Reject external authorities, cross-origin writes, and missing CSRF proof."""
        host = request.headers.get("host", "")
        if _normalized_authority(host) is None:
            return _secure_response(Response(status_code=400))
        origin = request.headers.get("origin")
        if origin is not None and not _same_loopback_origin(origin, host):
            return _secure_response(Response(status_code=403))
        if request.method in _UNSAFE_METHODS:
            supplied_token = request.headers.get(_CSRF_HEADER, "")
            if not secrets.compare_digest(supplied_token, csrf_token):
                return _secure_response(Response(status_code=403))
        try:
            response = await call_next(request)
        except Exception as exc:
            _LOGGER.error(
                "Request %s failed with an unhandled %s.",
                request.method,
                type(exc).__name__,
            )
            raise
        if response.status_code >= 500:
            route = request.scope.get("route")
            route_pattern = getattr(route, "path", "unmatched route")
            _LOGGER.error(
                "Request %s %s returned HTTP %s.",
                request.method,
                route_pattern,
                response.status_code,
            )
        return _secure_response(response)

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
                "csrf_token": csrf_token,
                "max_upload_mb": 25,
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

    @app.post("/api/chat", response_model=ChatResponse)
    def ask_documents(
        request: ChatRequest,
        repository: Repository,
    ) -> ChatResponse:
        """Answer from local document data and return validated citations."""
        question = request.question.strip()
        if not question:
            raise HTTPException(status_code=422, detail="The question cannot be empty.")
        _LOGGER.info("Chat request accepted; document contents are not logged.")
        history = (
            chat_memory.history(request.conversation_id)
            if request.conversation_id is not None
            else ()
        )
        expiry_year = requested_expiry_year(
            question,
            today=resolved.today_provider(),
        )
        structured_field = requested_structured_field(question)
        try:
            if expiry_year is not None:
                _LOGGER.info("Chat request is using the normalized expiry-date query.")
                answer = ExpirationYearQuestionPipeline(
                    repository,
                    today_provider=resolved.today_provider,
                ).ask(expiry_year)
            elif structured_field is not None:
                _LOGGER.info("Chat request is using a validated structured field.")
                if resolved.vector_index is None:
                    raise HTTPException(
                        status_code=503,
                        detail="The local document assistant is unavailable.",
                    )
                answer = StructuredFieldQuestionPipeline(
                    repository,
                    resolved.vector_index,
                ).ask(question, structured_field, history=history)
            else:
                _LOGGER.info("Chat request is using semantic retrieval and Ollama.")
                if resolved.vector_index is None or resolved.rag_generator is None:
                    raise HTTPException(
                        status_code=503,
                        detail="The local document assistant is unavailable.",
                    )
                answer = DocumentQuestionPipeline(
                    resolved.vector_index,
                    resolved.rag_generator,
                ).ask(question, history=history)
        except (
            DocumentParsingError,
            OllamaConfigurationError,
            OllamaConnectionError,
            OllamaResponseError,
            VectorDatabaseError,
        ) as exc:
            _LOGGER.error(
                "Chat request failed with %s.",
                type(exc).__name__,
            )
            raise HTTPException(
                status_code=503,
                detail=_chat_error_detail(exc),
            ) from exc

        documents: list[ChatDocumentReference] = []
        for document_id in dict.fromkeys(answer.document_ids):
            record = repository.get_document_by_id(document_id)
            if record is not None:
                documents.append(ChatDocumentReference.from_record(record))
        _LOGGER.info(
            "Chat request completed successfully (%s supporting documents).",
            len(documents),
        )
        if request.conversation_id is not None:
            chat_memory.remember(
                request.conversation_id,
                ConversationTurn(
                    question=question,
                    answer=answer.answer,
                    document_ids=tuple(answer.document_ids),
                ),
            )
        return ChatResponse(
            answer=answer.answer,
            claims=answer.claims,
            documents=documents,
            insufficient_information=answer.insufficient_information,
        )

    @app.delete("/api/chat/conversations/{conversation_id}", status_code=204)
    def clear_chat_conversation(conversation_id: str) -> Response:
        """Forget one process-local chat conversation."""
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", conversation_id):
            raise HTTPException(
                status_code=422,
                detail="Invalid conversation identifier.",
            )
        chat_memory.clear(conversation_id)
        return Response(status_code=204)

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

    @app.get("/api/documents/{document_id}/original")
    def get_document_original(
        document_id: str,
        repository: Repository,
        download: bool = False,
    ) -> FileResponse:
        """Open or download the original file from the local processed archive."""
        record = repository.get_document_by_id(document_id)
        if record is None:
            raise HTTPException(status_code=404, detail="Document not found.")
        if record.source_file_name is None:
            raise HTTPException(
                status_code=404,
                detail="The original file is not available for this document.",
            )
        processed_root = resolved.processed_path.expanduser().resolve()
        source_path = (processed_root / record.source_file_name).resolve()
        if source_path.parent != processed_root or not source_path.is_file():
            raise HTTPException(
                status_code=404,
                detail="The original file is not available for this document.",
            )
        return FileResponse(
            source_path,
            filename=record.source_file_name,
            content_disposition_type="attachment" if download else "inline",
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

    @app.put("/api/documents/{document_id}", response_model=DocumentUpdateResponse)
    def update_document(
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResponse:
        """Store one document update and queue its local search refresh."""
        service = _require_mutation_service(mutations)
        try:
            updated = service.update(document_id, document)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except CoordinatedMutationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        if updated is None:
            raise HTTPException(status_code=404, detail="Document not found.")
        return DocumentUpdateResponse.from_update(
            updated.record,
            index_update_id=updated.index_update_id,
            today=resolved.today_provider(),
            alert_days=30,
        )

    @app.post("/api/documents/manual", response_model=DocumentResponse)
    def create_manual_document(document: DocumentData) -> DocumentResponse:
        """Validate, persist, and index a document entered entirely by the user."""
        service = _require_mutation_service(mutations)
        try:
            result = service.create_manual(document)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except CoordinatedMutationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        return DocumentResponse.from_record(
            result.record,
            today=resolved.today_provider(),
            alert_days=30,
        )

    @app.get(
        "/api/document-updates/{update_id}",
        response_model=IndexUpdateJobResponse,
    )
    def get_document_update(update_id: str) -> IndexUpdateJobResponse:
        """Return simple progress for one accepted background refresh."""
        job = _require_index_jobs(index_jobs).get(update_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Update not found.")
        return IndexUpdateJobResponse.from_job(job)

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


def _normalized_authority(value: str) -> tuple[str, int] | None:
    """Parse an HTTP authority and accept only an exact loopback hostname."""
    if not value or any(character in value for character in "/?#@"):
        return None
    try:
        parsed = urlsplit(f"//{value}")
        port = parsed.port or 80
    except ValueError:
        return None
    hostname = parsed.hostname.lower() if parsed.hostname is not None else None
    if hostname not in _LOOPBACK_HOSTS:
        return None
    return hostname, port


def _same_loopback_origin(origin: str, host: str) -> bool:
    """Require browser requests to originate from the exact served authority."""
    try:
        parsed = urlsplit(origin)
        origin_authority = _normalized_authority(parsed.netloc)
    except ValueError:
        return False
    return (
        parsed.scheme == "http"
        and parsed.path == ""
        and parsed.query == ""
        and parsed.fragment == ""
        and origin_authority is not None
        and origin_authority == _normalized_authority(host)
    )


def _secure_response(response: Response) -> Response:
    """Apply restrictive browser policies to every local HTTP response."""
    response.headers["Content-Security-Policy"] = _CONTENT_SECURITY_POLICY
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    response.headers["Permissions-Policy"] = (
        "camera=(), geolocation=(), microphone=(), payment=(), usb=()"
    )
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response


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


def _require_index_jobs(
    service: DocumentIndexJobService | None,
) -> DocumentIndexJobService:
    """Return the configured local refresh queue or a safe service error."""
    if service is None:
        raise HTTPException(
            status_code=503,
            detail="Document updates are temporarily unavailable.",
        )
    return service


def _parse_query_value(value: str) -> Any:
    """Interpret JSON scalars and structures, falling back to a plain string."""
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def _chat_error_detail(exc: Exception) -> str:
    """Return a safe, actionable browser message for one local chat failure."""
    if isinstance(exc, OllamaConnectionError):
        return "The local Ollama service or language model is unavailable."
    if isinstance(exc, OllamaResponseError):
        return "The local Ollama service returned an invalid response."
    if isinstance(exc, VectorDatabaseError):
        return "The local document search could not be completed."
    if isinstance(exc, DocumentParsingError):
        return "The local model returned an invalid grounded answer."
    return "The local document assistant is not configured correctly."


def run(argv: Sequence[str] | None = None) -> None:
    """Run the dashboard and own its required local service lifecycle."""
    parser = argparse.ArgumentParser(description="Run the local document dashboard.")
    parser.add_argument("--host", default="127.0.0.1", choices=("127.0.0.1", "::1"))
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument(
        "--log-level",
        choices=_LOG_LEVELS,
        default="info",
        help="Terminal detail level (default: info).",
    )
    parser.add_argument(
        "--access-log",
        action="store_true",
        help="Show one terminal line for every HTTP request.",
    )
    arguments = parser.parse_args(argv)
    if not 1 <= arguments.port <= 65_535:
        parser.error("--port must be between 1 and 65535")
    _configure_application_logging(arguments.log_level)
    import uvicorn

    services = LocalWebServiceManager()
    try:
        services.start()
        uvicorn.run(
            "smart_doc_tracker.web.app:create_app",
            factory=True,
            host=arguments.host,
            port=arguments.port,
            workers=1,
            log_level=arguments.log_level,
            access_log=arguments.access_log,
        )
    except LocalServiceStartupError as exc:
        parser.exit(status=1, message=f"error: {exc}\n")
    finally:
        services.stop()


def _configure_application_logging(level: str) -> None:
    """Send application progress and safe diagnostics to the server terminal."""
    application_logger = logging.getLogger("smart_doc_tracker")
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    application_logger.handlers.clear()
    application_logger.addHandler(handler)
    application_logger.setLevel(level.upper())
    application_logger.propagate = False
