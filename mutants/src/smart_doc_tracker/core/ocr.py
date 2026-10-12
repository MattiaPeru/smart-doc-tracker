"""Local image-to-text extraction using Tesseract OCR."""

from __future__ import annotations

from collections.abc import Callable
from contextlib import AbstractContextManager
from pathlib import Path
from typing import cast

from ..interfaces.image_loader import ImageLoader
from ..interfaces.text_reader import TextReader

SUPPORTED_IMAGE_EXTENSIONS = frozenset(
    {".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class OCRInputError(ValueError):
    """Raised when an OCR input is missing, invalid, or unsupported."""


class OCRDependencyError(RuntimeError):
    """Raised when a local OCR dependency is unavailable."""


class OCRProcessingError(RuntimeError):
    """Raised when a local image cannot be decoded or processed."""


ImagePreprocessor = Callable[[object], object]
mutants_xǁTesseractOCRǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTesseractOCRǁextract_text__mutmut: MutantDict = {}  # type: ignore


class TesseractOCR:
    """Extract raw text from supported local image files."""

    @_mutmut_mutated(mutants_xǁTesseractOCRǁ__init____mutmut)
    def __init__(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = text_reader or _read_with_tesseract
        self._image_preprocessor = image_preprocessor or _prepare_ocr_fallback

    def xǁTesseractOCRǁ__init____mutmut_orig(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = text_reader or _read_with_tesseract
        self._image_preprocessor = image_preprocessor or _prepare_ocr_fallback

    def xǁTesseractOCRǁ__init____mutmut_1(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = None
        self._text_reader = text_reader or _read_with_tesseract
        self._image_preprocessor = image_preprocessor or _prepare_ocr_fallback

    def xǁTesseractOCRǁ__init____mutmut_2(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader and _open_image
        self._text_reader = text_reader or _read_with_tesseract
        self._image_preprocessor = image_preprocessor or _prepare_ocr_fallback

    def xǁTesseractOCRǁ__init____mutmut_3(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = None
        self._image_preprocessor = image_preprocessor or _prepare_ocr_fallback

    def xǁTesseractOCRǁ__init____mutmut_4(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = text_reader and _read_with_tesseract
        self._image_preprocessor = image_preprocessor or _prepare_ocr_fallback

    def xǁTesseractOCRǁ__init____mutmut_5(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = text_reader or _read_with_tesseract
        self._image_preprocessor = None

    def xǁTesseractOCRǁ__init____mutmut_6(
        self,
        image_loader: ImageLoader | None = None,
        text_reader: TextReader | None = None,
        image_preprocessor: ImagePreprocessor | None = None,
    ) -> None:
        """Configure injectable local image loading and OCR operations."""
        self._image_loader = image_loader or _open_image
        self._text_reader = text_reader or _read_with_tesseract
        self._image_preprocessor = image_preprocessor and _prepare_ocr_fallback

    @_mutmut_mutated(mutants_xǁTesseractOCRǁextract_text__mutmut)
    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_orig(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_1(self, image_path: str | Path, *, language: str = "XXengXX") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_2(self, image_path: str | Path, *, language: str = "ENG") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_3(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = None
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_4(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(None).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_5(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(None)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_6(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(None) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_7(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = None
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_8(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(None, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_9(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=None)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_10(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_11(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, )
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_12(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = None
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_13(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(None)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_14(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = None
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_15(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(None, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_16(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=None)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_17(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_18(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, )
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_19(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    None
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_20(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "XXTesseract returned no text from either the original or the XX"
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_21(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_22(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "TESSERACT RETURNED NO TEXT FROM EITHER THE ORIGINAL OR THE "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_23(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "XXenhanced image. Ensure the document is in focus, sufficiently XX"
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_24(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_25(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "ENHANCED IMAGE. ENSURE THE DOCUMENT IS IN FOCUS, SUFFICIENTLY "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_26(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "XXlarge, and evenly lit.XX"
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_27(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "LARGE, AND EVENLY LIT."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("The image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_28(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError(None) from exc

    def xǁTesseractOCRǁextract_text__mutmut_29(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("XXThe image could not be processed.XX") from exc

    def xǁTesseractOCRǁextract_text__mutmut_30(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("the image could not be processed.") from exc

    def xǁTesseractOCRǁextract_text__mutmut_31(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw OCR text without persisting or transmitting image contents."""
        path = Path(image_path).expanduser()
        _validate_input(path)

        try:
            with self._image_loader(path) as image:
                raw_text = self._text_reader(image, lang=language)
                if raw_text.strip():
                    return raw_text

                prepared_image = self._image_preprocessor(image)
                fallback_text = self._text_reader(prepared_image, lang=language)
                if fallback_text.strip():
                    return fallback_text
                raise OCRProcessingError(
                    "Tesseract returned no text from either the original or the "
                    "enhanced image. Ensure the document is in focus, sufficiently "
                    "large, and evenly lit."
                )
        except OCRDependencyError:
            raise
        except OCRProcessingError:
            raise
        except (OSError, ValueError) as exc:
            raise OCRProcessingError("THE IMAGE COULD NOT BE PROCESSED.") from exc

mutants_xǁTesseractOCRǁ__init____mutmut['_mutmut_orig'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁ__init____mutmut['xǁTesseractOCRǁ__init____mutmut_1'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁ__init____mutmut['xǁTesseractOCRǁ__init____mutmut_2'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁ__init____mutmut['xǁTesseractOCRǁ__init____mutmut_3'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁ__init____mutmut['xǁTesseractOCRǁ__init____mutmut_4'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁ__init____mutmut['xǁTesseractOCRǁ__init____mutmut_5'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁ__init____mutmut['xǁTesseractOCRǁ__init____mutmut_6'] = TesseractOCR.xǁTesseractOCRǁ__init____mutmut_6 # type: ignore # mutmut generated

mutants_xǁTesseractOCRǁextract_text__mutmut['_mutmut_orig'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_1'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_2'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_3'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_4'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_5'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_6'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_7'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_8'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_9'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_10'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_11'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_12'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_13'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_14'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_15'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_16'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_17'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_18'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_19'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_20'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_21'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_22'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_23'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_24'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_25'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_26'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_27'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_28'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_29'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_30'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTesseractOCRǁextract_text__mutmut['xǁTesseractOCRǁextract_text__mutmut_31'] = TesseractOCR.xǁTesseractOCRǁextract_text__mutmut_31 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_input__mutmut)
def _validate_input(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_orig(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_1(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_2(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError(None)
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_3(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("XXThe input image does not exist.XX")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_4(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("the input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_5(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("THE INPUT IMAGE DOES NOT EXIST.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_6(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_7(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError(None)
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_8(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("XXThe OCR input must be a file.XX")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_9(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("the ocr input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_10(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("THE OCR INPUT MUST BE A FILE.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_11(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.upper() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_12(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("The input image format is not supported.")


def x__validate_input__mutmut_13(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError(None)


def x__validate_input__mutmut_14(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("XXThe input image format is not supported.XX")


def x__validate_input__mutmut_15(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("the input image format is not supported.")


def x__validate_input__mutmut_16(path: Path) -> None:
    """Validate that a path identifies a supported local image."""
    if not path.exists():
        raise OCRInputError("The input image does not exist.")
    if not path.is_file():
        raise OCRInputError("The OCR input must be a file.")
    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        raise OCRInputError("THE INPUT IMAGE FORMAT IS NOT SUPPORTED.")

mutants_x__validate_input__mutmut['_mutmut_orig'] = x__validate_input__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_1'] = x__validate_input__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_2'] = x__validate_input__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_3'] = x__validate_input__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_4'] = x__validate_input__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_5'] = x__validate_input__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_6'] = x__validate_input__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_7'] = x__validate_input__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_8'] = x__validate_input__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_9'] = x__validate_input__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_10'] = x__validate_input__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_11'] = x__validate_input__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_12'] = x__validate_input__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_13'] = x__validate_input__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_14'] = x__validate_input__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_15'] = x__validate_input__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_input__mutmut['x__validate_input__mutmut_16'] = x__validate_input__mutmut_16 # type: ignore # mutmut generated
mutants_x__open_image__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__open_image__mutmut)
def _open_image(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for local image loading.") from exc

    return Image.open(path)


def x__open_image__mutmut_orig(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for local image loading.") from exc

    return Image.open(path)


def x__open_image__mutmut_1(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError(None) from exc

    return Image.open(path)


def x__open_image__mutmut_2(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("XXPillow is required for local image loading.XX") from exc

    return Image.open(path)


def x__open_image__mutmut_3(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("pillow is required for local image loading.") from exc

    return Image.open(path)


def x__open_image__mutmut_4(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("PILLOW IS REQUIRED FOR LOCAL IMAGE LOADING.") from exc

    return Image.open(path)


def x__open_image__mutmut_5(path: Path) -> AbstractContextManager[object]:
    """Open a local image through Pillow."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for local image loading.") from exc

    return Image.open(None)

mutants_x__open_image__mutmut['_mutmut_orig'] = x__open_image__mutmut_orig # type: ignore # mutmut generated
mutants_x__open_image__mutmut['x__open_image__mutmut_1'] = x__open_image__mutmut_1 # type: ignore # mutmut generated
mutants_x__open_image__mutmut['x__open_image__mutmut_2'] = x__open_image__mutmut_2 # type: ignore # mutmut generated
mutants_x__open_image__mutmut['x__open_image__mutmut_3'] = x__open_image__mutmut_3 # type: ignore # mutmut generated
mutants_x__open_image__mutmut['x__open_image__mutmut_4'] = x__open_image__mutmut_4 # type: ignore # mutmut generated
mutants_x__open_image__mutmut['x__open_image__mutmut_5'] = x__open_image__mutmut_5 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__prepare_ocr_fallback__mutmut)
def _prepare_ocr_fallback(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_orig(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_1(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError(None) from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_2(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("XXPillow is required for OCR preprocessing.XX") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_3(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("pillow is required for ocr preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_4(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("PILLOW IS REQUIRED FOR OCR PREPROCESSING.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_5(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = None
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_6(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(None)
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_7(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(None, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_8(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, None))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_9(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_10(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, ))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_11(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = None
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_12(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(None)
    return ImageOps.autocontrast(grayscale_image)


def x__prepare_ocr_fallback__mutmut_13(image: object) -> object:
    """Create an in-memory grayscale, contrast-enhanced OCR fallback image."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise OCRDependencyError("Pillow is required for OCR preprocessing.") from exc

    oriented_image = ImageOps.exif_transpose(cast(Image.Image, image))
    grayscale_image = ImageOps.grayscale(oriented_image)
    return ImageOps.autocontrast(None)

mutants_x__prepare_ocr_fallback__mutmut['_mutmut_orig'] = x__prepare_ocr_fallback__mutmut_orig # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_1'] = x__prepare_ocr_fallback__mutmut_1 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_2'] = x__prepare_ocr_fallback__mutmut_2 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_3'] = x__prepare_ocr_fallback__mutmut_3 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_4'] = x__prepare_ocr_fallback__mutmut_4 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_5'] = x__prepare_ocr_fallback__mutmut_5 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_6'] = x__prepare_ocr_fallback__mutmut_6 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_7'] = x__prepare_ocr_fallback__mutmut_7 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_8'] = x__prepare_ocr_fallback__mutmut_8 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_9'] = x__prepare_ocr_fallback__mutmut_9 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_10'] = x__prepare_ocr_fallback__mutmut_10 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_11'] = x__prepare_ocr_fallback__mutmut_11 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_12'] = x__prepare_ocr_fallback__mutmut_12 # type: ignore # mutmut generated
mutants_x__prepare_ocr_fallback__mutmut['x__prepare_ocr_fallback__mutmut_13'] = x__prepare_ocr_fallback__mutmut_13 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__read_with_tesseract__mutmut)
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


def x__read_with_tesseract__mutmut_orig(image: object, *, lang: str) -> str:
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


def x__read_with_tesseract__mutmut_1(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError(None) from exc

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


def x__read_with_tesseract__mutmut_2(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("XXpytesseract is required for OCR extraction.XX") from exc

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


def x__read_with_tesseract__mutmut_3(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for ocr extraction.") from exc

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


def x__read_with_tesseract__mutmut_4(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("PYTESSERACT IS REQUIRED FOR OCR EXTRACTION.") from exc

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


def x__read_with_tesseract__mutmut_5(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(None)
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "The local Tesseract executable was not found on PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_6(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(None, lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "The local Tesseract executable was not found on PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_7(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, lang=None))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "The local Tesseract executable was not found on PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_8(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "The local Tesseract executable was not found on PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_9(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, ))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "The local Tesseract executable was not found on PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_10(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            None
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_11(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "XXThe local Tesseract executable was not found on PATH.XX"
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_12(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "the local tesseract executable was not found on path."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_13(image: object, *, lang: str) -> str:
    """Extract raw text from an image through local Tesseract."""
    try:
        import pytesseract
    except ImportError as exc:
        raise OCRDependencyError("pytesseract is required for OCR extraction.") from exc

    try:
        return str(pytesseract.image_to_string(image, lang=lang))
    except pytesseract.TesseractNotFoundError as exc:
        raise OCRDependencyError(
            "THE LOCAL TESSERACT EXECUTABLE WAS NOT FOUND ON PATH."
        ) from exc
    except pytesseract.TesseractError as exc:
        raise OCRProcessingError(
            "Tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_14(image: object, *, lang: str) -> str:
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
            None
        ) from exc


def x__read_with_tesseract__mutmut_15(image: object, *, lang: str) -> str:
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
            "XXTesseract could not extract text from the image.XX"
        ) from exc


def x__read_with_tesseract__mutmut_16(image: object, *, lang: str) -> str:
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
            "tesseract could not extract text from the image."
        ) from exc


def x__read_with_tesseract__mutmut_17(image: object, *, lang: str) -> str:
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
            "TESSERACT COULD NOT EXTRACT TEXT FROM THE IMAGE."
        ) from exc

mutants_x__read_with_tesseract__mutmut['_mutmut_orig'] = x__read_with_tesseract__mutmut_orig # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_1'] = x__read_with_tesseract__mutmut_1 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_2'] = x__read_with_tesseract__mutmut_2 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_3'] = x__read_with_tesseract__mutmut_3 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_4'] = x__read_with_tesseract__mutmut_4 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_5'] = x__read_with_tesseract__mutmut_5 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_6'] = x__read_with_tesseract__mutmut_6 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_7'] = x__read_with_tesseract__mutmut_7 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_8'] = x__read_with_tesseract__mutmut_8 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_9'] = x__read_with_tesseract__mutmut_9 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_10'] = x__read_with_tesseract__mutmut_10 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_11'] = x__read_with_tesseract__mutmut_11 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_12'] = x__read_with_tesseract__mutmut_12 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_13'] = x__read_with_tesseract__mutmut_13 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_14'] = x__read_with_tesseract__mutmut_14 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_15'] = x__read_with_tesseract__mutmut_15 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_16'] = x__read_with_tesseract__mutmut_16 # type: ignore # mutmut generated
mutants_x__read_with_tesseract__mutmut['x__read_with_tesseract__mutmut_17'] = x__read_with_tesseract__mutmut_17 # type: ignore # mutmut generated
