from __future__ import annotations

import time
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any
from unittest import TestCase

from fastapi.testclient import TestClient

from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.web.app import WebDependencies, create_app


def _record(
    identifier: str,
    *,
    expiry_date: str | None,
    city: str = "Rome",
) -> StoredDocument:
    document = DocumentData(
        document_type="insurance_policy",
        summary="A local insurance policy",
        expiry_date=expiry_date,
        issue_date="2026-01-01",
        extracted_data={"holder": {"city": city}, "active": True},
    )
    return StoredDocument(
        id=identifier,
        file_hash="a" * 64,
        document=document,
        created_at=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
    )


class FakeRepository:
    def __init__(self, records: list[StoredDocument]) -> None:
        self.records = records
        self.searches: list[tuple[str, Any]] = []

    def __enter__(self) -> FakeRepository:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def get_all_documents(self) -> list[StoredDocument]:
        return self.records

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        return next((item for item in self.records if item.id == document_id), None)

    def search_by_dynamic_field(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        self.searches.append((field_key, field_value))
        if field_key == "active" and field_value is True:
            return self.records[:1]
        if field_key == "holder.city" and field_value == "Rome":
            return self.records[:1]
        return []


class WebApplicationTests(TestCase):
    def setUp(self) -> None:
        self.records = [
            _record("expired", expiry_date="2026-08-25"),
            _record("soon", expiry_date="2026-09-10"),
            _record("valid", expiry_date="2027-01-01"),
            _record("none", expiry_date=None),
        ]
        self.repository = FakeRepository(self.records)
        self.processed_paths: list[Path] = []

        def process(path: Path, language: str, reporter: Any) -> DocumentInsertResult:
            self.assertTrue(path.exists())
            self.assertEqual(language, "ita")
            self.processed_paths.append(path)
            return DocumentInsertResult(record=self.records[0], inserted=True)

        app = create_app(
            WebDependencies(
                repository_factory=lambda: self.repository,
                upload_processor=process,
                today_provider=lambda: date(2026, 8, 26),
            )
        )
        self.client_context = TestClient(app)
        self.client = self.client_context.__enter__()

    def tearDown(self) -> None:
        self.client_context.__exit__(None, None, None)

    def test_renders_dashboard_and_classifies_expirations(self) -> None:
        dashboard = self.client.get("/")
        response = self.client.get("/api/documents")

        self.assertEqual(dashboard.status_code, 200)
        self.assertIn("Smart Doc Tracker", dashboard.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [item["expiration_status"] for item in response.json()],
            ["expired", "soon", "valid", "none"],
        )

    def test_queries_dynamic_json_values_and_validates_parameter_pairs(self) -> None:
        response = self.client.get(
            "/api/documents",
            params={"field_key": "active", "field_value": "true"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.repository.searches, [("active", True)])
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(
            self.client.get(
                "/api/documents", params={"field_key": "active"}
            ).status_code,
            422,
        )

    def test_returns_document_detail_and_not_found(self) -> None:
        self.assertEqual(
            self.client.get("/api/documents/soon").json()["id"],
            "soon",
        )
        self.assertEqual(self.client.get("/api/documents/missing").status_code, 404)

    def test_uploads_to_a_job_and_removes_the_temporary_file(self) -> None:
        response = self.client.post(
            "/api/uploads",
            files={"file": ("policy.png", b"local fixture", "image/png")},
            data={"language": "ita"},
        )

        self.assertEqual(response.status_code, 202)
        job_id = response.json()["id"]
        job: dict[str, Any] = {}
        for _ in range(100):
            job = self.client.get(f"/api/jobs/{job_id}").json()
            if job["status"] in {"completed", "failed"}:
                break
            time.sleep(0.01)
        self.assertEqual(job["status"], "completed")
        self.assertEqual(job["document_id"], "expired")
        self.assertTrue(self.processed_paths)
        self.assertFalse(self.processed_paths[0].exists())

    def test_rejects_unsupported_or_empty_uploads(self) -> None:
        unsupported = self.client.post(
            "/api/uploads",
            files={"file": ("notes.txt", b"text", "text/plain")},
        )
        empty = self.client.post(
            "/api/uploads",
            files={"file": ("empty.pdf", b"", "application/pdf")},
        )

        self.assertEqual(unsupported.status_code, 415)
        self.assertEqual(empty.status_code, 422)
