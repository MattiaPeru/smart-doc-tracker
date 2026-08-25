from __future__ import annotations

import json
from io import StringIO
from unittest import TestCase

from smart_doc_tracker.core.parser import DocumentParsingError
from smart_doc_tracker.main import run
from smart_doc_tracker.models.rag import RetrievedDocumentChunk
from smart_doc_tracker.pipeline import DocumentQuestionPipeline


class FakeVectorIndex:
    def __init__(self, chunks: list[RetrievedDocumentChunk]) -> None:
        self.chunks = chunks
        self.calls: list[tuple[str, int]] = []

    def query(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        self.calls.append((question, limit))
        return self.chunks


class FakeGenerator:
    def __init__(self, response: str) -> None:
        self.response = response
        self.calls: list[tuple[str, str]] = []

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return self.response


class DocumentQuestionPipelineTests(TestCase):
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
