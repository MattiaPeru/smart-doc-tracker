"""Bounded process-local jobs for private document uploads."""

from __future__ import annotations

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


ProgressReporter = Callable[[DocumentProcessingStage], None]
UploadProcessor = Callable[[Path, str, ProgressReporter], DocumentProcessingResult]


class UploadJobService:
    """Execute uploaded documents locally with one bounded worker."""

    def __init__(
        self,
        processor: UploadProcessor,
        pending_documents: PendingDocumentService,
    ) -> None:
        """Configure an injected processor without starting external services."""
        self._processor = processor
        self._pending_documents = pending_documents
        self._jobs: dict[str, UploadJob] = {}
        self._lock = Lock()
        self._executor = ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix="smart-doc-upload",
        )

    def submit(self, path: Path, *, file_name: str, language: str) -> UploadJob:
        """Queue an owned temporary file and return its initial job snapshot."""
        now = datetime.now(UTC)
        job = UploadJob(
            id=uuid4().hex,
            file_name=file_name,
            status=UploadJobStatus.QUEUED,
            created_at=now,
            updated_at=now,
        )
        with self._lock:
            self._jobs[job.id] = job
        try:
            self._executor.submit(self._run, job.id, path, file_name, language)
        except RuntimeError:
            path.unlink(missing_ok=True)
            raise
        return job

    def get(self, job_id: str) -> UploadJob | None:
        """Return a stable snapshot of one job."""
        with self._lock:
            return self._jobs.get(job_id)

    def close(self) -> None:
        """Finish accepted work and release the worker thread."""
        self._executor.shutdown(wait=True, cancel_futures=False)

    def _run(
        self,
        job_id: str,
        path: Path,
        file_name: str,
        language: str,
    ) -> None:
        """Process one temporary file and remove it on every exit path."""
        owns_path = True
        try:
            self._set_status(job_id, UploadJobStatus.EXTRACTING)
            result = self._processor(
                path,
                language,
                lambda stage: self._report_stage(job_id, stage),
            )
            if result.document is None:
                raise RuntimeError("Structured processing returned no document")
            pending = self._pending_documents.add(
                path,
                file_name=file_name,
                raw_text=result.raw_text,
                document=result.document,
                sections=result.sections,
            )
            owns_path = False
            self._update(
                job_id,
                status=UploadJobStatus.AWAITING_CONFIRMATION,
                pending_id=pending.id,
            )
        except Exception:
            self._update(
                job_id,
                status=UploadJobStatus.FAILED,
                error="The document could not be processed locally.",
            )
        finally:
            if owns_path:
                path.unlink(missing_ok=True)

    def _report_stage(self, job_id: str, stage: DocumentProcessingStage) -> None:
        """Map pipeline progress onto public job states."""
        status_by_stage = {
            DocumentProcessingStage.EXTRACTION_STARTED: UploadJobStatus.EXTRACTING,
            DocumentProcessingStage.PARSING_STARTED: UploadJobStatus.PARSING,
        }
        status = status_by_stage.get(stage)
        if status is not None:
            self._set_status(job_id, status)

    def _set_status(self, job_id: str, status: UploadJobStatus) -> None:
        """Set a progress-only job status."""
        self._update(job_id, status=status)

    def _update(
        self,
        job_id: str,
        *,
        status: UploadJobStatus,
        document_id: str | None = None,
        pending_id: str | None = None,
        inserted: bool | None = None,
        error: str | None = None,
    ) -> None:
        """Atomically replace one job with an updated immutable snapshot."""
        with self._lock:
            current = self._jobs[job_id]
            self._jobs[job_id] = replace(
                current,
                status=status,
                updated_at=datetime.now(UTC),
                document_id=document_id,
                pending_id=pending_id,
                inserted=inserted,
                error=error,
            )
