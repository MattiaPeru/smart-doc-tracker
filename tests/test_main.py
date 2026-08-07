from __future__ import annotations

from io import StringIO
from pathlib import Path
from unittest import TestCase

from core.ocr import OCRInputError
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
        self.assertEqual(stderr.getvalue(), "")
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
            stderr.getvalue(), "OCR failed: The input image does not exist.\n"
        )
        self.assertNotIn("private-filename", stderr.getvalue())
