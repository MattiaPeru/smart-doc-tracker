"""Durable local staging for documents awaiting explicit confirmation."""

from __future__ import annotations

import json
import re
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
    """Persist staged uploads until they are confirmed or rejected."""

    def __init__(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is not None
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def add(
        self,
        source_path: Path,
        *,
        file_name: str,
        raw_text: str,
        document: DocumentData,
        sections: tuple[StructuredDocumentSection, ...] = (),
        identifier: str | None = None,
    ) -> PendingDocument:
        """Take durable ownership of one parsed source file."""
        identifier = identifier or uuid4().hex
        if re.fullmatch(r"[A-Za-z0-9_-]+", identifier) is None:
            raise ValueError("The pending identifier is invalid.")
        with self._lock:
            if identifier in self._items:
                raise PendingDocumentError("Pending document already exists.")
        staged_path = self._pending_path / f"{identifier}{source_path.suffix.lower()}"
        item = PendingDocument(
            id=identifier,
            file_name=Path(file_name).name,
            source_path=staged_path,
            raw_text=raw_text,
            document=document,
            sections=sections,
            created_at=datetime.now(UTC),
        )
        try:
            shutil.copy2(source_path, staged_path)
            with self._lock:
                self._items[item.id] = item
                self._persist(item)
        except Exception:
            with self._lock:
                self._items.pop(item.id, None)
            self._manifest_path(item.id).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
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
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def reject(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def close(self) -> None:
        """Leave durable confirmation items available for the next start."""

    def _load(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["page_from"]),
                        page_to=int(section["page_to"]),
                        document=DocumentData.model_validate(section["document"]),
                    )
                    for section in payload.get("sections", [])
                )
                item = PendingDocument(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    source_path=source_path,
                    raw_text=str(payload["raw_text"]),
                    document=DocumentData.model_validate(payload["document"]),
                    sections=sections,
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def _persist(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="json"),
            "sections": [
                {
                    "chunk_number": section.chunk_number,
                    "page_from": section.page_from,
                    "page_to": section.page_to,
                    "document": section.document.model_dump(mode="json"),
                }
                for section in item.sections
            ],
            "created_at": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def _manifest_path(self, pending_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._pending_path / f"{pending_id}.json"

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
