"""A stoppable daemon worker for durable local jobs."""

from __future__ import annotations

from collections.abc import Callable
from queue import Queue
from threading import Event, Lock, Thread


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁBackgroundWorkerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁBackgroundWorkerǁsubmit__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBackgroundWorkerǁclose__mutmut: MutantDict = {}  # type: ignore
mutants_xǁBackgroundWorkerǁ_work__mutmut: MutantDict = {}  # type: ignore


class BackgroundWorker:
    """Run queued identifiers without delaying process shutdown."""

    @_mutmut_mutated(mutants_xǁBackgroundWorkerǁ__init____mutmut)
    def __init__(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_orig(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_1(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = None
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_2(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = None
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_3(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = None
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_4(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = None
        self._thread = Thread(target=self._work, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_5(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = None
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_6(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=None, name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_7(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=None, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_8(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=None)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_9(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(name=name, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_10(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, daemon=True)
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_11(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, )
        self._thread.start()

    def xǁBackgroundWorkerǁ__init____mutmut_12(self, run: Callable[[str], None], *, name: str) -> None:
        """Start one daemon thread for the supplied job callback."""
        self._run = run
        self._queue: Queue[str | None] = Queue()
        self._stopping = Event()
        self._lock = Lock()
        self._thread = Thread(target=self._work, name=name, daemon=False)
        self._thread.start()

    @property
    def stopping(self) -> bool:
        """Report whether shutdown has been requested."""
        return self._stopping.is_set()

    @_mutmut_mutated(mutants_xǁBackgroundWorkerǁsubmit__mutmut)
    def submit(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("The background worker is closed.")
            self._queue.put_nowait(job_id)

    def xǁBackgroundWorkerǁsubmit__mutmut_orig(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("The background worker is closed.")
            self._queue.put_nowait(job_id)

    def xǁBackgroundWorkerǁsubmit__mutmut_1(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError(None)
            self._queue.put_nowait(job_id)

    def xǁBackgroundWorkerǁsubmit__mutmut_2(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("XXThe background worker is closed.XX")
            self._queue.put_nowait(job_id)

    def xǁBackgroundWorkerǁsubmit__mutmut_3(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("the background worker is closed.")
            self._queue.put_nowait(job_id)

    def xǁBackgroundWorkerǁsubmit__mutmut_4(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("THE BACKGROUND WORKER IS CLOSED.")
            self._queue.put_nowait(job_id)

    def xǁBackgroundWorkerǁsubmit__mutmut_5(self, job_id: str) -> None:
        """Queue an identifier while this worker accepts work."""
        with self._lock:
            if self._stopping.is_set():
                raise RuntimeError("The background worker is closed.")
            self._queue.put_nowait(None)

    @_mutmut_mutated(mutants_xǁBackgroundWorkerǁclose__mutmut)
    def close(self) -> None:
        """Stop accepting work and return without waiting for an active job."""
        with self._lock:
            if not self._stopping.is_set():
                self._stopping.set()
                self._queue.put_nowait(None)

    def xǁBackgroundWorkerǁclose__mutmut_orig(self) -> None:
        """Stop accepting work and return without waiting for an active job."""
        with self._lock:
            if not self._stopping.is_set():
                self._stopping.set()
                self._queue.put_nowait(None)

    def xǁBackgroundWorkerǁclose__mutmut_1(self) -> None:
        """Stop accepting work and return without waiting for an active job."""
        with self._lock:
            if self._stopping.is_set():
                self._stopping.set()
                self._queue.put_nowait(None)

    @_mutmut_mutated(mutants_xǁBackgroundWorkerǁ_work__mutmut)
    def _work(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = self._queue.get()
            if job_id is None or self._stopping.is_set():
                return
            self._run(job_id)

    def xǁBackgroundWorkerǁ_work__mutmut_orig(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = self._queue.get()
            if job_id is None or self._stopping.is_set():
                return
            self._run(job_id)

    def xǁBackgroundWorkerǁ_work__mutmut_1(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while False:
            job_id = self._queue.get()
            if job_id is None or self._stopping.is_set():
                return
            self._run(job_id)

    def xǁBackgroundWorkerǁ_work__mutmut_2(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = None
            if job_id is None or self._stopping.is_set():
                return
            self._run(job_id)

    def xǁBackgroundWorkerǁ_work__mutmut_3(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = self._queue.get()
            if job_id is None and self._stopping.is_set():
                return
            self._run(job_id)

    def xǁBackgroundWorkerǁ_work__mutmut_4(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = self._queue.get()
            if job_id is not None or self._stopping.is_set():
                return
            self._run(job_id)

    def xǁBackgroundWorkerǁ_work__mutmut_5(self) -> None:
        """Run accepted work until shutdown, leaving skipped jobs durable."""
        while True:
            job_id = self._queue.get()
            if job_id is None or self._stopping.is_set():
                return
            self._run(None)

mutants_xǁBackgroundWorkerǁ__init____mutmut['_mutmut_orig'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_1'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_2'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_3'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_4'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_5'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_6'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_7'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_8'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_9'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_10'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_11'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ__init____mutmut['xǁBackgroundWorkerǁ__init____mutmut_12'] = BackgroundWorker.xǁBackgroundWorkerǁ__init____mutmut_12 # type: ignore # mutmut generated

mutants_xǁBackgroundWorkerǁsubmit__mutmut['_mutmut_orig'] = BackgroundWorker.xǁBackgroundWorkerǁsubmit__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁsubmit__mutmut['xǁBackgroundWorkerǁsubmit__mutmut_1'] = BackgroundWorker.xǁBackgroundWorkerǁsubmit__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁsubmit__mutmut['xǁBackgroundWorkerǁsubmit__mutmut_2'] = BackgroundWorker.xǁBackgroundWorkerǁsubmit__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁsubmit__mutmut['xǁBackgroundWorkerǁsubmit__mutmut_3'] = BackgroundWorker.xǁBackgroundWorkerǁsubmit__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁsubmit__mutmut['xǁBackgroundWorkerǁsubmit__mutmut_4'] = BackgroundWorker.xǁBackgroundWorkerǁsubmit__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁsubmit__mutmut['xǁBackgroundWorkerǁsubmit__mutmut_5'] = BackgroundWorker.xǁBackgroundWorkerǁsubmit__mutmut_5 # type: ignore # mutmut generated

mutants_xǁBackgroundWorkerǁclose__mutmut['_mutmut_orig'] = BackgroundWorker.xǁBackgroundWorkerǁclose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁclose__mutmut['xǁBackgroundWorkerǁclose__mutmut_1'] = BackgroundWorker.xǁBackgroundWorkerǁclose__mutmut_1 # type: ignore # mutmut generated

mutants_xǁBackgroundWorkerǁ_work__mutmut['_mutmut_orig'] = BackgroundWorker.xǁBackgroundWorkerǁ_work__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ_work__mutmut['xǁBackgroundWorkerǁ_work__mutmut_1'] = BackgroundWorker.xǁBackgroundWorkerǁ_work__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ_work__mutmut['xǁBackgroundWorkerǁ_work__mutmut_2'] = BackgroundWorker.xǁBackgroundWorkerǁ_work__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ_work__mutmut['xǁBackgroundWorkerǁ_work__mutmut_3'] = BackgroundWorker.xǁBackgroundWorkerǁ_work__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ_work__mutmut['xǁBackgroundWorkerǁ_work__mutmut_4'] = BackgroundWorker.xǁBackgroundWorkerǁ_work__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBackgroundWorkerǁ_work__mutmut['xǁBackgroundWorkerǁ_work__mutmut_5'] = BackgroundWorker.xǁBackgroundWorkerǁ_work__mutmut_5 # type: ignore # mutmut generated
