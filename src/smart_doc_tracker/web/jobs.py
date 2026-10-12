"""Persistent bounded jobs for private document uploads."""

from __future__ import annotations

import json
import logging
import shutil
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from threading import Lock
from uuid import uuid4

from ..pipeline import DocumentProcessingResult, DocumentProcessingStage
from .pending import PendingDocumentService

_LOGGER = logging.getLogger(__name__)


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


class UploadJobService:
    """Persist and execute uploaded documents locally with one bounded worker."""

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
        self._executor = ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix="smart-doc-upload",
        )
        for job_id in self._load():
            self._executor.submit(self._run, job_id)

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
            self._executor.submit(self._run, job.id)
        except Exception:
            with self._lock:
                self._jobs.pop(job.id, None)
            self._manifest_path(job.id).unlink(missing_ok=True)
            source_path.unlink(missing_ok=True)
            raise
        _LOGGER.info("Upload job %s queued.", job.id)
        return job

    def get(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            stored = self._jobs.get(job_id)
            return stored.job if stored is not None else None

    def list_processing(self) -> list[UploadJob]:
        """List queued, active, and failed jobs in creation order."""
        with self._lock:
            jobs = [
                stored.job
                for stored in self._jobs.values()
                if stored.job.status is not UploadJobStatus.AWAITING_CONFIRMATION
            ]
        return sorted(jobs, key=lambda item: (item.created_at, item.id))

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
                self._executor.submit(self._run, job_id)
            except RuntimeError:
                self._jobs[job_id] = stored
                self._persist(stored)
                raise
        return True

    def retry_all_failed(self) -> int:
        """Queue every failed job with an available local source."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.retry_failed(job_id) for job_id in job_ids)

    def discard_all_failed(self) -> int:
        """Remove all failed jobs and their owned local source files."""
        with self._lock:
            job_ids = [
                job_id for job_id, stored in self._jobs.items()
                if stored.job.status is UploadJobStatus.FAILED
            ]
        return sum(self.discard_failed(job_id) for job_id in job_ids)

    def close(self) -> None:
        """Finish accepted work while retaining durable queue state."""
        self._executor.shutdown(wait=True, cancel_futures=False)

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
                if source_path.is_file():
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

    def _run(self, job_id: str) -> None:
        """Process one durable source and transfer it to confirmation staging."""
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

    def _report_stage(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            self._set_status(job_id, status)
        _LOGGER.info(
            "Upload job %s: %s.",
            job_id,
            stage.value.replace("_", " "),
        )

    def _set_status(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(job_id, status=status)

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

    def _manifest_path(self, job_id: str) -> Path:
        """Return the manifest path for one validated internal identifier."""
        return self._queue_path / f"{job_id}.json"
