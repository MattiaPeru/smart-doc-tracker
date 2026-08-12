"""Cross-component orchestration for local document workflows."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Protocol

from core.file_hash import calculate_file_sha256
from db.database import DocumentInsertResult, StoredDocument
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
