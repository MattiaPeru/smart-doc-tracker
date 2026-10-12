"""Durable local jobs for refreshing document search data."""

from __future__ import annotations

import json
import logging
from _thread import LockType
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from threading import Lock
from uuid import uuid4

from ..db.database import StoredDocument
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..mutation_pipeline import RepositoryFactory
from ._background_worker import BackgroundWorker

_LOGGER = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IndexUpdateStatus(StrEnum):
    """Observable states of one local search refresh."""

    QUEUED = "queued"
    UPDATING = "updating"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class IndexUpdateJob:
    """Privacy-conscious snapshot of one search refresh."""

    id: str
    document_id: str
    status: IndexUpdateStatus
    created_at: datetime
    updated_at: datetime
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁ_get_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentIndexJobServiceǁ_manifest_path__mutmut: MutantDict = {}  # type: ignore


class DocumentIndexJobService:
    """Persist and run local search refreshes with one bounded worker."""

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ__init____mutmut)
    def __init__(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_orig(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_1(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = None
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_2(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = None
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_3(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = None
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_4(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(None).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_5(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=None, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_6(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=None)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_7(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_8(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, )
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_9(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=False, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_10(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=False)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_11(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = None
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_12(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock and Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_13(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = None
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_14(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = None
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_15(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = None
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_16(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(None, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_17(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name=None)
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_18(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_19(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, )
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_20(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="XXsmart-doc-index-updateXX")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_21(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="SMART-DOC-INDEX-UPDATE")
        for job_id in self._load():
            self._worker.submit(job_id)

    def xǁDocumentIndexJobServiceǁ__init____mutmut_22(
        self,
        repository_factory: RepositoryFactory,
        vector_index: DocumentVectorIndex,
        queue_path: str | Path = Path("data/index_update_queue"),
        operation_lock: LockType | None = None,
    ) -> None:
        """Load durable jobs and resume unfinished local refreshes."""
        self._repository_factory = repository_factory
        self._vector_index = vector_index
        self._queue_path = Path(queue_path).expanduser()
        self._queue_path.mkdir(parents=True, exist_ok=True)
        self._operation_lock = operation_lock or Lock()
        self._jobs: dict[str, IndexUpdateJob] = {}
        self._lock = Lock()
        self._worker = BackgroundWorker(self._run, name="smart-doc-index-update")
        for job_id in self._load():
            self._worker.submit(None)

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut)
    def submit(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_orig(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_1(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_2(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError(None)
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_3(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("XXdocument_id cannot be emptyXX")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_4(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("DOCUMENT_ID CANNOT BE EMPTY")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_5(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = None
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_6(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(None)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_7(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = None
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_8(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=None,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_9(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=None,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_10(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=None,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_11(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=None,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_12(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=None,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_13(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_14(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_15(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_16(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_17(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_18(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = None
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_19(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(None)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_20(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(None)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_21(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(None, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_22(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_23(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, )
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_24(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=None)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_25(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(None).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_26(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=False)
            raise
        _LOGGER.info("Search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_27(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info(None, job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_28(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", None)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_29(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info(job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_30(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("Search refresh job %s queued.", )
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_31(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("XXSearch refresh job %s queued.XX", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_32(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("search refresh job %s queued.", job.id)
        return job

    def xǁDocumentIndexJobServiceǁsubmit__mutmut_33(self, document_id: str) -> IndexUpdateJob:
        """Durably queue the latest stored version of one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        now = datetime.now(UTC)
        job = IndexUpdateJob(
            id=uuid4().hex,
            document_id=document_id,
            status=IndexUpdateStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        try:
            with self._lock:
                self._jobs[job.id] = job
                self._persist(job)
            self._worker.submit(job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        _LOGGER.info("SEARCH REFRESH JOB %S QUEUED.", job.id)
        return job

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁget__mutmut)
    def get(self, job_id: str) -> IndexUpdateJob | None:
        """Return one stable in-memory job snapshot."""
        with self._lock:
            return self._jobs.get(job_id)

    def xǁDocumentIndexJobServiceǁget__mutmut_orig(self, job_id: str) -> IndexUpdateJob | None:
        """Return one stable in-memory job snapshot."""
        with self._lock:
            return self._jobs.get(job_id)

    def xǁDocumentIndexJobServiceǁget__mutmut_1(self, job_id: str) -> IndexUpdateJob | None:
        """Return one stable in-memory job snapshot."""
        with self._lock:
            return self._jobs.get(None)

    def close(self) -> None:
        """Stop promptly and leave unfinished refreshes for the next start."""
        self._worker.close()

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ_load__mutmut)
    def _load(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_orig(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_1(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = None
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_2(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(None):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_3(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob(None)):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_4(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("XX*.jsonXX")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_5(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.JSON")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_6(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = None
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_7(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(None)
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_8(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding=None))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_9(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="XXutf-8XX"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_10(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="UTF-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_11(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = None
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_12(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=None,
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_13(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=None,
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_14(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=None,
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_15(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=None,
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_16(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=None,
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_17(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_18(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_19(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_20(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_21(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_22(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(None),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_23(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["XXidXX"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_24(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["ID"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_25(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(None),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_26(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["XXdocument_idXX"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_27(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["DOCUMENT_ID"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_28(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(None),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_29(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(None)),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_30(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["XXstatusXX"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_31(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["STATUS"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_32(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(None),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_33(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(None)),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_34(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["XXcreated_atXX"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_35(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["CREATED_AT"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_36(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(None),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_37(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(None)),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_38(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["XXupdated_atXX"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_39(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["UPDATED_AT"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_40(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path == self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_41(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(None):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_42(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    break
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_43(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_44(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    break
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_45(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                break
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_46(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_47(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = None
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_48(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    None,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_49(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=None,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_50(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=None,
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_51(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_52(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_53(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_54(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(None),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_55(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(None)
                resumable.append(job.id)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_56(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(None)
            self._jobs[job.id] = job
        return resumable

    def xǁDocumentIndexJobServiceǁ_load__mutmut_57(self) -> list[str]:
        """Load valid manifests and reset unfinished work to queued."""
        resumable: list[str] = []
        for manifest_path in sorted(self._queue_path.glob("*.json")):
            try:
                payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                job = IndexUpdateJob(
                    id=str(payload["id"]),
                    document_id=str(payload["document_id"]),
                    status=IndexUpdateStatus(str(payload["status"])),
                    created_at=datetime.fromisoformat(str(payload["created_at"])),
                    updated_at=datetime.fromisoformat(str(payload["updated_at"])),
                )
                if manifest_path != self._manifest_path(job.id):
                    continue
                if not job.document_id.strip():
                    continue
            except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError):
                continue
            if job.status is not IndexUpdateStatus.COMPLETED:
                job = replace(
                    job,
                    status=IndexUpdateStatus.QUEUED,
                    updated_at=datetime.now(UTC),
                )
                self._persist(job)
                resumable.append(job.id)
            self._jobs[job.id] = None
        return resumable

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ_run__mutmut)
    def _run(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_orig(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_1(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info(None, job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_2(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", None)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_3(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info(job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_4(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", )
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_5(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("XXSearch refresh job %s started.XX", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_6(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_7(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("SEARCH REFRESH JOB %S STARTED.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_8(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(None, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_9(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, None)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_10(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_11(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, )
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_12(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = None
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_13(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(None, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_14(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, None)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_15(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_16(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, )
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_17(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_18(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        None,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_19(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        None,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_20(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_21(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_22(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(None, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_23(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, None)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_24(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_25(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, )
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_26(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=None)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_27(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(None).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_28(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=False)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_29(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info(None, job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_30(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", None)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_31(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info(job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_32(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", )
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_33(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("XXSearch refresh job %s completed.XX", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_34(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_35(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("SEARCH REFRESH JOB %S COMPLETED.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_36(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                None,
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_37(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                None,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_38(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                None,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_39(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_40(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_41(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_42(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "XXSearch refresh job %s failed (%s).XX",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_43(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_44(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "SEARCH REFRESH JOB %S FAILED (%S).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_45(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(None).__name__,
            )
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_46(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(None, IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_47(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, None)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_48(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(IndexUpdateStatus.FAILED)

    def xǁDocumentIndexJobServiceǁ_run__mutmut_49(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        if self._worker.stopping:
            return
        try:
            _LOGGER.info("Search refresh job %s started.", job_id)
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    if self._worker.stopping:
                        return
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            if self._worker.stopping:
                return
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
            _LOGGER.info("Search refresh job %s completed.", job_id)
        except Exception as exc:
            if self._worker.stopping:
                return
            # Do not include exception text: adapters may embed document data in it.
            _LOGGER.error(
                "Search refresh job %s failed (%s).",
                job_id,
                type(exc).__name__,
            )
            self._set_status(job_id, )

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ_get_document__mutmut)
    def _get_document(
        self,
        repository: DocumentRepository,
        job_id: str,
    ) -> StoredDocument | None:
        """Read the current document without copying content into job metadata."""
        with self._lock:
            document_id = self._jobs[job_id].document_id
        return repository.get_document_by_id(document_id)

    def xǁDocumentIndexJobServiceǁ_get_document__mutmut_orig(
        self,
        repository: DocumentRepository,
        job_id: str,
    ) -> StoredDocument | None:
        """Read the current document without copying content into job metadata."""
        with self._lock:
            document_id = self._jobs[job_id].document_id
        return repository.get_document_by_id(document_id)

    def xǁDocumentIndexJobServiceǁ_get_document__mutmut_1(
        self,
        repository: DocumentRepository,
        job_id: str,
    ) -> StoredDocument | None:
        """Read the current document without copying content into job metadata."""
        with self._lock:
            document_id = None
        return repository.get_document_by_id(document_id)

    def xǁDocumentIndexJobServiceǁ_get_document__mutmut_2(
        self,
        repository: DocumentRepository,
        job_id: str,
    ) -> StoredDocument | None:
        """Read the current document without copying content into job metadata."""
        with self._lock:
            document_id = self._jobs[job_id].document_id
        return repository.get_document_by_id(None)

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut)
    def _set_status(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_orig(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_1(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = None
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_2(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                None,
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_3(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=None,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_4(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=None,
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_5(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_6(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_7(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_8(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=datetime.now(None),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_9(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = None
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_10(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is IndexUpdateStatus.COMPLETED:
                self._persist(job)

    def xǁDocumentIndexJobServiceǁ_set_status__mutmut_11(self, job_id: str, status: IndexUpdateStatus) -> None:
        """Atomically update and persist one job status."""
        with self._lock:
            job = replace(
                self._jobs[job_id],
                status=status,
                updated_at=datetime.now(UTC),
            )
            self._jobs[job_id] = job
            if status is not IndexUpdateStatus.COMPLETED:
                self._persist(None)

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut)
    def _persist(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_orig(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_1(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = None
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_2(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "XXidXX": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_3(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "ID": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_4(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "XXdocument_idXX": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_5(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "DOCUMENT_ID": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_6(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "XXstatusXX": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_7(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "STATUS": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_8(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "XXcreated_atXX": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_9(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "CREATED_AT": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_10(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "XXupdated_atXX": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_11(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "UPDATED_AT": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_12(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = None
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_13(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(None)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_14(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = None
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_15(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(None)
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_16(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix("XX.json.tmpXX")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_17(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".JSON.TMP")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_18(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(None, encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_19(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding=None)
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_20(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_21(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), )
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_22(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(None), encoding="utf-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_23(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="XXutf-8XX")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_24(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="UTF-8")
        temporary.replace(destination)

    def xǁDocumentIndexJobServiceǁ_persist__mutmut_25(self, job: IndexUpdateJob) -> None:
        """Atomically persist identifiers and status without document content."""
        payload = {
            "id": job.id,
            "document_id": job.document_id,
            "status": job.status.value,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
        }
        destination = self._manifest_path(job.id)
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(payload), encoding="utf-8")
        temporary.replace(None)

    @_mutmut_mutated(mutants_xǁDocumentIndexJobServiceǁ_manifest_path__mutmut)
    def _manifest_path(self, job_id: str) -> Path:
        """Return the manifest path for one internal job identifier."""
        return self._queue_path / f"{job_id}.json"

    def xǁDocumentIndexJobServiceǁ_manifest_path__mutmut_orig(self, job_id: str) -> Path:
        """Return the manifest path for one internal job identifier."""
        return self._queue_path / f"{job_id}.json"

    def xǁDocumentIndexJobServiceǁ_manifest_path__mutmut_1(self, job_id: str) -> Path:
        """Return the manifest path for one internal job identifier."""
        return self._queue_path * f"{job_id}.json"

mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_3'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_4'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_5'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_6'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_7'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_8'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_9'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_10'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_11'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_12'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_13'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_14'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_15'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_16'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_17'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_18'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_19'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_20'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_21'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ__init____mutmut['xǁDocumentIndexJobServiceǁ__init____mutmut_22'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ__init____mutmut_22 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_3'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_4'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_5'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_6'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_7'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_8'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_9'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_10'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_11'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_12'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_13'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_14'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_15'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_16'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_17'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_18'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_19'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_20'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_21'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_22'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_23'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_24'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_25'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_26'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_27'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_28'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_29'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_30'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_31'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_32'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁsubmit__mutmut['xǁDocumentIndexJobServiceǁsubmit__mutmut_33'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁsubmit__mutmut_33 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁget__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁget__mutmut['xǁDocumentIndexJobServiceǁget__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁget__mutmut_1 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_3'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_4'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_5'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_6'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_7'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_8'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_9'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_10'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_11'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_12'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_13'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_14'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_15'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_16'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_17'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_18'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_19'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_20'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_21'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_22'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_23'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_24'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_25'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_26'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_27'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_28'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_29'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_30'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_31'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_32'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_33'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_34'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_35'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_36'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_37'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_38'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_39'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_40'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_41'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_42'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_43'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_44'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_45'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_46'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_47'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_48'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_49'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_50'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_51'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_52'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_53'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_54'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_55'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_56'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_load__mutmut['xǁDocumentIndexJobServiceǁ_load__mutmut_57'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_load__mutmut_57 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_3'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_4'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_5'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_6'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_7'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_8'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_9'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_10'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_11'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_12'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_13'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_14'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_15'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_16'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_17'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_18'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_19'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_20'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_21'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_22'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_23'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_24'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_25'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_26'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_27'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_28'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_29'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_30'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_31'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_32'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_33'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_34'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_35'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_36'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_37'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_38'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_39'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_40'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_41'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_42'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_43'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_44'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_45'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_46'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_47'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_48'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_run__mutmut['xǁDocumentIndexJobServiceǁ_run__mutmut_49'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_run__mutmut_49 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁ_get_document__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_get_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_get_document__mutmut['xǁDocumentIndexJobServiceǁ_get_document__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_get_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_get_document__mutmut['xǁDocumentIndexJobServiceǁ_get_document__mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_get_document__mutmut_2 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_3'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_4'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_5'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_6'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_7'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_8'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_9'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_10'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_set_status__mutmut['xǁDocumentIndexJobServiceǁ_set_status__mutmut_11'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_set_status__mutmut_11 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_2'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_3'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_4'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_5'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_6'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_7'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_8'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_9'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_10'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_11'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_12'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_13'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_14'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_15'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_16'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_17'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_18'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_19'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_20'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_21'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_22'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_23'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_24'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_persist__mutmut['xǁDocumentIndexJobServiceǁ_persist__mutmut_25'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_persist__mutmut_25 # type: ignore # mutmut generated

mutants_xǁDocumentIndexJobServiceǁ_manifest_path__mutmut['_mutmut_orig'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_manifest_path__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexJobServiceǁ_manifest_path__mutmut['xǁDocumentIndexJobServiceǁ_manifest_path__mutmut_1'] = DocumentIndexJobService.xǁDocumentIndexJobServiceǁ_manifest_path__mutmut_1 # type: ignore # mutmut generated
