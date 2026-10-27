"""Explicit dependencies shared by local HTTP route groups."""

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Protocol

from fastapi import HTTPException
from fastapi.templating import Jinja2Templates

from ...db.database import DatabaseConfigurationError, DatabaseError
from ...interfaces.document_repository import DocumentRepository
from ...interfaces.document_vector_index import DocumentVectorIndex
from ...mutation_pipeline import DocumentMutationPipeline
from ...settings import LocalReminderSettingsStore, ReminderSettingsError
from ..chat import ChatCancellation, DocumentChatService
from ..index_jobs import DocumentIndexJobService
from ..insertion import PendingInsertionCoordinator
from ..jobs import UploadJobService
from ..pending import PendingDocumentService
from ..upload import UploadIntake


class WebRouteDependencies(Protocol):
    """Read-only application dependencies needed by HTTP handlers."""

    @property
    def repository_factory(self) -> Callable[[], DocumentRepository]:
        """Return the local repository factory."""
        ...

    @property
    def today_provider(self) -> Callable[[], date]:
        """Return the injected local date provider."""
        ...

    @property
    def vector_index(self) -> DocumentVectorIndex | None:
        """Return the optional local vector index."""
        ...

    @property
    def processed_path(self) -> Path:
        """Return the local archive path."""
        ...


@dataclass(frozen=True, slots=True)
class WebRouteContext:
    """Application-scoped services passed to each route group."""

    dependencies: WebRouteDependencies
    reminder_settings: LocalReminderSettingsStore
    pending_documents: PendingDocumentService
    jobs: UploadJobService
    upload_intake: UploadIntake
    mutations: DocumentMutationPipeline | None
    insertion: PendingInsertionCoordinator
    index_jobs: DocumentIndexJobService | None
    chat_service: DocumentChatService
    chat_cancellation: ChatCancellation
    templates: Jinja2Templates
    csrf_token: str

    def repository(self) -> Iterator[DocumentRepository]:
        """Open and close one local repository for an HTTP request."""
        try:
            with self.dependencies.repository_factory() as opened_repository:
                yield opened_repository
        except (DatabaseConfigurationError, DatabaseError) as exc:
            raise HTTPException(
                status_code=503,
                detail="The local document database is unavailable.",
            ) from exc

    def default_reminder_days(self) -> int:
        """Return the configured reminder window or a safe service error."""
        try:
            return self.reminder_settings.load().default_notification_days_before
        except ReminderSettingsError as exc:
            raise HTTPException(
                status_code=503,
                detail="The local reminder settings are unavailable.",
            ) from exc
