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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁPendingDocumentServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁadd__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁlist__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁarchive__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁreject__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁ_load__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁ_persist__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁ_manifest_path__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut: MutantDict = {}  # type: ignore


class PendingDocumentService:
    """Persist staged uploads until they are confirmed or rejected."""

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁ__init____mutmut)
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

    def xǁPendingDocumentServiceǁ__init____mutmut_orig(
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

    def xǁPendingDocumentServiceǁ__init____mutmut_1(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = None
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is not None
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_2(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(None).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is not None
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_3(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = None
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_4(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if (pending_path is not None) and False
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_5(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if (pending_path is not None) or True
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_6(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(None).expanduser()
            if pending_path is not None
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_7(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is None
            else self._processed_path.parent / "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_8(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is not None
            else self._processed_path.parent * "pending_confirmation"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_9(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is not None
            else self._processed_path.parent / "XXpending_confirmationXX"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_10(
        self,
        processed_path: str | Path = Path("data/processed"),
        pending_path: str | Path | None = None,
    ) -> None:
        """Configure local archive and durable confirmation staging paths."""
        self._processed_path = Path(processed_path).expanduser()
        self._pending_path = (
            Path(pending_path).expanduser()
            if pending_path is not None
            else self._processed_path.parent / "PENDING_CONFIRMATION"
        )
        self._pending_path.mkdir(parents=True, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_11(
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
        self._pending_path.mkdir(parents=None, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_12(
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
        self._pending_path.mkdir(parents=True, exist_ok=None)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_13(
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
        self._pending_path.mkdir(exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_14(
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
        self._pending_path.mkdir(parents=True, )
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_15(
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
        self._pending_path.mkdir(parents=False, exist_ok=True)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_16(
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
        self._pending_path.mkdir(parents=True, exist_ok=False)
        self._items: dict[str, PendingDocument] = {}
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_17(
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
        self._items: dict[str, PendingDocument] = None
        self._lock = Lock()
        self._load()

    def xǁPendingDocumentServiceǁ__init____mutmut_18(
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
        self._lock = None
        self._load()

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁadd__mutmut)
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

    def xǁPendingDocumentServiceǁadd__mutmut_orig(
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

    def xǁPendingDocumentServiceǁadd__mutmut_1(
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
        identifier = None
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

    def xǁPendingDocumentServiceǁadd__mutmut_2(
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
        identifier = identifier and uuid4().hex
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

    def xǁPendingDocumentServiceǁadd__mutmut_3(
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
        if re.fullmatch(None, identifier) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_4(
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
        if re.fullmatch(r"[A-Za-z0-9_-]+", None) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_5(
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
        if re.fullmatch(identifier) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_6(
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
        if re.fullmatch(r"[A-Za-z0-9_-]+", ) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_7(
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
        if re.fullmatch(r"XX[A-Za-z0-9_-]+XX", identifier) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_8(
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
        if re.fullmatch(r"[a-za-z0-9_-]+", identifier) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_9(
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
        if re.fullmatch(r"[A-ZA-Z0-9_-]+", identifier) is None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_10(
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
        if re.fullmatch(r"[A-Za-z0-9_-]+", identifier) is not None:
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

    def xǁPendingDocumentServiceǁadd__mutmut_11(
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
            raise ValueError(None)
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

    def xǁPendingDocumentServiceǁadd__mutmut_12(
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
            raise ValueError("XXThe pending identifier is invalid.XX")
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

    def xǁPendingDocumentServiceǁadd__mutmut_13(
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
            raise ValueError("the pending identifier is invalid.")
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

    def xǁPendingDocumentServiceǁadd__mutmut_14(
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
            raise ValueError("THE PENDING IDENTIFIER IS INVALID.")
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

    def xǁPendingDocumentServiceǁadd__mutmut_15(
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
            if identifier not in self._items:
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

    def xǁPendingDocumentServiceǁadd__mutmut_16(
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
                raise PendingDocumentError(None)
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

    def xǁPendingDocumentServiceǁadd__mutmut_17(
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
                raise PendingDocumentError("XXPending document already exists.XX")
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

    def xǁPendingDocumentServiceǁadd__mutmut_18(
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
                raise PendingDocumentError("pending document already exists.")
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

    def xǁPendingDocumentServiceǁadd__mutmut_19(
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
                raise PendingDocumentError("PENDING DOCUMENT ALREADY EXISTS.")
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

    def xǁPendingDocumentServiceǁadd__mutmut_20(
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
        staged_path = None
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

    def xǁPendingDocumentServiceǁadd__mutmut_21(
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
        staged_path = self._pending_path * f"{identifier}{source_path.suffix.lower()}"
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

    def xǁPendingDocumentServiceǁadd__mutmut_22(
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
        staged_path = self._pending_path / f"{identifier}{source_path.suffix.upper()}"
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

    def xǁPendingDocumentServiceǁadd__mutmut_23(
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
        item = None
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

    def xǁPendingDocumentServiceǁadd__mutmut_24(
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
            id=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_25(
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
            file_name=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_26(
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
            source_path=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_27(
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
            raw_text=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_28(
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
            document=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_29(
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
            sections=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_30(
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
            created_at=None,
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

    def xǁPendingDocumentServiceǁadd__mutmut_31(
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

    def xǁPendingDocumentServiceǁadd__mutmut_32(
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

    def xǁPendingDocumentServiceǁadd__mutmut_33(
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

    def xǁPendingDocumentServiceǁadd__mutmut_34(
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

    def xǁPendingDocumentServiceǁadd__mutmut_35(
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

    def xǁPendingDocumentServiceǁadd__mutmut_36(
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

    def xǁPendingDocumentServiceǁadd__mutmut_37(
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

    def xǁPendingDocumentServiceǁadd__mutmut_38(
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
            file_name=Path(None).name,
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

    def xǁPendingDocumentServiceǁadd__mutmut_39(
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
            created_at=datetime.now(None),
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

    def xǁPendingDocumentServiceǁadd__mutmut_40(
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
            shutil.copy2(None, staged_path)
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

    def xǁPendingDocumentServiceǁadd__mutmut_41(
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
            shutil.copy2(source_path, None)
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

    def xǁPendingDocumentServiceǁadd__mutmut_42(
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
            shutil.copy2(staged_path)
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

    def xǁPendingDocumentServiceǁadd__mutmut_43(
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
            shutil.copy2(source_path, )
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

    def xǁPendingDocumentServiceǁadd__mutmut_44(
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
                self._items[item.id] = None
                self._persist(item)
        except Exception:
            with self._lock:
                self._items.pop(item.id, None)
            self._manifest_path(item.id).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_45(
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
                self._persist(None)
        except Exception:
            with self._lock:
                self._items.pop(item.id, None)
            self._manifest_path(item.id).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_46(
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
                self._items.pop(None, None)
            self._manifest_path(item.id).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_47(
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
                self._items.pop(None)
            self._manifest_path(item.id).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_48(
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
                self._items.pop(item.id, )
            self._manifest_path(item.id).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_49(
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
            self._manifest_path(item.id).unlink(missing_ok=None)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_50(
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
            self._manifest_path(None).unlink(missing_ok=True)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_51(
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
            self._manifest_path(item.id).unlink(missing_ok=False)
            staged_path.unlink(missing_ok=True)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_52(
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
            staged_path.unlink(missing_ok=None)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_53(
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
            staged_path.unlink(missing_ok=False)
            raise
        source_path.unlink(missing_ok=True)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_54(
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
        source_path.unlink(missing_ok=None)
        return item

    def xǁPendingDocumentServiceǁadd__mutmut_55(
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
        source_path.unlink(missing_ok=False)
        return item

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁlist__mutmut)
    def list(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                self._items.values(),
                key=lambda item: (item.created_at, item.id),
            )

    def xǁPendingDocumentServiceǁlist__mutmut_orig(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                self._items.values(),
                key=lambda item: (item.created_at, item.id),
            )

    def xǁPendingDocumentServiceǁlist__mutmut_1(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                None,
                key=lambda item: (item.created_at, item.id),
            )

    def xǁPendingDocumentServiceǁlist__mutmut_2(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                self._items.values(),
                key=None,
            )

    def xǁPendingDocumentServiceǁlist__mutmut_3(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                key=lambda item: (item.created_at, item.id),
            )

    def xǁPendingDocumentServiceǁlist__mutmut_4(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                self._items.values(),
                )

    def xǁPendingDocumentServiceǁlist__mutmut_5(self) -> list[PendingDocument]:
        """Return stable pending snapshots in creation order."""
        with self._lock:
            return sorted(
                self._items.values(),
                key=lambda item: None,
            )

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁget__mutmut)
    def get(self, pending_id: str) -> PendingDocument | None:
        """Return one pending document snapshot."""
        with self._lock:
            return self._items.get(pending_id)

    def xǁPendingDocumentServiceǁget__mutmut_orig(self, pending_id: str) -> PendingDocument | None:
        """Return one pending document snapshot."""
        with self._lock:
            return self._items.get(pending_id)

    def xǁPendingDocumentServiceǁget__mutmut_1(self, pending_id: str) -> PendingDocument | None:
        """Return one pending document snapshot."""
        with self._lock:
            return self._items.get(None)

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁarchive__mutmut)
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

    def xǁPendingDocumentServiceǁarchive__mutmut_orig(self, pending_id: str) -> Path:
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

    def xǁPendingDocumentServiceǁarchive__mutmut_1(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = None
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

    def xǁPendingDocumentServiceǁarchive__mutmut_2(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(None)
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

    def xǁPendingDocumentServiceǁarchive__mutmut_3(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is not None:
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

    def xǁPendingDocumentServiceǁarchive__mutmut_4(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError(None)
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

    def xǁPendingDocumentServiceǁarchive__mutmut_5(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("XXPending document not found.XX")
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

    def xǁPendingDocumentServiceǁarchive__mutmut_6(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("pending document not found.")
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

    def xǁPendingDocumentServiceǁarchive__mutmut_7(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("PENDING DOCUMENT NOT FOUND.")
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

    def xǁPendingDocumentServiceǁarchive__mutmut_8(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=None, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_9(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=None)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_10(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_11(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, )
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_12(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=False, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_13(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=False)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_14(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = None
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_15(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(None)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_16(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(None, str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_17(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), None)
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_18(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_19(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), )
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_20(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(None), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_21(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(None))
                self._manifest_path(pending_id).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_22(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=None)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_23(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(None).unlink(missing_ok=True)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_24(self, pending_id: str) -> Path:
        """Move a confirmed source into processed and remove its manifest."""
        with self._lock:
            item = self._items.get(pending_id)
            if item is None:
                raise PendingDocumentError("Pending document not found.")
            try:
                self._processed_path.mkdir(parents=True, exist_ok=True)
                destination = self._available_destination(item.file_name)
                shutil.move(str(item.source_path), str(destination))
                self._manifest_path(pending_id).unlink(missing_ok=False)
            except OSError as exc:
                raise PendingDocumentError(
                    "The confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_25(self, pending_id: str) -> Path:
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
                    None
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_26(self, pending_id: str) -> Path:
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
                    "XXThe confirmed document could not be archived locally.XX"
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_27(self, pending_id: str) -> Path:
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
                    "the confirmed document could not be archived locally."
                ) from exc
            del self._items[pending_id]
            return destination

    def xǁPendingDocumentServiceǁarchive__mutmut_28(self, pending_id: str) -> Path:
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
                    "THE CONFIRMED DOCUMENT COULD NOT BE ARCHIVED LOCALLY."
                ) from exc
            del self._items[pending_id]
            return destination

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁreject__mutmut)
    def reject(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_orig(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_1(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = None
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_2(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(None, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_3(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_4(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, )
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_5(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is not None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_6(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return True
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_7(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=None)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_8(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=False)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_9(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=None)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_10(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(None).unlink(missing_ok=True)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_11(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=False)
        return True

    def xǁPendingDocumentServiceǁreject__mutmut_12(self, pending_id: str) -> bool:
        """Discard one unconfirmed source and its local manifest."""
        with self._lock:
            item = self._items.pop(pending_id, None)
        if item is None:
            return False
        item.source_path.unlink(missing_ok=True)
        self._manifest_path(pending_id).unlink(missing_ok=True)
        return False

    def close(self) -> None:
        """Leave durable confirmation items available for the next start."""

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁ_load__mutmut)
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

    def xǁPendingDocumentServiceǁ_load__mutmut_orig(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_1(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(None):
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

    def xǁPendingDocumentServiceǁ_load__mutmut_2(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob(None)):
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

    def xǁPendingDocumentServiceǁ_load__mutmut_3(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("XX*.jsonXX")):
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

    def xǁPendingDocumentServiceǁ_load__mutmut_4(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.JSON")):
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

    def xǁPendingDocumentServiceǁ_load__mutmut_5(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = None
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

    def xǁPendingDocumentServiceǁ_load__mutmut_6(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(None)
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

    def xǁPendingDocumentServiceǁ_load__mutmut_7(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding=None))
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

    def xǁPendingDocumentServiceǁ_load__mutmut_8(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="XXutf-8XX"))
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

    def xǁPendingDocumentServiceǁ_load__mutmut_9(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="UTF-8"))
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

    def xǁPendingDocumentServiceǁ_load__mutmut_10(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = None
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

    def xǁPendingDocumentServiceǁ_load__mutmut_11(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path * str(payload["source_file"])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_12(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(None)
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

    def xǁPendingDocumentServiceǁ_load__mutmut_13(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["XXsource_fileXX"])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_14(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["SOURCE_FILE"])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_15(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = None
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

    def xǁPendingDocumentServiceǁ_load__mutmut_16(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    None
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

    def xǁPendingDocumentServiceǁ_load__mutmut_17(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_18(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_19(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["page_from"]),
                        page_to=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_20(self) -> None:
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
                        document=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_21(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
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

    def xǁPendingDocumentServiceǁ_load__mutmut_22(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_23(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["page_from"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_24(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_25(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_26(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["XXchunk_numberXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_27(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["CHUNK_NUMBER"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_28(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_29(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["XXpage_fromXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_30(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["PAGE_FROM"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_31(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["page_from"]),
                        page_to=int(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_32(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["page_from"]),
                        page_to=int(section["XXpage_toXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_33(self) -> None:
        """Restore valid staged documents without exposing their contents."""
        for manifest_path in sorted(self._pending_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_path = self._pending_path / str(payload["source_file"])
                sections = tuple(
                    StructuredDocumentSection(
                        chunk_number=int(section["chunk_number"]),
                        page_from=int(section["page_from"]),
                        page_to=int(section["PAGE_TO"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_34(self) -> None:
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
                        document=DocumentData.model_validate(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_35(self) -> None:
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
                        document=DocumentData.model_validate(section["XXdocumentXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_36(self) -> None:
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
                        document=DocumentData.model_validate(section["DOCUMENT"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_37(self) -> None:
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
                    for section in payload.get(None, [])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_38(self) -> None:
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
                    for section in payload.get("sections", None)
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

    def xǁPendingDocumentServiceǁ_load__mutmut_39(self) -> None:
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
                    for section in payload.get([])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_40(self) -> None:
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
                    for section in payload.get("sections", )
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

    def xǁPendingDocumentServiceǁ_load__mutmut_41(self) -> None:
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
                    for section in payload.get("XXsectionsXX", [])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_42(self) -> None:
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
                    for section in payload.get("SECTIONS", [])
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

    def xǁPendingDocumentServiceǁ_load__mutmut_43(self) -> None:
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
                item = None
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_44(self) -> None:
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
                    id=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_45(self) -> None:
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
                    file_name=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_46(self) -> None:
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
                    source_path=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_47(self) -> None:
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
                    raw_text=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_48(self) -> None:
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
                    document=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_49(self) -> None:
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
                    sections=None,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_50(self) -> None:
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
                    created_at=None,
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_51(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_52(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_53(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_54(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_55(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_56(self) -> None:
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

    def xǁPendingDocumentServiceǁ_load__mutmut_57(self) -> None:
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
                    )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_58(self) -> None:
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
                    id=str(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_59(self) -> None:
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
                    id=str(payload["XXidXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_60(self) -> None:
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
                    id=str(payload["ID"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_61(self) -> None:
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
                    file_name=Path(None).name,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_62(self) -> None:
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
                    file_name=Path(str(None)).name,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_63(self) -> None:
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
                    file_name=Path(str(payload["XXfile_nameXX"])).name,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_64(self) -> None:
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
                    file_name=Path(str(payload["FILE_NAME"])).name,
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

    def xǁPendingDocumentServiceǁ_load__mutmut_65(self) -> None:
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
                    raw_text=str(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_66(self) -> None:
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
                    raw_text=str(payload["XXraw_textXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_67(self) -> None:
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
                    raw_text=str(payload["RAW_TEXT"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_68(self) -> None:
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
                    document=DocumentData.model_validate(None),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_69(self) -> None:
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
                    document=DocumentData.model_validate(payload["XXdocumentXX"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_70(self) -> None:
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
                    document=DocumentData.model_validate(payload["DOCUMENT"]),
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

    def xǁPendingDocumentServiceǁ_load__mutmut_71(self) -> None:
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
                    created_at=datetime.fromisoformat(None),
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_72(self) -> None:
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
                    created_at=datetime.fromisoformat(str(None)),
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_73(self) -> None:
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
                    created_at=datetime.fromisoformat(str(payload["XXcreated_atXX"])),
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_74(self) -> None:
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
                    created_at=datetime.fromisoformat(str(payload["CREATED_AT"])),
                )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_75(self) -> None:
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
                break
            if source_path.is_file():
                self._items[item.id] = item
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_76(self) -> None:
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
                self._items[item.id] = None
        owned_sources = {item.source_path for item in self._items.values()}
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_77(self) -> None:
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
        owned_sources = None
        for path in self._pending_path.iterdir():
            if path.is_file() and path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_78(self) -> None:
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
            if path.is_file() and path.suffix != ".json" or path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_79(self) -> None:
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
            if path.is_file() or path.suffix != ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_80(self) -> None:
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
            if path.is_file() and path.suffix == ".json" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_81(self) -> None:
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
            if path.is_file() and path.suffix != "XX.jsonXX" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_82(self) -> None:
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
            if path.is_file() and path.suffix != ".JSON" and path not in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_83(self) -> None:
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
            if path.is_file() and path.suffix != ".json" and path in owned_sources:
                path.unlink(missing_ok=True)

    def xǁPendingDocumentServiceǁ_load__mutmut_84(self) -> None:
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
                path.unlink(missing_ok=None)

    def xǁPendingDocumentServiceǁ_load__mutmut_85(self) -> None:
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
                path.unlink(missing_ok=False)

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁ_persist__mutmut)
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_orig(self, item: PendingDocument) -> None:
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_1(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = None
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_2(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "XXidXX": item.id,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_3(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "ID": item.id,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_4(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "XXfile_nameXX": item.file_name,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_5(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "FILE_NAME": item.file_name,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_6(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "XXsource_fileXX": item.source_path.name,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_7(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "SOURCE_FILE": item.source_path.name,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_8(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "XXraw_textXX": item.raw_text,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_9(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "RAW_TEXT": item.raw_text,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_10(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "XXdocumentXX": item.document.model_dump(mode="json"),
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_11(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "DOCUMENT": item.document.model_dump(mode="json"),
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_12(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode=None),
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_13(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="XXjsonXX"),
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_14(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="JSON"),
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_15(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="json"),
            "XXsectionsXX": [
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_16(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="json"),
            "SECTIONS": [
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_17(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="json"),
            "sections": [
                {
                    "XXchunk_numberXX": section.chunk_number,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_18(self, item: PendingDocument) -> None:
        """Atomically persist extracted data in the private local staging area."""
        payload = {
            "id": item.id,
            "file_name": item.file_name,
            "source_file": item.source_path.name,
            "raw_text": item.raw_text,
            "document": item.document.model_dump(mode="json"),
            "sections": [
                {
                    "CHUNK_NUMBER": section.chunk_number,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_19(self, item: PendingDocument) -> None:
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
                    "XXpage_fromXX": section.page_from,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_20(self, item: PendingDocument) -> None:
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
                    "PAGE_FROM": section.page_from,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_21(self, item: PendingDocument) -> None:
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
                    "XXpage_toXX": section.page_to,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_22(self, item: PendingDocument) -> None:
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
                    "PAGE_TO": section.page_to,
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

    def xǁPendingDocumentServiceǁ_persist__mutmut_23(self, item: PendingDocument) -> None:
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
                    "XXdocumentXX": section.document.model_dump(mode="json"),
                }
                for section in item.sections
            ],
            "created_at": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_24(self, item: PendingDocument) -> None:
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
                    "DOCUMENT": section.document.model_dump(mode="json"),
                }
                for section in item.sections
            ],
            "created_at": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_25(self, item: PendingDocument) -> None:
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
                    "document": section.document.model_dump(mode=None),
                }
                for section in item.sections
            ],
            "created_at": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_26(self, item: PendingDocument) -> None:
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
                    "document": section.document.model_dump(mode="XXjsonXX"),
                }
                for section in item.sections
            ],
            "created_at": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_27(self, item: PendingDocument) -> None:
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
                    "document": section.document.model_dump(mode="JSON"),
                }
                for section in item.sections
            ],
            "created_at": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_28(self, item: PendingDocument) -> None:
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
            "XXcreated_atXX": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_29(self, item: PendingDocument) -> None:
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
            "CREATED_AT": item.created_at.isoformat(),
        }
        destination = self._manifest_path(item.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_30(self, item: PendingDocument) -> None:
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
        destination = None
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_31(self, item: PendingDocument) -> None:
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
        destination = self._manifest_path(None)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_32(self, item: PendingDocument) -> None:
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
        temporary = None
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_33(self, item: PendingDocument) -> None:
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
        temporary = destination.with_suffix(None)
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_34(self, item: PendingDocument) -> None:
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
        temporary = destination.with_suffix("XX.json.tmpXX")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_35(self, item: PendingDocument) -> None:
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
        temporary = destination.with_suffix(".JSON.TMP")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_36(self, item: PendingDocument) -> None:
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
        temporary.write_text(None, encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_37(self, item: PendingDocument) -> None:
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
        temporary.write_text(json.dumps(payload), encoding=None)
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_38(self, item: PendingDocument) -> None:
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
        temporary.write_text(encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_39(self, item: PendingDocument) -> None:
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
        temporary.write_text(json.dumps(payload), )
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_40(self, item: PendingDocument) -> None:
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
        temporary.write_text(json.dumps(None), encoding="utf-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_41(self, item: PendingDocument) -> None:
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
        temporary.write_text(json.dumps(payload), encoding="XXutf-8XX")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_42(self, item: PendingDocument) -> None:
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
        temporary.write_text(json.dumps(payload), encoding="UTF-8")
        temporary.replace(destination)

    def xǁPendingDocumentServiceǁ_persist__mutmut_43(self, item: PendingDocument) -> None:
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
        temporary.replace(None)

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁ_manifest_path__mutmut)
    def _manifest_path(self, pending_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._pending_path / f"{pending_id}.json"

    def xǁPendingDocumentServiceǁ_manifest_path__mutmut_orig(self, pending_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._pending_path / f"{pending_id}.json"

    def xǁPendingDocumentServiceǁ_manifest_path__mutmut_1(self, pending_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._pending_path * f"{pending_id}.json"

    @_mutmut_mutated(mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut)
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

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_orig(self, file_name: str) -> Path:
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

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_1(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = None
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_2(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path * file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_3(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = None
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_4(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 2
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_5(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = None
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_6(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(None)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_7(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = None
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_8(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path * (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_9(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter = 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_10(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter -= 1
        return candidate

    def xǁPendingDocumentServiceǁ_available_destination__mutmut_11(self, file_name: str) -> Path:
        """Return a collision-free path inside the configured archive."""
        candidate = self._processed_path / file_name
        counter = 1
        while candidate.exists():
            source_name = Path(file_name)
            candidate = self._processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            counter += 2
        return candidate

mutants_xǁPendingDocumentServiceǁ__init____mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_12'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_13'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_14'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_15'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_16'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_17'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ__init____mutmut['xǁPendingDocumentServiceǁ__init____mutmut_18'] = PendingDocumentService.xǁPendingDocumentServiceǁ__init____mutmut_18 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁadd__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_12'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_13'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_14'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_15'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_16'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_17'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_18'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_19'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_20'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_21'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_22'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_23'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_24'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_25'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_26'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_27'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_28'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_29'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_30'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_31'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_32'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_33'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_34'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_35'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_36'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_37'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_38'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_39'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_40'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_41'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_42'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_43'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_44'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_45'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_46'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_47'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_48'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_49'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_50'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_51'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_52'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_53'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_54'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁadd__mutmut['xǁPendingDocumentServiceǁadd__mutmut_55'] = PendingDocumentService.xǁPendingDocumentServiceǁadd__mutmut_55 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁlist__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁlist__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁlist__mutmut['xǁPendingDocumentServiceǁlist__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁlist__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁlist__mutmut['xǁPendingDocumentServiceǁlist__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁlist__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁlist__mutmut['xǁPendingDocumentServiceǁlist__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁlist__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁlist__mutmut['xǁPendingDocumentServiceǁlist__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁlist__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁlist__mutmut['xǁPendingDocumentServiceǁlist__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁlist__mutmut_5 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁget__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁget__mutmut['xǁPendingDocumentServiceǁget__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁget__mutmut_1 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁarchive__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_12'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_13'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_14'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_15'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_16'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_17'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_18'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_19'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_20'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_21'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_22'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_23'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_24'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_25'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_26'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_27'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁarchive__mutmut['xǁPendingDocumentServiceǁarchive__mutmut_28'] = PendingDocumentService.xǁPendingDocumentServiceǁarchive__mutmut_28 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁreject__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁreject__mutmut['xǁPendingDocumentServiceǁreject__mutmut_12'] = PendingDocumentService.xǁPendingDocumentServiceǁreject__mutmut_12 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁ_load__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_12'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_13'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_14'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_15'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_16'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_17'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_18'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_19'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_20'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_21'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_22'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_23'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_24'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_25'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_26'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_27'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_28'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_29'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_30'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_31'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_32'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_33'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_34'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_35'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_36'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_37'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_38'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_39'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_40'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_41'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_42'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_43'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_44'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_45'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_46'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_47'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_48'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_49'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_50'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_51'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_52'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_53'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_54'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_55'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_55 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_56'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_56 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_57'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_57 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_58'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_58 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_59'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_59 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_60'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_60 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_61'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_61 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_62'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_62 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_63'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_63 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_64'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_64 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_65'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_65 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_66'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_66 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_67'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_67 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_68'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_68 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_69'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_69 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_70'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_70 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_71'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_71 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_72'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_72 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_73'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_73 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_74'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_74 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_75'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_75 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_76'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_76 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_77'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_77 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_78'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_78 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_79'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_79 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_80'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_80 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_81'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_81 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_82'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_82 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_83'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_83 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_84'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_84 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_load__mutmut['xǁPendingDocumentServiceǁ_load__mutmut_85'] = PendingDocumentService.xǁPendingDocumentServiceǁ_load__mutmut_85 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁ_persist__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_12'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_13'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_14'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_15'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_16'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_17'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_18'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_19'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_20'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_21'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_22'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_23'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_24'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_25'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_26'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_27'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_28'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_29'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_30'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_31'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_32'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_33'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_34'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_35'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_36'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_37'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_38'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_39'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_40'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_41'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_42'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_persist__mutmut['xǁPendingDocumentServiceǁ_persist__mutmut_43'] = PendingDocumentService.xǁPendingDocumentServiceǁ_persist__mutmut_43 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁ_manifest_path__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁ_manifest_path__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_manifest_path__mutmut['xǁPendingDocumentServiceǁ_manifest_path__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁ_manifest_path__mutmut_1 # type: ignore # mutmut generated

mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['_mutmut_orig'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_1'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_2'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_3'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_4'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_5'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_6'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_7'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_8'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_9'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_10'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPendingDocumentServiceǁ_available_destination__mutmut['xǁPendingDocumentServiceǁ_available_destination__mutmut_11'] = PendingDocumentService.xǁPendingDocumentServiceǁ_available_destination__mutmut_11 # type: ignore # mutmut generated
