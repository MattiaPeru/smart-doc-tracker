"""Parsing interface for page-aware PDF content."""

from __future__ import annotations

from typing import Protocol

from core.pdf import ExtractedPage
from models.document import ParsedLongDocument


class LongStructuredDocumentParser(Protocol):
    """Parse page-aware PDF content into validated document data."""

    def parse_pages(self, pages: tuple[ExtractedPage, ...]) -> ParsedLongDocument:
        """Parse extracted pages into one structured document."""
        ...
