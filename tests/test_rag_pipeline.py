from __future__ import annotations

import json
from datetime import UTC, date, datetime
from io import StringIO
from unittest import TestCase

from smart_doc_tracker.core.parser import DocumentParsingError
from smart_doc_tracker.db.database import StoredDocument
from smart_doc_tracker.main import run
from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.models.rag import (
    ConversationTurn,
    IndexedDocumentFragment,
    RetrievedDocumentChunk,
)
from smart_doc_tracker.pipeline import (
    DocumentQuestionPipeline,
    ExpirationYearQuestionPipeline,
    requested_expiry_year,
)


class FakeVectorIndex:
    def __init__(self, chunks: list[RetrievedDocumentChunk]) -> None:
        self.chunks = chunks
        self.calls: list[tuple[str, int]] = []

    def query(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        self.calls.append((question, limit))
        return self.chunks

    def get_document_fragments(
        self, document_id: str
    ) -> list[IndexedDocumentFragment]:
        return [
            IndexedDocumentFragment(
                f"{document_id}:structured",
                "Remembered issue date: 2025-01-01",
                "structured_data",
            )
        ]


class FakeGenerator:
    def __init__(self, response: str) -> None:
        self.response = response
        self.calls: list[tuple[str, str]] = []

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return self.response


class FakeExpirationRepository:
    def __init__(self, documents: list[StoredDocument]) -> None:
        self.documents = documents
        self.year_calls: list[int] = []

    def __enter__(self) -> FakeExpirationRepository:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def get_documents_expiring_in_year(self, year: int) -> list[StoredDocument]:
        self.year_calls.append(year)
        return [
            record
            for record in self.documents
            if record.document.expiry_date is not None
            and record.document.expiry_date.year == year
        ]


def _stored_document(
    identifier: str, document_type: str, expiry_date: str
) -> StoredDocument:
    return StoredDocument(
        id=identifier,
        file_hash="a" * 64,
        document=DocumentData(
            document_type=document_type,
            summary="A local document",
            expiry_date=expiry_date,
            issue_date=None,
            extracted_data={},
        ),
        created_at=datetime(2026, 8, 1, tzinfo=UTC),
    )


class DocumentQuestionPipelineTests(TestCase):
    def test_recognizes_unambiguous_expiry_year_questions(self) -> None:
        self.assertEqual(requested_expiry_year("Which documents expire in 2026?"), 2026)
        self.assertEqual(
            requested_expiry_year(
                "Quali documenti scadono quest'anno?",
                today=date(2026, 8, 25),
            ),
            2026,
        )
        self.assertIsNone(requested_expiry_year("What happened in 2026?"))
        self.assertIsNone(requested_expiry_year("What expires in 2026 or 2027?"))

    def test_answers_expiry_year_question_from_normalized_dates(self) -> None:
        certificate = _stored_document(
            "certificate-id", "sport_practicability_certificate", "2026-08-21"
        )
        identity_card = _stored_document("identity-id", "identity_card", "2034-06-03")
        repository = FakeExpirationRepository([certificate, identity_card])

        answer = ExpirationYearQuestionPipeline(
            repository,
            today_provider=lambda: date(2026, 8, 25),
        ).ask(2026)

        self.assertEqual(repository.year_calls, [2026])
        self.assertEqual(answer.document_ids, ["certificate-id"])
        self.assertEqual(
            answer.answer,
            "Sport Practicability Certificate expired on 2026-08-21.",
        )

    def test_answers_from_retrieved_context_and_preserves_source_ids(self) -> None:
        index = FakeVectorIndex(
            [
                RetrievedDocumentChunk(
                    "doc-1", "Expiry: 2030-01-01", "structured_data", 0.1
                )
            ]
        )
        generator = FakeGenerator(
            '{"answer":"It expires on 2030-01-01.","document_ids":["doc-1"]}'
        )

        answer = DocumentQuestionPipeline(index, generator).ask(
            "When does it expire?", limit=3
        )

        self.assertEqual(answer.document_ids, ["doc-1"])
        self.assertEqual(index.calls, [("When does it expire?", 3)])
        self.assertIn("Expiry: 2030-01-01", generator.calls[0][1])

    def test_uses_recent_conversation_to_resolve_a_follow_up_question(self) -> None:
        index = FakeVectorIndex(
            [
                RetrievedDocumentChunk(
                    "doc-1", "Issue date: 2025-01-01", "structured_data", 0.1
                )
            ]
        )
        generator = FakeGenerator(
            '{"answer":"It was issued on 2025-01-01.","document_ids":["doc-1"]}'
        )
        history = (
            ConversationTurn(
                "When does my insurance policy expire?",
                "It expires in 2030.",
                ("doc-1",),
            ),
        )

        DocumentQuestionPipeline(index, generator).ask(
            "And when was it issued?",
            history=history,
        )

        retrieval_question = index.calls[0][0]
        self.assertIn("When does my insurance policy expire?", retrieval_question)
        self.assertIn("And when was it issued?", retrieval_question)
        prompt = generator.calls[0][1]
        self.assertIn('"document_ids": ["doc-1"]', prompt)
        self.assertIn("Current question: And when was it issued?", prompt)
        self.assertIn("Remembered issue date: 2025-01-01", prompt)

    def test_rejects_document_ids_not_present_in_retrieved_context(self) -> None:
        index = FakeVectorIndex(
            [RetrievedDocumentChunk("doc-1", "Local context", "summary", 0.1)]
        )
        generator = FakeGenerator('{"answer":"Unsupported.","document_ids":["doc-2"]}')

        with self.assertRaises(DocumentParsingError):
            DocumentQuestionPipeline(index, generator).ask("Question")

    def test_returns_explicit_empty_answer_without_calling_generator(self) -> None:
        generator = FakeGenerator("not used")

        answer = DocumentQuestionPipeline(FakeVectorIndex([]), generator).ask(
            "Question"
        )

        self.assertEqual(answer.document_ids, [])
        self.assertEqual(generator.calls, [])

    def test_cli_returns_grounded_json_answer_with_injected_local_dependencies(
        self,
    ) -> None:
        index = FakeVectorIndex(
            [RetrievedDocumentChunk("doc-1", "Expiry: 2030-01-01", "summary", 0.1)]
        )
        generator = FakeGenerator(
            '{"answer":"It expires in 2030.","document_ids":["doc-1"]}'
        )
        stdout = StringIO()
        stderr = StringIO()

        exit_code = run(
            ["--ask-documents", "When does it expire?", "--rag-results", "2"],
            document_vector_index=index,
            rag_generator=generator,
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            json.loads(stdout.getvalue()),
            {"answer": "It expires in 2030.", "document_ids": ["doc-1"]},
        )
        self.assertEqual(index.calls, [("When does it expire?", 2)])
        self.assertIn("Local document answer completed", stderr.getvalue())

    def test_cli_bypasses_vector_search_and_generation_for_expiry_year(self) -> None:
        certificate = _stored_document(
            "certificate-id", "sport_practicability_certificate", "2020-08-21"
        )
        identity_card = _stored_document("identity-id", "identity_card", "2034-06-03")
        repository = FakeExpirationRepository([certificate, identity_card])
        index = FakeVectorIndex([])
        generator = FakeGenerator("not used")
        stdout = StringIO()
        stderr = StringIO()

        exit_code = run(
            ["--ask-documents", "Which documents expired in 2020?"],
            repository_factory=lambda: repository,
            document_vector_index=index,
            rag_generator=generator,
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(repository.year_calls, [2020])
        self.assertEqual(index.calls, [])
        self.assertEqual(generator.calls, [])
        self.assertEqual(
            json.loads(stdout.getvalue()),
            {
                "answer": "Sport Practicability Certificate expired on 2020-08-21.",
                "document_ids": ["certificate-id"],
            },
        )
        self.assertIn("normalized local expiration dates", stderr.getvalue())
