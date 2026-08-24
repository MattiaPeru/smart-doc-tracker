"""OCR extraction interface for local images."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol


class OCRExtractor(Protocol):
    """Extract raw text from local images."""

    def extract_text(
        self,
        image_path: str | Path,
        *,
        language: str = "eng",
    ) -> str:
        """Extract raw text from one local image."""
        ...
