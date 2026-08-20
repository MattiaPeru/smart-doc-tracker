"""Direct persistence and retrieval operations for local documents."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from core.file_hash import calculate_file_sha256
from db.database import DocumentInsertResult, StoredDocument
from db.interfaces import DocumentRepository
from models.document import DocumentData, StructuredDocumentSection


@dataclass(slots=True)
class DocumentManager:
    """Insert, retrieve, and query documents through one repository."""

    repository: DocumentRepository
    today_provider: Callable[[], date] = date.today

    def insert_document(
        self,
        source_path: str | Path,
        document: DocumentData,
        *,
        sections: Sequence[StructuredDocumentSection] = (),
    ) -> DocumentInsertResult:
        """Persist one document and its optional structured PDF sections."""
        result = self.repository.insert_document(
            document,
            file_hash=calculate_file_sha256(source_path),
        )
        if sections:
            self.repository.upsert_document_sections(result.record.id, sections)
        return result

    def get_all_documents(self) -> list[StoredDocument]:
        """Return every document stored in the repository."""
        return self.repository.get_all_documents()

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        """Return one stored document by identifier when present."""
        return self.repository.get_document_by_id(document_id)

    def get_expiring_documents(self, days_threshold: int) -> list[StoredDocument]:
        """Return documents expiring inside the inclusive date window."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        return self.repository.get_expiring_documents(
            days_threshold,
            today=self.today_provider(),
        )
