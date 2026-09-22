from __future__ import annotations

import json
from datetime import UTC, date, datetime
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from smart_doc_tracker.core.ocr import OCRInputError
from smart_doc_tracker.core.parser import DocumentParsingError
from smart_doc_tracker.core.pdf import ExtractedPage
from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.inbox import LocalDocumentFolders
from smart_doc_tracker.main import run
from smart_doc_tracker.models.document import (
    DocumentData,
    ParsedLongDocument,
    StructuredDocumentSection,
)
from smart_doc_tracker.notifier.desktop import ExpirationNotification


class FakeOCR:
    def __init__(self, result: str = "", error: Exception | None = None) -> None:
        self.result = result
        self.error = error
        self.calls: list[tuple[Path, str]] = []

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        self.calls.append((Path(image_path), language))
        if self.error:
            raise self.error
        return self.result


class FakeParser:
    def __init__(self, result: DocumentData) -> None:
        self.result = result
        self.calls: list[str] = []

    def parse(self, raw_text: str) -> DocumentData:
        self.calls.append(raw_text)
        return self.result


class FailingParser:
    def parse(self, raw_text: str) -> DocumentData:
        raise DocumentParsingError(
            "The generated document data is not valid structured output.",
            generated_response="not valid JSON",
        )


class FakeRepository:
    def __init__(self, documents: list[StoredDocument] | None = None) -> None:
        self.documents = list(documents or [])
        self.insert_calls: list[tuple[DocumentData, str]] = []
        self.expiration_calls: list[tuple[int, date | None]] = []
        self.section_calls: list[tuple[str, tuple[StructuredDocumentSection, ...]]] = []
        self.update_calls: list[tuple[str, DocumentData]] = []

    def __enter__(self) -> FakeRepository:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def insert_document(
        self, document: DocumentData, *, file_hash: str
    ) -> DocumentInsertResult:
        self.insert_calls.append((document, file_hash))
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash=file_hash,
            document=document,
            created_at=datetime(2026, 8, 11, 12, 0, tzinfo=UTC),
        )
        self.documents.append(record)
        return DocumentInsertResult(record=record, inserted=True)

    def get_all_documents(self) -> list[StoredDocument]:
        return list(self.documents)

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        return next((item for item in self.documents if item.id == document_id), None)

    def update_document(
        self, document_id: str, document: DocumentData
    ) -> StoredDocument | None:
        self.update_calls.append((document_id, document))
        for index, item in enumerate(self.documents):
            if item.id == document_id:
                updated = StoredDocument(
                    id=item.id,
                    file_hash=item.file_hash,
                    document=document,
                    created_at=item.created_at,
                )
                self.documents[index] = updated
                return updated
        return None

    def set_source_file_name(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        record = self.get_document_by_id(document_id)
        if record is None:
            return None
        updated = StoredDocument(
            id=record.id,
            file_hash=record.file_hash,
            document=record.document,
            created_at=record.created_at,
            source_file_name=source_file_name,
        )
        self.documents[self.documents.index(record)] = updated
        return updated

    def get_expiring_documents(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        self.expiration_calls.append((days_threshold, today))
        return [
            item for item in self.documents if item.document.expiry_date is not None
        ]

    def upsert_document_sections(
        self,
        document_id: str,
        sections: tuple[StructuredDocumentSection, ...],
    ) -> None:
        self.section_calls.append((document_id, sections))


class FakePDFExtractor:
    def extract_pages(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        return (
            ExtractedPage(1, "First local page", False),
            ExtractedPage(2, "Second local page", True),
        )


class FakeLongParser:
    def __init__(self, document: DocumentData) -> None:
        self.document = document

    def parse_pages(self, pages: tuple[ExtractedPage, ...]) -> ParsedLongDocument:
        sections = tuple(
            StructuredDocumentSection(
                chunk_number=index,
                page_from=page.page_number,
                page_to=page.page_number,
                document=self.document,
            )
            for index, page in enumerate(pages, start=1)
        )
        return ParsedLongDocument(self.document, sections)


class FakeNotifier:
    def __init__(self) -> None:
        self.notifications: list[ExpirationNotification] = []

    def send(self, notification: ExpirationNotification) -> None:
        self.notifications.append(notification)


class ImmediateScheduler:
    def __init__(self) -> None:
        self.scheduled_times: list[str] = []

    def run(self, task: object, *, check_time: object) -> None:
        self.scheduled_times.append(str(check_time))
        assert callable(task)
        task()


class MainTests(TestCase):
    def test_run_outputs_raw_text(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        ocr = FakeOCR("Extracted locally")

        exit_code = run(
            ["sample.png", "--language", "ita"],
            ocr=ocr,
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout.getvalue(), "Extracted locally\n")
        self.assertEqual(
            stderr.getvalue(),
            "[1/1] Waiting for local Tesseract OCR to extract text...\n"
            "[1/1] OCR completed.\n",
        )
        self.assertEqual(ocr.calls, [(Path("sample.png"), "ita")])

    def test_run_reports_sanitized_ocr_error(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        ocr = FakeOCR(error=OCRInputError("The input image does not exist."))

        exit_code = run(["private-filename.png"], ocr=ocr, stdout=stdout, stderr=stderr)

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(
            stderr.getvalue(),
            "[1/1] Waiting for local Tesseract OCR to extract text...\n"
            "OCR failed: The input image does not exist.\n",
        )
        self.assertNotIn("private-filename", stderr.getvalue())

    def test_run_outputs_validated_structured_json(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        parser = FakeParser(
            DocumentData(
                document_type="invoice",
                summary="A local invoice",
                expiry_date=None,
                issue_date="2026-08-01",
                extracted_data={"invoice_number": "42"},
            )
        )

        exit_code = run(
            ["sample.png", "--structured"],
            ocr=FakeOCR("raw local text"),
            document_parser=parser,
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 0)
        self.assertIn('"document_type": "invoice"', stdout.getvalue())
        self.assertIn('"issue_date": "2026-08-01"', stdout.getvalue())
        self.assertEqual(
            stderr.getvalue(),
            "[1/2] Waiting for local Tesseract OCR to extract text...\n"
            "[1/2] OCR completed.\n"
            "[2/2] Waiting for local Ollama model 'qwen2.5:3b' to generate "
            "structured data...\n"
            "[2/2] Structured parsing completed.\n",
        )
        self.assertEqual(parser.calls, ["raw local text"])

    def test_run_does_not_output_raw_llm_response_when_parsing_fails(self) -> None:
        stdout = StringIO()
        stderr = StringIO()

        exit_code = run(
            ["sample.png", "--structured"],
            ocr=FakeOCR("raw local text"),
            document_parser=FailingParser(),
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("Parsing failed:", stderr.getvalue())
        self.assertNotIn("not valid JSON", stderr.getvalue())

    def test_run_stores_structured_document_using_source_file_hash(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        repository = FakeRepository()
        document = DocumentData(
            document_type="identity_card",
            summary="A local identity card",
            expiry_date="2030-01-01",
            issue_date=None,
            extracted_data={"document_number": "TEST-42"},
        )

        with TemporaryDirectory() as directory:
            image_path = Path(directory) / "sample.jpeg"
            image_path.write_bytes(b"offline image fixture")
            exit_code = run(
                [str(image_path), "--structured", "--store"],
                ocr=FakeOCR("raw local text"),
                document_parser=FakeParser(document),
                repository_factory=lambda: repository,
                stdout=stdout,
                stderr=stderr,
            )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertTrue(payload["inserted"])
        self.assertEqual(payload["id"], "64b64b64b64b64b64b64b64b")
        self.assertEqual(payload["document"]["document_type"], "identity_card")
        self.assertEqual(len(repository.insert_calls[0][1]), 64)
        self.assertIn("MongoDB storage completed (inserted).", stderr.getvalue())

    def test_run_processes_and_stores_a_generic_pdf_with_sections(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        repository = FakeRepository()
        document = DocumentData(
            document_type="technical_report",
            summary="A generic multi-page report",
            expiry_date=None,
            issue_date="2026-08-01",
            extracted_data={"report_number": "R-42"},
        )

        with TemporaryDirectory() as directory:
            pdf_path = Path(directory) / "report.pdf"
            pdf_path.write_bytes(b"local pdf fixture")
            exit_code = run(
                [str(pdf_path), "--structured", "--store"],
                pdf_extractor=FakePDFExtractor(),
                long_document_parser=FakeLongParser(document),
                repository_factory=lambda: repository,
                stdout=stdout,
                stderr=stderr,
            )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["document"]["document_type"], "technical_report")
        self.assertEqual(len(repository.section_calls), 1)
        self.assertEqual(len(repository.section_calls[0][1]), 2)
        self.assertIn("PDF extraction completed", stderr.getvalue())

    def test_run_lists_and_gets_stored_documents_without_ocr(self) -> None:
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="invoice",
                summary="A stored invoice",
                expiry_date=None,
                issue_date="2026-08-01",
                extracted_data={"invoice_number": "42"},
            ),
            created_at=datetime(2026, 8, 11, 12, 0, tzinfo=UTC),
        )
        repository = FakeRepository([record])

        list_stdout = StringIO()
        list_stderr = StringIO()
        list_exit_code = run(
            ["--list-stored"],
            repository_factory=lambda: repository,
            stdout=list_stdout,
            stderr=list_stderr,
        )
        get_stdout = StringIO()
        get_stderr = StringIO()
        get_exit_code = run(
            ["--get-stored", record.id],
            repository_factory=lambda: repository,
            stdout=get_stdout,
            stderr=get_stderr,
        )

        self.assertEqual(list_exit_code, 0)
        self.assertEqual(json.loads(list_stdout.getvalue())[0]["id"], record.id)
        self.assertEqual(get_exit_code, 0)
        self.assertEqual(json.loads(get_stdout.getvalue())["id"], record.id)
        self.assertIn("[1/1] Reading stored documents", list_stderr.getvalue())
        self.assertIn("[1/1] Database read completed", list_stderr.getvalue())
        self.assertIn("[1/1] Reading the stored document", get_stderr.getvalue())
        self.assertIn("[1/1] Database read completed", get_stderr.getvalue())

    def test_run_updates_selected_stored_document_fields(self) -> None:
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="invoice",
                summary="Original summary",
                expiry_date="2026-12-31",
                issue_date="2026-08-01",
                extracted_data={"invoice_number": "42"},
            ),
            created_at=datetime(2026, 8, 11, 12, 0, tzinfo=UTC),
        )
        repository = FakeRepository([record])
        stdout = StringIO()
        stderr = StringIO()

        exit_code = run(
            [
                "--update-stored",
                record.id,
                "--summary",
                "Corrected summary",
                "--expiry-date",
                "null",
                "--extracted-data-json",
                '{"invoice_number":"43","paid":true}',
            ],
            repository_factory=lambda: repository,
            stdout=stdout,
            stderr=stderr,
        )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["document"]["summary"], "Corrected summary")
        self.assertIsNone(payload["document"]["expiry_date"])
        self.assertEqual(
            payload["document"]["extracted_data"],
            {"invoice_number": "43", "paid": True},
        )
        self.assertEqual(payload["document"]["issue_date"], "2026-08-01")
        self.assertEqual(repository.update_calls[0][0], record.id)
        self.assertIn("Database update completed", stderr.getvalue())

    def test_run_rejects_invalid_stored_document_updates(self) -> None:
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="invoice",
                summary="Original summary",
                expiry_date=None,
                issue_date=None,
                extracted_data={},
            ),
            created_at=datetime(2026, 8, 11, 12, 0, tzinfo=UTC),
        )
        repository = FakeRepository([record])

        no_fields_error = StringIO()
        no_fields_code = run(
            ["--update-stored", record.id],
            repository_factory=lambda: repository,
            stderr=no_fields_error,
        )
        invalid_json_error = StringIO()
        invalid_json_code = run(
            ["--update-stored", record.id, "--extracted-data-json", "not-json"],
            repository_factory=lambda: repository,
            stderr=invalid_json_error,
        )
        invalid_date_error = StringIO()
        invalid_date_code = run(
            ["--update-stored", record.id, "--issue-date", "tomorrow"],
            repository_factory=lambda: repository,
            stderr=invalid_date_error,
        )

        self.assertEqual(no_fields_code, 2)
        self.assertIn("requires at least one edit field", no_fields_error.getvalue())
        self.assertEqual(invalid_json_code, 2)
        self.assertIn("must contain valid JSON", invalid_json_error.getvalue())
        self.assertEqual(invalid_date_code, 2)
        self.assertIn("fields are invalid", invalid_date_error.getvalue())
        self.assertEqual(repository.update_calls, [])

    def test_store_requires_structured_output(self) -> None:
        stderr = StringIO()

        exit_code = run(["sample.png", "--store"], stderr=stderr)

        self.assertEqual(exit_code, 2)
        self.assertEqual(
            stderr.getvalue(), "Input error: --store requires --structured.\n"
        )

    def test_run_checks_expirations_without_ocr(self) -> None:
        record = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="identity_card",
                summary="A stored identity card",
                expiry_date="2026-08-30",
                issue_date=None,
                extracted_data={"document_number": "PRIVATE-42"},
            ),
            created_at=datetime(2026, 8, 11, 12, 0, tzinfo=UTC),
        )
        repository = FakeRepository([record])
        notifier = FakeNotifier()
        stdout = StringIO()
        stderr = StringIO()

        exit_code = run(
            ["--check-expirations", "--days-threshold", "21"],
            repository_factory=lambda: repository,
            notifier=notifier,
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            json.loads(stdout.getvalue()),
            {"documents_found": 1, "notifications_sent": 1},
        )
        self.assertEqual(repository.expiration_calls[0][0], 21)
        self.assertEqual(len(notifier.notifications), 1)
        self.assertIn("[1/1] Checking documents expiring", stderr.getvalue())
        self.assertIn("[1/1] Expiration check completed", stderr.getvalue())

    def test_run_schedules_daily_expiration_monitor(self) -> None:
        repository = FakeRepository([])
        stderr = StringIO()
        scheduler = ImmediateScheduler()

        exit_code = run(
            ["--monitor-expirations", "--check-time", "07:15"],
            repository_factory=lambda: repository,
            notifier=FakeNotifier(),
            scheduler=scheduler,
            stdout=StringIO(),
            stderr=stderr,
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(scheduler.scheduled_times, ["07:15:00"])
        self.assertIn("scheduled daily at 07:15", stderr.getvalue())
        self.assertIn("Daily expiration check completed", stderr.getvalue())

    def test_run_processes_the_local_inbox(self) -> None:
        repository = FakeRepository()
        document = DocumentData(
            document_type="invoice",
            summary="A local invoice",
            expiry_date=None,
            issue_date="2026-08-01",
            extracted_data={"invoice_number": "42"},
        )

        with TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "inbox"
            processed = root / "processed"
            inbox.mkdir()
            (inbox / "invoice.png").write_bytes(b"offline image fixture")
            stdout = StringIO()
            stderr = StringIO()

            exit_code = run(
                [
                    "--process-inbox",
                    "--inbox-dir",
                    str(inbox),
                    "--processed-dir",
                    str(processed),
                    "--language",
                    "ita",
                ],
                ocr=FakeOCR("raw local text"),
                document_parser=FakeParser(document),
                repository_factory=lambda: repository,
                stdout=stdout,
                stderr=stderr,
            )

            self.assertTrue((processed / "invoice.png").is_file())

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            json.loads(stdout.getvalue()),
            {
                "discovered": 1,
                "processed": 1,
                "already_present": 0,
                "failed": 0,
                "skipped": 0,
            },
        )
        self.assertIn("completed for 1 file(s)", stderr.getvalue())

    def test_days_threshold_runs_the_complete_local_pipeline(self) -> None:
        repository = FakeRepository()
        notifier = FakeNotifier()
        document = DocumentData(
            document_type="insurance_policy",
            summary="A local insurance policy",
            expiry_date="2026-08-30",
            issue_date="2025-08-30",
            extracted_data={"policy_number": "42"},
        )

        with TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "inbox"
            processed = root / "processed"
            inbox.mkdir()
            (inbox / "policy.png").write_bytes(b"offline image fixture")
            stdout = StringIO()
            stderr = StringIO()

            exit_code = run(
                ["--days-threshold", "21", "--language", "ita"],
                ocr=FakeOCR("raw local text"),
                document_parser=FakeParser(document),
                repository_factory=lambda: repository,
                notifier=notifier,
                folders_factory=lambda _inbox, _processed: LocalDocumentFolders(
                    inbox,
                    processed,
                ),
                stdout=stdout,
                stderr=stderr,
            )

            self.assertTrue((processed / "policy.png").is_file())

        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["inbox"]["processed"], 1)
        self.assertEqual(payload["expirations"]["documents_found"], 1)
        self.assertEqual(repository.expiration_calls[0][0], 21)
        self.assertEqual(len(notifier.notifications), 1)
        self.assertIn("[1/2] Scanning and processing", stderr.getvalue())
        self.assertIn("[1/2] Inbox processing completed", stderr.getvalue())
        self.assertIn("[2/2] Checking documents expiring", stderr.getvalue())
        self.assertIn("[2/2] Expiration check completed", stderr.getvalue())

    def test_complete_pipeline_checks_expirations_after_inbox_failure(self) -> None:
        stored = StoredDocument(
            id="64b64b64b64b64b64b64b64b",
            file_hash="a" * 64,
            document=DocumentData(
                document_type="identity_card",
                summary="A stored identity card",
                expiry_date="2026-08-30",
                issue_date=None,
                extracted_data={},
            ),
            created_at=datetime(2026, 8, 11, 12, 0, tzinfo=UTC),
        )
        repository = FakeRepository([stored])
        notifier = FakeNotifier()

        with TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "inbox"
            inbox.mkdir()
            failed_file = inbox / "unreadable.png"
            failed_file.write_bytes(b"invalid image")
            stderr = StringIO()

            exit_code = run(
                ["--days-threshold", "30"],
                ocr=FakeOCR(error=OCRInputError("The image could not be processed.")),
                document_parser=FakeParser(stored.document),
                repository_factory=lambda: repository,
                notifier=notifier,
                folders_factory=lambda _inbox, _processed: LocalDocumentFolders(
                    inbox,
                    root / "processed",
                ),
                stdout=StringIO(),
                stderr=stderr,
            )

            self.assertTrue(failed_file.is_file())
            error_output = stderr.getvalue()
            self.assertIn("[ERROR] File 'unreadable.png'", error_output)
            self.assertIn("failed during text extraction (OCR/PDF)", error_output)
            self.assertIn(
                "OCRInputError: The image could not be processed.",
                error_output,
            )

        self.assertEqual(exit_code, 1)
        self.assertEqual(repository.expiration_calls[0][0], 30)
        self.assertEqual(len(notifier.notifications), 1)
