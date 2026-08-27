"""Durable local jobs for refreshing document search data."""

from __future__ import annotations

import json
from _thread import LockType
from concurrent.futures import ThreadPoolExecutor
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


class DocumentIndexJobService:
    """Persist and run local search refreshes with one bounded worker."""

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
        self._executor = ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix="smart-doc-index-update",
        )
        for job_id in self._load():
            self._executor.submit(self._run, job_id)

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
            self._executor.submit(self._run, job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            raise
        return job

    def get(self, job_id: str) -> IndexUpdateJob | None:
        """Return one stable in-memory job snapshot."""
        with self._lock:
            return self._jobs.get(job_id)

    def close(self) -> None:
        """Finish accepted refreshes while retaining failed durable jobs."""
        self._executor.shutdown(wait=True, cancel_futures=False)

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

    def _run(self, job_id: str) -> None:
        """Refresh mutable search fragments from the latest stored document."""
        try:
            self._set_status(job_id, IndexUpdateStatus.UPDATING)
            with self._operation_lock:
                with self._repository_factory() as repository:
                    document = self._get_document(repository, job_id)
                if document is not None:
                    self._vector_index.update_document_data(
                        document.id,
                        document.document,
                    )
            self._set_status(job_id, IndexUpdateStatus.COMPLETED)
            self._manifest_path(job_id).unlink(missing_ok=True)
        except Exception:
            self._set_status(job_id, IndexUpdateStatus.FAILED)

    def _get_document(
        self,
        repository: DocumentRepository,
        job_id: str,
    ) -> StoredDocument | None:
        """Read the current document without copying content into job metadata."""
        with self._lock:
            document_id = self._jobs[job_id].document_id
        return repository.get_document_by_id(document_id)

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

    def _manifest_path(self, job_id: str) -> Path:
        """Return the manifest path for one internal job identifier."""
        return self._queue_path / f"{job_id}.json"
