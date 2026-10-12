"""Local inbox discovery and processed-file archiving."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from .core.ocr import SUPPORTED_IMAGE_EXTENSIONS
from .core.pdf import SUPPORTED_PDF_EXTENSIONS

SUPPORTED_DOCUMENT_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS | SUPPORTED_PDF_EXTENSIONS


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class InboxError(RuntimeError):
    """Raised when local inbox files cannot be discovered or archived."""


@dataclass(frozen=True, slots=True)
class InboxScan:
    """Supported inbox files and the number of entries left untouched."""

    files: tuple[Path, ...]
    skipped: int
mutants_xǁLocalDocumentFoldersǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalDocumentFoldersǁscan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalDocumentFoldersǁarchive__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut: MutantDict = {}  # type: ignore


@dataclass(slots=True)
class LocalDocumentFolders:
    """Manage local inbox and processed folders without reading document data."""

    inbox_path: Path
    processed_path: Path

    @_mutmut_mutated(mutants_xǁLocalDocumentFoldersǁ__init____mutmut)
    def __init__(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        """Configure local inbox and processed-folder paths."""
        self.inbox_path = Path(inbox_path).expanduser()
        self.processed_path = Path(processed_path).expanduser()

    def xǁLocalDocumentFoldersǁ__init____mutmut_orig(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        """Configure local inbox and processed-folder paths."""
        self.inbox_path = Path(inbox_path).expanduser()
        self.processed_path = Path(processed_path).expanduser()

    def xǁLocalDocumentFoldersǁ__init____mutmut_1(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        """Configure local inbox and processed-folder paths."""
        self.inbox_path = None
        self.processed_path = Path(processed_path).expanduser()

    def xǁLocalDocumentFoldersǁ__init____mutmut_2(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        """Configure local inbox and processed-folder paths."""
        self.inbox_path = Path(None).expanduser()
        self.processed_path = Path(processed_path).expanduser()

    def xǁLocalDocumentFoldersǁ__init____mutmut_3(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        """Configure local inbox and processed-folder paths."""
        self.inbox_path = Path(inbox_path).expanduser()
        self.processed_path = None

    def xǁLocalDocumentFoldersǁ__init____mutmut_4(
        self,
        inbox_path: str | Path = Path("data/inbox"),
        processed_path: str | Path = Path("data/processed"),
    ) -> None:
        """Configure local inbox and processed-folder paths."""
        self.inbox_path = Path(inbox_path).expanduser()
        self.processed_path = Path(None).expanduser()

    @_mutmut_mutated(mutants_xǁLocalDocumentFoldersǁscan__mutmut)
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

    def xǁLocalDocumentFoldersǁscan__mutmut_orig(self) -> InboxScan:
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

    def xǁLocalDocumentFoldersǁscan__mutmut_1(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = None
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

    def xǁLocalDocumentFoldersǁscan__mutmut_2(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                None,
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

    def xǁLocalDocumentFoldersǁscan__mutmut_3(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=None,
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

    def xǁLocalDocumentFoldersǁscan__mutmut_4(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
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

    def xǁLocalDocumentFoldersǁscan__mutmut_5(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
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

    def xǁLocalDocumentFoldersǁscan__mutmut_6(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: None,
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

    def xǁLocalDocumentFoldersǁscan__mutmut_7(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: (item.name.casefold(), item.name),
            )
        except OSError as exc:
            raise InboxError(None) from exc

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

    def xǁLocalDocumentFoldersǁscan__mutmut_8(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: (item.name.casefold(), item.name),
            )
        except OSError as exc:
            raise InboxError("XXThe local inbox could not be read.XX") from exc

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

    def xǁLocalDocumentFoldersǁscan__mutmut_9(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: (item.name.casefold(), item.name),
            )
        except OSError as exc:
            raise InboxError("the local inbox could not be read.") from exc

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

    def xǁLocalDocumentFoldersǁscan__mutmut_10(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: (item.name.casefold(), item.name),
            )
        except OSError as exc:
            raise InboxError("THE LOCAL INBOX COULD NOT BE READ.") from exc

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

    def xǁLocalDocumentFoldersǁscan__mutmut_11(self) -> InboxScan:
        """Create the folder structure and return supported regular files."""
        self._ensure_directories()
        try:
            entries = sorted(
                self.inbox_path.iterdir(),
                key=lambda item: (item.name.casefold(), item.name),
            )
        except OSError as exc:
            raise InboxError("The local inbox could not be read.") from exc

        files: list[Path] = None
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

    def xǁLocalDocumentFoldersǁscan__mutmut_12(self) -> InboxScan:
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
        skipped = None
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

    def xǁLocalDocumentFoldersǁscan__mutmut_13(self) -> InboxScan:
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
        skipped = 1
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

    def xǁLocalDocumentFoldersǁscan__mutmut_14(self) -> InboxScan:
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
            if entry.name != ".gitkeep":
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

    def xǁLocalDocumentFoldersǁscan__mutmut_15(self) -> InboxScan:
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
            if entry.name == "XX.gitkeepXX":
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

    def xǁLocalDocumentFoldersǁscan__mutmut_16(self) -> InboxScan:
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
            if entry.name == ".GITKEEP":
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

    def xǁLocalDocumentFoldersǁscan__mutmut_17(self) -> InboxScan:
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
                break
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

    def xǁLocalDocumentFoldersǁscan__mutmut_18(self) -> InboxScan:
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
                is_supported = None
            except OSError:
                is_supported = False
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_19(self) -> InboxScan:
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
                    and entry.is_file() or entry.suffix.lower() in SUPPORTED_DOCUMENT_EXTENSIONS
                )
            except OSError:
                is_supported = False
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_20(self) -> InboxScan:
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
                    not entry.is_symlink() or entry.is_file()
                    and entry.suffix.lower() in SUPPORTED_DOCUMENT_EXTENSIONS
                )
            except OSError:
                is_supported = False
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_21(self) -> InboxScan:
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
                    entry.is_symlink()
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

    def xǁLocalDocumentFoldersǁscan__mutmut_22(self) -> InboxScan:
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
                    and entry.suffix.upper() in SUPPORTED_DOCUMENT_EXTENSIONS
                )
            except OSError:
                is_supported = False
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_23(self) -> InboxScan:
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
                    and entry.suffix.lower() not in SUPPORTED_DOCUMENT_EXTENSIONS
                )
            except OSError:
                is_supported = False
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_24(self) -> InboxScan:
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
                is_supported = None
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_25(self) -> InboxScan:
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
                is_supported = True
            if is_supported:
                files.append(entry)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_26(self) -> InboxScan:
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
                files.append(None)
            else:
                skipped += 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_27(self) -> InboxScan:
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
                skipped = 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_28(self) -> InboxScan:
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
                skipped -= 1
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_29(self) -> InboxScan:
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
                skipped += 2
        return InboxScan(files=tuple(files), skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_30(self) -> InboxScan:
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
        return InboxScan(files=None, skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_31(self) -> InboxScan:
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
        return InboxScan(files=tuple(files), skipped=None)

    def xǁLocalDocumentFoldersǁscan__mutmut_32(self) -> InboxScan:
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
        return InboxScan(skipped=skipped)

    def xǁLocalDocumentFoldersǁscan__mutmut_33(self) -> InboxScan:
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
        return InboxScan(files=tuple(files), )

    def xǁLocalDocumentFoldersǁscan__mutmut_34(self) -> InboxScan:
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
        return InboxScan(files=tuple(None), skipped=skipped)

    @_mutmut_mutated(mutants_xǁLocalDocumentFoldersǁarchive__mutmut)
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

    def xǁLocalDocumentFoldersǁarchive__mutmut_orig(self, source_path: str | Path) -> Path:
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

    def xǁLocalDocumentFoldersǁarchive__mutmut_1(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = None
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

    def xǁLocalDocumentFoldersǁarchive__mutmut_2(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(None)
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

    def xǁLocalDocumentFoldersǁarchive__mutmut_3(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() == self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_4(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError(None)
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_5(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("XXOnly files inside the local inbox can be archived.XX")
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_6(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_7(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("ONLY FILES INSIDE THE LOCAL INBOX CAN BE ARCHIVED.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_8(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = None
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_9(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(None)
            shutil.move(str(source), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_10(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(None, str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_11(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), None)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_12(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_13(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), )
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_14(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(None), str(destination))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_15(self, source_path: str | Path) -> Path:
        """Move one inbox file to processed without overwriting an existing file."""
        self._ensure_directories()
        source = Path(source_path)
        try:
            if source.parent.resolve() != self.inbox_path.resolve():
                raise InboxError("Only files inside the local inbox can be archived.")
            destination = self._available_destination(source.name)
            shutil.move(str(source), str(None))
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError("The processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_16(self, source_path: str | Path) -> Path:
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
            raise InboxError(None) from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_17(self, source_path: str | Path) -> Path:
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
            raise InboxError("XXThe processed document could not be archived.XX") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_18(self, source_path: str | Path) -> Path:
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
            raise InboxError("the processed document could not be archived.") from exc
        return destination

    def xǁLocalDocumentFoldersǁarchive__mutmut_19(self, source_path: str | Path) -> Path:
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
            raise InboxError("THE PROCESSED DOCUMENT COULD NOT BE ARCHIVED.") from exc
        return destination

    @_mutmut_mutated(mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut)
    def _ensure_directories(self) -> None:
        """Create and validate the configured local directories."""
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
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_orig(self) -> None:
        """Create and validate the configured local directories."""
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
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_1(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = None
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_2(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = None
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_3(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox != processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_4(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError(None)
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_5(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("XXInbox and processed folders must be different.XX")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_6(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_7(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("INBOX AND PROCESSED FOLDERS MUST BE DIFFERENT.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_8(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=None, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_9(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=None)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_10(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_11(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, )
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_12(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=False, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_13(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=False)
            self.processed_path.mkdir(parents=True, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_14(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=None, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_15(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=None)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_16(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_17(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, )
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_18(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=False, exist_ok=True)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_19(self) -> None:
        """Create and validate the configured local directories."""
        try:
            inbox = self.inbox_path.resolve()
            processed = self.processed_path.resolve()
            if inbox == processed:
                raise InboxError("Inbox and processed folders must be different.")
            self.inbox_path.mkdir(parents=True, exist_ok=True)
            self.processed_path.mkdir(parents=True, exist_ok=False)
        except InboxError:
            raise
        except OSError as exc:
            raise InboxError(
                "The local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_20(self) -> None:
        """Create and validate the configured local directories."""
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
            raise InboxError(
                None
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_21(self) -> None:
        """Create and validate the configured local directories."""
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
            raise InboxError(
                "XXThe local document folders could not be created.XX"
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_22(self) -> None:
        """Create and validate the configured local directories."""
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
            raise InboxError(
                "the local document folders could not be created."
            ) from exc

    def xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_23(self) -> None:
        """Create and validate the configured local directories."""
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
            raise InboxError(
                "THE LOCAL DOCUMENT FOLDERS COULD NOT BE CREATED."
            ) from exc

    @_mutmut_mutated(mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut)
    def _available_destination(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
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

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_orig(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
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

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_1(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = None
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

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_2(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path * filename
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

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_3(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if candidate.exists():
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

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_4(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = None
        counter = 1
        while True:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_5(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(None)
        counter = 1
        while True:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_6(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = None
        while True:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_7(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = 2
        while True:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_8(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = 1
        while False:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_9(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = 1
        while True:
            candidate = None
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_10(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = 1
        while True:
            candidate = self.processed_path * (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_11(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
        candidate = self.processed_path / filename
        if not candidate.exists():
            return candidate

        source_name = Path(filename)
        counter = 1
        while True:
            candidate = self.processed_path / (
                f"{source_name.stem}_{counter}{source_name.suffix}"
            )
            if candidate.exists():
                return candidate
            counter += 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_12(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
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
            counter = 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_13(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
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
            counter -= 1

    def xǁLocalDocumentFoldersǁ_available_destination__mutmut_14(self, filename: str) -> Path:
        """Return a collision-free destination in the processed folder."""
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
            counter += 2

mutants_xǁLocalDocumentFoldersǁ__init____mutmut['_mutmut_orig'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ__init____mutmut['xǁLocalDocumentFoldersǁ__init____mutmut_1'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ__init____mutmut['xǁLocalDocumentFoldersǁ__init____mutmut_2'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ__init____mutmut['xǁLocalDocumentFoldersǁ__init____mutmut_3'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ__init____mutmut['xǁLocalDocumentFoldersǁ__init____mutmut_4'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁLocalDocumentFoldersǁscan__mutmut['_mutmut_orig'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_1'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_2'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_3'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_4'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_5'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_6'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_7'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_8'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_9'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_10'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_11'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_12'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_13'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_14'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_15'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_16'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_17'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_18'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_19'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_20'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_21'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_22'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_23'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_24'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_25'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_26'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_27'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_28'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_29'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_30'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_30 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_31'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_31 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_32'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_32 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_33'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_33 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁscan__mutmut['xǁLocalDocumentFoldersǁscan__mutmut_34'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁscan__mutmut_34 # type: ignore # mutmut generated

mutants_xǁLocalDocumentFoldersǁarchive__mutmut['_mutmut_orig'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_1'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_2'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_3'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_4'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_5'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_6'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_7'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_8'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_9'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_10'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_11'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_12'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_13'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_14'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_15'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_16'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_17'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_18'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁarchive__mutmut['xǁLocalDocumentFoldersǁarchive__mutmut_19'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁarchive__mutmut_19 # type: ignore # mutmut generated

mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['_mutmut_orig'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_1'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_2'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_3'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_4'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_5'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_6'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_7'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_8'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_9'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_10'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_11'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_12'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_13'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_14'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_15'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_16'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_17'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_18'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_19'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_20'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_21'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_22'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_ensure_directories__mutmut['xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_23'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_ensure_directories__mutmut_23 # type: ignore # mutmut generated

mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['_mutmut_orig'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_1'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_2'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_3'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_4'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_5'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_6'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_7'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_8'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_9'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_10'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_11'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_12'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_13'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalDocumentFoldersǁ_available_destination__mutmut['xǁLocalDocumentFoldersǁ_available_destination__mutmut_14'] = LocalDocumentFolders.xǁLocalDocumentFoldersǁ_available_destination__mutmut_14 # type: ignore # mutmut generated
