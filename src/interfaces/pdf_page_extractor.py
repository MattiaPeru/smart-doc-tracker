"""Page extraction interface for local PDF files."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from core.pdf import ExtractedPage


class PDFPageExtractor(Protocol):
    """Extract page-aware text from local PDF files."""

    def extract_pages(
        self,
        pdf_path: str | Path,
        *,
        language: str = "eng",
    ) -> tuple[ExtractedPage, ...]:
        """Extract page-aware text from one local PDF."""
        ...
