"""Local inbox discovery and processed-file archiving."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from core.ocr import SUPPORTED_IMAGE_EXTENSIONS
from core.pdf import SUPPORTED_PDF_EXTENSIONS


SUPPORTED_DOCUMENT_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS | SUPPORTED_PDF_EXTENSIONS


class InboxError(RuntimeError):
    """Raised when local inbox files cannot be discovered or archived."""


@dataclass(frozen=True, slots=True)
class InboxScan:
    """Supported inbox files and the number of entries left untouched."""

    files: tuple[Path, ...]
    skipped: int


@dataclass(slots=True)
class LocalDocumentFolders:
    """Manage local inbox and processed folders without reading document data."""

    inbox_path: Path
    processed_path: Path

    def __init__(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        self.inbox_path = Path(inbox_path).expanduser()
        self.processed_path = Path(processed_path).expanduser()

    def scan(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: (item.name.casefold(), item.name),
            )
        except OSError as exc:
            raise InboxError("The local inbox could not be read.") from exc

        files: list[Path] = []
        skipped = 0
        for entry in entries:
            if entry.name == ".gitkeep":
                continue
            try:
                is_supported = (
                    not entry.is_symlink()
                    and entry.is_file()
                    and entry.suffix.lower() in SUPPORTED_DOCUMENT_EXTENSIONS
                )
            except OSError:
                is_supported = False
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def archive(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def _ensure_directories(self) -> None:
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The local document folders could not be created.") from exc

    def _available_destination(self, filename: str) -> Path:
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = 1
        while True:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1
