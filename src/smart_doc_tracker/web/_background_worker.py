"""A stoppable daemon worker for durable local jobs."""

from __future__ import annotations

from collections.abc import Callable
from queue import Queue
from threading import Event, Lock, Thread


class BackgroundWorker:
    """Run queued identifiers without delaying process shutdown."""

    def __init__(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    @property
    def stopping(self) -> bool:
        """Report whether shutdown has been requested."""
        return self._stopping.is_set()

    def submit(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("The background worker is closed.")
            self._queue.put_nowait(job_id)

    def close(self) -> None:
        """Stop accepting work and return without waiting for an active job."""
        with self._lock:
            if not self._stopping.is_set():
                self._stopping.set()
                self._queue.put_nowait(None)

    def _work(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = self._queue.get()
            if job_id is None or self._stopping.is_set():
                return
            self._run(job_id)
