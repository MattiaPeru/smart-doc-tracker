from __future__ import annotations

import json
import time
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
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
                submitted = jobs.submit(upload, file_name="invoice.png", language="eng")
                for _ in range(100):
                    job = jobs.get(submitted.id)
                    if job is not None and job.status == "failed":
                        break
                    time.sleep(0.01)
                queued_files = list(
                    (root / "processing_queue").glob(f"{submitted.id}.*")
                )
                self.assertEqual(len(queued_files), 2)

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
