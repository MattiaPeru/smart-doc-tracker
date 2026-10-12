"""Durable local reminder settings for the application."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from threading import Lock

from pydantic import BaseModel, ConfigDict, Field, ValidationError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ReminderSettings(BaseModel):
    """User-selected defaults for document expiration reminders."""

    model_config = ConfigDict(extra="forbid")

    default_notification_days_before: int = Field(default=30, ge=0, le=3_650)


class ReminderSettingsError(RuntimeError):
    """Raised when local reminder settings cannot be read or persisted."""
mutants_xǁLocalReminderSettingsStoreǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalReminderSettingsStoreǁload__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut: MutantDict = {}  # type: ignore


class LocalReminderSettingsStore:
    """Read and atomically persist reminder settings on the local host."""

    @_mutmut_mutated(mutants_xǁLocalReminderSettingsStoreǁ__init____mutmut)
    def __init__(self, path: str | Path = Path("data/settings.json")) -> None:
        """Configure the local settings file without performing any I/O."""
        self._path = Path(path)
        self._lock = Lock()

    def xǁLocalReminderSettingsStoreǁ__init____mutmut_orig(self, path: str | Path = Path("data/settings.json")) -> None:
        """Configure the local settings file without performing any I/O."""
        self._path = Path(path)
        self._lock = Lock()

    def xǁLocalReminderSettingsStoreǁ__init____mutmut_1(self, path: str | Path = Path("data/settings.json")) -> None:
        """Configure the local settings file without performing any I/O."""
        self._path = None
        self._lock = Lock()

    def xǁLocalReminderSettingsStoreǁ__init____mutmut_2(self, path: str | Path = Path("data/settings.json")) -> None:
        """Configure the local settings file without performing any I/O."""
        self._path = Path(None)
        self._lock = Lock()

    def xǁLocalReminderSettingsStoreǁ__init____mutmut_3(self, path: str | Path = Path("data/settings.json")) -> None:
        """Configure the local settings file without performing any I/O."""
        self._path = Path(path)
        self._lock = None

    @_mutmut_mutated(mutants_xǁLocalReminderSettingsStoreǁload__mutmut)
    def load(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_orig(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_1(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_2(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = None
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_3(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(None)
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_4(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding=None))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_5(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="XXutf-8XX"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_6(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="UTF-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_7(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(None)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_8(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    None
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_9(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "XXThe local reminder settings could not be read.XX"
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_10(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "the local reminder settings could not be read."
                ) from exc

    def xǁLocalReminderSettingsStoreǁload__mutmut_11(self) -> ReminderSettings:
        """Return persisted settings or application defaults when absent."""
        with self._lock:
            if not self._path.exists():
                return ReminderSettings()
            try:
                payload = json.loads(self._path.read_text(encoding="utf-8"))
                return ReminderSettings.model_validate(payload)
            except (OSError, json.JSONDecodeError, ValidationError) as exc:
                raise ReminderSettingsError(
                    "THE LOCAL REMINDER SETTINGS COULD NOT BE READ."
                ) from exc

    @_mutmut_mutated(mutants_xǁLocalReminderSettingsStoreǁsave__mutmut)
    def save(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_orig(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_1(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = ""
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_2(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=None, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_3(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=None)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_4(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_5(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, )
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_6(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=False, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_7(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=False)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_8(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = None
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_9(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=None,
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_10(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=None,
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_11(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=None,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_12(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_13(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_14(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_15(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix="XX.tmpXX",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_16(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".TMP",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_17(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = None
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_18(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(None)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_19(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(None, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_20(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, None, encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_21(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding=None) as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_22(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen("w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_23(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_24(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", ) as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_25(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "XXwXX", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_26(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "W", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_27(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="XXutf-8XX") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_28(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="UTF-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_29(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(None, stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_30(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), None, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_31(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=None)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_32(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_33(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_34(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, )
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_35(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=3)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_36(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write(None)
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_37(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("XX\nXX")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_38(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(None)
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_39(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(None)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_40(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    None
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_41(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "XXThe local reminder settings could not be saved.XX"
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_42(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "the local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_43(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "THE LOCAL REMINDER SETTINGS COULD NOT BE SAVED."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_44(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is None:
                    temporary_path.unlink(missing_ok=True)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_45(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=None)

    def xǁLocalReminderSettingsStoreǁsave__mutmut_46(self, settings: ReminderSettings) -> ReminderSettings:
        """Atomically replace the local settings file with validated values."""
        with self._lock:
            temporary_path: Path | None = None
            try:
                self._path.parent.mkdir(parents=True, exist_ok=True)
                descriptor, raw_path = tempfile.mkstemp(
                    prefix=f".{self._path.name}.",
                    suffix=".tmp",
                    dir=self._path.parent,
                )
                temporary_path = Path(raw_path)
                with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                    json.dump(settings.model_dump(), stream, indent=2)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._path)
                return settings
            except OSError as exc:
                raise ReminderSettingsError(
                    "The local reminder settings could not be saved."
                ) from exc
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=False)

mutants_xǁLocalReminderSettingsStoreǁ__init____mutmut['_mutmut_orig'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁ__init____mutmut['xǁLocalReminderSettingsStoreǁ__init____mutmut_1'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁ__init____mutmut['xǁLocalReminderSettingsStoreǁ__init____mutmut_2'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁ__init____mutmut['xǁLocalReminderSettingsStoreǁ__init____mutmut_3'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁLocalReminderSettingsStoreǁload__mutmut['_mutmut_orig'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_1'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_2'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_3'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_4'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_5'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_6'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_7'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_8'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_9'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_10'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁload__mutmut['xǁLocalReminderSettingsStoreǁload__mutmut_11'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁload__mutmut_11 # type: ignore # mutmut generated

mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['_mutmut_orig'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_1'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_2'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_3'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_4'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_5'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_6'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_7'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_8'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_9'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_10'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_11'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_12'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_13'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_14'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_15'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_16'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_17'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_18'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_19'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_20'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_21'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_22'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_23'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_24'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_25'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_26'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_27'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_28'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_29'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_30'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_30 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_31'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_31 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_32'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_32 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_33'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_33 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_34'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_34 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_35'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_35 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_36'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_36 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_37'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_37 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_38'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_38 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_39'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_39 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_40'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_40 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_41'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_41 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_42'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_42 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_43'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_43 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_44'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_44 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_45'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_45 # type: ignore # mutmut generated
mutants_xǁLocalReminderSettingsStoreǁsave__mutmut['xǁLocalReminderSettingsStoreǁsave__mutmut_46'] = LocalReminderSettingsStore.xǁLocalReminderSettingsStoreǁsave__mutmut_46 # type: ignore # mutmut generated
