from __future__ import annotations

import hashlib
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.models.document import DocumentData, StructuredDocumentSection
from smart_doc_tracker.pipeline import DocumentStoragePipeline


class FakeDocumentRepository:
    def __init__(self, record: StoredDocument) -> None:
        self.record = record
        self.file_hash: str | None = None
        self.sections: tuple[StructuredDocumentSection, ...] = ()
        self.sections_document_id: str | None = None

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
    ) -> DocumentInsertResult:
        self.file_hash = file_hash
        self.record = StoredDocument(
            id=self.record.id,
            file_hash=file_hash,
            document=document,
            created_at=self.record.created_at,
        )
        return DocumentInsertResult(record=self.record, inserted=True)

    def upsert_document_sections(
        self,
        document_id: str,
        sections: tuple[StructuredDocumentSection, ...],
    ) -> None:
        self.sections_document_id = document_id
        self.sections = sections


class DocumentStoragePipelineTests(TestCase):
    def test_stores_document_and_optional_sections_using_source_hash(self) -> None:
        document = DocumentData(
            document_type="invoice",
            summary="A local invoice",
            expiry_date=None,
            issue_date=None,
            extracted_data={},
        )
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=document,
            created_at=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
        )
        repository = FakeDocumentRepository(record)
        sections = (
            StructuredDocumentSection(
                chunk_number=1,
                page_from=1,
                page_to=1,
                document=document,
            ),
        )

        with TemporaryDirectory() as directory:
            source_path = Path(directory) / "invoice.png"
            source_path.write_bytes(b"local fixture")
            result = DocumentStoragePipeline(repository).store(
                source_path,
                document,
                sections=sections,
            )

        self.assertTrue(result.inserted)
        self.assertEqual(
            repository.file_hash, hashlib.sha256(b"local fixture").hexdigest()
        )
        self.assertEqual(result.record.file_hash, repository.file_hash)
        self.assertEqual(result.record.document, document)
        self.assertEqual(repository.sections_document_id, record.id)
        self.assertEqual(repository.sections, sections)
