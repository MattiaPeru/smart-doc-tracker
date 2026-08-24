"""JSON serialization for command-line results."""

from __future__ import annotations

import json
from typing import TextIO

from ..db.database import DocumentInsertResult, StoredDocument
from ..models.document import DocumentData
from ..pipeline import ExpirationCheckResult, InboxProcessingResult


class JsonResultSerializer:
    """Convert domain and workflow results to stable CLI JSON payloads."""

    @staticmethod
    def write(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=2))
        stream.write("\n")

    @staticmethod
    def document(document: DocumentData) -> dict[str, object]:
        """Serialize validated document data for JSON output."""
        return document.model_dump(mode="json")

    @classmethod
    def insert_result(cls, result: DocumentInsertResult) -> dict[str, object]:
        """Serialize a document insertion result."""
        return {"inserted": result.inserted, **cls.stored_document(result.record)}

    @staticmethod
    def stored_document(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def expiration_result(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "documents_found": result.documents_found,
            "notifications_sent": result.notifications_sent,
        }

    @staticmethod
    def inbox_result(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }
