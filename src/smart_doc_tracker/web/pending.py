"""Durable local staging for documents awaiting explicit confirmation."""

from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from pathlib import Path
from secrets import token_hex
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
    confirmation_document: DocumentData | None = None
    insertion_document_id: str | None = None
    archived_file_name: str | None = None
    file_hash: str | None = None
    is_manual: bool = False
    cancelling: bool = False
    index_failures: int = 0


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

    def add_manual(self, document: DocumentData) -> PendingDocument:
        """Durably stage a user-authored document for coordinated insertion."""
        identifier = uuid4().hex
        source_path = self._pending_path / f"{identifier}.manual"
        item = PendingDocument(
            id=identifier,
            file_name="Manual document",
            source_path=source_path,
            raw_text="",
            document=document,
            sections=(),
            created_at=datetime.now(UTC),
            confirmation_document=document,
            file_hash=token_hex(32),
            is_manual=True,
        )
        try:
            source_path.touch(exist_ok=False)
            with self._lock:
                self._persist(item)
                self._items[item.id] = item
        except Exception as exc:
            self._manifest_path(item.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise PendingDocumentError(
                "The manual document could not be staged locally."
            ) from exc
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

    def insertion_ids(self) -> frozenset[str]:
        """Return IDs that must stay hidden until both stores commit."""
        with self._lock:
            return frozenset(
                item.insertion_document_id
                for item in self._items.values()
                if item.confirmation_document is not None
                and item.insertion_document_id is not None
            )

    def insertion_hashes(self) -> frozenset[str]:
        """Return source hashes that are still awaiting both local stores."""
        with self._lock:
            return frozenset(
                item.file_hash
                for item in self._items.values()
                if item.confirmation_document is not None and item.file_hash is not None
            )

    def begin_insertion(
        self, pending_id: str, document: DocumentData, *, file_hash: str
    ) -> PendingDocument:
        """Durably record the user's confirmation before touching either store."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            if item.cancelling:
                raise PendingDocumentError("This document is being cancelled.")
            updated = replace(item, confirmation_document=document, file_hash=file_hash)
            self._persist(updated)
            self._items[pending_id] = updated
            return updated

    def mark_cancelling(self, pending_id: str) -> PendingDocument:
        """Stop automatic retries before cleaning a partial insertion."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            updated = replace(item, cancelling=True)
            self._persist(updated)
            self._items[pending_id] = updated
            return updated

    def record_insertion_id(self, pending_id: str, document_id: str) -> None:
        """Track a partial local insertion so rejection can remove it."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            updated = replace(item, insertion_document_id=document_id)
            self._persist(updated)
            self._items[pending_id] = updated

    def record_index_failure(self, pending_id: str) -> int:
        """Persist one failed indexing attempt and return its total."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            updated = replace(item, index_failures=item.index_failures + 1)
            self._persist(updated)
            self._items[pending_id] = updated
            return updated.index_failures

    def archive(self, pending_id: str) -> Path:
        """Move a confirmed source while retaining its recovery manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                updated = replace(item, archived_file_name=destination.name)
                self._persist(updated)
                shutil.move(str(item.source_path), str(destination))
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            self._items[pending_id] = updated
            return destination

    def finish_archive(self, pending_id: str) -> None:
        """Forget a staged item only after its database link is verified."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None or item.archived_file_name is None:
                raise PendingDocumentError("The archived document is unavailable.")
            self._manifest_path(pending_id).unlink()
            del self._items[pending_id]

    def restore_archive(self, item: PendingDocument, archived_path: Path) -> None:
        """Return a source to confirmation staging after a later failure."""
        with self._lock:
            current = self._items.get(item.id)
            if current is None or item.source_path.exists():
                raise PendingDocumentError(
                    "The confirmation source cannot be restored."
                )
            if archived_path.parent.resolve() != self._processed_path.resolve():
                raise PendingDocumentError(
                    "The archived source is outside the archive."
                )
            shutil.move(str(archived_path), str(item.source_path))
            restored = replace(current, archived_file_name=None)
            self._persist(restored)
            self._items[item.id] = restored

    def reject(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                return False
            item.source_path.unlink(missing_ok=True)
            if item.archived_file_name is not None:
                (self._processed_path / item.archived_file_name).unlink(missing_ok=True)
            self._manifest_path(pending_id).unlink(missing_ok=True)
            del self._items[pending_id]
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
                    confirmation_document=(
                        DocumentData.model_validate(payload["confirmation_document"])
                        if payload.get("confirmation_document") is not None
                        else None
                    ),
                    insertion_document_id=payload.get("insertion_document_id"),
                    archived_file_name=payload.get("archived_file_name"),
                    file_hash=payload.get("file_hash"),
                    is_manual=bool(payload.get("is_manual", False)),
                    cancelling=bool(payload.get("cancelling", False)),
                    index_failures=int(payload.get("index_failures", 0)),
                )
                if (
                    re.fullmatch(r"[A-Za-z0-9_-]+", item.id) is None
                    or manifest_path != self._manifest_path(item.id)
                    or source_path.parent != self._pending_path
                    or (
                        item.archived_file_name is not None
                        and (
                            not isinstance(item.archived_file_name, str)
                            or Path(item.archived_file_name).name
                            != item.archived_file_name
                        )
                    )
                ):
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            archived_path = (
                self._processed_path / item.archived_file_name
                if item.archived_file_name is not None
                else None
            )
            if source_path.is_file() or (
                archived_path is not None and archived_path.is_file()
            ):
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
            "confirmation_document": (
                item.confirmation_document.model_dump(mode="json")
                if item.confirmation_document is not None
                else None
            ),
            "insertion_document_id": item.insertion_document_id,
            "archived_file_name": item.archived_file_name,
            "file_hash": item.file_hash,
            "is_manual": item.is_manual,
            "cancelling": item.cancelling,
            "index_failures": item.index_failures,
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
