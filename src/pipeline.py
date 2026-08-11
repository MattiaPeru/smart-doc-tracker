"""Cross-component orchestration for local document persistence."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from core.file_hash import calculate_file_sha256
from db.database import DocumentInsertResult
from models.document import DocumentData


class DocumentWriter(Protocol):
    """Narrow persistence interface required by the storage pipeline."""

    def insert_document(
        self, document: DocumentData, *, file_hash: str
    ) -> DocumentInsertResult: ...


FileHasher = Callable[[str | Path], str]


@dataclass(slots=True)
class DocumentStoragePipeline:
    """Hash a local source file and persist its validated document data."""

    repository: DocumentWriter
    file_hasher: FileHasher = calculate_file_sha256

    def store(
        self, source_path: str | Path, document: DocumentData
    ) -> DocumentInsertResult:
        """Persist document data idempotently using the source file hash."""
        return self.repository.insert_document(
            document,
            file_hash=self.file_hasher(source_path),
        )
