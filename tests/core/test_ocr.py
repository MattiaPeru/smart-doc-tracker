from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from core.ocr import OCRInputError, OCRProcessingError, TesseractOCR


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

    def test_extract_text_rejects_missing_input(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "missing.png"
            with self.assertRaises(OCRInputError):
                TesseractOCR(fake_image_loader, lambda image, *, lang: "").extract_text(path)

    def test_extract_text_rejects_unsupported_input(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "unsupported.pdf"
            path.write_bytes(b"not an image")
            with self.assertRaises(OCRInputError):
                TesseractOCR(fake_image_loader, lambda image, *, lang: "").extract_text(path)

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
