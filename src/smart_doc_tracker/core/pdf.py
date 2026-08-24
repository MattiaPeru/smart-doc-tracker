"""Extract page-aware text from local PDF documents."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

SUPPORTED_PDF_EXTENSIONS = frozenset({".pdf"})


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


class LocalPDFTextExtractor:
    """Read text locally from PDFs and OCR pages without a usable text layer."""

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


def _validate_pdf_input(path: Path) -> None:
    """Validate that a path identifies a supported local PDF."""
    if not path.exists():
        raise PDFInputError("The input PDF does not exist.")
    if not path.is_file():
        raise PDFInputError("The PDF input must be a file.")
    if path.suffix.lower() not in SUPPORTED_PDF_EXTENSIONS:
        raise PDFInputError("The input file is not a supported PDF.")


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
