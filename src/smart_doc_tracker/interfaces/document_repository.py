"""Persistence and query interface for local documents."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from typing import Any, Protocol

from ..db.database import DocumentInsertResult, StoredDocument
from ..models.document import DocumentData, StructuredDocumentSection


class DocumentRepository(Protocol):
    """Persist and query validated local documents."""

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
        insertion_pending: bool = False,
    ) -> DocumentInsertResult:
        """Persist one validated document using its content hash."""
        ...

    def mark_document_committed(self, document_id: str) -> StoredDocument | None:
        """Expose a verified record to ordinary document queries."""
        ...

    def upsert_document_sections(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist structured page sections for one document."""
        ...

    def get_all_documents(self) -> list[StoredDocument]:
        """Return every stored document."""
        ...

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        """Return one stored document by identifier when present."""
        ...

    def get_document_by_file_hash(self, file_hash: str) -> StoredDocument | None:
        """Return one document by source hash when present."""
        ...

    def update_document(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields while preserving record metadata."""
        ...

    def set_source_file_name(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach one safe processed-file name to a stored document."""
        ...

    def delete_document(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its local structured sections."""
        ...

    def get_expiring_documents(
        self,
        days_threshold: int,
        *,
        today: date | None = None,
    ) -> list[StoredDocument]:
        """Return documents expiring within an inclusive date window."""
        ...

    def get_documents_expiring_in_year(self, year: int) -> list[StoredDocument]:
        """Return documents whose normalized expiry date falls in one year."""
        ...

    def search_by_dynamic_field(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Return documents matching an exact dynamic JSON field value."""
        ...
