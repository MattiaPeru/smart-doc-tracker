"""Local scheduling for recurring expiration checks."""

from __future__ import annotations

from collections.abc import Callable
from datetime import time

from interfaces.blocking_scheduler_backend import BlockingSchedulerBackend


class SchedulerConfigurationError(ValueError):
    """Raised when the daily schedule is invalid or unavailable."""


class SchedulerError(RuntimeError):
    """Raised when the local scheduler cannot run."""


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
        backend: BlockingSchedulerBackend | None = None,
    ) -> None:
        """Configure the local scheduler backend."""
        self._backend = backend

    def run(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
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
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return BlockingScheduler()
