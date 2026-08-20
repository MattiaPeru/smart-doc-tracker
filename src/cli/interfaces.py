"""Narrow interfaces required by command-line workflows."""

from __future__ import annotations

from collections.abc import Callable
from datetime import time
from pathlib import Path
from typing import Protocol

from db.interfaces import DocumentRepository
from inbox import LocalDocumentFolders
from models.document import DocumentData


class OCRService(Protocol):
    """Extract raw text from one local image."""

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str:
        """Return raw text extracted from a local image."""
        ...


class ParserService(Protocol):
    """Convert raw text into validated document data."""

    def parse(self, raw_text: str) -> DocumentData:
        """Convert raw text into validated document data."""
        ...


class SchedulerRunner(Protocol):
    """Run a blocking local scheduler."""

    def run(self) -> None:
        """Run the scheduler until interruption."""
        ...


RepositoryFactory = Callable[[], DocumentRepository]
SchedulerFactory = Callable[[Callable[[], None], time], SchedulerRunner]
DocumentFoldersFactory = Callable[[Path, Path], LocalDocumentFolders]
