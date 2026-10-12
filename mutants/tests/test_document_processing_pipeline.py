from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.models.document import DocumentData, StructuredDocumentSection
from smart_doc_tracker.pipeline import (
    DocumentProcessingPipeline,
    DocumentProcessingStage,
)


class FakeOCR:
    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        return "Local extracted text"


class FakeParser:
    def __init__(self, document: DocumentData) -> None:
        self.document = document

    def parse(self, raw_text: str) -> DocumentData:
        return self.document


class FakeWriter:
    def __init__(self, record: StoredDocument) -> None:
        self.record = record

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
    ) -> DocumentInsertResult:
        return DocumentInsertResult(record=self.record, inserted=True)

    def upsert_document_sections(
        self,
        document_id: str,
        sections: tuple[StructuredDocumentSection, ...],
    ) -> None:
        return None


class FakeVectorIndex:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, DocumentData]] = []

    def upsert_document(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        self.calls.append((document_id, raw_text, document))


class DocumentProcessingPipelineTests(TestCase):
    def test_coordinates_extraction_parsing_and_storage_in_order(self) -> None:
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
        stages: list[DocumentProcessingStage] = []
        extracted_texts: list[tuple[Path, str]] = []
        vector_index = FakeVectorIndex()

        with TemporaryDirectory() as directory:
            source_path = Path(directory) / "invoice.png"
            source_path.write_bytes(b"local fixture")
            result = DocumentProcessingPipeline(
                ocr=FakeOCR(),
                parser=FakeParser(document),
                repository=FakeWriter(record),
                vector_index=vector_index,
                progress_reporter=stages.append,
                extracted_text_reporter=lambda path, text: extracted_texts.append(
                    (path, text)
                ),
            ).process(source_path, structured=True, store=True)

        self.assertEqual(result.raw_text, "Local extracted text")
        self.assertEqual(result.document, document)
        self.assertEqual(extracted_texts, [(source_path, "Local extracted text")])
        self.assertIsNotNone(result.insert_result)
        self.assertEqual(
            vector_index.calls,
            [(record.id, "Local extracted text", document)],
        )
        self.assertEqual(
            stages,
            [
                DocumentProcessingStage.EXTRACTION_STARTED,
                DocumentProcessingStage.EXTRACTION_COMPLETED,
                DocumentProcessingStage.PARSING_STARTED,
                DocumentProcessingStage.PARSING_COMPLETED,
                DocumentProcessingStage.STORAGE_STARTED,
                DocumentProcessingStage.INDEXING_STARTED,
            ],
        )
