"""Cross-component orchestration for local document workflows."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Protocol

from core.file_hash import calculate_file_sha256
from core.file_hash import FileHashingError
from core.ocr import OCRDependencyError, OCRInputError, OCRProcessingError
from core.parser import DocumentParsingError
from db.database import DatabaseError
from db.database import DocumentInsertResult, StoredDocument
from inbox import InboxError, InboxScan
from infrastructure.ollama import (
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from models.document import DocumentData
from notifier.desktop import ExpirationNotification


class DocumentWriter(Protocol):
    """Narrow persistence interface required by the storage pipeline."""

    def insert_document(
        self, document: DocumentData, *, file_hash: str
    ) -> DocumentInsertResult: ...


FileHasher = Callable[[str | Path], str]


class ExpiringDocumentReader(Protocol):
    """Narrow query interface required by expiration tracking."""

    def get_expiring_documents(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]: ...


class NotificationSender(Protocol):
    """Narrow interface for sending prepared local notifications."""

    def send(self, notification: ExpirationNotification) -> None: ...


class OCRExtractor(Protocol):
    """Narrow OCR interface required by inbox automation."""

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str: ...


class StructuredDocumentParser(Protocol):
    """Narrow structured parsing interface required by inbox automation."""

    def parse(self, raw_text: str) -> DocumentData: ...


class DocumentFolders(Protocol):
    """Narrow local file-management interface required by inbox automation."""

    def scan(self) -> InboxScan: ...
    def archive(self, source_path: str | Path) -> Path: ...


@dataclass(slots=True)
class DocumentStoragePipeline:
    """Hash a local source file and persist its validated document data."""

    repository: DocumentWriter
    file_hasher: FileHasher = calculate_file_sha256

    def store(
        self, source_path: str | Path, document: DocumentData
    ) -> DocumentInsertResult:
        """Persist document data idempotently using the source file hash."""
        return self.repository.insert_document(
            document,
            file_hash=self.file_hasher(source_path),
        )


@dataclass(frozen=True, slots=True)
class InboxProcessingResult:
    """Privacy-conscious summary of one inbox scan."""

    discovered: int
    processed: int
    already_present: int
    failed: int
    skipped: int


@dataclass(slots=True)
class InboxProcessingPipeline:
    """Run OCR, parsing, persistence, and archiving for local inbox files."""

    ocr: OCRExtractor
    parser: StructuredDocumentParser
    repository: DocumentWriter
    folders: DocumentFolders
    language: str = "eng"

    def process(self) -> InboxProcessingResult:
        """Process every supported inbox file, isolating expected per-file failures."""
        scan = self.folders.scan()
        processed = 0
        already_present = 0
        failed = 0

        storage = DocumentStoragePipeline(self.repository)
        for source_path in scan.files:
            try:
                raw_text = self.ocr.extract_text(source_path, language=self.language)
                document = self.parser.parse(raw_text)
                insert_result = storage.store(source_path, document)
                self.folders.archive(source_path)
            except (
                OCRInputError,
                OCRDependencyError,
                OCRProcessingError,
                DocumentParsingError,
                OllamaConfigurationError,
                OllamaConnectionError,
                OllamaResponseError,
                FileHashingError,
                DatabaseError,
                InboxError,
            ):
                failed += 1
                continue

            processed += 1
            if not insert_result.inserted:
                already_present += 1

        return InboxProcessingResult(
            discovered=len(scan.files),
            processed=processed,
            already_present=already_present,
            failed=failed,
            skipped=scan.skipped,
        )


@dataclass(frozen=True, slots=True)
class ExpirationCheckResult:
    """Summary of a completed expiration check."""

    documents_found: int
    notifications_sent: int


@dataclass(slots=True)
class ExpirationTrackingPipeline:
    """Query upcoming expirations and send privacy-conscious local alerts."""

    repository: ExpiringDocumentReader
    notifier: NotificationSender
    today_provider: Callable[[], date] = date.today

    def check(self, days_threshold: int = 30) -> ExpirationCheckResult:
        """Notify once for each document expiring inside the inclusive window."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")

        documents = self.repository.get_expiring_documents(
            days_threshold,
            today=self.today_provider(),
        )
        notifications_sent = 0
        for record in documents:
            expiry_date = record.document.expiry_date
            if expiry_date is None:
                continue
            document_label = record.document.document_type.replace("_", " ").title()
            self.notifier.send(
                ExpirationNotification(
                    title="Document expiration reminder",
                    message=f"{document_label} expires on {expiry_date.isoformat()}.",
                )
            )
            notifications_sent += 1

        return ExpirationCheckResult(
            documents_found=len(documents),
            notifications_sent=notifications_sent,
        )
