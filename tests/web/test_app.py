from __future__ import annotations

import time
from datetime import UTC, date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
from unittest import TestCase

from fastapi.testclient import TestClient

from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.db.vector_database import (
    VectorDatabaseError,
    VectorDatabaseUnavailableError,
)
from smart_doc_tracker.infrastructure.ollama import OllamaConnectionError
from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.models.rag import IndexedDocumentFragment, RetrievedDocumentChunk
from smart_doc_tracker.pipeline import DocumentProcessingResult
from smart_doc_tracker.web.app import WebDependencies, create_app


def _record(
    identifier: str,
    *,
    expiry_date: str | None,
    city: str = "Rome",
    source_file_name: str | None = None,
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
        source_file_name=source_file_name,
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

    def get_document_by_file_hash(self, file_hash: str) -> StoredDocument | None:
        return next(
            (item for item in self.records if item.file_hash == file_hash), None
        )

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
        insertion_pending: bool = False,
    ) -> DocumentInsertResult:
        existing = self.get_document_by_file_hash(file_hash)
        if existing is not None:
            return DocumentInsertResult(record=existing, inserted=False)
        record = StoredDocument(
            id="confirmed",
            file_hash=file_hash,
            document=document,
            created_at=datetime(2026, 8, 26, 12, 0, tzinfo=UTC),
        )
        self.records.append(record)
        return DocumentInsertResult(record=record, inserted=True)

    def mark_document_committed(self, document_id: str) -> StoredDocument | None:
        return self.get_document_by_id(document_id)

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
                    source_file_name=record.source_file_name,
                )
                self.records[index] = updated
                return updated
        return None

    def set_source_file_name(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        record = self.get_document_by_id(document_id)
        if record is None:
            return None
        updated = StoredDocument(
            id=record.id,
            file_hash=record.file_hash,
            document=record.document,
            created_at=record.created_at,
            source_file_name=source_file_name,
        )
        self.records[self.records.index(record)] = updated
        return updated

    def delete_document(self, document_id: str) -> StoredDocument | None:
        record = self.get_document_by_id(document_id)
        if record is not None:
            self.records.remove(record)
        return record


class FakeVectorIndex:
    def __init__(self) -> None:
        self.fail_upsert = False
        self.index_error = False
        self.fail_delete = False
        self.upserts: list[tuple[str, str, DocumentData]] = []
        self.updates: list[tuple[str, DocumentData]] = []
        self.deletes: list[str] = []
        self.absent: set[str] = set()
        self.query_results: list[RetrievedDocumentChunk] = []
        self.queries: list[str] = []

    def upsert_document(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        if self.fail_upsert:
            raise VectorDatabaseUnavailableError("Local index unavailable")
        if self.index_error:
            raise VectorDatabaseError("Local index rejected the insertion")
        self.upserts.append((document_id, raw_text, document))
        self.absent.discard(document_id)

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
        if self.fail_delete:
            raise RuntimeError("Local index unavailable")
        self.deletes.append(document_id)
        self.absent.add(document_id)

    def query(
        self,
        question: str,
        *,
        limit: int = 5,
    ) -> list[RetrievedDocumentChunk]:
        self.queries.append(question)
        return self.query_results[:limit]

    def get_document_fragments(self, document_id: str) -> list[IndexedDocumentFragment]:
        if document_id in self.absent:
            return []
        return [
            IndexedDocumentFragment(
                f"{document_id}:raw:0001",
                "[Page 1]\nPrivate local text",
                "raw_text",
            )
        ]


class FakeGenerator:
    def __init__(self) -> None:
        self.questions: list[str] = []
        self.response = (
            '{"answer":"The policy indicates a local insurance record.",'
            '"claims":[{"claim":"The record is a local insurance policy",'
            '"evidence":[{"document_id":"expired",'
            '"quote":"The policy expires on 2026-08-25.",'
            '"source":"structured_document","page":null}]}],'
            '"document_ids":["expired"],"insufficient_information":false}'
        )

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.questions.append(user_prompt)
        return self.response


class UnavailableGenerator:
    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        raise OllamaConnectionError("The local Ollama service is unavailable.")


class WebApplicationTests(TestCase):
    dashboard_module_paths = (
        "/static/js/dashboard.js",
        "/static/js/errors.js",
        "/static/js/messages.js",
        "/static/js/attribute-model.js",
        "/static/js/attribute-view.js",
        "/static/js/attribute-editor.js",
    )

    def dashboard_source(self) -> str:
        modules = [self.client.get(path) for path in self.dashboard_module_paths]
        self.assertTrue(all(module.status_code == 200 for module in modules))
        return "\n".join(module.text for module in modules)

    def setUp(self) -> None:
        self.records = [
            _record("expired", expiry_date="2026-08-25"),
            _record(
                "soon",
                expiry_date="2026-09-10",
                source_file_name="policy.pdf",
            ),
            _record("valid", expiry_date="2027-01-01"),
            _record("none", expiry_date=None),
        ]
        self.repository = FakeRepository(self.records)
        self.vector_index = FakeVectorIndex()
        self.vector_index.query_results = [
            RetrievedDocumentChunk(
                document_id="expired",
                content="The policy expires on 2026-08-25.",
                source="structured_document",
                distance=0.1,
            )
        ]
        self.generator = FakeGenerator()
        self.temporary_directory = TemporaryDirectory()
        processed_path = Path(self.temporary_directory.name) / "processed"
        processed_path.mkdir()
        (processed_path / "policy.pdf").write_bytes(b"local pdf fixture")
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
                rag_generator=self.generator,
                processed_path=processed_path,
            )
        )
        self.app = app
        self.client_context = TestClient(
            app,
            base_url="http://127.0.0.1:8080",
            headers={"X-Smart-Doc-CSRF": app.state.csrf_token},
        )
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

    def test_saves_default_reminder_and_uses_document_override(self) -> None:
        saved = self.client.put(
            "/api/settings/reminders",
            json={"default_notification_days_before": 10},
        )

        self.assertEqual(saved.status_code, 200)
        self.assertEqual(saved.json()["default_notification_days_before"], 10)
        self.assertEqual(
            self.client.get("/api/settings/reminders").json(),
            {"default_notification_days_before": 10},
        )
        documents = self.client.get("/api/documents").json()
        soon = next(item for item in documents if item["id"] == "soon")
        self.assertEqual(soon["expiration_status"], "valid")
        self.assertIsNone(soon["notification_days_before"])
        self.assertEqual(soon["effective_notification_days_before"], 10)

        payload = self.records[1].document.model_dump(mode="json")
        payload["notification_days_before"] = 20
        updated = self.client.put("/api/documents/soon", json=payload)

        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json()["expiration_status"], "soon")
        self.assertEqual(updated.json()["notification_days_before"], 20)
        self.assertEqual(updated.json()["effective_notification_days_before"], 20)

    def test_dashboard_exposes_default_and_document_reminder_controls(self) -> None:
        dashboard = self.client.get("/").text
        script = self.client.get("/static/js/dashboard.js").text

        self.assertIn('id="reminder-settings-form"', dashboard)
        self.assertIn('id="default-reminder-days"', dashboard)
        self.assertIn('name="notification_days_before"', script)
        self.assertIn("days before (default value)", script)

    def test_answers_chat_questions_with_clickable_document_references(self) -> None:
        with self.assertLogs("smart_doc_tracker.pipeline", level="INFO") as captured:
            response = self.client.post(
                "/api/chat",
                json={"question": "What does my insurance policy indicate?"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "answer": "The policy indicates a local insurance record.",
                "claims": [
                    {
                        "claim": "The record is a local insurance policy",
                        "evidence": [
                            {
                                "document_id": "expired",
                                "quote": "The policy expires on 2026-08-25.",
                                "source": "structured_document",
                                "page": None,
                            }
                        ],
                    }
                ],
                "documents": [
                    {
                        "id": "expired",
                        "document_type": "insurance_policy",
                        "summary": "A local insurance policy",
                    }
                ],
                "insufficient_information": False,
            },
        )
        self.assertIn("Retrieved evidence passages", self.generator.questions[0])
        log_output = "\n".join(captured.output)
        self.assertIn("retrieval completed (1 fragments)", log_output)
        self.assertIn("local generation started", log_output)
        self.assertNotIn("insurance policy indicate", log_output)

    def test_chat_remembers_only_questions_from_the_same_temporary_conversation(
        self,
    ) -> None:
        first = self.client.post(
            "/api/chat",
            json={
                "question": "When does my insurance policy expire?",
                "conversation_id": "conversation-a",
            },
        )
        second = self.client.post(
            "/api/chat",
            json={
                "question": "And when was it issued?",
                "conversation_id": "conversation-a",
            },
        )
        separate = self.client.post(
            "/api/chat",
            json={
                "question": "And who owns it?",
                "conversation_id": "conversation-b",
            },
        )

        self.assertEqual(first.status_code, 200)
        self.assertEqual(second.status_code, 200)
        self.assertEqual(separate.status_code, 200)
        previous_question = "When does my insurance policy expire?"
        self.assertEqual(
            second.json()["answer"],
            "The policy indicates a local insurance record.",
        )
        self.assertIn(previous_question, self.vector_index.queries[-2])
        self.assertNotIn(previous_question, self.vector_index.queries[-1])
        self.assertEqual(self.vector_index.queries[-1], "And who owns it?")
        self.assertEqual(len(self.generator.questions), 3)

    def test_new_conversation_endpoint_forgets_temporary_history(self) -> None:
        payload = {
            "question": "When does my insurance policy expire?",
            "conversation_id": "conversation-to-clear",
        }
        self.assertEqual(self.client.post("/api/chat", json=payload).status_code, 200)

        cleared = self.client.delete("/api/chat/conversations/conversation-to-clear")
        follow_up = self.client.post(
            "/api/chat",
            json={
                "question": "And when was it issued?",
                "conversation_id": "conversation-to-clear",
            },
        )

        self.assertEqual(cleared.status_code, 204)
        self.assertEqual(follow_up.status_code, 200)
        self.assertEqual(self.vector_index.queries[-1], "And when was it issued?")
        self.assertEqual(len(self.generator.questions), 2)

    def test_reports_chat_failure_cause_without_logging_the_question(self) -> None:
        unavailable_app = create_app(
            WebDependencies(
                repository_factory=lambda: self.repository,
                upload_processor=lambda *_args: DocumentProcessingResult(raw_text=""),
                today_provider=lambda: date(2026, 8, 26),
                vector_index=self.vector_index,
                rag_generator=UnavailableGenerator(),
                processed_path=(
                    Path(self.temporary_directory.name)
                    / "unavailable-chat"
                    / "processed"
                ),
            )
        )
        with TestClient(
            unavailable_app,
            base_url="http://127.0.0.1:8080",
            headers={"X-Smart-Doc-CSRF": unavailable_app.state.csrf_token},
        ) as client:
            with self.assertLogs(
                "smart_doc_tracker.web.app",
                level="INFO",
            ) as captured:
                response = client.post(
                    "/api/chat",
                    json={"question": "private diagnostic question"},
                )

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json()["detail"],
            "The local Ollama service or language model is unavailable.",
        )
        log_output = "\n".join(captured.output)
        self.assertIn("Chat request failed with OllamaConnectionError", log_output)
        self.assertNotIn("private diagnostic question", log_output)

    def test_answers_expiry_year_chat_with_grounded_retrieval(self) -> None:
        self.vector_index.query_results = [
            RetrievedDocumentChunk(
                document_id="valid",
                content="The policy expires on 2027-01-01.",
                source="structured_document",
                distance=0.1,
            )
        ]
        self.generator.response = (
            '{"claims":[{"claim":"The policy expires on 2027-01-01.",'
            '"evidence_ids":["E1"]}]}'
        )
        response = self.client.post(
            "/api/chat",
            json={"question": "Quali documenti scadono nel 2027?"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["documents"][0]["id"], "valid")
        self.assertEqual(response.json()["answer"], "The policy expires on 2027-01-01.")
        self.assertEqual(self.vector_index.queries, ["Quali documenti scadono nel 2027?"])
        self.assertEqual(len(self.generator.questions), 1)

    def test_dashboard_keeps_chat_and_document_preview_in_the_same_page(self) -> None:
        dashboard = self.client.get("/")
        script = self.client.get("/static/js/dashboard.js")

        self.assertIn('id="chat-panel"', dashboard.text)
        self.assertIn('id="document-dialog"', dashboard.text)
        self.assertIn("openChatDocument", script.text)
        self.assertIn("showDetail(await response.json())", script.text)
        self.assertNotIn("window.open(", script.text)
        self.assertIn('>Open original</a>', script.text)
        self.assertIn("documents.forEach((sourceDocument)", script.text)
        self.assertIn("window.document.createElement", script.text)
        self.assertNotIn("documents.forEach((document)", script.text)
        self.assertIn('id="new-chat-button"', dashboard.text)
        self.assertIn("conversation_id: conversationId", script.text)
        self.assertIn("crypto.randomUUID()", script.text)
        chat_renderer = script.text.split("function appendChatMessage", 1)[1].split(
            "async function openChatDocument", 1
        )[0]
        self.assertNotIn("innerHTML", chat_renderer)
        self.assertNotIn("payload.claims", script.text)
        self.assertNotIn("claim.evidence.forEach", chat_renderer)
        self.assertNotIn("chat-evidence", chat_renderer)
        self.assertNotIn("Supporting documents", chat_renderer)
        self.assertIn("documents.forEach((sourceDocument)", chat_renderer)

    def test_dashboard_omits_json_attribute_query_controls(self) -> None:
        dashboard = self.client.get("/")
        script = self.client.get("/static/js/dashboard.js")

        self.assertNotIn("Query JSON attributes", dashboard.text)
        self.assertNotIn('id="query-form"', dashboard.text)
        self.assertNotIn('id="field-key"', dashboard.text)
        self.assertNotIn('id="field-value"', dashboard.text)
        self.assertNotIn('querySelector("#query-form")', script.text)
        self.assertNotIn('querySelector("#clear-query")', script.text)

    def test_rejects_external_hosts_cross_origin_writes_and_missing_csrf(self) -> None:
        valid_payload = self.records[0].document.model_dump(mode="json")
        external_host = self.client.get(
            "/api/documents",
            headers={"Host": "attacker.example"},
        )
        external_origin = self.client.put(
            "/api/documents/expired",
            json=valid_payload,
            headers={"Origin": "https://attacker.example"},
        )
        without_csrf = TestClient(
            self.app,
            base_url="http://127.0.0.1:8080",
        ).put("/api/documents/expired", json=valid_payload)

        self.assertEqual(external_host.status_code, 400)
        self.assertEqual(external_origin.status_code, 403)
        self.assertEqual(without_csrf.status_code, 403)
        self.assertEqual(self.records[0].document.summary, "A local insurance policy")

    def test_serves_csrf_proof_and_restrictive_browser_headers(self) -> None:
        response = self.client.get("/")

        self.assertIn('name="csrf-token"', response.text)
        self.assertIn("script-src 'self'", response.headers["content-security-policy"])
        self.assertIn(
            "frame-ancestors 'none'",
            response.headers["content-security-policy"],
        )
        self.assertEqual(response.headers["x-frame-options"], "DENY")
        self.assertEqual(response.headers["x-content-type-options"], "nosniff")
        self.assertEqual(response.headers["referrer-policy"], "no-referrer")
        self.assertEqual(self.client.get("/docs").status_code, 404)
        self.assertEqual(self.client.get("/openapi.json").status_code, 404)

    def test_dashboard_messages_are_visible_and_dismissible(self) -> None:
        script = self.client.get("/static/js/messages.js")
        stylesheet = self.client.get("/static/dashboard.css")

        self.assertEqual(script.status_code, 200)
        self.assertIn('message.addEventListener("click", clearMessage)', script.text)
        self.assertIn('isError ? "alert" : "status"', script.text)
        self.assertEqual(stylesheet.status_code, 200)
        self.assertIn("position: fixed", stylesheet.text)
        self.assertIn("z-index: 1000", stylesheet.text)

    def test_dashboard_uses_simple_messages_without_storage_details(self) -> None:
        script = self.dashboard_source()

        self.assertIn("Document added successfully.", script)
        self.assertIn("Changes saved successfully.", script)
        self.assertIn("Document deleted successfully.", script)
        self.assertIn("This file type is not supported. Choose a PDF or image.", script)
        self.assertIn("Something went wrong. Please try again in a moment.", script)
        self.assertNotIn("payload.detail", script)
        self.assertNotIn("updated in both local stores", script)
        self.assertNotIn("deleted from both local stores", script)
        self.assertNotIn("Delete this document from MongoDB and ChromaDB", script)
        self.assertNotIn("job.error", script)

    def test_dashboard_loads_modular_scripts_without_stale_cache(self) -> None:
        dashboard = self.client.get("/")
        script = self.client.get("/static/js/dashboard.js")

        self.assertIn('href="/static/dashboard.css"', dashboard.text)
        self.assertIn('type="module" src="/static/js/dashboard.js"', dashboard.text)
        self.assertIn('from "./attribute-editor.js"', script.text)
        self.assertEqual(dashboard.headers["cache-control"], "no-store, max-age=0")
        self.assertEqual(script.headers["cache-control"], "no-store, max-age=0")

    def test_dashboard_sends_csrf_proof_for_every_write(self) -> None:
        script = self.client.get("/static/js/dashboard.js").text

        self.assertIn('meta[name="csrf-token"]', script)
        self.assertIn('headers.set("X-Smart-Doc-CSRF", csrfToken)', script)
        self.assertIn("return fetch(resource, { ...options, headers })", script)
        self.assertNotIn("await fetch(", script)

    def test_dashboard_exposes_a_separate_processing_queue(self) -> None:
        dashboard = self.client.get("/")
        script = self.client.get("/static/js/dashboard.js")
        response = self.client.get("/api/jobs")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
        self.assertIn('id="queue-tab"', dashboard.text)
        self.assertIn('id="queue-panel"', dashboard.text)
        self.assertNotIn('id="job-status"', dashboard.text)
        self.assertIn("Reading document", script.text)
        self.assertIn("Organizing information", script.text)
        self.assertIn("discardFailedJob", script.text)
        self.assertIn("retryFailedJob", script.text)
        self.assertNotIn("Needs attention", script.text)
        self.assertIn('id="retry-all-jobs"', dashboard.text)
        self.assertIn('id="remove-all-jobs"', dashboard.text)
        self.assertIn('method: "DELETE"', script.text)

    def test_retry_and_bulk_queue_routes_handle_empty_or_invalid_jobs(self) -> None:
        self.assertEqual(self.client.post("/api/jobs/retry-all").json(), {"retried": 0})
        self.assertEqual(self.client.delete("/api/jobs/failed").json(), {"removed": 0})
        self.assertEqual(self.client.post("/api/jobs/missing/retry").status_code, 404)

    def test_retry_and_remove_all_failed_uploads_through_api(self) -> None:
        def fail(path: Path, language: str, reporter: Any) -> DocumentProcessingResult:
            raise RuntimeError("Private failure detail")

        self.app.state.upload_jobs._processor = fail
        job_ids = []
        for index in range(2):
            response = self.client.post(
                "/api/uploads",
                files={"file": (f"failed-{index}.png", b"local fixture", "image/png")},
                data={"language": "ita"},
            )
            self.assertEqual(response.status_code, 202)
            job_ids.append(response.json()["id"])
        for _ in range(100):
            if all(
                self.client.get(f"/api/jobs/{job_id}").json()["status"] == "failed"
                for job_id in job_ids
            ):
                break
            time.sleep(0.01)
        self.assertEqual(len(self.client.get("/api/jobs").json()), 2)
        self.assertEqual(
            self.client.post(f"/api/jobs/{job_ids[0]}/retry").status_code, 200
        )
        for _ in range(100):
            if self.client.get(f"/api/jobs/{job_ids[0]}").json()["status"] == "failed":
                break
            time.sleep(0.01)
        self.assertEqual(self.client.post("/api/jobs/retry-all").json(), {"retried": 2})
        for _ in range(100):
            if all(
                self.client.get(f"/api/jobs/{job_id}").json()["status"] == "failed"
                for job_id in job_ids
            ):
                break
            time.sleep(0.01)
        self.assertEqual(self.client.delete("/api/jobs/failed").json(), {"removed": 2})
        self.assertEqual(self.client.get("/api/jobs").json(), [])

    def test_dashboard_shows_confirmation_errors_inside_review_dialog(self) -> None:
        script = self.dashboard_source()
        stylesheet = self.client.get("/static/dashboard.css")

        self.assertIn('id="editor-message"', script)
        self.assertIn("Give every field a name before saving", script)
        self.assertIn("editorMessage.hidden = false", script)
        self.assertIn(".editor-message", stylesheet.text)

    def test_dashboard_renders_nested_values_as_expandable_fields(self) -> None:
        script = self.client.get("/static/js/attribute-editor.js")
        stylesheet = self.client.get("/static/dashboard.css")

        self.assertEqual(script.status_code, 200)
        self.assertIn('details.className = "nested-value"', script.text)
        self.assertIn('"<span>Field name</span><span>Value</span>"', script.text)
        self.assertIn(
            "addButton.textContent = isArrayKind(node.dataset.valueKind) "
            '? "Add item" : "Add field"',
            script.text,
        )
        self.assertIn("children.map(readNodeValue)", script.text)
        self.assertNotIn("JSON.stringify(value)", script.text)
        self.assertIn(".nested-value > summary", stylesheet.text)

    def test_document_editor_can_add_groups_at_multiple_levels(self) -> None:
        dashboard_script = self.client.get("/static/js/dashboard.js").text
        editor_script = self.client.get("/static/js/attribute-editor.js").text
        stylesheet = self.client.get("/static/dashboard.css").text

        self.assertIn("addGroupRow", dashboard_script)
        self.assertIn('id="add-group"', dashboard_script)
        self.assertIn("addValueNode(container, key, {}, false)", editor_script)
        self.assertIn('.nested-value").open = true', editor_script)
        self.assertIn(
            "addGroupButton.textContent = node.dataset.valueKind", editor_script
        )
        self.assertIn(
            'addGroupButton.addEventListener("click", () => addChild({}))',
            editor_script,
        )
        self.assertIn('addActions.className = "nested-add-actions"', editor_script)
        self.assertIn(".nested-add-actions", stylesheet)

    def test_dashboard_shows_extracted_attributes_without_raw_json(self) -> None:
        script = self.dashboard_source()

        self.assertIn("renderAttributeView", script)
        self.assertIn('class="attribute-view"', script)
        self.assertIn("keyLabel.textContent = key", script)
        self.assertNotIn("JSON.stringify(item.extracted_data", script)

    def test_dashboard_flattens_common_extracted_lists_for_people(self) -> None:
        script = self.dashboard_source()
        stylesheet = self.client.get("/static/dashboard.css").text

        self.assertIn('return "typed-array"', script)
        self.assertIn('return "single-field-array"', script)
        self.assertIn('return "scalar-array"', script)
        self.assertIn("value.map((item) => [item.type, item.value])", script)
        self.assertIn("{ type, value: readNodeValue(child) }", script)
        self.assertIn('list.className = "compact-list-editor"', script)
        self.assertIn('values.className = "compact-list-view-values"', script)
        self.assertIn("item[itemField]", script)
        self.assertIn('details.className = "nested-value grouped-list-editor"', script)
        self.assertIn('fieldInput.className = "grouped-list-key"', script)
        self.assertIn("groupedSingleFieldItems(value).forEach", script)
        self.assertIn('fieldDetails.className = "grouped-list-field"', script)
        self.assertIn(
            'removeButton.className = "secondary compact grouped-list-remove"',
            script,
        )
        self.assertIn("fieldDetails.remove()", script)
        self.assertIn("updateGroupedListSummary", script)
        self.assertIn("records.sort", script)
        self.assertIn(".grouped-list-row", stylesheet)
        self.assertIn(".grouped-list-field > summary", stylesheet)
        self.assertIn(".grouped-list-remove", stylesheet)
        self.assertIn("grid-template-columns: minmax(0, 1fr) auto", stylesheet)
        self.assertIn("overflow-wrap: anywhere", stylesheet)

    def test_document_editor_allows_scrolling_long_nested_values(self) -> None:
        stylesheet = self.client.get("/static/dashboard.css")

        self.assertIn("max-height: calc(100vh - 32px)", stylesheet.text)
        self.assertIn("overflow-x: auto", stylesheet.text)
        self.assertIn("min-width: 520px", stylesheet.text)

    def test_dashboard_preserves_form_references_across_async_requests(self) -> None:
        script = self.dashboard_source()

        self.assertIn("const form = event.currentTarget;", script)
        self.assertIn("body: new FormData(form)", script)
        self.assertIn("form.reset();", script)
        self.assertNotIn("event.currentTarget.reset();", script)
        self.assertIn('form.querySelector("#editor-message")', script)

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

    def test_logs_server_errors_using_route_patterns(self) -> None:
        def unused_processor(
            path: Path,
            language: str,
            reporter: Any,
        ) -> DocumentProcessingResult:
            raise AssertionError("No upload is expected in this test")

        unavailable_app = create_app(
            WebDependencies(
                repository_factory=lambda: self.repository,
                upload_processor=unused_processor,
                today_provider=lambda: date(2026, 8, 26),
                processed_path=Path(self.temporary_directory.name) / "unavailable",
            )
        )
        with TestClient(
            unavailable_app,
            base_url="http://127.0.0.1:8080",
            headers={"X-Smart-Doc-CSRF": unavailable_app.state.csrf_token},
        ) as client:
            with self.assertLogs(
                "smart_doc_tracker.web.app", level="ERROR"
            ) as captured:
                response = client.get("/api/documents/soon/indexed-content")

        self.assertEqual(response.status_code, 503)
        log_output = "\n".join(captured.output)
        self.assertIn(
            "GET /api/documents/{document_id}/indexed-content returned HTTP 503",
            log_output,
        )
        self.assertNotIn("/soon/", log_output)

    def test_dashboard_opens_and_downloads_the_original_document(self) -> None:
        script = self.client.get("/static/js/dashboard.js")

        self.assertEqual(script.status_code, 200)
        self.assertIn("Original document", script.text)
        self.assertIn("Open original", script.text)
        self.assertIn("Download", script.text)
        self.assertNotIn("Complete indexed content", script.text)

        opened = self.client.get("/api/documents/soon/original")
        downloaded = self.client.get(
            "/api/documents/soon/original", params={"download": "true"}
        )

        self.assertEqual(opened.status_code, 200)
        self.assertEqual(opened.content, b"local pdf fixture")
        self.assertTrue(opened.headers["content-disposition"].startswith("inline"))
        self.assertTrue(
            downloaded.headers["content-disposition"].startswith("attachment")
        )
        self.assertEqual(
            self.client.get("/api/documents/valid/original").status_code,
            404,
        )

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
                    (Path(self.temporary_directory.name) / "pending_confirmation").glob(
                        "*.png"
                    )
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
        self.assertEqual(confirmed.json()["original_file_name"], "policy.png")
        self.assertEqual(len(self.client.get("/api/pending-documents").json()), 0)
        self.assertFalse(self.processed_paths[0].exists())
        self.assertTrue(
            (Path(self.temporary_directory.name) / "processed" / "policy.png").exists()
        )
        original = self.client.get(f"/api/documents/{confirmed.json()['id']}/original")
        self.assertEqual(original.status_code, 200)
        self.assertEqual(original.content, b"local fixture")
        self.assertEqual(self.vector_index.upserts[0][0], "confirmed")

    def test_failed_confirmation_stays_pending_and_can_be_retried(self) -> None:
        response = self.client.post(
            "/api/uploads",
            files={"file": ("retry.png", b"local fixture", "image/png")},
            data={"language": "ita"},
        )
        job_id = response.json()["id"]
        for _ in range(100):
            job = self.client.get(f"/api/jobs/{job_id}").json()
            if job["status"] == "awaiting_confirmation":
                break
            time.sleep(0.01)
        pending_id = job["pending_id"]
        payload = self.client.get(f"/api/pending-documents/{pending_id}").json()[
            "document"
        ]
        self.vector_index.fail_upsert = True

        failed = self.client.post(
            f"/api/pending-documents/{pending_id}/confirm", json=payload
        )

        self.assertEqual(failed.status_code, 503)
        self.assertIn("try again later", failed.json()["detail"])
        self.assertEqual(
            self.client.get(f"/api/pending-documents/{pending_id}").json()["status"],
            "inserting",
        )
        self.assertIsNotNone(self.repository.get_document_by_id("confirmed"))
        self.vector_index.fail_upsert = False

        retried = self.client.post(
            f"/api/pending-documents/{pending_id}/confirm", json=payload
        )

        self.assertEqual(retried.status_code, 200)
        self.assertEqual(self.client.get("/api/pending-documents").json(), [])
        self.assertIsNotNone(self.repository.get_document_by_id("confirmed"))

    def test_failed_confirmation_recovers_automatically_when_index_returns(
        self,
    ) -> None:
        response = self.client.post(
            "/api/uploads",
            files={"file": ("recover.png", b"local fixture", "image/png")},
            data={"language": "ita"},
        )
        job_id = response.json()["id"]
        for _ in range(100):
            job = self.client.get(f"/api/jobs/{job_id}").json()
            if job["status"] == "awaiting_confirmation":
                break
            time.sleep(0.01)
        pending_id = job["pending_id"]
        payload = self.client.get(f"/api/pending-documents/{pending_id}").json()[
            "document"
        ]
        self.vector_index.fail_upsert = True
        self.assertEqual(
            self.client.post(
                f"/api/pending-documents/{pending_id}/confirm", json=payload
            ).status_code,
            503,
        )
        self.vector_index.fail_upsert = False

        for _ in range(125):
            if not self.client.get("/api/pending-documents").json():
                break
            time.sleep(0.05)

        self.assertEqual(self.client.get("/api/pending-documents").json(), [])
        self.assertIsNotNone(self.repository.get_document_by_id("confirmed"))

    def test_two_index_errors_move_upload_to_failed_ocr_queue(self) -> None:
        response = self.client.post(
            "/api/uploads",
            files={"file": ("broken.png", b"local fixture", "image/png")},
            data={"language": "ita"},
        )
        job_id = response.json()["id"]
        for _ in range(100):
            job = self.client.get(f"/api/jobs/{job_id}").json()
            if job["status"] == "awaiting_confirmation":
                break
            time.sleep(0.01)
        self.assertEqual(job["status"], "awaiting_confirmation")
        payload = self.client.get(f"/api/pending-documents/{job_id}").json()[
            "document"
        ]
        self.vector_index.index_error = True

        for _ in range(2):
            failed = self.client.post(
                f"/api/pending-documents/{job_id}/confirm", json=payload
            )
            self.assertEqual(failed.status_code, 503)

        self.assertIsNone(self.repository.get_document_by_id("confirmed"))
        self.assertEqual(self.client.get("/api/pending-documents").json(), [])
        self.assertEqual(
            self.client.get(f"/api/jobs/{job_id}").json()["status"], "failed"
        )
        self.assertEqual(
            (
                Path(self.temporary_directory.name)
                / "processing_queue"
                / f"{job_id}.png"
            ).read_bytes(),
            b"local fixture",
        )

        self.vector_index.index_error = False
        retried = self.client.post(f"/api/jobs/{job_id}/retry")
        self.assertEqual(retried.status_code, 200)
        for _ in range(100):
            job = self.client.get(f"/api/jobs/{job_id}").json()
            if job["status"] == "awaiting_confirmation":
                break
            time.sleep(0.01)
        self.assertEqual(job["status"], "awaiting_confirmation")
        self.assertEqual(len(self.processed_paths), 2)

    def test_creates_manual_document_without_upload_processing(self) -> None:
        payload = {
            "document_type": "membership card",
            "summary": "Local club membership",
            "issue_date": "2026-09-01",
            "expiry_date": "2027-08-31",
            "extracted_data": {
                "membership_number": "M-42",
                "holder": {"name": "Test User"},
            },
        }

        response = self.client.post("/api/documents/manual", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["document_type"], "membership_card")
        self.assertEqual(response.json()["summary"], "Local club membership")
        self.assertEqual(self.processed_paths, [])
        self.assertEqual(self.vector_index.upserts[-1][1], "")
        self.assertEqual(
            self.vector_index.upserts[-1][2].extracted_data, payload["extracted_data"]
        )
        self.assertRegex(self.records[-1].file_hash, r"^[0-9a-f]{64}$")

    def test_failed_manual_insertion_can_be_cancelled(self) -> None:
        payload = self.records[0].document.model_dump(mode="json")
        self.vector_index.fail_upsert = True

        failed = self.client.post("/api/documents/manual", json=payload)

        self.assertEqual(failed.status_code, 503)
        pending = self.client.get("/api/pending-documents").json()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["status"], "inserting")
        self.assertEqual(pending[0]["file_name"], "Manual document")

        cancelled = self.client.delete(f"/api/pending-documents/{pending[0]['id']}")

        self.assertEqual(cancelled.status_code, 204)
        self.assertEqual(self.client.get("/api/pending-documents").json(), [])
        self.assertIsNone(self.repository.get_document_by_id("confirmed"))

    def test_cancellation_waits_until_both_stores_can_be_cleaned(self) -> None:
        payload = self.records[0].document.model_dump(mode="json")
        self.vector_index.fail_upsert = True
        self.vector_index.fail_delete = True
        self.assertEqual(
            self.client.post("/api/documents/manual", json=payload).status_code,
            503,
        )
        pending = self.client.get("/api/pending-documents").json()[0]
        self.assertIsNotNone(self.repository.get_document_by_id("confirmed"))

        rejected = self.client.delete(f"/api/pending-documents/{pending['id']}")

        self.assertEqual(rejected.status_code, 503)
        self.assertEqual(
            self.client.get(f"/api/pending-documents/{pending['id']}").json()["status"],
            "cancelling",
        )
        self.assertEqual(
            self.client.get("/api/documents").json()[-1]["id"],
            "none",
        )
        self.vector_index.fail_delete = False

        self.assertEqual(
            self.client.delete(f"/api/pending-documents/{pending['id']}").status_code,
            204,
        )
        self.assertIsNone(self.repository.get_document_by_id("confirmed"))

    def test_dashboard_offers_manual_document_entry(self) -> None:
        dashboard = self.client.get("/")
        script = self.client.get("/static/js/dashboard.js")

        self.assertIn('id="add-manual-document"', dashboard.text)
        self.assertIn('"/api/documents/manual"', script.text)
        self.assertIn("Document title", script.text)
        self.assertIn('"Additional fields"', script.text)

    def test_updates_and_deletes_a_document_in_both_stores(self) -> None:
        payload = self.records[1].document.model_dump(mode="json")
        payload["summary"] = "Updated summary"

        updated = self.client.put("/api/documents/soon", json=payload)
        update_id = updated.json()["index_update_id"]
        update: dict[str, Any] = {}
        for _ in range(100):
            update = self.client.get(f"/api/document-updates/{update_id}").json()
            if update["status"] in {"completed", "failed"}:
                break
            time.sleep(0.01)
        deleted = self.client.delete("/api/documents/soon")

        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json()["summary"], "Updated summary")
        self.assertEqual(update["status"], "completed")
        self.assertEqual(self.vector_index.updates[0][0], "soon")
        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.vector_index.deletes, ["soon"])
        self.assertIsNone(self.repository.get_document_by_id("soon"))
        self.assertFalse(
            (Path(self.temporary_directory.name) / "processed" / "policy.pdf").exists()
        )

    def test_rejects_incomplete_container_placeholders_before_update(self) -> None:
        payload = self.records[1].document.model_dump(mode="json")
        payload["extracted_data"]["education"] = "[{"

        response = self.client.put("/api/documents/soon", json=payload)

        self.assertEqual(response.status_code, 422)
        self.assertIn("incomplete JSON container", response.json()["detail"])
        self.assertEqual(self.vector_index.updates, [])

    def test_editor_shows_plain_language_save_progress(self) -> None:
        script = self.dashboard_source()
        stylesheet = self.client.get("/static/dashboard.css").text

        self.assertIn('submitButton.textContent = "Saving..."', script)
        self.assertIn("Search will be ready shortly.", script)
        self.assertIn("Search is taking longer than expected.", script)
        self.assertIn("monitorDocumentUpdate", script)
        self.assertIn("button.is-saving::before", stylesheet)
        self.assertNotIn("embedding", script.lower())
        self.assertNotIn("chromadb", script.lower())
        self.assertNotIn("mongodb", script.lower())

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
