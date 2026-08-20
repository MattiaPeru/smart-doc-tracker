from __future__ import annotations

import json
from unittest import TestCase

from core.parser import DocumentParser, DocumentParsingError, SYSTEM_PROMPT


class FakeGenerator:
    def __init__(self, response: str) -> None:
        self.response = response
        self.calls: list[tuple[str, str]] = []

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return self.response


class DocumentParserTests(TestCase):
    def test_system_prompt_contains_explicit_json_response_structure(self) -> None:
        self.assertIn('"document_type": "document_category"', SYSTEM_PROMPT)
        self.assertIn('"summary": "A concise factual summary in English."', SYSTEM_PROMPT)
        self.assertIn('"expiry_date": "2030-12-31"', SYSTEM_PROMPT)
        self.assertIn('"issue_date": null', SYSTEM_PROMPT)
        self.assertIn('"extracted_data": {', SYSTEM_PROMPT)
        self.assertIn("All five top-level fields are required", SYSTEM_PROMPT)
        self.assertIn("Translate the semantic meaning", SYSTEM_PROMPT)
        self.assertIn('"nazionalità" becomes "nationality"', SYSTEM_PROMPT)
        self.assertIn("only lowercase ASCII", SYSTEM_PROMPT)
        self.assertIn("Preserve the original language, accents, and Unicode", SYSTEM_PROMPT)

    def test_parses_valid_generated_json(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "document_type": "Insurance Policy",
                    "summary": "A vehicle insurance policy",
                    "expiry_date": "2031-04-15",
                    "issue_date": "2026-04-15",
                    "extracted_data": {"policy_number": "P-123"},
                }
            )
        )

        document = DocumentParser(generator).parse("OCR contents")

        self.assertEqual(document.document_type, "insurance_policy")
        self.assertEqual(document.extracted_data, {"policy_number": "P-123"})
        self.assertEqual(len(generator.calls), 1)
        self.assertEqual(generator.calls[0][0], SYSTEM_PROMPT)
        self.assertIn("<ocr_text>\nOCR contents\n</ocr_text>", generator.calls[0][1])

    def test_accepts_markdown_fence_from_imperfect_local_model(self) -> None:
        generator = FakeGenerator(
            "```json\n"
            '{"document_type":"invoice","summary":"Invoice",'
            '"expiry_date":null,"issue_date":null,"extracted_data":{}}\n'
            "```"
        )

        document = DocumentParser(generator).parse("OCR contents")

        self.assertEqual(document.document_type, "invoice")

    def test_rejects_empty_ocr_without_calling_generator(self) -> None:
        generator = FakeGenerator("{}")

        with self.assertRaisesRegex(DocumentParsingError, "cannot be empty"):
            DocumentParser(generator).parse("  \n")

        self.assertEqual(generator.calls, [])

    def test_rejects_invalid_generated_output_without_exposing_it(self) -> None:
        generator = FakeGenerator("private invalid model output")

        with self.assertRaisesRegex(
            DocumentParsingError, "not valid structured output"
        ) as raised:
            DocumentParser(generator).parse("private OCR contents")

        self.assertNotIn("private", str(raised.exception))
        self.assertEqual(
            raised.exception.generated_response, "private invalid model output"
        )

    def test_enforces_local_input_size_limit(self) -> None:
        generator = FakeGenerator("{}")

        with self.assertRaisesRegex(DocumentParsingError, "exceeds"):
            DocumentParser(generator, max_ocr_characters=3).parse("four")

        self.assertEqual(generator.calls, [])

    def test_rejects_duplicate_generated_keys(self) -> None:
        generator = FakeGenerator(
            '{"document_type":"invoice","document_type":"contract",'
            '"summary":"Document","expiry_date":null,"issue_date":null,'
            '"extracted_data":{}}'
        )

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")
