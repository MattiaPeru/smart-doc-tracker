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
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..interfaces.long_structured_document_parser import LongStructuredDocumentParser
from ..interfaces.notification_sender import NotificationSender
from ..interfaces.ocr_extractor import OCRExtractor
from ..interfaces.pdf_page_extractor import PDFPageExtractor
from ..interfaces.scheduler import Scheduler
from ..interfaces.structured_document_parser import StructuredDocumentParser
from ..interfaces.text_generator import TextGenerator
from ..settings import LocalReminderSettingsStore

RepositoryFactory = Callable[[], DocumentRepository]
DocumentFoldersFactory = Callable[[Path, Path], DocumentFolders]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
    document_vector_index: DocumentVectorIndex | None = None
    rag_generator: TextGenerator | None = None
    stdout: TextIO = field(default_factory=lambda: sys.stdout)
    stderr: TextIO = field(default_factory=lambda: sys.stderr)
    reminder_settings: LocalReminderSettingsStore | None = None

    @classmethod
    def with_overrides(cls, **overrides: object) -> CliDependencies:
        """Create production dependencies with optional test or embedding overrides."""
        return cls(**overrides)  # type: ignore[arg-type]
