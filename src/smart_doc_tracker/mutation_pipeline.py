"""Coordinate application-visible mutations across MongoDB and ChromaDB."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

from .db.database import DocumentInsertResult, StoredDocument
from .interfaces.document_repository import DocumentRepository
from .interfaces.document_vector_index import DocumentVectorIndex
from .models.document import DocumentData, StructuredDocumentSection


class CoordinatedMutationError(RuntimeError):
    """Raised when a coordinated mutation fails and is compensated."""


RepositoryFactory = Callable[[], DocumentRepository]


@dataclass(slots=True)
class DocumentMutationPipeline:
    """Apply local document mutations with compensating cross-store rollback."""

    repository_factory: RepositoryFactory
    vector_index: DocumentVectorIndex

    def confirm(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], object] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    finalize()
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def update(self, document_id: str, document: DocumentData) -> StoredDocument | None:
        """Update MongoDB and ChromaDB, restoring both snapshots on failure."""
        try:
            with self.repository_factory() as repository:
                previous = repository.get_document_by_id(document_id)
                if previous is None:
                    return None
                snapshot = self.vector_index.snapshot_document(document_id)
                updated = repository.update_document(document_id, document)
                if updated is None:
                    return None
                try:
                    self.vector_index.update_document_data(document_id, document)
                except Exception as exc:
                    rollback_complete = True
                    try:
                        repository.update_document(document_id, previous.document)
                    except Exception:
                        rollback_complete = False
                    try:
                        self.vector_index.restore_document(snapshot)
                    except Exception:
                        rollback_complete = False
                    if not rollback_complete:
                        raise CoordinatedMutationError(
                            "The document update failed and automatic rollback was "
                            "incomplete."
                        ) from exc
                    raise CoordinatedMutationError(
                        "The document update was rolled back in both local stores."
                    ) from exc
                return updated
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def delete(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.repository_factory() as repository:
                if repository.get_document_by_id(document_id) is None:
                    return None
                snapshot = self.vector_index.snapshot_document(document_id)
                try:
                    self.vector_index.delete_document(document_id)
                    deleted = repository.delete_document(document_id)
                except Exception as exc:
                    try:
                        self.vector_index.restore_document(snapshot)
                    except Exception:
                        raise CoordinatedMutationError(
                            "The document deletion failed and automatic rollback was "
                            "incomplete."
                        ) from exc
                    raise CoordinatedMutationError(
                        "The document deletion was rolled back in both local stores."
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
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed
