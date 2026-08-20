from __future__ import annotations

from datetime import UTC, date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from controllers.document_manager import DocumentManager
from db.database import DocumentInsertResult, StoredDocument
from models.document import DocumentData, StructuredDocumentSection


class FakeExpirationRepository:
    def __init__(self, document: StoredDocument) -> None:
        self.document = document

    def __enter__(self) -> FakeExpirationRepository:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def get_expiring_documents(
        self,
        days_threshold: int,
        *,
        today: date | None = None,
    ) -> list[StoredDocument]:
        return [self.document]

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
    ) -> DocumentInsertResult:
        self.document = StoredDocument(
            id=self.document.id,
            file_hash=file_hash,
            document=document,
            created_at=self.document.created_at,
        )
        return DocumentInsertResult(record=self.document, inserted=True)

    def get_all_documents(self) -> list[StoredDocument]:
        return [self.document]

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        return self.document if document_id == self.document.id else None

    def upsert_document_sections(
        self,
        document_id: str,
        sections: tuple[StructuredDocumentSection, ...],
    ) -> None:
        return None


class DocumentManagerTests(TestCase):
    def test_manager_checks_document_expirations(self) -> None:
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="identity_card",
                summary="A local identity card",
                expiry_date="2026-08-30",
                issue_date=None,
                extracted_data={},
            ),
            created_at=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        )
        repository = FakeExpirationRepository(record)
        manager = DocumentManager(repository)

        documents = manager.get_expiring_documents(30)

        self.assertEqual(documents, [record])

    def test_manager_inserts_and_retrieves_a_document(self) -> None:
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="invoice",
                summary="A local invoice",
                expiry_date=None,
                issue_date=None,
                extracted_data={},
            ),
            created_at=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        )
        repository = FakeExpirationRepository(record)
        manager = DocumentManager(repository)

        with TemporaryDirectory() as directory:
            source_path = Path(directory) / "invoice.png"
            source_path.write_bytes(b"local fixture")
            result = manager.insert_document(source_path, record.document)

        self.assertTrue(result.inserted)
        self.assertEqual(manager.get_document_by_id(record.id), result.record)
        self.assertEqual(manager.get_all_documents(), [result.record])
