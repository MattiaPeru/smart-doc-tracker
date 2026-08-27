from __future__ import annotations

import json
import time
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Event
from unittest import TestCase

from smart_doc_tracker.db.database import StoredDocument
from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.web.index_jobs import DocumentIndexJobService


def _record() -> StoredDocument:
    return StoredDocument(
        id="document-id",
        file_hash="a" * 64,
        document=DocumentData(
            document_type="invoice",
            summary="Sensitive local summary",
            expiry_date=None,
            issue_date=None,
            extracted_data={"account_number": "private-value"},
        ),
        created_at=datetime(2026, 8, 27, tzinfo=UTC),
    )


class FakeRepository:
    def __init__(self, record: StoredDocument | None) -> None:
        self.record = record

    def __enter__(self) -> FakeRepository:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        if self.record is not None and self.record.id == document_id:
            return self.record
        return None


class BlockingVectorIndex:
    def __init__(self) -> None:
        self.started = Event()
        self.release = Event()
        self.updated: list[str] = []

    def update_document_data(
        self,
        document_id: str,
        document: DocumentData,
    ) -> None:
        self.started.set()
        self.release.wait(timeout=2)
        self.updated.append(document_id)


class FailingVectorIndex:
    def update_document_data(
        self,
        document_id: str,
        document: DocumentData,
    ) -> None:
        raise RuntimeError("Sensitive local summary")


class PersistentIndexJobTests(TestCase):
    def test_reports_refresh_failure_without_document_contents(self) -> None:
        with TemporaryDirectory() as directory:
            jobs = DocumentIndexJobService(
                lambda: FakeRepository(_record()),
                FailingVectorIndex(),  # type: ignore[arg-type]
                Path(directory) / "index_update_queue",
            )
            try:
                with self.assertLogs(
                    "smart_doc_tracker.web.index_jobs", level="ERROR"
                ) as captured:
                    submitted = jobs.submit("document-id")
                    for _ in range(100):
                        job = jobs.get(submitted.id)
                        if job is not None and job.status == "failed":
                            break
                        time.sleep(0.01)
                log_output = "\n".join(captured.output)
                self.assertIn("failed (RuntimeError)", log_output)
                self.assertNotIn("Sensitive local summary", log_output)
            finally:
                jobs.close()

    def test_persists_only_identifiers_before_background_refresh(self) -> None:
        with TemporaryDirectory() as directory:
            queue_path = Path(directory) / "index_update_queue"
            repository = FakeRepository(_record())
            vector = BlockingVectorIndex()
            jobs = DocumentIndexJobService(
                lambda: repository,
                vector,  # type: ignore[arg-type]
                queue_path,
            )
            try:
                submitted = jobs.submit("document-id")
                self.assertTrue(vector.started.wait(timeout=1))
                manifest = json.loads(
                    (queue_path / f"{submitted.id}.json").read_text(encoding="utf-8")
                )
                self.assertEqual(manifest["document_id"], "document-id")
                self.assertNotIn("Sensitive local summary", json.dumps(manifest))
                self.assertNotIn("private-value", json.dumps(manifest))

                vector.release.set()
                for _ in range(100):
                    job = jobs.get(submitted.id)
                    if job is not None and job.status == "completed":
                        break
                    time.sleep(0.01)
                self.assertEqual(jobs.get(submitted.id).status, "completed")
                self.assertEqual(vector.updated, ["document-id"])
                self.assertFalse((queue_path / f"{submitted.id}.json").exists())
            finally:
                vector.release.set()
                jobs.close()

    def test_resumes_an_interrupted_refresh_on_startup(self) -> None:
        with TemporaryDirectory() as directory:
            queue_path = Path(directory) / "index_update_queue"
            queue_path.mkdir()
            now = datetime.now(UTC).isoformat()
            (queue_path / "job-id.json").write_text(
                json.dumps(
                    {
                        "id": "job-id",
                        "document_id": "document-id",
                        "status": "updating",
                        "created_at": now,
                        "updated_at": now,
                    }
                ),
                encoding="utf-8",
            )
            repository = FakeRepository(_record())
            vector = BlockingVectorIndex()
            vector.release.set()
            jobs = DocumentIndexJobService(
                lambda: repository,
                vector,  # type: ignore[arg-type]
                queue_path,
            )
            try:
                for _ in range(100):
                    job = jobs.get("job-id")
                    if job is not None and job.status == "completed":
                        break
                    time.sleep(0.01)
                self.assertEqual(jobs.get("job-id").status, "completed")
                self.assertEqual(vector.updated, ["document-id"])
                self.assertFalse((queue_path / "job-id.json").exists())
            finally:
                jobs.close()
