from __future__ import annotations

import json
from unittest import TestCase

from core.parser import LongDocumentParser
from core.pdf import ExtractedPage


class SequencedGenerator:
    def __init__(self, responses: list[dict[str, object]]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, str]] = []

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return json.dumps(self.responses[len(self.calls) - 1])


class LongDocumentParserTests(TestCase):
    def test_chunks_pages_and_merges_generic_structured_data(self) -> None:
        generator = SequencedGenerator(
            [
                {
                    "document_type": "service agreement",
                    "summary": "Parties and service details.",
                    "expiry_date": None,
                    "issue_date": "2026-01-01",
                    "extracted_data": {
                        "provider": "Local Company",
                        "reference_number": "A-42",
                    },
                },
                {
                    "document_type": "service agreement",
                    "summary": "Payment and renewal terms.",
                    "expiry_date": "2027-01-01",
                    "issue_date": None,
                    "extracted_data": {
                        "annual_fee": 1200,
                        "currency": "EUR",
                    },
                },
            ]
        )
        pages = (
            ExtractedPage(1, "A" * 800, False),
            ExtractedPage(2, "B" * 800, False),
        )

        result = LongDocumentParser(
            generator,
            max_chunk_characters=1_000,
        ).parse_pages(pages)

        self.assertEqual(len(result.sections), 2)
        self.assertEqual(result.sections[0].page_from, 1)
        self.assertEqual(result.sections[1].page_from, 2)
        self.assertEqual(result.document.document_type, "service_agreement")
        self.assertEqual(result.document.expiry_date.isoformat(), "2027-01-01")
        self.assertEqual(result.document.extracted_data["annual_fee"], 1200)
        self.assertIn("[Page 1]", generator.calls[0][1])
        self.assertNotIn("[Page 2]", generator.calls[0][1])

    def test_preserves_conflicting_values_instead_of_inventing_one(self) -> None:
        generator = SequencedGenerator(
            [
                {
                    "document_type": "report",
                    "summary": "First section.",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {"status": "draft"},
                },
                {
                    "document_type": "report",
                    "summary": "Second section.",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {"status": "approved"},
                },
            ]
        )

        result = LongDocumentParser(
            generator,
            max_chunk_characters=1_000,
        ).parse_pages(
            (
                ExtractedPage(1, "A" * 800, False),
                ExtractedPage(2, "B" * 800, False),
            )
        )

        self.assertEqual(
            result.document.extracted_data["status"],
            ["draft", "approved"],
        )
