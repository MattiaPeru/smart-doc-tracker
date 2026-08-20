from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from core.pdf import ExtractedPage, LocalPDFTextExtractor, PDFInputError


class LocalPDFTextExtractorTests(TestCase):
    def test_extracts_text_from_a_real_local_digital_pdf(self) -> None:
        import pymupdf

        with TemporaryDirectory() as directory:
            path = Path(directory) / "digital.pdf"
            document = pymupdf.open()
            page = document.new_page()
            page.insert_text((72, 72), "Offline generic PDF document")
            document.new_page()
            document.save(path)
            document.close()

            pages = LocalPDFTextExtractor().extract_pages(path)

        self.assertEqual(len(pages), 2)
        self.assertIn("Offline generic PDF document", pages[0].text)
        self.assertFalse(pages[0].used_ocr)
        self.assertEqual(pages[1].text, "")
        self.assertFalse(pages[1].used_ocr)

    def test_extracts_page_aware_text_with_injected_local_reader(self) -> None:
        calls: list[tuple[Path, str, int]] = []

        def reader(
            path: Path, language: str, minimum_characters: int
        ) -> tuple[ExtractedPage, ...]:
            calls.append((path, language, minimum_characters))
            return (
                ExtractedPage(1, "Digital page", False),
                ExtractedPage(2, "Scanned page", True),
            )

        with TemporaryDirectory() as directory:
            path = Path(directory) / "document.PDF"
            path.write_bytes(b"local pdf fixture")
            pages = LocalPDFTextExtractor(
                reader,
                minimum_text_characters=30,
            ).extract_pages(path, language="ita")

        self.assertEqual([page.page_number for page in pages], [1, 2])
        self.assertTrue(pages[1].used_ocr)
        self.assertEqual(calls, [(path, "ita", 30)])

    def test_rejects_non_pdf_input_before_reading_contents(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "document.txt"
            path.write_text("private contents")

            with self.assertRaises(PDFInputError):
                LocalPDFTextExtractor().extract_pages(path)
