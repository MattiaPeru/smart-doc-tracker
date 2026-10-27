"""Coordinate confirmed web insertions and recovery of local stores."""

import logging
from collections.abc import Callable
from pathlib import Path
from threading import Event, Lock

from fastapi import HTTPException

from ..core.file_hash import calculate_file_sha256
from ..db.database import DocumentInsertResult
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..mutation_pipeline import (
    CoordinatedMutationError,
    DocumentIndexingError,
    DocumentMutationPipeline,
)
from .jobs import UploadJobService
from .pending import PendingDocumentError, PendingDocumentService

_LOGGER = logging.getLogger(__name__)


class PendingSourceRemovalError(OSError):
    """The staged source could not be removed after cancellation was recorded."""


class PendingInsertionCoordinator:
    """Complete confirmed insertions and retry recoverable local store failures."""

    def __init__(
        self,
        pending_documents: PendingDocumentService,
        jobs: UploadJobService,
        repository_factory: Callable[[], DocumentRepository],
        vector_index: DocumentVectorIndex | None,
        mutations: DocumentMutationPipeline | None,
        mutation_lock: Lock,
        insertion_lock: Lock,
        processed_path: Path,
    ) -> None:
        """Bind the local stores, job queue, and synchronization primitives."""
        self._pending_documents = pending_documents
        self._jobs = jobs
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._mutations = mutations
        self._mutation_lock = mutation_lock
        self.lock = insertion_lock
        self._processed_path = processed_path
        self._stop = Event()

    def complete(self, pending_id: str) -> DocumentInsertResult:
        """Resume a confirmed insertion from its durable local manifest."""
        pending = self._pending_documents.get(pending_id)
        if pending is None or pending.confirmation_document is None:
            raise PendingDocumentError("The confirmed insertion is unavailable.")
        if pending.cancelling:
            raise PendingDocumentError("This insertion is being cancelled.")
        if pending.archived_file_name is not None:
            archived = self._processed_path / pending.archived_file_name
            if pending.source_path.is_file():
                # The archive move was interrupted before it started.
                pass
            elif archived.is_file():
                with self._repository_factory() as repository:
                    record = (
                        repository.get_document_by_id(pending.insertion_document_id)
                        if pending.insertion_document_id is not None
                        else None
                    )
                if record is not None and record.source_file_name == archived.name:
                    if self._vector_index is None:
                        raise CoordinatedMutationError(
                            "The local search index is unavailable."
                        )
                    with self._mutation_lock:
                        self._vector_index.upsert_document(
                            record.id,
                            raw_text=pending.raw_text,
                            document=record.document,
                        )
                        if not self._vector_index.get_document_fragments(record.id):
                            raise CoordinatedMutationError(
                                "The document is not indexed locally."
                            )
                        with self._repository_factory() as repository:
                            committed = repository.mark_document_committed(record.id)
                        if committed is None:
                            raise CoordinatedMutationError(
                                "The document could not be committed locally."
                            )
                        record = committed
                    self._pending_documents.finish_archive(pending_id)
                    self._jobs.discard_for_pending(pending_id)
                    return DocumentInsertResult(record, False)
                self._pending_documents.restore_archive(pending, archived)
                pending = self._pending_documents.get(pending_id)
                if pending is None:
                    raise PendingDocumentError(
                        "The confirmation source is unavailable."
                    )
        if self._mutations is None:
            raise HTTPException(
                status_code=503,
                detail="The local vector database is unavailable.",
            )
        confirmation_document = pending.confirmation_document
        if confirmation_document is None:
            raise PendingDocumentError("The confirmed insertion is unavailable.")
        try:
            result = self._mutations.confirm(
                confirmation_document,
                file_hash=pending.file_hash
                or calculate_file_sha256(pending.source_path),
                raw_text=pending.raw_text,
                sections=pending.sections,
                finalize=(
                    None
                    if pending.is_manual
                    else lambda: self._pending_documents.archive(pending.id)
                ),
                undo_finalize=(
                    None
                    if pending.is_manual
                    else lambda archived: self._pending_documents.restore_archive(
                        pending, archived
                    )
                ),
                commit_finalize=(
                    None
                    if pending.is_manual
                    else lambda: self._pending_documents.finish_archive(pending.id)
                ),
                record_insert=lambda document_id: self._record_insertion_id(
                    pending.id, document_id
                ),
            )
        except DocumentIndexingError as exc:
            if not exc.unavailable and not pending.is_manual:
                failures = self._pending_documents.record_index_failure(pending.id)
                if failures >= 2:
                    cancelling = self._pending_documents.mark_cancelling(pending.id)
                    if cancelling.insertion_document_id is not None:
                        self._mutations.cancel_insertion(
                            cancelling.insertion_document_id
                        )
                    self._jobs.fail_pending_insertion(pending.id)
                    self._pending_documents.reject(pending.id)
            raise
        if pending.is_manual:
            self._pending_documents.reject(pending.id)
        self._jobs.discard_for_pending(pending_id)
        return result

    def retry_until_stopped(self) -> None:
        """Retry interrupted or unavailable local stores until shutdown."""
        while not self._stop.wait(5):
            for item in self._pending_documents.list():
                if (
                    item.confirmation_document is None
                    or item.cancelling
                    or self._stop.is_set()
                ):
                    continue
                with self.lock:
                    try:
                        self.complete(item.id)
                    except Exception as exc:
                        _LOGGER.warning(
                            "Pending insertion %s still needs a local store (%s).",
                            item.id,
                            type(exc).__name__,
                        )

    def stop(self) -> None:
        """Signal the background recovery worker to stop."""
        self._stop.set()

    def reject(self, pending_id: str) -> None:
        """Cancel partial store entries and discard a staged source atomically."""
        with self.lock:
            pending = self._pending_documents.mark_cancelling(pending_id)
            document_ids = set()
            if pending.insertion_document_id is not None:
                document_ids.add(pending.insertion_document_id)
            if pending.file_hash is not None:
                with self._repository_factory() as repository:
                    partial = repository.get_document_by_file_hash(pending.file_hash)
                if partial is not None and partial.source_file_name is None:
                    document_ids.add(partial.id)
            if document_ids and self._mutations is None:
                raise HTTPException(
                    status_code=503,
                    detail="The local vector database is unavailable.",
                )
            if self._mutations is not None:
                for document_id in document_ids:
                    self._mutations.cancel_insertion(document_id)
            try:
                self._pending_documents.reject(pending_id)
            except OSError as exc:
                raise PendingSourceRemovalError(
                    "The pending source could not be removed."
                ) from exc
            self._jobs.discard_for_pending(pending_id)

    def _record_insertion_id(self, pending_id: str, document_id: str) -> None:
        """Record the database identifier in the durable confirmation manifest."""
        self._pending_documents.record_insertion_id(pending_id, document_id)
