"""Dependency container for the command-line application."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import TextIO

from cli.interfaces import (
    DocumentFoldersFactory,
    OCRService,
    ParserService,
    RepositoryFactory,
    SchedulerFactory,
)
from inbox import LocalDocumentFolders
from pipeline import LongStructuredDocumentParser, NotificationSender, PDFPageExtractor


@dataclass(slots=True)
class CliDependencies:
    """Explicit local dependencies used by command handlers."""

    ocr: OCRService | None = None
    document_parser: ParserService | None = None
    repository_factory: RepositoryFactory | None = None
    notifier: NotificationSender | None = None
    scheduler_factory: SchedulerFactory | None = None
    folders_factory: DocumentFoldersFactory = LocalDocumentFolders
    pdf_extractor: PDFPageExtractor | None = None
    long_document_parser: LongStructuredDocumentParser | None = None
    stdout: TextIO = field(default_factory=lambda: sys.stdout)
    stderr: TextIO = field(default_factory=lambda: sys.stderr)

    @classmethod
    def with_overrides(cls, **overrides: object) -> CliDependencies:
        """Create production dependencies with optional test or embedding overrides."""
        return cls(**overrides)  # type: ignore[arg-type]
