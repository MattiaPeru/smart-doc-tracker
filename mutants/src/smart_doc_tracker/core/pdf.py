"""Extract page-aware text from local PDF documents."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

SUPPORTED_PDF_EXTENSIONS = frozenset({".pdf"})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PDFInputError(ValueError):
    """Raised when a PDF input is missing, invalid, or unsupported."""


class PDFDependencyError(RuntimeError):
    """Raised when a local PDF or OCR dependency is unavailable."""


class PDFProcessingError(RuntimeError):
    """Raised when a local PDF cannot be decoded or processed."""


@dataclass(frozen=True, slots=True)
class ExtractedPage:
    """Text extracted from one PDF page without retaining page images."""

    page_number: int
    text: str
    used_ocr: bool


PageReader = Callable[[Path, str, int], tuple[ExtractedPage, ...]]
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut: MutantDict = {}  # type: ignore


class LocalPDFTextExtractor:
    """Read text locally from PDFs and OCR pages without a usable text layer."""

    @_mutmut_mutated(mutants_xǁLocalPDFTextExtractorǁ__init____mutmut)
    def __init__(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_orig(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_1(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 21,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_2(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters <= 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_3(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 1:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_4(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError(None)
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_5(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("XXminimum_text_characters cannot be negativeXX")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_6(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("MINIMUM_TEXT_CHARACTERS CANNOT BE NEGATIVE")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_7(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = None
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_8(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader and _read_pages_with_pymupdf
        self._minimum_text_characters = minimum_text_characters

    def xǁLocalPDFTextExtractorǁ__init____mutmut_9(
        self,
        page_reader: PageReader | None = None,
        *,
        minimum_text_characters: int = 20,
    ) -> None:
        """Configure page reading and the OCR fallback threshold."""
        if minimum_text_characters < 0:
            raise ValueError("minimum_text_characters cannot be negative")
        self._page_reader = page_reader or _read_pages_with_pymupdf
        self._minimum_text_characters = None

    @_mutmut_mutated(mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut)
    def extract_pages(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_orig(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_1(
        self, pdf_path: str | Path, *, language: str = "XXengXX"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_2(
        self, pdf_path: str | Path, *, language: str = "ENG"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_3(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = None
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_4(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(None).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_5(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(None)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_6(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_7(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError(None)

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_8(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("XXThe PDF OCR language cannot be empty.XX")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_9(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("the pdf ocr language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_10(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("THE PDF OCR LANGUAGE CANNOT BE EMPTY.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_11(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = None
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_12(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                None,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_13(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                None,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_14(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                None,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_15(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_16(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_17(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_18(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError(None) from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_19(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("XXThe PDF could not be processed.XX") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_20(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("the pdf could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_21(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("THE PDF COULD NOT BE PROCESSED.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_22(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages and not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_23(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_24(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or any(page.text.strip() for page in pages):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_25(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(None):
            raise PDFProcessingError("No readable text was found in the PDF.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_26(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError(None)
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_27(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("XXNo readable text was found in the PDF.XX")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_28(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("no readable text was found in the pdf.")
        return pages

    def xǁLocalPDFTextExtractorǁextract_pages__mutmut_29(
        self, pdf_path: str | Path, *, language: str = "eng"
    ) -> tuple[ExtractedPage, ...]:
        """Return page-aware text while keeping all processing on the host."""
        path = Path(pdf_path).expanduser()
        _validate_pdf_input(path)
        if not language.strip():
            raise PDFInputError("The PDF OCR language cannot be empty.")

        try:
            pages = self._page_reader(
                path,
                language,
                self._minimum_text_characters,
            )
        except (PDFInputError, PDFDependencyError, PDFProcessingError):
            raise
        except (OSError, RuntimeError, ValueError) as exc:
            raise PDFProcessingError("The PDF could not be processed.") from exc

        if not pages or not any(page.text.strip() for page in pages):
            raise PDFProcessingError("NO READABLE TEXT WAS FOUND IN THE PDF.")
        return pages

mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['_mutmut_orig'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_1'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_2'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_3'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_4'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_5'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_6'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_7'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_8'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁ__init____mutmut['xǁLocalPDFTextExtractorǁ__init____mutmut_9'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁ__init____mutmut_9 # type: ignore # mutmut generated

mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['_mutmut_orig'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_1'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_2'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_3'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_4'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_5'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_6'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_7'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_8'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_9'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_10'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_11'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_12'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_13'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_14'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_15'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_16'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_17'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_18'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_19'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_20'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_21'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_22'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_23'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_24'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_25'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_26'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_27'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_28'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLocalPDFTextExtractorǁextract_pages__mutmut['xǁLocalPDFTextExtractorǁextract_pages__mutmut_29'] = LocalPDFTextExtractor.xǁLocalPDFTextExtractorǁextract_pages__mutmut_29 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_pdf_input__mutmut)
def _validate_pdf_input(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_orig(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_1(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_2(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError(None)
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_3(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("XXThe input PDF does not exist.XX")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_4(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("the input pdf does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_5(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("THE INPUT PDF DOES NOT EXIST.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_6(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_7(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError(None)
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_8(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("XXThe PDF input must be a file.XX")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_9(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("the pdf input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_10(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("THE PDF INPUT MUST BE A FILE.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_11(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.upper() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_12(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


def x__validate_pdf_input__mutmut_13(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError(None)


def x__validate_pdf_input__mutmut_14(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("XXThe input file is not a supported PDF.XX")


def x__validate_pdf_input__mutmut_15(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("the input file is not a supported pdf.")


def x__validate_pdf_input__mutmut_16(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("THE INPUT FILE IS NOT A SUPPORTED PDF.")

mutants_x__validate_pdf_input__mutmut['_mutmut_orig'] = x__validate_pdf_input__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_1'] = x__validate_pdf_input__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_2'] = x__validate_pdf_input__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_3'] = x__validate_pdf_input__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_4'] = x__validate_pdf_input__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_5'] = x__validate_pdf_input__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_6'] = x__validate_pdf_input__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_7'] = x__validate_pdf_input__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_8'] = x__validate_pdf_input__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_9'] = x__validate_pdf_input__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_10'] = x__validate_pdf_input__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_11'] = x__validate_pdf_input__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_12'] = x__validate_pdf_input__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_13'] = x__validate_pdf_input__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_14'] = x__validate_pdf_input__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_15'] = x__validate_pdf_input__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_pdf_input__mutmut['x__validate_pdf_input__mutmut_16'] = x__validate_pdf_input__mutmut_16 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__read_pages_with_pymupdf__mutmut)
def _read_pages_with_pymupdf(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_orig(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_1(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            None
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_2(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "XXPyMuPDF is required for local PDF extraction.XX"
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_3(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "pymupdf is required for local pdf extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_4(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PYMUPDF IS REQUIRED FOR LOCAL PDF EXTRACTION."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_5(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = None
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_6(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(None) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_7(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError(None)
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_8(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("XXPassword-protected PDFs are not supported.XX")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_9(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("password-protected pdfs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_10(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("PASSWORD-PROTECTED PDFS ARE NOT SUPPORTED.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_11(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(None):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_12(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = None
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_13(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(None).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_14(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text(None, sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_15(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=None)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_16(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text(sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_17(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", )).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_18(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("XXtextXX", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_19(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("TEXT", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_20(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=False)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_21(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = None
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_22(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = True
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_23(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) <= minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_24(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = None
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_25(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        None
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_26(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) and page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_27(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=None) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_28(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=False) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_29(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text or not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_30(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_31(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_32(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            None
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_33(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=None,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_34(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text=None,
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_35(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=None,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_36(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_37(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_38(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_39(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index - 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_40(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 2,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_41(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="XXXX",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_42(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=True,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_43(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        break
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_44(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = None
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_45(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=None,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_46(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=None,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_47(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=None,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_48(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_49(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_50(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_51(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=301,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_52(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=False,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_53(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            None
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_54(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "XXLocal Tesseract OCR could not process a PDF page.XX"
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_55(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "local tesseract ocr could not process a pdf page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_56(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "LOCAL TESSERACT OCR COULD NOT PROCESS A PDF PAGE."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_57(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = None
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_58(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        None
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_59(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text(None, textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_60(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=None, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_61(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=None)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_62(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text(textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_63(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_64(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, )
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_65(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("XXtextXX", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_66(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("TEXT", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_67(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=False)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_68(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = None
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_69(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = False
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_70(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    None
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_71(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=None,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_72(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=None,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_73(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=None,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_74(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_75(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_76(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_77(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index - 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_78(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 2,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_79(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError(None) from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_80(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("XXThe PDF could not be processed.XX") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_81(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("the pdf could not be processed.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_82(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("THE PDF COULD NOT BE PROCESSED.") from exc
    return tuple(pages)


def x__read_pages_with_pymupdf__mutmut_83(
    path: Path,
    language: str,
    minimum_text_characters: int,
) -> tuple[ExtractedPage, ...]:
    """Read PDF pages locally and OCR pages with insufficient text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise PDFDependencyError(
            "PyMuPDF is required for local PDF extraction."
        ) from exc

    pages: list[ExtractedPage] = []
    try:
        with pymupdf.open(path) as document:  # type: ignore[no-untyped-call]
            if document.needs_pass:
                raise PDFInputError("Password-protected PDFs are not supported.")
            for page_index, page in enumerate(document):
                text = str(page.get_text("text", sort=True)).strip()
                used_ocr = False
                if len(text) < minimum_text_characters:
                    has_visual_content = bool(
                        page.get_images(full=True) or page.get_drawings()
                    )
                    if not text and not has_visual_content:
                        pages.append(
                            ExtractedPage(
                                page_number=page_index + 1,
                                text="",
                                used_ocr=False,
                            )
                        )
                        continue
                    try:
                        text_page = page.get_textpage_ocr(
                            language=language,
                            dpi=300,
                            full=True,
                        )
                    except (RuntimeError, OSError) as exc:
                        raise PDFDependencyError(
                            "Local Tesseract OCR could not process a PDF page."
                        ) from exc
                    text = str(
                        page.get_text("text", textpage=text_page, sort=True)
                    ).strip()
                    used_ocr = True
                pages.append(
                    ExtractedPage(
                        page_number=page_index + 1,
                        text=text,
                        used_ocr=used_ocr,
                    )
                )
    except PDFInputError:
        raise
    except PDFDependencyError:
        raise
    except (RuntimeError, OSError, ValueError) as exc:
        raise PDFProcessingError("The PDF could not be processed.") from exc
    return tuple(None)

mutants_x__read_pages_with_pymupdf__mutmut['_mutmut_orig'] = x__read_pages_with_pymupdf__mutmut_orig # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_1'] = x__read_pages_with_pymupdf__mutmut_1 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_2'] = x__read_pages_with_pymupdf__mutmut_2 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_3'] = x__read_pages_with_pymupdf__mutmut_3 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_4'] = x__read_pages_with_pymupdf__mutmut_4 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_5'] = x__read_pages_with_pymupdf__mutmut_5 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_6'] = x__read_pages_with_pymupdf__mutmut_6 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_7'] = x__read_pages_with_pymupdf__mutmut_7 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_8'] = x__read_pages_with_pymupdf__mutmut_8 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_9'] = x__read_pages_with_pymupdf__mutmut_9 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_10'] = x__read_pages_with_pymupdf__mutmut_10 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_11'] = x__read_pages_with_pymupdf__mutmut_11 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_12'] = x__read_pages_with_pymupdf__mutmut_12 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_13'] = x__read_pages_with_pymupdf__mutmut_13 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_14'] = x__read_pages_with_pymupdf__mutmut_14 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_15'] = x__read_pages_with_pymupdf__mutmut_15 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_16'] = x__read_pages_with_pymupdf__mutmut_16 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_17'] = x__read_pages_with_pymupdf__mutmut_17 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_18'] = x__read_pages_with_pymupdf__mutmut_18 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_19'] = x__read_pages_with_pymupdf__mutmut_19 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_20'] = x__read_pages_with_pymupdf__mutmut_20 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_21'] = x__read_pages_with_pymupdf__mutmut_21 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_22'] = x__read_pages_with_pymupdf__mutmut_22 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_23'] = x__read_pages_with_pymupdf__mutmut_23 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_24'] = x__read_pages_with_pymupdf__mutmut_24 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_25'] = x__read_pages_with_pymupdf__mutmut_25 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_26'] = x__read_pages_with_pymupdf__mutmut_26 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_27'] = x__read_pages_with_pymupdf__mutmut_27 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_28'] = x__read_pages_with_pymupdf__mutmut_28 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_29'] = x__read_pages_with_pymupdf__mutmut_29 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_30'] = x__read_pages_with_pymupdf__mutmut_30 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_31'] = x__read_pages_with_pymupdf__mutmut_31 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_32'] = x__read_pages_with_pymupdf__mutmut_32 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_33'] = x__read_pages_with_pymupdf__mutmut_33 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_34'] = x__read_pages_with_pymupdf__mutmut_34 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_35'] = x__read_pages_with_pymupdf__mutmut_35 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_36'] = x__read_pages_with_pymupdf__mutmut_36 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_37'] = x__read_pages_with_pymupdf__mutmut_37 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_38'] = x__read_pages_with_pymupdf__mutmut_38 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_39'] = x__read_pages_with_pymupdf__mutmut_39 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_40'] = x__read_pages_with_pymupdf__mutmut_40 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_41'] = x__read_pages_with_pymupdf__mutmut_41 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_42'] = x__read_pages_with_pymupdf__mutmut_42 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_43'] = x__read_pages_with_pymupdf__mutmut_43 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_44'] = x__read_pages_with_pymupdf__mutmut_44 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_45'] = x__read_pages_with_pymupdf__mutmut_45 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_46'] = x__read_pages_with_pymupdf__mutmut_46 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_47'] = x__read_pages_with_pymupdf__mutmut_47 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_48'] = x__read_pages_with_pymupdf__mutmut_48 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_49'] = x__read_pages_with_pymupdf__mutmut_49 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_50'] = x__read_pages_with_pymupdf__mutmut_50 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_51'] = x__read_pages_with_pymupdf__mutmut_51 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_52'] = x__read_pages_with_pymupdf__mutmut_52 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_53'] = x__read_pages_with_pymupdf__mutmut_53 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_54'] = x__read_pages_with_pymupdf__mutmut_54 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_55'] = x__read_pages_with_pymupdf__mutmut_55 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_56'] = x__read_pages_with_pymupdf__mutmut_56 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_57'] = x__read_pages_with_pymupdf__mutmut_57 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_58'] = x__read_pages_with_pymupdf__mutmut_58 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_59'] = x__read_pages_with_pymupdf__mutmut_59 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_60'] = x__read_pages_with_pymupdf__mutmut_60 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_61'] = x__read_pages_with_pymupdf__mutmut_61 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_62'] = x__read_pages_with_pymupdf__mutmut_62 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_63'] = x__read_pages_with_pymupdf__mutmut_63 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_64'] = x__read_pages_with_pymupdf__mutmut_64 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_65'] = x__read_pages_with_pymupdf__mutmut_65 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_66'] = x__read_pages_with_pymupdf__mutmut_66 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_67'] = x__read_pages_with_pymupdf__mutmut_67 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_68'] = x__read_pages_with_pymupdf__mutmut_68 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_69'] = x__read_pages_with_pymupdf__mutmut_69 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_70'] = x__read_pages_with_pymupdf__mutmut_70 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_71'] = x__read_pages_with_pymupdf__mutmut_71 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_72'] = x__read_pages_with_pymupdf__mutmut_72 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_73'] = x__read_pages_with_pymupdf__mutmut_73 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_74'] = x__read_pages_with_pymupdf__mutmut_74 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_75'] = x__read_pages_with_pymupdf__mutmut_75 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_76'] = x__read_pages_with_pymupdf__mutmut_76 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_77'] = x__read_pages_with_pymupdf__mutmut_77 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_78'] = x__read_pages_with_pymupdf__mutmut_78 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_79'] = x__read_pages_with_pymupdf__mutmut_79 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_80'] = x__read_pages_with_pymupdf__mutmut_80 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_81'] = x__read_pages_with_pymupdf__mutmut_81 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_82'] = x__read_pages_with_pymupdf__mutmut_82 # type: ignore # mutmut generated
mutants_x__read_pages_with_pymupdf__mutmut['x__read_pages_with_pymupdf__mutmut_83'] = x__read_pages_with_pymupdf__mutmut_83 # type: ignore # mutmut generated
