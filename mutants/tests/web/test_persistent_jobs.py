from __future__ import annotations

import json
import time
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Event
from unittest import TestCase

from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.pipeline import DocumentProcessingResult
from smart_doc_tracker.web.jobs import UploadJobService
from smart_doc_tracker.web.pending import PendingDocumentService


def _document() -> DocumentData:
    return DocumentData(
        document_type="invoice",
        summary="A local invoice",
        expiry_date=None,
        issue_date=None,
        extracted_data={},
    )


class PersistentUploadJobTests(TestCase):
    def test_retries_failed_job_from_its_retained_source(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            attempts = 0

            def process(path: Path, language: str, reporter: object) -> DocumentProcessingResult:
                nonlocal attempts
                attempts += 1
                if attempts == 1:
                    raise RuntimeError("Private failure detail")
                return DocumentProcessingResult(raw_text="Private local text", document=_document())

            upload = root / "upload.png"
            upload.write_bytes(b"local fixture")
            pending = PendingDocumentService(root / "processed")
            queue_path = root / "processing_queue"
            jobs = UploadJobService(process, pending, queue_path)
            try:
                submitted = jobs.submit(upload, file_name="invoice.png", language="eng")
                for _ in range(100):
                    if jobs.get(submitted.id).status == "failed":
                        break
                    time.sleep(0.01)
                self.assertEqual(jobs.get(submitted.id).status, "failed")
                self.assertTrue(jobs.retry_failed(submitted.id))
                self.assertFalse(jobs.retry_failed(submitted.id))
                for _ in range(100):
                    if jobs.get(submitted.id).status == "awaiting_confirmation":
                        break
                    time.sleep(0.01)
                self.assertEqual(jobs.get(submitted.id).status, "awaiting_confirmation")
                self.assertIsNone(jobs.get(submitted.id).error)
                self.assertEqual(attempts, 2)
                self.assertEqual(len(pending.list()), 1)
            finally:
                jobs.close()
                pending.close()

    def test_bulk_actions_only_change_failed_jobs(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)

            def fail(path: Path, language: str, reporter: object) -> DocumentProcessingResult:
                raise RuntimeError("Private failure detail")

            pending = PendingDocumentService(root / "processed")
            jobs = UploadJobService(fail, pending, root / "processing_queue")
            try:
                identifiers = []
                for index in range(2):
                    upload = root / f"upload-{index}.png"
                    upload.write_bytes(b"local fixture")
                    identifiers.append(jobs.submit(upload, file_name=upload.name, language="eng").id)
                for _ in range(100):
                    if all(jobs.get(job_id).status == "failed" for job_id in identifiers):
                        break
                    time.sleep(0.01)
                self.assertEqual(jobs.retry_all_failed(), 2)
                for _ in range(100):
                    if all(jobs.get(job_id).status == "failed" for job_id in identifiers):
                        break
                    time.sleep(0.01)
                self.assertTrue(all(jobs.get(job_id).status == "failed" for job_id in identifiers))
                self.assertEqual(jobs.discard_all_failed(), 2)
                self.assertEqual(jobs.discard_all_failed(), 0)
                self.assertEqual(list((root / "processing_queue").iterdir()), [])
            finally:
                jobs.close()
                pending.close()

    def test_discards_failed_job_and_its_local_source(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)

            def fail(
                path: Path,
                language: str,
                reporter: object,
            ) -> DocumentProcessingResult:
                raise RuntimeError("Sensitive processing detail")

            upload = root / "upload.png"
            upload.write_bytes(b"local fixture")
            pending = PendingDocumentService(root / "processed")
            jobs = UploadJobService(fail, pending, root / "processing_queue")
            try:
                with self.assertLogs(
                    "smart_doc_tracker.web.jobs", level="ERROR"
                ) as captured:
                    submitted = jobs.submit(
                        upload,
                        file_name="invoice.png",
                        language="eng",
                    )
                    for _ in range(100):
                        job = jobs.get(submitted.id)
                        if job is not None and job.status == "failed":
                            break
                        time.sleep(0.01)
                queued_files = list(
                    (root / "processing_queue").glob(f"{submitted.id}.*")
                )
                self.assertEqual(len(queued_files), 2)
                log_output = "\n".join(captured.output)
                self.assertIn(
                    "failed during local processing (RuntimeError)",
                    log_output,
                )
                self.assertNotIn("Sensitive processing detail", log_output)

                self.assertTrue(jobs.discard_failed(submitted.id))

                self.assertIsNone(jobs.get(submitted.id))
                self.assertEqual(
                    list((root / "processing_queue").glob(f"{submitted.id}.*")),
                    [],
                )
            finally:
                jobs.close()
                pending.close()

    def test_resumes_an_interrupted_processing_job_on_startup(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            queue_path = root / "processing_queue"
            queue_path.mkdir()
            source_path = queue_path / "job-id.png"
            source_path.write_bytes(b"local fixture")
            now = datetime.now(UTC).isoformat()
            (queue_path / "job-id.json").write_text(
                json.dumps(
                    {
                        "id": "job-id",
                        "file_name": "invoice.png",
                        "status": "parsing",
                        "created_at": now,
                        "updated_at": now,
                        "pending_id": None,
                        "error": None,
                        "source_file": source_path.name,
                        "language": "eng",
                    }
                ),
                encoding="utf-8",
            )
            processed: list[Path] = []

            def process(
                path: Path,
                language: str,
                reporter: object,
            ) -> DocumentProcessingResult:
                processed.append(path)
                return DocumentProcessingResult(
                    raw_text="Private local text",
                    document=_document(),
                )

            pending = PendingDocumentService(root / "processed")
            jobs = UploadJobService(process, pending, queue_path)
            try:
                for _ in range(100):
                    job = jobs.get("job-id")
                    if job is not None and job.status == "awaiting_confirmation":
                        break
                    time.sleep(0.01)
                self.assertEqual(len(processed), 1)
                self.assertEqual(jobs.get("job-id").status, "awaiting_confirmation")
                self.assertEqual(len(pending.list()), 1)
            finally:
                jobs.close()
                pending.close()

    def test_shutdown_leaves_active_and_queued_uploads_for_restart(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            queue_path = root / "processing_queue"
            started = Event()
            release = Event()
            processed: list[str] = []

            def blocked_process(
                path: Path, language: str, reporter: object
            ) -> DocumentProcessingResult:
                processed.append(path.name)
                started.set()
                release.wait(timeout=5)
                return DocumentProcessingResult(raw_text="Local text", document=_document())

            pending = PendingDocumentService(root / "processed")
            first = UploadJobService(blocked_process, pending, queue_path)
            try:
                uploads = []
                for index in range(2):
                    upload = root / f"upload-{index}.png"
                    upload.write_bytes(b"local fixture")
                    uploads.append(first.submit(upload, file_name=upload.name, language="eng"))
                self.assertTrue(started.wait(timeout=1))
                before = time.monotonic()
                first.close()
                self.assertLess(time.monotonic() - before, 0.5)
                release.set()
                time.sleep(0.05)
                self.assertEqual(len(processed), 1)
                self.assertEqual(len(pending.list()), 0)
                self.assertTrue(all((queue_path / f"{job.id}.json").exists() for job in uploads))

                resumed = UploadJobService(blocked_process, pending, queue_path)
                try:
                    for _ in range(100):
                        if all(resumed.get(job.id).status == "awaiting_confirmation" for job in uploads):
                            break
                        time.sleep(0.01)
                    self.assertTrue(all(resumed.get(job.id).status == "awaiting_confirmation" for job in uploads))
                    self.assertEqual(len(pending.list()), 2)
                finally:
                    resumed.close()
            finally:
                release.set()
                first.close()
                pending.close()

    def test_recovers_transfer_completed_before_job_manifest_update(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            queue_path = root / "processing_queue"
            queue_path.mkdir()
            source = queue_path / "job-id.png"
            source.write_bytes(b"local fixture")
            pending = PendingDocumentService(root / "processed")
            staged = pending.add(
                source,
                file_name="invoice.png",
                raw_text="Private local text",
                document=_document(),
                identifier="job-id",
            )
            now = datetime.now(UTC).isoformat()
            (queue_path / "job-id.json").write_text(
                json.dumps(
                    {
                        "id": "job-id",
                        "file_name": "invoice.png",
                        "status": "parsing",
                        "created_at": now,
                        "updated_at": now,
                        "pending_id": None,
                        "error": None,
                        "source_file": source.name,
                        "language": "eng",
                    }
                ),
                encoding="utf-8",
            )

            def unexpected_process(
                path: Path, language: str, reporter: object
            ) -> DocumentProcessingResult:
                self.fail("A transferred document must not be processed again.")

            jobs = UploadJobService(unexpected_process, pending, queue_path)
            try:
                restored = jobs.get("job-id")
                self.assertEqual(restored.status, "awaiting_confirmation")
                self.assertEqual(restored.pending_id, staged.id)
                self.assertEqual(len(pending.list()), 1)
            finally:
                jobs.close()
                pending.close()

    def test_restores_documents_awaiting_confirmation(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source_path = root / "upload.png"
            source_path.write_bytes(b"local fixture")
            first = PendingDocumentService(root / "processed")
            added = first.add(
                source_path,
                file_name="invoice.png",
                raw_text="Private local text",
                document=_document(),
            )
            first.close()

            restored = PendingDocumentService(root / "processed")
            try:
                item = restored.get(added.id)
                self.assertIsNotNone(item)
                self.assertEqual(item.file_name, "invoice.png")
                self.assertTrue(item.source_path.exists())
            finally:
                restored.close()
