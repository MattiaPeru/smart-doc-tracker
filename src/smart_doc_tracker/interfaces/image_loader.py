"""Image loading interface for local OCR."""

from __future__ import annotations

from contextlib import AbstractContextManager
from pathlib import Path
from typing import Protocol


class ImageLoader(Protocol):
    """Open a local image as a managed resource."""

    def __call__(self, path: Path) -> AbstractContextManager[object]:
        """Open an image as a managed resource."""
        ...
