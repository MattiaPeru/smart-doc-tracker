from __future__ import annotations

from io import StringIO
from pathlib import Path
from unittest import TestCase

from core.ocr import OCRInputError
from core.parser import DocumentParsingError
from models.document import DocumentData
from main import run


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

        exit_code = run(
            ["private-filename.png"], ocr=ocr, stdout=stdout, stderr=stderr
        )

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

    def test_run_outputs_raw_llm_response_when_parsing_fails(self) -> None:
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
        self.assertIn("Raw LLM response:\n---\nnot valid JSON\n---\n", stderr.getvalue())
