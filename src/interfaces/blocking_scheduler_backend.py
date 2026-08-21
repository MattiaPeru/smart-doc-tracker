"""Backend interface for blocking local scheduling."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Protocol


class BlockingSchedulerBackend(Protocol):
    """Expose the scheduler operations required by the application."""

    def add_job(self, function: Callable[[], None], **kwargs: Any) -> Any:
        """Register a callable with scheduler-specific options."""
        ...

    def start(self) -> None:
        """Start the blocking scheduler loop."""
        ...
