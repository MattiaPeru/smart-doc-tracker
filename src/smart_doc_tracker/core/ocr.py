"""Local image-to-text extraction using Tesseract OCR."""

from __future__ import annotations

from contextlib import AbstractContextManager
from pathlib import Path

from ..interfaces.image_loader import ImageLoader
from ..interfaces.text_reader import TextReader

SUPPORTED_IMAGE_EXTENSIONS = frozenset(
    {".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}
)


class OCRInputError(ValueError):
    """Raised when an OCR input is missing, invalid, or unsupported."""


class OCRDependencyError(RuntimeError):
    """Raised when a local OCR dependency is unavailable."""


class OCRProcessingError(RuntimeError):
    """Raised when a local image cannot be decoded or processed."""


class TesseractOCR:
    """Extract raw text from supported local image files."""

    def __init__(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = text_reader or _read_with_tesseract

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                return self._text_reader(image, lang=language)
        except OCRDependencyError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc


def _validate_input(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def _open_image(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for local image loading.") from exc

    return Image.open(path)


def _read_with_tesseract(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "The local Tesseract executable was not found on PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc
