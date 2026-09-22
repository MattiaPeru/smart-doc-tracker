"""Durable local reminder settings for the application."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from threading import Lock

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class ReminderSettings(BaseModel):
    """User-selected defaults for document expiration reminders."""

    model_config = ConfigDict(extra="forbid")

    default_notification_days_before: int = Field(default=30, ge=0, le=3_650)


class ReminderSettingsError(RuntimeError):
    """Raised when local reminder settings cannot be read or persisted."""


class LocalReminderSettingsStore:
    """Read and atomically persist reminder settings on the local host."""

    def __init__(self, path: str | Path = Path("data/settings.json")) -> None:
        """Configure the local settings file without performing any I/O."""
        self._path = Path(path)
        self._lock = Lock()

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
