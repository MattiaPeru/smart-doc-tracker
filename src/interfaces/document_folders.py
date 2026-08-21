"""File-management interface for the local document inbox."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from inbox import InboxScan


class DocumentFolders(Protocol):
    """Scan and archive files in local document folders."""

    def scan(self) -> InboxScan:
        """Return supported files currently available in the inbox."""
        ...

    def archive(self, source_path: str | Path) -> Path:
        """Move a processed file into the local archive."""
        ...
