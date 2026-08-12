"""Local scheduling for recurring expiration checks."""

from __future__ import annotations

from collections.abc import Callable
from datetime import time
from typing import Any, Protocol


class SchedulerConfigurationError(ValueError):
    """Raised when the daily schedule is invalid or unavailable."""


class SchedulerError(RuntimeError):
    """Raised when the local scheduler cannot run."""


class BlockingSchedulerBackend(Protocol):
    """Subset of APScheduler used by the daily task runner."""

    def add_job(self, function: Callable[[], None], **kwargs: Any) -> Any: ...
    def start(self) -> None: ...


def parse_daily_time(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


class DailyTaskScheduler:
    """Run one callable every day using the host's local timezone."""

    def __init__(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
        backend: BlockingSchedulerBackend | None = None,
    ) -> None:
        self._task = task
        self._check_time = check_time
        self._backend = backend

    def run(self) -> None:
        """Register the daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                self._task,
                trigger="cron",
                hour=self._check_time.hour,
                minute=self._check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError("The local daily scheduler stopped unexpectedly.") from exc


def _load_scheduler_backend() -> BlockingSchedulerBackend:
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return BlockingScheduler()
