from __future__ import annotations

import json
from io import StringIO
from unittest import TestCase

from smart_doc_tracker.core.parser import DocumentParsingError
from smart_doc_tracker.main import run
from smart_doc_tracker.models.rag import (
    ConversationTurn,
    IndexedDocumentFragment,
    RetrievedDocumentChunk,
)
from smart_doc_tracker.pipeline import DocumentQuestionPipeline


class FakeVectorIndex:
    def __init__(self, chunks: list[RetrievedDocumentChunk]) -> None:
        self.chunks = chunks
        self.calls: list[tuple[str, int]] = []

    def query(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        self.calls.append((question, limit))
        return self.chunks

    def get_document_fragments(self, document_id: str) -> list[IndexedDocumentFragment]:
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


class SequencedFakeGenerator(FakeGenerator):
    def __init__(self, responses: list[str]) -> None:
        super().__init__(responses[-1])
        self.responses = iter(responses)

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return next(self.responses)


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
            json.dumps(
                {
                    "answer": "The document&#x20;explicitly states an expiry date.",
                    "claims": [
                        {
                            "claim": "The expiry date is 2030-01-01.",
                            "evidence": [
                                {
                                    "document_id": "doc-1",
                                    "quote": "Expiry:&#x20;2030-01-01",
                                    "source": "structured_data",
                                    "page": None,
                                }
                            ],
                        }
                    ],
                    "document_ids": ["doc-1"],
                    "insufficient_information": False,
                }
            )
        )

        answer = DocumentQuestionPipeline(index, generator).ask(
            "When does it expire?", limit=3
        )

        self.assertEqual(answer.document_ids, ["doc-1"])
        self.assertNotIn("&#x20;", answer.answer)
        self.assertEqual(
            answer.claims[0].evidence[0].quote,
            "Expiry: 2030-01-01",
        )
        self.assertEqual(index.calls, [("When does it expire?", 3)])
        self.assertIn("Expiry: 2030-01-01", generator.calls[0][1])

    def test_uses_recent_conversation_to_resolve_interpretive_follow_up(
        self,
    ) -> None:
        index = FakeVectorIndex(
            [
                RetrievedDocumentChunk(
                    "doc-1", "Issue date: 2025-01-01", "structured_data", 0.1
                )
            ]
        )
        generator = FakeGenerator(
            json.dumps(
                {
                    "answer": "The record indicates a 2025 issue date.",
                    "claims": [
                        {
                            "claim": "The record indicates a 2025 issue date.",
                            "evidence": [
                                {
                                    "document_id": "doc-1",
                                    "quote": "Issue date: 2025-01-01",
                                    "source": "structured_data",
                                    "page": None,
                                }
                            ],
                        }
                    ],
                    "document_ids": ["doc-1"],
                    "insufficient_information": False,
                }
            )
        )
        history = (
            ConversationTurn(
                "When does my insurance policy expire?",
                "It expires in 2030.",
                ("doc-1",),
            ),
        )

        DocumentQuestionPipeline(index, generator).ask(
            "What does that date suggest?",
            history=history,
        )

        retrieval_question = index.calls[0][0]
        self.assertIn("When does my insurance policy expire?", retrieval_question)
        self.assertIn("What does that date suggest?", retrieval_question)
        prompt = generator.calls[0][1]
        self.assertIn('"document_ids": ["doc-1"]', prompt)
        self.assertIn("Current question: What does that date suggest?", prompt)
        self.assertIn("Remembered issue date: 2025-01-01", prompt)

    def test_rejects_document_ids_not_present_in_retrieved_context(self) -> None:
        index = FakeVectorIndex(
            [RetrievedDocumentChunk("doc-1", "Local context", "summary", 0.1)]
        )
        generator = FakeGenerator('{"answer":"Unsupported.","document_ids":["doc-2"]}')

        with self.assertRaises(DocumentParsingError):
            DocumentQuestionPipeline(index, generator).ask("Question")

        self.assertEqual(len(generator.calls), 2)

    def test_rejects_an_invented_quote(self) -> None:
        index = FakeVectorIndex(
            [
                RetrievedDocumentChunk(
                    "doc-1", "Python Backend Developer", "raw_text", 0.1
                )
            ]
        )
        generator = FakeGenerator(
            json.dumps(
                {
                    "answer": "The CV suggests backend specialization.",
                    "claims": [
                        {
                            "claim": "Backend specialization",
                            "evidence": [
                                {
                                    "document_id": "doc-1",
                                    "quote": "Senior Java architect",
                                    "source": "raw_text",
                                    "page": None,
                                }
                            ],
                        }
                    ],
                    "document_ids": ["doc-1"],
                    "insufficient_information": False,
                }
            )
        )

        with self.assertRaises(DocumentParsingError) as raised:
            DocumentQuestionPipeline(index, generator).ask("What is the specialty?")

        self.assertIn("Senior Java architect", raised.exception.generated_response)
        self.assertEqual(
            raised.exception.validation_reason,
            "The local model returned a quote absent from retrieved context.",
        )
        self.assertEqual(len(raised.exception.validation_diagnostics), 2)

    def test_retry_explains_grounding_failure_and_accepts_corrected_quote(
        self,
    ) -> None:
        invalid = json.dumps(
            {
                "answer": "The CV concerns a backend developer.",
                "claims": [
                    {
                        "claim": "The CV concerns a backend developer.",
                        "evidence": [
                            {
                                "document_id": "doc-1",
                                "quote": "Experienced backend developer",
                                "source": "raw_text",
                                "page": None,
                            }
                        ],
                    }
                ],
                "document_ids": ["doc-1"],
                "insufficient_information": False,
            }
        )
        corrected = json.dumps(
            {
                "answer": "The CV identifies a Python backend developer.",
                "claims": [
                    {
                        "claim": "The CV identifies a Python backend developer.",
                        "evidence": [
                            {
                                "document_id": "doc-1",
                                "quote": "Python Backend Developer",
                                "source": "raw_text",
                                "page": None,
                            }
                        ],
                    }
                ],
                "document_ids": ["doc-1"],
                "insufficient_information": False,
            }
        )
        generator = SequencedFakeGenerator([invalid, corrected])
        index = FakeVectorIndex(
            [
                RetrievedDocumentChunk(
                    "doc-1", "Python Backend Developer", "raw_text", 0.1
                )
            ]
        )

        answer = DocumentQuestionPipeline(index, generator).ask(
            "What is the specialty?"
        )

        self.assertEqual(answer.claims[0].evidence[0].quote, "Python Backend Developer")
        self.assertEqual(len(generator.calls), 2)
        system_prompt = generator.calls[0][0]
        self.assertNotIn("A prudent synthesis", system_prompt)
        self.assertNotIn("One concrete conclusion", system_prompt)
        retry_prompt = generator.calls[1][1]
        self.assertIn(
            "The local model returned a quote absent from retrieved context.",
            retry_prompt,
        )
        self.assertIn("select only evidence_ids", retry_prompt)

    def test_materializes_exact_evidence_from_generated_passage_ids(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "claims": [
                        {
                            "claim": "The CV lists Python, Java, and SQL skills.",
                            "evidence_ids": ["E1"],
                        }
                    ],
                    "insufficient_information": False,
                }
            )
        )
        exact_skills = "Technical skills: Python, Java, SQL"
        index = FakeVectorIndex(
            [RetrievedDocumentChunk("doc-1", exact_skills, "raw_text", 0.1, 2)]
        )

        answer = DocumentQuestionPipeline(index, generator).ask(
            "Which skills are in the CV?"
        )

        self.assertEqual(answer.answer, "The CV lists Python, Java, and SQL skills.")
        self.assertEqual(answer.document_ids, ["doc-1"])
        evidence = answer.claims[0].evidence[0]
        self.assertEqual(evidence.quote, exact_skills)
        self.assertEqual(evidence.source, "raw_text")
        self.assertEqual(evidence.page, 2)
        self.assertIn('id="E1"', generator.calls[0][1])
        self.assertIn("evidence_ids", generator.calls[0][0])

    def test_replaces_factual_content_in_an_insufficient_answer(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "answer": "The CV lists Python, Java, and SQL.",
                    "claims": [],
                    "document_ids": [],
                    "insufficient_information": True,
                }
            )
        )
        index = FakeVectorIndex(
            [RetrievedDocumentChunk("doc-1", "Unrelated text", "raw_text", 0.1)]
        )

        answer = DocumentQuestionPipeline(index, generator).ask(
            "Which skills are listed?"
        )

        self.assertEqual(
            answer.answer,
            "The retrieved context does not contain enough verifiable information "
            "to answer.",
        )
        self.assertNotIn("Python", answer.answer)
        self.assertEqual(answer.claims, [])
        self.assertEqual(answer.document_ids, [])

    def test_cli_can_print_explicitly_requested_rag_failure_details(self) -> None:
        rejected_response = json.dumps(
            {
                "answer": "The CV suggests backend specialization.",
                "claims": [
                    {
                        "claim": "Backend specialization",
                        "evidence": [
                            {
                                "document_id": "doc-1",
                                "quote": "Senior Java architect",
                                "source": "raw_text",
                                "page": None,
                            }
                        ],
                    }
                ],
                "document_ids": ["doc-1"],
                "insufficient_information": False,
            }
        )
        stdout = StringIO()
        stderr = StringIO()

        exit_code = run(
            [
                "--ask-documents",
                "What is the specialty?",
                "--show-rag-validation-details",
            ],
            document_vector_index=FakeVectorIndex(
                [
                    RetrievedDocumentChunk(
                        "doc-1", "Python Backend Developer", "raw_text", 0.1
                    )
                ]
            ),
            rag_generator=FakeGenerator(rejected_response),
            stdout=stdout,
            stderr=stderr,
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn(rejected_response, stderr.getvalue())
        self.assertIn(
            "The local model returned a quote absent from retrieved context.",
            stderr.getvalue(),
        )
        self.assertIn("attempt 1", stderr.getvalue())
        self.assertIn("attempt 2", stderr.getvalue())

    def test_cli_hides_rag_failure_details_without_explicit_option(self) -> None:
        rejected_response = '{"answer":"Private rejected answer"}'
        stderr = StringIO()

        exit_code = run(
            ["--ask-documents", "What is the specialty?"],
            document_vector_index=FakeVectorIndex(
                [
                    RetrievedDocumentChunk(
                        "doc-1", "Python Backend Developer", "raw_text", 0.1
                    )
                ]
            ),
            rag_generator=FakeGenerator(rejected_response),
            stdout=StringIO(),
            stderr=stderr,
        )

        self.assertEqual(exit_code, 1)
        self.assertNotIn(rejected_response, stderr.getvalue())
        self.assertNotIn("Validation reason:", stderr.getvalue())

    def test_rejects_a_claim_without_evidence(self) -> None:
        index = FakeVectorIndex(
            [
                RetrievedDocumentChunk(
                    "doc-1", "Python Backend Developer", "raw_text", 0.1
                )
            ]
        )
        generator = FakeGenerator(
            json.dumps(
                {
                    "answer": "The CV suggests backend specialization.",
                    "claims": [{"claim": "Backend specialization", "evidence": []}],
                    "document_ids": ["doc-1"],
                    "insufficient_information": False,
                }
            )
        )

        with self.assertRaises(DocumentParsingError):
            DocumentQuestionPipeline(index, generator).ask("What is the specialty?")

    def test_successful_grounding_logs_no_question_answer_or_quote(self) -> None:
        secret_quote = "Confidential Python Backend Developer"
        index = FakeVectorIndex(
            [RetrievedDocumentChunk("doc-1", secret_quote, "raw_text", 0.1)]
        )
        generator = FakeGenerator(
            json.dumps(
                {
                    "answer": "Sensitive synthesized answer",
                    "claims": [
                        {
                            "claim": "Sensitive claim",
                            "evidence": [
                                {
                                    "document_id": "doc-1",
                                    "quote": secret_quote,
                                    "source": "raw_text",
                                    "page": None,
                                }
                            ],
                        }
                    ],
                    "document_ids": ["doc-1"],
                    "insufficient_information": False,
                }
            )
        )

        with self.assertLogs("smart_doc_tracker.pipeline", level="INFO") as captured:
            DocumentQuestionPipeline(index, generator).ask("Private CV question")

        output = "\n".join(captured.output)
        self.assertNotIn("Private CV question", output)
        self.assertNotIn("Sensitive synthesized answer", output)
        self.assertNotIn("Sensitive claim", output)
        self.assertNotIn(secret_quote, output)

    def test_returns_explicit_empty_answer_without_calling_generator(self) -> None:
        generator = FakeGenerator("not used")

        answer = DocumentQuestionPipeline(FakeVectorIndex([]), generator).ask(
            "Question"
        )

        self.assertEqual(
            answer.answer,
            "No indexed document contains enough information to answer.",
        )
        self.assertEqual(answer.claims, [])
        self.assertEqual(answer.document_ids, [])
        self.assertTrue(answer.insufficient_information)
        self.assertEqual(generator.calls, [])

    def test_cli_routes_expiry_and_other_fields_through_grounded_retrieval(self) -> None:
        questions = (
            "Which documents expired in 2020?",
            "What is extracted_data.membership_number?",
        )
        for question in questions:
            with self.subTest(question=question):
                index = FakeVectorIndex(
                    [
                        RetrievedDocumentChunk(
                            "doc-1",
                            "Membership number: MEM-0042; expiry date: 2020-08-21",
                            "structured_data",
                            0.1,
                        )
                    ]
                )
                generator = FakeGenerator(
                    json.dumps(
                        {
                            "claims": [
                                {
                                    "claim": "The requested value appears in the document.",
                                    "evidence_ids": ["E1"],
                                }
                            ]
                        }
                    )
                )
                stdout = StringIO()
                stderr = StringIO()

                exit_code = run(
                    ["--ask-documents", question, "--rag-results", "2"],
                    repository_factory=lambda: self.fail(
                        "Question answering must not open the repository."
                    ),
                    document_vector_index=index,
                    rag_generator=generator,
                    stdout=stdout,
                    stderr=stderr,
                )

                self.assertEqual(exit_code, 0)
                self.assertEqual(index.calls, [(question, 2)])
                self.assertEqual(len(generator.calls), 1)
                self.assertEqual(
                    json.loads(stdout.getvalue())["document_ids"], ["doc-1"]
                )
                self.assertIn(question, generator.calls[0][1])
