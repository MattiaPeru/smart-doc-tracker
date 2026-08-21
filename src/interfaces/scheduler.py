"""Scheduling interface for recurring local tasks."""

from __future__ import annotations

from collections.abc import Callable
from datetime import time
from typing import Protocol


class Scheduler(Protocol):
    """Schedule and run one recurring local task."""

    def run(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Schedule the task at the requested daily time and start execution."""
        ...
