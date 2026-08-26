from __future__ import annotations

import time
from datetime import UTC, date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
from unittest import TestCase

from fastapi.testclient import TestClient

from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.models.rag import IndexedDocumentFragment
from smart_doc_tracker.pipeline import DocumentProcessingResult
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

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
    ) -> DocumentInsertResult:
        record = StoredDocument(
            id="confirmed",
            file_hash=file_hash,
            document=document,
            created_at=datetime(2026, 8, 26, 12, 0, tzinfo=UTC),
        )
        self.records.append(record)
        return DocumentInsertResult(record=record, inserted=True)

    def upsert_document_sections(self, document_id: str, sections: Any) -> None:
        return None

    def update_document(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        for index, record in enumerate(self.records):
            if record.id == document_id:
                updated = StoredDocument(
                    id=record.id,
                    file_hash=record.file_hash,
                    document=document,
                    created_at=record.created_at,
                )
                self.records[index] = updated
                return updated
        return None

    def delete_document(self, document_id: str) -> StoredDocument | None:
        record = self.get_document_by_id(document_id)
        if record is not None:
            self.records.remove(record)
        return record


class FakeVectorIndex:
    def __init__(self) -> None:
        self.upserts: list[tuple[str, str, DocumentData]] = []
        self.updates: list[tuple[str, DocumentData]] = []
        self.deletes: list[str] = []

    def upsert_document(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        self.upserts.append((document_id, raw_text, document))

    def snapshot_document(self, document_id: str) -> dict[str, Any]:
        return {"ids": []}

    def restore_document(self, snapshot: dict[str, Any]) -> None:
        return None

    def update_document_data(
        self,
        document_id: str,
        document: DocumentData,
    ) -> None:
        self.updates.append((document_id, document))

    def delete_document(self, document_id: str) -> None:
        self.deletes.append(document_id)

    def query(self, question: str, *, limit: int = 5) -> list[Any]:
        return []

    def get_document_fragments(self, document_id: str) -> list[IndexedDocumentFragment]:
        return [
            IndexedDocumentFragment(
                f"{document_id}:raw:0001",
                "[Page 1]\nPrivate local text",
                "raw_text",
            )
        ]


class WebApplicationTests(TestCase):
    def setUp(self) -> None:
        self.records = [
            _record("expired", expiry_date="2026-08-25"),
            _record("soon", expiry_date="2026-09-10"),
            _record("valid", expiry_date="2027-01-01"),
            _record("none", expiry_date=None),
        ]
        self.repository = FakeRepository(self.records)
        self.vector_index = FakeVectorIndex()
        self.temporary_directory = TemporaryDirectory()
        self.processed_paths: list[Path] = []

        def process(
            path: Path,
            language: str,
            reporter: Any,
        ) -> DocumentProcessingResult:
            self.assertTrue(path.exists())
            self.assertEqual(language, "ita")
            self.processed_paths.append(path)
            return DocumentProcessingResult(
                raw_text="Private local text",
                document=self.records[0].document,
            )

        app = create_app(
            WebDependencies(
                repository_factory=lambda: self.repository,
                upload_processor=process,
                today_provider=lambda: date(2026, 8, 26),
                vector_index=self.vector_index,
                processed_path=Path(self.temporary_directory.name) / "processed",
            )
        )
        self.client_context = TestClient(app)
        self.client = self.client_context.__enter__()

    def tearDown(self) -> None:
        self.client_context.__exit__(None, None, None)
        self.temporary_directory.cleanup()

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

    def test_dashboard_messages_are_visible_and_dismissible(self) -> None:
        script = self.client.get("/static/dashboard.js")
        stylesheet = self.client.get("/static/dashboard.css")

        self.assertEqual(script.status_code, 200)
        self.assertIn('message.addEventListener("click", clearMessage)', script.text)
        self.assertIn('isError ? "alert" : "status"', script.text)
        self.assertEqual(stylesheet.status_code, 200)
        self.assertIn("position: fixed", stylesheet.text)
        self.assertIn("z-index: 1000", stylesheet.text)

    def test_dashboard_exposes_a_separate_processing_queue(self) -> None:
        dashboard = self.client.get("/")
        script = self.client.get("/static/dashboard.js")
        response = self.client.get("/api/jobs")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
        self.assertIn('id="queue-tab"', dashboard.text)
        self.assertIn('id="queue-panel"', dashboard.text)
        self.assertNotIn('id="job-status"', dashboard.text)
        self.assertIn("OCR / text extraction", script.text)
        self.assertIn("Local LLM analysis", script.text)
        self.assertIn("discardFailedJob", script.text)
        self.assertIn('method: "DELETE"', script.text)

    def test_dashboard_shows_confirmation_errors_inside_review_dialog(self) -> None:
        script = self.client.get("/static/dashboard.js")
        stylesheet = self.client.get("/static/dashboard.css")

        self.assertIn('id="editor-message"', script.text)
        self.assertIn("contains incomplete JSON", script.text)
        self.assertIn("editorMessage.hidden = false", script.text)
        self.assertIn(".editor-message", stylesheet.text)

    def test_dashboard_preserves_form_references_across_async_requests(self) -> None:
        script = self.client.get("/static/dashboard.js")

        self.assertEqual(script.status_code, 200)
        self.assertIn("const form = event.currentTarget;", script.text)
        self.assertIn("body: new FormData(form)", script.text)
        self.assertIn("form.reset();", script.text)
        self.assertNotIn("event.currentTarget.reset();", script.text)
        self.assertIn('form.querySelector("#editor-message")', script.text)

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

    def test_returns_complete_indexed_content_without_embeddings(self) -> None:
        response = self.client.get("/api/documents/soon/indexed-content")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["document_id"], "soon")
        self.assertEqual(
            response.json()["fragments"][0],
            {
                "fragment_id": "soon:raw:0001",
                "source": "raw_text",
                "content": "[Page 1]\nPrivate local text",
            },
        )
        self.assertNotIn("embedding", response.text)
        self.assertEqual(
            self.client.get("/api/documents/missing/indexed-content").status_code,
            404,
        )

    def test_dashboard_loads_indexed_content_only_on_request(self) -> None:
        script = self.client.get("/static/dashboard.js")

        self.assertEqual(script.status_code, 200)
        self.assertIn("Complete indexed content", script.text)
        self.assertIn("/indexed-content`);", script.text)
        self.assertIn("fragment.content", script.text)

    def test_upload_waits_for_confirmation_then_stores_and_archives(self) -> None:
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
            if job["status"] in {"awaiting_confirmation", "failed"}:
                break
            time.sleep(0.01)
        self.assertEqual(job["status"], "awaiting_confirmation")
        self.assertIsNotNone(job["pending_id"])
        self.assertTrue(self.processed_paths)
        self.assertFalse(self.processed_paths[0].exists())
        self.assertEqual(
            len(
                list(
                    (
                        Path(self.temporary_directory.name)
                        / "pending_confirmation"
                    ).glob("*.png")
                )
            ),
            1,
        )
        pending = self.client.get("/api/pending-documents").json()
        self.assertEqual(len(pending), 1)

        payload = pending[0]["document"]
        payload["summary"] = "User-confirmed summary"
        payload["extracted_data"]["contract_number"] = "C-9"
        confirmed = self.client.post(
            f"/api/pending-documents/{job['pending_id']}/confirm",
            json=payload,
        )

        self.assertEqual(confirmed.status_code, 200)
        self.assertEqual(confirmed.json()["summary"], "User-confirmed summary")
        self.assertEqual(len(self.client.get("/api/pending-documents").json()), 0)
        self.assertFalse(self.processed_paths[0].exists())
        self.assertTrue(
            (Path(self.temporary_directory.name) / "processed" / "policy.png").exists()
        )
        self.assertEqual(self.vector_index.upserts[0][0], "confirmed")

    def test_updates_and_deletes_a_document_in_both_stores(self) -> None:
        payload = self.records[1].document.model_dump(mode="json")
        payload["summary"] = "Updated summary"

        updated = self.client.put("/api/documents/soon", json=payload)
        deleted = self.client.delete("/api/documents/soon")

        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json()["summary"], "Updated summary")
        self.assertEqual(self.vector_index.updates[0][0], "soon")
        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.vector_index.deletes, ["soon"])
        self.assertIsNone(self.repository.get_document_by_id("soon"))

    def test_rejects_incomplete_container_placeholders_before_update(self) -> None:
        payload = self.records[1].document.model_dump(mode="json")
        payload["extracted_data"]["education"] = "[{"

        response = self.client.put("/api/documents/soon", json=payload)

        self.assertEqual(response.status_code, 422)
        self.assertIn("incomplete JSON container", response.json()["detail"])
        self.assertEqual(self.vector_index.updates, [])

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
