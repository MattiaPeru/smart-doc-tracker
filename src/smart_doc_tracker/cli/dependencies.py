"""Dependency container for the command-line application."""

from __future__ import annotations

import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TextIO

from ..inbox import LocalDocumentFolders
from ..interfaces.document_folders import DocumentFolders
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.long_structured_document_parser import LongStructuredDocumentParser
from ..interfaces.notification_sender import NotificationSender
from ..interfaces.ocr_extractor import OCRExtractor
from ..interfaces.pdf_page_extractor import PDFPageExtractor
from ..interfaces.scheduler import Scheduler
from ..interfaces.structured_document_parser import StructuredDocumentParser

RepositoryFactory = Callable[[], DocumentRepository]
DocumentFoldersFactory = Callable[[Path, Path], DocumentFolders]


@dataclass(slots=True)
class CliDependencies:
    """Explicit local dependencies used by command handlers."""

    ocr: OCRExtractor | None = None
    document_parser: StructuredDocumentParser | None = None
    repository_factory: RepositoryFactory | None = None
    notifier: NotificationSender | None = None
    scheduler: Scheduler | None = None
    folders_factory: DocumentFoldersFactory = LocalDocumentFolders
    pdf_extractor: PDFPageExtractor | None = None
    long_document_parser: LongStructuredDocumentParser | None = None
    stdout: TextIO = field(default_factory=lambda: sys.stdout)
    stderr: TextIO = field(default_factory=lambda: sys.stderr)

    @classmethod
    def with_overrides(cls, **overrides: object) -> CliDependencies:
        """Create production dependencies with optional test or embedding overrides."""
        return cls(**overrides)  # type: ignore[arg-type]
