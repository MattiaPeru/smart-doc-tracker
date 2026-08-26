from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from smart_doc_tracker.core.ocr import OCRInputError, OCRProcessingError, TesseractOCR


@contextmanager
def fake_image_loader(path: Path):
    yield {"loaded_from": path}


class TesseractOCRTests(TestCase):
    def test_extract_text_reads_supported_local_image(self) -> None:
        with TemporaryDirectory() as directory:
            image_path = Path(directory) / "sample.PNG"
            image_path.write_bytes(b"local test image")
            calls: list[tuple[object, str]] = []

            def text_reader(image: object, *, lang: str) -> str:
                calls.append((image, lang))
                return "Raw OCR text\n"

            extractor = TesseractOCR(fake_image_loader, text_reader)
            result = extractor.extract_text(image_path, language="ita")

        self.assertEqual(result, "Raw OCR text\n")
        self.assertEqual(calls, [({"loaded_from": image_path}, "ita")])

    def test_retries_empty_ocr_with_an_enhanced_image(self) -> None:
        with TemporaryDirectory() as directory:
            image_path = Path(directory) / "sample.jpg"
            image_path.write_bytes(b"local test image")
            original_image = {"loaded_from": image_path}
            enhanced_image = object()
            calls: list[tuple[object, str]] = []

            def text_reader(image: object, *, lang: str) -> str:
                """Return text only for the enhanced fallback image."""
                calls.append((image, lang))
                return "" if len(calls) == 1 else "Recovered OCR text"

            extractor = TesseractOCR(
                fake_image_loader,
                text_reader,
                image_preprocessor=lambda _image: enhanced_image,
            )
            result = extractor.extract_text(image_path, language="ita")

        self.assertEqual(result, "Recovered OCR text")
        self.assertEqual(
            calls,
            [(original_image, "ita"), (enhanced_image, "ita")],
        )

    def test_reports_an_ocr_error_when_both_attempts_are_empty(self) -> None:
        with TemporaryDirectory() as directory:
            image_path = Path(directory) / "blank.jpg"
            image_path.write_bytes(b"local test image")
            extractor = TesseractOCR(
                fake_image_loader,
                lambda image, *, lang: "",
                image_preprocessor=lambda image: image,
            )

            with self.assertRaisesRegex(
                OCRProcessingError,
                "returned no text.*original.*enhanced",
            ):
                extractor.extract_text(image_path, language="ita")

    def test_extract_text_rejects_missing_input(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "missing.png"
            with self.assertRaises(OCRInputError):
                TesseractOCR(fake_image_loader, lambda image, *, lang: "").extract_text(
                    path
                )

    def test_extract_text_rejects_unsupported_input(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "unsupported.pdf"
            path.write_bytes(b"not an image")
            with self.assertRaises(OCRInputError):
                TesseractOCR(fake_image_loader, lambda image, *, lang: "").extract_text(
                    path
                )

    def test_extract_text_wraps_image_processing_errors(self) -> None:
        with TemporaryDirectory() as directory:
            image_path = Path(directory) / "broken.jpg"
            image_path.write_bytes(b"broken")

            @contextmanager
            def broken_loader(path: Path):
                raise OSError("decoder details")
                yield

            with self.assertRaisesRegex(OCRProcessingError, "could not be processed"):
                TesseractOCR(broken_loader, lambda image, *, lang: "").extract_text(
                    image_path
                )
