"""Repository interfaces shared by document controllers and CLI composition."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from typing import Protocol

from db.database import DocumentInsertResult, StoredDocument
from models.document import DocumentData, StructuredDocumentSection


class DocumentRepository(Protocol):
    """Expose direct persistence and query operations for local documents."""

    def __enter__(self) -> DocumentRepository:
        """Open the repository context."""
        ...

    def __exit__(self, *args: object) -> None:
        """Close the repository context."""
        ...

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
    ) -> DocumentInsertResult:
        """Persist one validated document using its file hash."""
        ...

    def get_all_documents(self) -> list[StoredDocument]:
        """Return every stored document."""
        ...

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        """Return one stored document by identifier when present."""
        ...

    def get_expiring_documents(
        self,
        days_threshold: int,
        *,
        today: date | None = None,
    ) -> list[StoredDocument]:
        """Return documents expiring within the requested window."""
        ...

    def upsert_document_sections(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist structured sections for one document."""
        ...
