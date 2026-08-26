"""Process-local staging for documents awaiting explicit user confirmation."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock
from uuid import uuid4

from ..models.document import DocumentData, StructuredDocumentSection


class PendingDocumentError(RuntimeError):
    """Raised when a staged local document cannot be managed safely."""


@dataclass(frozen=True, slots=True)
class PendingDocument:
    """A parsed document and owned local source awaiting confirmation."""

    id: str
    file_name: str
    source_path: Path
    raw_text: str
    document: DocumentData
    sections: tuple[StructuredDocumentSection, ...]
    created_at: datetime


class PendingDocumentService:
    """Own staged uploads until they are confirmed, rejected, or shutdown."""

    def __init__(self, processed_path: str | Path = Path("data/processed")) -> None:
        """Configure the local archive destination."""
        self._processed_path = Path(processed_path).expanduser()
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()

    def add(
        self,
        source_path: Path,
        *,
        file_name: str,
        raw_text: str,
        document: DocumentData,
        sections: tuple[StructuredDocumentSection, ...] = (),
    ) -> PendingDocument:
        """Take ownership of one parsed source file."""
        item = PendingDocument(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            source_path=source_path,
            raw_text=raw_text,
            document=document,
            sections=sections,
            created_at=datetime.now(UTC),
        )
        with self._lock:
            self._items[item.id] = item
        return item

    def list(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                self._items.values(),
                key=lambda item: (item.created_at, item.id),
            )

    def get(self, pending_id: str) -> PendingDocument | None:
        """Return one pending document snapshot."""
        with self._lock:
            return self._items.get(pending_id)

    def archive(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove it from the queue."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def reject(self, pending_id: str) -> bool:
        """Discard one unconfirmed source without exposing its contents."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        return True

    def close(self) -> None:
        """Deterministically remove every still-unconfirmed temporary file."""
        with self._lock:
            items = tuple(self._items.values())
            self._items.clear()
        for item in items:
            item.source_path.unlink(missing_ok=True)

    def _available_destination(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate
