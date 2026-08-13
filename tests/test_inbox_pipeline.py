from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from core.ocr import OCRProcessingError
from db.database import DocumentInsertResult, StoredDocument
from inbox import LocalDocumentFolders
from models.document import DocumentData
from pipeline import InboxProcessingPipeline


class FakeOCR:
    def __init__(self, *, fail_on: bytes | None = None) -> None:
        self.fail_on = fail_on
        self.calls: list[tuple[Path, str]] = []

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        path = Path(image_path)
        self.calls.append((path, language))
        if path.read_bytes() == self.fail_on:
            raise OCRProcessingError("The image could not be processed.")
        return "local OCR text"


class FakeParser:
    def __init__(self, document: DocumentData) -> None:
        self.document = document
        self.calls: list[str] = []

    def parse(self, raw_text: str) -> DocumentData:
        self.calls.append(raw_text)
        return self.document


class FakeWriter:
    def __init__(self) -> None:
        self.calls: list[tuple[DocumentData, str]] = []

    def insert_document(
        self, document: DocumentData, *, file_hash: str
    ) -> DocumentInsertResult:
        self.calls.append((document, file_hash))
        return DocumentInsertResult(
            record=StoredDocument(
                id="64b64b64b64b64b64b64b64b",
                file_hash=file_hash,
                document=document,
                created_at=datetime(2026, 8, 13, tzinfo=UTC),
            ),
            inserted=True,
        )


def _document() -> DocumentData:
    return DocumentData(
        document_type="invoice",
        summary="A local invoice",
        expiry_date=None,
        issue_date="2026-08-01",
        extracted_data={"invoice_number": "42"},
    )


class InboxProcessingPipelineTests(TestCase):
    def test_processes_supported_files_and_leaves_unsupported_entries(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "inbox"
            processed = root / "processed"
            inbox.mkdir()
            (inbox / "b.png").write_bytes(b"second")
            (inbox / "a.jpg").write_bytes(b"first")
            (inbox / "notes.txt").write_text("not a document image")
            ocr = FakeOCR()
            parser = FakeParser(_document())
            writer = FakeWriter()

            result = InboxProcessingPipeline(
                ocr=ocr,
                parser=parser,
                repository=writer,
                folders=LocalDocumentFolders(inbox, processed),
                language="ita",
            ).process()

            self.assertEqual(result.discovered, 2)
            self.assertEqual(result.processed, 2)
            self.assertEqual(result.failed, 0)
            self.assertEqual(result.skipped, 1)
            self.assertEqual([call[0].name for call in ocr.calls], ["a.jpg", "b.png"])
            self.assertTrue(all(call[1] == "ita" for call in ocr.calls))
            self.assertEqual(len(writer.calls), 2)
            self.assertTrue((processed / "a.jpg").is_file())
            self.assertTrue((processed / "b.png").is_file())
            self.assertTrue((inbox / "notes.txt").is_file())

    def test_keeps_failed_file_in_inbox_and_continues(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "inbox"
            processed = root / "processed"
            inbox.mkdir()
            (inbox / "broken.png").write_bytes(b"broken")
            (inbox / "valid.png").write_bytes(b"valid")
            writer = FakeWriter()

            result = InboxProcessingPipeline(
                ocr=FakeOCR(fail_on=b"broken"),
                parser=FakeParser(_document()),
                repository=writer,
                folders=LocalDocumentFolders(inbox, processed),
            ).process()

            self.assertEqual(result.processed, 1)
            self.assertEqual(result.failed, 1)
            self.assertTrue((inbox / "broken.png").is_file())
            self.assertTrue((processed / "valid.png").is_file())
            self.assertEqual(len(writer.calls), 1)

    def test_archive_does_not_overwrite_an_existing_processed_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "inbox"
            processed = root / "processed"
            inbox.mkdir()
            processed.mkdir()
            source = inbox / "document.png"
            source.write_bytes(b"new")
            (processed / "document.png").write_bytes(b"existing")

            destination = LocalDocumentFolders(inbox, processed).archive(source)

            self.assertEqual(destination.name, "document_1.png")
            self.assertEqual(destination.read_bytes(), b"new")
            self.assertEqual((processed / "document.png").read_bytes(), b"existing")
