"""Coordinate application-visible mutations across MongoDB and ChromaDB."""

from __future__ import annotations

import shutil
from _thread import LockType
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from secrets import token_hex
from tempfile import TemporaryDirectory
from threading import Lock

from .db.database import DocumentInsertResult, StoredDocument
from .db.vector_database import VectorDatabaseError, VectorDatabaseUnavailableError
from .interfaces.document_repository import DocumentRepository
from .interfaces.document_vector_index import DocumentVectorIndex
from .models.document import DocumentData, StructuredDocumentSection


class CoordinatedMutationError(RuntimeError):
    """Raised when a coordinated mutation fails and is compensated."""


class DocumentIndexingError(CoordinatedMutationError):
    """An insertion remains pending because local indexing failed."""

    def __init__(self, *, unavailable: bool) -> None:
        """Record whether Chroma could be reached after the failed operation."""
        super().__init__("The document could not be indexed locally.")
        self.unavailable = unavailable


RepositoryFactory = Callable[[], DocumentRepository]
IndexUpdateSubmitter = Callable[[str], str]


@dataclass(frozen=True, slots=True)
class DocumentUpdateResult:
    """Stored document together with its durable local refresh job."""

    record: StoredDocument
    index_update_id: str


@dataclass(slots=True)
class DocumentMutationPipeline:
    """Apply local document mutations with compensating cross-store rollback."""

    repository_factory: RepositoryFactory
    vector_index: DocumentVectorIndex
    index_update_submitter: IndexUpdateSubmitter
    operation_lock: LockType = field(default_factory=Lock)
    processed_path: Path | None = None

    def create_manual(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(32),
            raw_text="",
        )

    def confirm(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
        undo_finalize: Callable[[Path], None] | None = None,
        commit_finalize: Callable[[], None] | None = None,
        record_insert: Callable[[str], None] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        archived_path: Path | None = None
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    inserted = repository.insert_document(
                        document, file_hash=file_hash, insertion_pending=True
                    )
                    if (
                        not inserted.inserted
                        and inserted.record.source_file_name is not None
                    ):
                        raise CoordinatedMutationError(
                            "This source is already linked to a stored document."
                        )
                    if record_insert is not None:
                        record_insert(inserted.record.id)
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=inserted.record.document,
                    )
                    self._verify_insert(repository, inserted.record.id)
                    if finalize is not None:
                        archived_path = finalize()
                        archived_record = repository.set_source_file_name(
                            inserted.record.id,
                            archived_path.name,
                        )
                        if archived_record is None:
                            raise CoordinatedMutationError(
                                "The archived source could not be linked."
                            )
                        inserted = DocumentInsertResult(
                            record=archived_record,
                            inserted=inserted.inserted,
                        )
                    committed_record = repository.mark_document_committed(
                        inserted.record.id
                    )
                    if committed_record is None:
                        raise CoordinatedMutationError(
                            "The document could not be committed locally."
                        )
                    inserted = DocumentInsertResult(
                        record=committed_record, inserted=inserted.inserted
                    )
                if archived_path is not None and commit_finalize is not None:
                    commit_finalize()
                return inserted
        except Exception as exc:
            if isinstance(exc, DocumentIndexingError):
                raise
            if isinstance(exc, VectorDatabaseError):
                raise DocumentIndexingError(
                    unavailable=isinstance(exc, VectorDatabaseUnavailableError)
                ) from exc
            compensated = True
            if archived_path is not None and undo_finalize is not None:
                try:
                    undo_finalize(archived_path)
                except Exception:
                    compensated = False
            if inserted is not None and inserted.inserted:
                compensated = (
                    self._compensate_insert(inserted.record.id) and compensated
                )
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def update(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def delete(self, document_id: str) -> StoredDocument | None:
        """Delete both stores and the archived source, restoring on failure."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    record = repository.get_document_by_id(document_id)
                    if record is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    source = self._source_path(record)
                    with TemporaryDirectory(prefix="smart-doc-delete-") as temporary:
                        backup = Path(temporary) / "source"
                        if source is not None:
                            shutil.copy2(source, backup)
                            source.unlink()
                        try:
                            self.vector_index.delete_document(document_id)
                            if self.vector_index.get_document_fragments(document_id):
                                raise CoordinatedMutationError(
                                    "The document remains in the local search index."
                                )
                            deleted = repository.delete_document(document_id)
                            if (
                                deleted is None
                                or repository.get_document_by_id(document_id)
                                is not None
                            ):
                                raise CoordinatedMutationError(
                                    "The document remains in the local database."
                                )
                        except Exception as exc:
                            restored = True
                            try:
                                self.vector_index.restore_document(snapshot)
                            except Exception:
                                restored = False
                            if source is not None:
                                try:
                                    shutil.copy2(backup, source)
                                except Exception:
                                    restored = False
                            if not restored:
                                raise CoordinatedMutationError(
                                    "Document deletion failed; rollback was incomplete."
                                ) from exc
                            raise CoordinatedMutationError(
                                "Document deletion was rolled back. Try again later."
                            ) from exc
                        return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def _compensate_insert(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        try:
            self.vector_index.delete_document(document_id)
            if self.vector_index.get_document_fragments(document_id):
                return False
        except Exception:
            return False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
                if repository.get_document_by_id(document_id) is not None:
                    return False
        except Exception:
            return False
        return True

    def cancel_insertion(self, document_id: str) -> None:
        """Remove both sides of a confirmed but incomplete insertion."""
        with self.operation_lock:
            if not self._compensate_insert(document_id):
                raise CoordinatedMutationError(
                    "The insertion could not be cancelled in both local stores."
                )

    def _verify_insert(self, repository: DocumentRepository, document_id: str) -> None:
        """Require a readable record and indexed content before reporting success."""
        if repository.get_document_by_id(document_id) is None:
            raise CoordinatedMutationError("The document was not stored locally.")
        fragments = self.vector_index.get_document_fragments(document_id)
        if not fragments:
            raise DocumentIndexingError(unavailable=False)

    def _source_path(self, record: StoredDocument) -> Path | None:
        """Resolve a linked source strictly inside the configured archive."""
        if record.source_file_name is None or self.processed_path is None:
            return None
        root = self.processed_path.expanduser().resolve()
        source = (root / record.source_file_name).resolve()
        if source.parent != root:
            raise CoordinatedMutationError("The archived source is unavailable.")
        if not source.exists():
            return None
        if not source.is_file():
            raise CoordinatedMutationError("The archived source is unavailable.")
        return source
