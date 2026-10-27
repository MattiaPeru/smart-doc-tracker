"""FastAPI composition root for the loopback-only web dashboard."""

import os
import secrets
from collections.abc import AsyncIterator, Callable, Sequence
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from threading import Lock, Thread

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from ..core.ocr import TesseractOCR
from ..core.parser import DocumentParser, LongDocumentParser
from ..core.pdf import LocalPDFTextExtractor
from ..db.database import MongoDocumentRepository
from ..db.vector_database import (
    ChromaDocumentVectorIndex,
    collection_name_for_embedding_model,
)
from ..infrastructure.ollama import (
    OllamaClient,
    OllamaEmbeddingClient,
)
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..interfaces.text_generator import TextGenerator
from ..mutation_pipeline import DocumentMutationPipeline
from ..pipeline import DocumentProcessingPipeline, DocumentProcessingResult
from ..settings import LocalReminderSettingsStore
from .chat import ChatCancellation, DocumentChatService
from .chat_memory import TemporaryChatMemory
from .index_jobs import DocumentIndexJobService
from .insertion import PendingInsertionCoordinator
from .jobs import ProgressReporter, UploadJobService, UploadProcessor
from .local_services import LocalWebServiceManager
from .pending import PendingDocumentService
from .routes.context import WebRouteContext
from .routes.document_chat import register_document_chat_routes
from .routes.documents import register_documents_routes
from .routes.pending_documents import register_pending_document_routes
from .routes.settings import register_settings_routes
from .routes.upload_jobs import register_upload_job_routes
from .security import LocalStaticFiles, LocalWebSecurity
from .upload import UploadIntake

RepositoryFactory = Callable[[], DocumentRepository]
_WEB_ROOT = Path(__file__).parent


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
    reminder_settings: LocalReminderSettingsStore | None = None


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
    chat_debug = os.environ.get("SMART_DOC_TRACKER_CHAT_DEBUG") == "1"
    chat_memory = resolved.chat_memory or TemporaryChatMemory()
    chat_cancellation = ChatCancellation(chat_memory)
    data_path = resolved.processed_path.parent
    reminder_settings = resolved.reminder_settings or LocalReminderSettingsStore(
        data_path / "settings.json"
    )
    pending_documents = PendingDocumentService(
        resolved.processed_path,
        data_path / "pending_confirmation",
    )
    jobs = UploadJobService(
        resolved.upload_processor,
        pending_documents,
        data_path / "processing_queue",
    )
    upload_intake = UploadIntake(jobs)
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
            resolved.processed_path,
        )
        if resolved.vector_index is not None
        else None
    )
    insertion = PendingInsertionCoordinator(
        pending_documents,
        jobs,
        resolved.repository_factory,
        resolved.vector_index,
        mutations,
        mutation_lock,
        Lock(),
        resolved.processed_path,
    )

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        """Stop workers promptly and release shared local connections."""
        insertion_worker = Thread(
            target=insertion.retry_until_stopped,
            name="smart-doc-insertion-retry",
            daemon=True,
        )
        insertion_worker.start()
        yield
        insertion.stop()
        insertion_worker.join(timeout=1)
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

    app.middleware("http")(LocalWebSecurity(csrf_token).enforce)

    chat_service = DocumentChatService(
        resolved.vector_index,
        resolved.rag_generator,
        pending_documents,
        chat_memory,
        chat_cancellation,
        chat_debug,
    )
    context = WebRouteContext(
        dependencies=resolved,
        reminder_settings=reminder_settings,
        pending_documents=pending_documents,
        jobs=jobs,
        upload_intake=upload_intake,
        mutations=mutations,
        insertion=insertion,
        index_jobs=index_jobs,
        chat_service=chat_service,
        chat_cancellation=chat_cancellation,
        templates=templates,
        csrf_token=csrf_token,
    )
    for router in (
        register_settings_routes(context),
        register_documents_routes(context),
        register_document_chat_routes(context),
        register_pending_document_routes(context),
        register_upload_job_routes(context),
    ):
        app.include_router(router)
    return app


def run(argv: Sequence[str] | None = None) -> None:
    """Run the dashboard and own its required local service lifecycle."""
    from .cli import run as run_cli

    run_cli(argv, service_manager_factory=LocalWebServiceManager)
