"""Persistent bounded jobs for private document uploads."""

from __future__ import annotations

import json
import logging
import shutil
from collections.abc import Callable
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from threading import Lock
from uuid import uuid4

from ..pipeline import DocumentProcessingResult, DocumentProcessingStage
from ._background_worker import BackgroundWorker
from .pending import PendingDocumentService

_LOGGER = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UploadJobStatus(StrEnum):
    """Observable states of one local upload job."""

    QUEUED = "queued"
    EXTRACTING = "extracting"
    PARSING = "parsing"
    AWAITING_CONFIRMATION = "awaiting_confirmation"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class UploadJob:
    """Privacy-conscious snapshot of one local upload job."""

    id: str
    file_name: str
    status: UploadJobStatus
    created_at: datetime
    updated_at: datetime
    document_id: str | None = None
    pending_id: str | None = None
    inserted: bool | None = None
    error: str | None = None


@dataclass(frozen=True, slots=True)
class _StoredUploadJob:
    """Internal job state including the local source and OCR language."""

    job: UploadJob
    source_path: Path
    language: str


ProgressReporter = Callable[[DocumentProcessingStage], None]
UploadProcessor = Callable[[Path, str, ProgressReporter], DocumentProcessingResult]
mutants_xǁUploadJobServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁsubmit__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁlist_processing__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁretry_failed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁretry_all_failed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_load__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_report_stage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_set_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_update__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_persist__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUploadJobServiceǁ_manifest_path__mutmut: MutantDict = {}  # type: ignore


class UploadJobService:
    """Persist and execute uploaded documents locally with one bounded worker."""

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ__init____mutmut)
    def __init__(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_orig(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_1(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = None
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_2(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = None
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_3(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = None
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_4(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(None).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_5(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=None, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_6(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=None)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_7(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_8(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, )
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_9(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=False, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_10(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=False)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_11(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = None
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_12(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = None
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_13(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = None
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_14(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(None, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_15(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name=None)
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_16(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_17(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, )
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_18(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="XXsmart-doc-uploadXX")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_19(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="SMART-DOC-UPLOAD")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁUploadJobServiceǁ__init____mutmut_20(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
        queue_path: str | Path = Path("data/processing_queue"),
    ) -> None:
        """Load durable jobs and resume interrupted local processing."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._jobs: dict[str, _StoredUploadJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-upload")
        for job_id in self._load():
            self._worker.submit(None)

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁsubmit__mutmut)
    def submit(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_orig(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_1(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = None
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_2(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(None)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_3(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = None
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_4(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=None,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_5(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=None,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_6(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=None,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_7(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=None,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_8(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=None,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_9(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_10(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_11(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_12(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_13(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_14(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(None).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_15(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = None
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_16(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path * f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_17(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.upper()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_18(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(None, str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_19(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), None)
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_20(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_21(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), )
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_22(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(None), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_23(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(None))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_24(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = None
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_25(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(None, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_26(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, None, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_27(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, None)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_28(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_29(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_30(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, )
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_31(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = None
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_32(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(None)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_33(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(None)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_34(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(None, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_35(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_36(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, )
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_37(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=None)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_38(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(None).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_39(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=False)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_40(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=None)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_41(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=False)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_42(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info(None, job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_43(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", None)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_44(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info(job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_45(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", )
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_46(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("XXUpload job %s queued.XX", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_47(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("upload job %s queued.", job.id)
        return job

    def xǁUploadJobServiceǁsubmit__mutmut_48(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Move an upload into durable local storage and queue it."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=Path(file_name).name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        source_path = self._queue_path / f"{job.id}{path.suffix.lower()}"
        shutil.move(str(path), str(source_path))
        stored = _StoredUploadJob(job, source_path, language)
        try:
            with self._lock:
                self._jobs[job.id] = stored
                self._persist(stored)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("UPLOAD JOB %S QUEUED.", job.id)
        return job

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁget__mutmut)
    def get(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(job_id)
            return stored.job if stored is not None else None

    def xǁUploadJobServiceǁget__mutmut_orig(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(job_id)
            return stored.job if stored is not None else None

    def xǁUploadJobServiceǁget__mutmut_1(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = None
            return stored.job if stored is not None else None

    def xǁUploadJobServiceǁget__mutmut_2(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(None)
            return stored.job if stored is not None else None

    def xǁUploadJobServiceǁget__mutmut_3(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(job_id)
            return stored.job if (stored is not None) and False else None

    def xǁUploadJobServiceǁget__mutmut_4(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(job_id)
            return stored.job if (stored is not None) or True else None

    def xǁUploadJobServiceǁget__mutmut_5(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(job_id)
            return stored.job if stored is None else None

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁlist_processing__mutmut)
    def list_processing(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, key=lambda item: (item.created_at, item.id))

    def xǁUploadJobServiceǁlist_processing__mutmut_orig(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, key=lambda item: (item.created_at, item.id))

    def xǁUploadJobServiceǁlist_processing__mutmut_1(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = None
        return sorted(jobs, key=lambda item: (item.created_at, item.id))

    def xǁUploadJobServiceǁlist_processing__mutmut_2(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, key=lambda item: (item.created_at, item.id))

    def xǁUploadJobServiceǁlist_processing__mutmut_3(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(None, key=lambda item: (item.created_at, item.id))

    def xǁUploadJobServiceǁlist_processing__mutmut_4(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, key=None)

    def xǁUploadJobServiceǁlist_processing__mutmut_5(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(key=lambda item: (item.created_at, item.id))

    def xǁUploadJobServiceǁlist_processing__mutmut_6(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, )

    def xǁUploadJobServiceǁlist_processing__mutmut_7(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, key=lambda item: None)

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut)
    def discard_for_pending(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_orig(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_1(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = None
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_2(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                None,
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_3(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_4(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_5(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id != pending_id
                ),
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_6(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                None,
            )
            if matching_id is None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_7(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=None)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_8(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(None).unlink(missing_ok=True)

    def xǁUploadJobServiceǁdiscard_for_pending__mutmut_9(self, pending_id: str) -> None:
        """Remove completed job metadata after confirmation or rejection."""
        with self._lock:
            matching_id = next(
                (
                    job_id
                    for job_id, stored in self._jobs.items()
                    if stored.job.pending_id == pending_id
                ),
                None,
            )
            if matching_id is not None:
                del self._jobs[matching_id]
                self._manifest_path(matching_id).unlink(missing_ok=False)

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁdiscard_failed__mutmut)
    def discard_failed(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_orig(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_1(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = None
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_2(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(None)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_3(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None and stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_4(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is not None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_5(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_6(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return True
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_7(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=None)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_8(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=False)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_9(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=None)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_10(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(None).unlink(missing_ok=True)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_11(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=False)
            del self._jobs[job_id]
        return True

    def xǁUploadJobServiceǁdiscard_failed__mutmut_12(self, job_id: str) -> bool:
        """Remove one failed job and its owned local source file."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if stored is None or stored.job.status is not UploadJobStatus.FAILED:
                return False
            stored.source_path.unlink(missing_ok=True)
            self._manifest_path(job_id).unlink(missing_ok=True)
            del self._jobs[job_id]
        return False

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁretry_failed__mutmut)
    def retry_failed(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_orig(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_1(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = None
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_2(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(None)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_3(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED and not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_4(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None and stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_5(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is not None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_6(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_7(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_8(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return True
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_9(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = None
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_10(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                None,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_11(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=None,
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_12(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_13(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_14(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    None,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_15(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=None,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_16(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=None,
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_17(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_18(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_19(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_20(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_21(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(None),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_22(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(None)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_23(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = None
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_24(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(None)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_25(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = None
                self._persist(stored)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_26(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(None)
                raise
        return True

    def xǁUploadJobServiceǁretry_failed__mutmut_27(self, job_id: str) -> bool:
        """Queue one failed job again when its local source is available."""
        with self._lock:
            stored = self._jobs.get(job_id)
            if (
                stored is None
                or stored.job.status is not UploadJobStatus.FAILED
                or not stored.source_path.is_file()
            ):
                return False
            queued = replace(
                stored,
                job=replace(
                    stored.job,
                    status=UploadJobStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                    error=None,
                ),
            )
            self._persist(queued)
            self._jobs[job_id] = queued
            try:
                self._worker.submit(job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return False

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁretry_all_failed__mutmut)
    def retry_all_failed(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.retry_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁretry_all_failed__mutmut_orig(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.retry_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁretry_all_failed__mutmut_1(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = None
        return sum(self.retry_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁretry_all_failed__mutmut_2(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is not UploadJobStatus.FAILED
            ]
        return sum(self.retry_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁretry_all_failed__mutmut_3(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(None)

    def xǁUploadJobServiceǁretry_all_failed__mutmut_4(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.retry_failed(None) for job_id in job_ids)

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut)
    def discard_all_failed(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.discard_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁdiscard_all_failed__mutmut_orig(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.discard_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁdiscard_all_failed__mutmut_1(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = None
        return sum(self.discard_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁdiscard_all_failed__mutmut_2(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is not UploadJobStatus.FAILED
            ]
        return sum(self.discard_failed(job_id) for job_id in job_ids)

    def xǁUploadJobServiceǁdiscard_all_failed__mutmut_3(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(None)

    def xǁUploadJobServiceǁdiscard_all_failed__mutmut_4(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.discard_failed(None) for job_id in job_ids)

    def close(self) -> None:
        """Stop promptly and leave unfinished jobs for the next start."""
        self._worker.close()

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_load__mutmut)
    def _load(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_orig(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_1(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = None
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_2(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(None):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_3(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob(None)):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_4(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("XX*.jsonXX")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_5(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.JSON")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_6(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = None
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_7(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(None)
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_8(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding=None))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_9(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="XXutf-8XX"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_10(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="UTF-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_11(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = None
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_12(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=None,
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_13(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=None,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_14(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=None,
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_15(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=None,
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_16(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=None,
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_17(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=None,
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_18(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=None,
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_19(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_20(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_21(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_22(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_23(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_24(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_25(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_26(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(None),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_27(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["XXidXX"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_28(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["ID"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_29(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(None).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_30(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(None)).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_31(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["XXfile_nameXX"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_32(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["FILE_NAME"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_33(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(None),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_34(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(None)),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_35(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["XXstatusXX"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_36(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["STATUS"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_37(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(None),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_38(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(None)),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_39(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["XXcreated_atXX"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_40(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["CREATED_AT"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_41(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(None),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_42(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(None)),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_43(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["XXupdated_atXX"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_44(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["UPDATED_AT"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_45(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get(None),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_46(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("XXpending_idXX"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_47(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("PENDING_ID"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_48(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get(None),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_49(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("XXerrorXX"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_50(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("ERROR"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_51(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = None
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_52(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path * str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_53(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(None)
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_54(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["XXsource_fileXX"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_55(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["SOURCE_FILE"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_56(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = None
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_57(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(None, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_58(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, None, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_59(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, None)
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_60(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_61(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_62(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, )
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_63(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(None))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_64(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["XXlanguageXX"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_65(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["LANGUAGE"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_66(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                break
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_67(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status not in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_68(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = None
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_69(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(None)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_70(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_71(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=None)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_72(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=False)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_73(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = None
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_74(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        None,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_75(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=None,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_76(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=None,
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_77(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=None,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_78(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_79(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_80(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_81(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_82(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_83(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(None),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_84(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = None
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_85(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(None, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_86(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=None)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_87(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_88(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, )
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_89(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(None)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_90(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = None
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_91(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        None,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_92(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=None,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_93(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=None,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_94(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_95(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_96(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_97(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_98(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(None),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_99(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = None
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_100(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(None, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_101(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=None)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_102(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_103(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, )
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_104(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(None)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_105(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(None)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_106(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = None
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_107(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        None,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_108(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=None,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_109(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=None,
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_110(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_111(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_112(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_113(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_114(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_115(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(None),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_116(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="XXThe queued source file is no longer available.XX",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_117(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="the queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_118(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="THE QUEUED SOURCE FILE IS NO LONGER AVAILABLE.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_119(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = None
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_120(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(None, job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_121(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=None)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_122(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(job=job)
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_123(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, )
                    self._persist(stored)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_124(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(None)
            self._jobs[job.id] = stored
        return resumable

    def xǁUploadJobServiceǁ_load__mutmut_125(self) -> list[str]:
        """Load valid manifests and reset interrupted work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = UploadJob(
                    id=str(payload["id"]),
                    file_name=Path(str(payload["file_name"])).name,
                    status=UploadJobStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                    pending_id=payload.get("pending_id"),
                    error=payload.get("error"),
                )
                source_path = self._queue_path / str(payload["source_file"])
                stored = _StoredUploadJob(job, source_path, str(payload["language"]))
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status in {
                UploadJobStatus.QUEUED,
                UploadJobStatus.EXTRACTING,
                UploadJobStatus.PARSING,
            }:
                pending = self._pending_documents.get(job.id)
                if pending is not None:
                    source_path.unlink(missing_ok=True)
                    job = replace(
                        job,
                        status=UploadJobStatus.AWAITING_CONFIRMATION,
                        updated_at=datetime.now(UTC),
                        pending_id=pending.id,
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                elif source_path.is_file():
                    job = replace(
                        job,
                        status=UploadJobStatus.QUEUED,
                        updated_at=datetime.now(UTC),
                        error=None,
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
                    resumable.append(job.id)
                else:
                    job = replace(
                        job,
                        status=UploadJobStatus.FAILED,
                        updated_at=datetime.now(UTC),
                        error="The queued source file is no longer available.",
                    )
                    stored = replace(stored, job=job)
                    self._persist(stored)
            self._jobs[job.id] = None
        return resumable

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_run__mutmut)
    def _run(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_orig(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_1(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = None
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_2(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info(None, job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_3(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", None)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_4(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info(job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_5(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", )
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_6(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("XXUpload job %s started.XX", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_7(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_8(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("UPLOAD JOB %S STARTED.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_9(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(None, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_10(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, None)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_11(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_12(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, )
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_13(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = None
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_14(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                None,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_15(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                None,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_16(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                None,
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_17(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_18(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_19(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_20(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: None,
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_21(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(None, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_22(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, None),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_23(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_24(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, ),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_25(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is not None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_26(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError(None)
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_27(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("XXStructured processing returned no documentXX")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_28(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_29(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("STRUCTURED PROCESSING RETURNED NO DOCUMENT")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_30(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = None
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_31(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                None,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_32(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=None,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_33(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=None,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_34(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=None,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_35(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=None,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_36(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=None,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_37(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_38(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_39(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_40(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_41(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_42(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_43(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                None,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_44(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=None,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_45(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=None,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_46(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_47(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_48(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_49(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info(None, job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_50(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", None)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_51(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info(job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_52(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", )
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_53(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("XXUpload job %s is ready for confirmation.XX", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_54(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_55(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("UPLOAD JOB %S IS READY FOR CONFIRMATION.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_56(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                None,
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_57(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                None,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_58(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                None,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_59(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_60(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_61(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_62(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "XXUpload job %s failed during local processing (%s).XX",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_63(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_64(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "UPLOAD JOB %S FAILED DURING LOCAL PROCESSING (%S).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_65(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(None).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_66(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                None,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_67(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=None,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_68(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error=None,
            )

    def xǁUploadJobServiceǁ_run__mutmut_69(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_70(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                error="The document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_71(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                )

    def xǁUploadJobServiceǁ_run__mutmut_72(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="XXThe document could not be processed locally.XX",
            )

    def xǁUploadJobServiceǁ_run__mutmut_73(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="the document could not be processed locally.",
            )

    def xǁUploadJobServiceǁ_run__mutmut_74(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
        if self._worker.stopping:
            return
        with self._lock:
            stored = self._jobs[job_id]
        try:
            _LOGGER.info("Upload job %s started.", job_id)
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                stored.source_path,
                stored.language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if self._worker.stopping:
                return
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                stored.source_path,
                file_name=stored.job.file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
                identifier=job_id,
            )
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
            _LOGGER.info("Upload job %s is ready for confirmation.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Exception messages can contain OCR or model output. Record the type
            # and job identifier for terminal diagnostics without leaking content.
            _LOGGER.error(
                "Upload job %s failed during local processing (%s).",
                job_id,
                type(exc).__name__,
            )
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="THE DOCUMENT COULD NOT BE PROCESSED LOCALLY.",
            )

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_report_stage__mutmut)
    def _report_stage(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_orig(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_1(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = None
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_2(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = None
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_3(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(None)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_4(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_5(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(None, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_6(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, None)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_7(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_8(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, )
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_9(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            None,
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_10(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            None,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_11(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            None,
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_12(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_13(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_14(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            )

    def xǁUploadJobServiceǁ_report_stage__mutmut_15(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "XXUpload job %s: %s.XX",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_16(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_17(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "UPLOAD JOB %S: %S.",
            job_id,
            stage.value.replace("_", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_18(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace(None, " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_19(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", None),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_20(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace(" "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_21(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", ),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_22(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("XX_XX", " "),
        )

    def xǁUploadJobServiceǁ_report_stage__mutmut_23(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            if self._worker.stopping:
                return
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", "XX XX"),
        )

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_set_status__mutmut)
    def _set_status(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(job_id, status=status)

    def xǁUploadJobServiceǁ_set_status__mutmut_orig(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(job_id, status=status)

    def xǁUploadJobServiceǁ_set_status__mutmut_1(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(None, status=status)

    def xǁUploadJobServiceǁ_set_status__mutmut_2(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(job_id, status=None)

    def xǁUploadJobServiceǁ_set_status__mutmut_3(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(status=status)

    def xǁUploadJobServiceǁ_set_status__mutmut_4(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(job_id, )

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_update__mutmut)
    def _update(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_orig(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_1(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = None
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_2(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = None
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_3(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                None,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_4(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=None,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_5(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=None,
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_6(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=None,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_7(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=None,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_8(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_9(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_10(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_11(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_12(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_13(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(None),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_14(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = None
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_15(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(None, job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_16(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=None)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_17(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(job=job)
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_18(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, )
            self._jobs[job_id] = stored
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_19(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = None
            self._persist(stored)

    def xǁUploadJobServiceǁ_update__mutmut_20(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        pending_id: str | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically update and persist one immutable job snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            job = replace(
                current.job,
                status=status,
                updated_at=datetime.now(UTC),
                pending_id=pending_id,
                error=error,
            )
            stored = replace(current, job=job)
            self._jobs[job_id] = stored
            self._persist(None)

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_persist__mutmut)
    def _persist(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_orig(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_1(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = None
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_2(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = None
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_3(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "XXidXX": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_4(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "ID": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_5(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "XXfile_nameXX": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_6(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "FILE_NAME": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_7(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "XXstatusXX": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_8(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "STATUS": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_9(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "XXcreated_atXX": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_10(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "CREATED_AT": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_11(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "XXupdated_atXX": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_12(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "UPDATED_AT": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_13(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "XXpending_idXX": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_14(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "PENDING_ID": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_15(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "XXerrorXX": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_16(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "ERROR": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_17(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "XXsource_fileXX": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_18(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "SOURCE_FILE": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_19(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "XXlanguageXX": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_20(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "LANGUAGE": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_21(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = None
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_22(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(None)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_23(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = None
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_24(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(None)
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_25(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix("XX.json.tmpXX")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_26(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".JSON.TMP")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_27(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(None, encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_28(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding=None)
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_29(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_30(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), )
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_31(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(None), encoding="utf-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_32(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="XXutf-8XX")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_33(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="UTF-8")
        temporary.replace(destination)

    def xǁUploadJobServiceǁ_persist__mutmut_34(self, stored: _StoredUploadJob) -> None:
        """Atomically write non-content job metadata beside the local source."""
        job = stored.job
        payload = {
            "id": job.id,
            "file_name": job.file_name,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "pending_id": job.pending_id,
            "error": job.error,
            "source_file": stored.source_path.name,
            "language": stored.language,
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(None)

    @_mutmut_mutated(mutants_xǁUploadJobServiceǁ_manifest_path__mutmut)
    def _manifest_path(self, job_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._queue_path / f"{job_id}.json"

    def xǁUploadJobServiceǁ_manifest_path__mutmut_orig(self, job_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._queue_path / f"{job_id}.json"

    def xǁUploadJobServiceǁ_manifest_path__mutmut_1(self, job_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._queue_path * f"{job_id}.json"

mutants_xǁUploadJobServiceǁ__init____mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_5'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_6'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_7'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_8'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_9'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_10'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_11'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_12'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_13'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_14'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_15'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_16'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_17'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_18'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_19'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ__init____mutmut['xǁUploadJobServiceǁ__init____mutmut_20'] = UploadJobService.xǁUploadJobServiceǁ__init____mutmut_20 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁsubmit__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_21'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_22'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_23'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_24'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_25'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_26'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_27'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_28'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_29'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_30'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_31'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_32'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_33'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_34'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_34 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_35'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_35 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_36'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_36 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_37'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_37 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_38'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_38 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_39'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_39 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_40'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_40 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_41'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_41 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_42'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_42 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_43'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_43 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_44'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_44 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_45'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_45 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_46'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_46 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_47'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_47 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁsubmit__mutmut['xǁUploadJobServiceǁsubmit__mutmut_48'] = UploadJobService.xǁUploadJobServiceǁsubmit__mutmut_48 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁget__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁget__mutmut['xǁUploadJobServiceǁget__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁget__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁget__mutmut['xǁUploadJobServiceǁget__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁget__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁget__mutmut['xǁUploadJobServiceǁget__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁget__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁget__mutmut['xǁUploadJobServiceǁget__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁget__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁget__mutmut['xǁUploadJobServiceǁget__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁget__mutmut_5 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁlist_processing__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁlist_processing__mutmut['xǁUploadJobServiceǁlist_processing__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁlist_processing__mutmut_7 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_for_pending__mutmut['xǁUploadJobServiceǁdiscard_for_pending__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁdiscard_for_pending__mutmut_9 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_failed__mutmut['xǁUploadJobServiceǁdiscard_failed__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁdiscard_failed__mutmut_12 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁretry_failed__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_21'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_22'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_23'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_24'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_25'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_26'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_failed__mutmut['xǁUploadJobServiceǁretry_failed__mutmut_27'] = UploadJobService.xǁUploadJobServiceǁretry_failed__mutmut_27 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁretry_all_failed__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁretry_all_failed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_all_failed__mutmut['xǁUploadJobServiceǁretry_all_failed__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁretry_all_failed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_all_failed__mutmut['xǁUploadJobServiceǁretry_all_failed__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁretry_all_failed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_all_failed__mutmut['xǁUploadJobServiceǁretry_all_failed__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁretry_all_failed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁretry_all_failed__mutmut['xǁUploadJobServiceǁretry_all_failed__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁretry_all_failed__mutmut_4 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁdiscard_all_failed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut['xǁUploadJobServiceǁdiscard_all_failed__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁdiscard_all_failed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut['xǁUploadJobServiceǁdiscard_all_failed__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁdiscard_all_failed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut['xǁUploadJobServiceǁdiscard_all_failed__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁdiscard_all_failed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁdiscard_all_failed__mutmut['xǁUploadJobServiceǁdiscard_all_failed__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁdiscard_all_failed__mutmut_4 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_load__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_21'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_22'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_23'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_24'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_25'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_26'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_27'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_28'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_29'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_30'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_31'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_32'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_33'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_34'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_34 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_35'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_35 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_36'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_36 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_37'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_37 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_38'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_38 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_39'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_39 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_40'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_40 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_41'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_41 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_42'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_42 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_43'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_43 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_44'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_44 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_45'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_45 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_46'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_46 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_47'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_47 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_48'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_48 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_49'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_49 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_50'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_50 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_51'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_51 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_52'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_52 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_53'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_53 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_54'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_54 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_55'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_55 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_56'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_56 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_57'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_57 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_58'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_58 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_59'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_59 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_60'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_60 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_61'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_61 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_62'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_62 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_63'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_63 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_64'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_64 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_65'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_65 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_66'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_66 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_67'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_67 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_68'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_68 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_69'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_69 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_70'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_70 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_71'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_71 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_72'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_72 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_73'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_73 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_74'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_74 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_75'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_75 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_76'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_76 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_77'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_77 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_78'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_78 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_79'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_79 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_80'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_80 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_81'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_81 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_82'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_82 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_83'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_83 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_84'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_84 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_85'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_85 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_86'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_86 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_87'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_87 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_88'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_88 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_89'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_89 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_90'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_90 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_91'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_91 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_92'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_92 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_93'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_93 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_94'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_94 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_95'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_95 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_96'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_96 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_97'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_97 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_98'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_98 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_99'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_99 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_100'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_100 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_101'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_101 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_102'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_102 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_103'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_103 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_104'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_104 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_105'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_105 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_106'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_106 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_107'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_107 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_108'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_108 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_109'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_109 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_110'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_110 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_111'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_111 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_112'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_112 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_113'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_113 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_114'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_114 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_115'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_115 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_116'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_116 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_117'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_117 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_118'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_118 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_119'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_119 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_120'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_120 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_121'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_121 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_122'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_122 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_123'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_123 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_124'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_124 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_load__mutmut['xǁUploadJobServiceǁ_load__mutmut_125'] = UploadJobService.xǁUploadJobServiceǁ_load__mutmut_125 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_run__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_21'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_22'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_23'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_24'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_25'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_26'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_27'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_28'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_29'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_30'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_31'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_32'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_33'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_34'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_34 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_35'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_35 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_36'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_36 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_37'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_37 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_38'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_38 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_39'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_39 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_40'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_40 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_41'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_41 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_42'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_42 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_43'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_43 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_44'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_44 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_45'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_45 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_46'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_46 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_47'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_47 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_48'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_48 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_49'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_49 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_50'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_50 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_51'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_51 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_52'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_52 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_53'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_53 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_54'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_54 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_55'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_55 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_56'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_56 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_57'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_57 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_58'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_58 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_59'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_59 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_60'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_60 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_61'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_61 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_62'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_62 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_63'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_63 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_64'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_64 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_65'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_65 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_66'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_66 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_67'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_67 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_68'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_68 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_69'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_69 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_70'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_70 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_71'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_71 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_72'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_72 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_73'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_73 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_run__mutmut['xǁUploadJobServiceǁ_run__mutmut_74'] = UploadJobService.xǁUploadJobServiceǁ_run__mutmut_74 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_report_stage__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_21'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_22'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_report_stage__mutmut['xǁUploadJobServiceǁ_report_stage__mutmut_23'] = UploadJobService.xǁUploadJobServiceǁ_report_stage__mutmut_23 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_set_status__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_set_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_set_status__mutmut['xǁUploadJobServiceǁ_set_status__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_set_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_set_status__mutmut['xǁUploadJobServiceǁ_set_status__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ_set_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_set_status__mutmut['xǁUploadJobServiceǁ_set_status__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ_set_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_set_status__mutmut['xǁUploadJobServiceǁ_set_status__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ_set_status__mutmut_4 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_update__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_update__mutmut['xǁUploadJobServiceǁ_update__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁ_update__mutmut_20 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_persist__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_2'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_3'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_4'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_5'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_6'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_7'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_8'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_9'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_10'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_11'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_12'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_13'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_14'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_15'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_16'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_17'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_18'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_19'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_20'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_21'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_22'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_23'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_24'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_25'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_26'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_27'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_28'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_29'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_30'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_31'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_32'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_33'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_persist__mutmut['xǁUploadJobServiceǁ_persist__mutmut_34'] = UploadJobService.xǁUploadJobServiceǁ_persist__mutmut_34 # type: ignore # mutmut generated

mutants_xǁUploadJobServiceǁ_manifest_path__mutmut['_mutmut_orig'] = UploadJobService.xǁUploadJobServiceǁ_manifest_path__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobServiceǁ_manifest_path__mutmut['xǁUploadJobServiceǁ_manifest_path__mutmut_1'] = UploadJobService.xǁUploadJobServiceǁ_manifest_path__mutmut_1 # type: ignore # mutmut generated
