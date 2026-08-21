"""Text recognition interface for decoded images."""

from __future__ import annotations

from typing import Protocol


class TextReader(Protocol):
    """Extract text from a decoded local image."""

    def __call__(self, image: object, *, lang: str) -> str:
        """Extract text using the requested language."""
        ...
