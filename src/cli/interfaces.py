"""Narrow interfaces required by command-line workflows."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from datetime import date, time
from pathlib import Path
from typing import Protocol

from db.database import DocumentInsertResult, StoredDocument
from inbox import LocalDocumentFolders
from models.document import DocumentData, StructuredDocumentSection


class OCRService(Protocol):
    """Extract raw text from one local image."""

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw text extracted from a local image."""
        ...


class ParserService(Protocol):
    """Convert raw text into validated document data."""

    def parse(self, raw_text: str) -> DocumentData:
        """Convert raw text into validated document data."""
        ...


class RepositoryService(Protocol):
    """Persistence operations required by command handlers."""

    def __enter__(self) -> RepositoryService:
        """Open the repository context."""
        ...
    def __exit__(self, *args: object) -> None:
        """Close the repository context."""
        ...
    def insert_document(
        self, document: DocumentData, *, file_hash: str
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
        self, days_threshold: int, *, today: date | None = None
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


class SchedulerRunner(Protocol):
    """Run a blocking local scheduler."""

    def run(self) -> None:
        """Run the scheduler until interruption."""
        ...


RepositoryFactory = Callable[[], RepositoryService]
SchedulerFactory = Callable[[Callable[[], None], time], SchedulerRunner]
DocumentFoldersFactory = Callable[[Path, Path], LocalDocumentFolders]
