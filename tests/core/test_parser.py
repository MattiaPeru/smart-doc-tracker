from __future__ import annotations

import json
from datetime import date
from unittest import TestCase

from smart_doc_tracker.core.parser import (
    SYSTEM_PROMPT,
    DocumentParser,
    DocumentParsingError,
)


class FakeGenerator:
    def __init__(self, response: str) -> None:
        self.response = response
        self.calls: list[tuple[str, str]] = []

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return self.response


class SequencedGenerator:
    def __init__(self, responses: list[str]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, str]] = []

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        self.calls.append((system_prompt, user_prompt))
        return self.responses[len(self.calls) - 1]


class DocumentParserTests(TestCase):
    def test_system_prompt_contains_explicit_json_response_structure(self) -> None:
        self.assertIn('"document_type": "document_category"', SYSTEM_PROMPT)
        self.assertIn(
            '"summary": "A concise factual summary in English."', SYSTEM_PROMPT
        )
        self.assertIn('"expiry_date": "2030-12-31"', SYSTEM_PROMPT)
        self.assertIn('"issue_date": null', SYSTEM_PROMPT)
        self.assertIn('"extracted_data": {', SYSTEM_PROMPT)
        self.assertIn("Only document_type and summary are required", SYSTEM_PROMPT)
        self.assertIn("Translate the semantic meaning", SYSTEM_PROMPT)
        self.assertIn('"nazionalità" becomes "nationality"', SYSTEM_PROMPT)
        self.assertIn("only lowercase ASCII", SYSTEM_PROMPT)
        self.assertIn(
            "Preserve the original language, accents, and Unicode", SYSTEM_PROMPT
        )
        self.assertIn("real JSON values", SYSTEM_PROMPT)
        self.assertIn("incomplete container placeholders", SYSTEM_PROMPT)

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
        self.assertEqual(document.summary, "A vehicle insurance policy")
        self.assertEqual(document.expiry_date, date(2031, 4, 15))
        self.assertEqual(document.issue_date, date(2026, 4, 15))
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
        self.assertEqual(document.summary, "Invoice")
        self.assertIsNone(document.expiry_date)
        self.assertIsNone(document.issue_date)
        self.assertEqual(document.extracted_data, {})

    def test_recovers_nested_containers_encoded_as_json_strings(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "document_type": "resume",
                    "summary": "A resume",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {
                        "education": '[{"institution":"Local University"}]',
                        "skills": '["Python", "SQL"]',
                    },
                }
            )
        )

        document = DocumentParser(generator).parse("OCR contents")

        self.assertEqual(
            document.extracted_data["education"],
            [{"institution": "Local University"}],
        )
        self.assertEqual(document.extracted_data["skills"], ["Python", "SQL"])

    def test_retries_incomplete_container_placeholders_once(self) -> None:
        incomplete = {
            "document_type": "resume",
            "summary": "A resume",
            "expiry_date": None,
            "issue_date": None,
            "extracted_data": {"education": "[{", "skills": "["},
        }
        corrected = {
            **incomplete,
            "extracted_data": {
                "education": [{"institution": "Local University"}],
                "skills": ["Python"],
            },
        }
        generator = SequencedGenerator([json.dumps(incomplete), json.dumps(corrected)])

        document = DocumentParser(generator).parse("OCR contents")

        self.assertEqual(
            document.extracted_data["education"],
            [{"institution": "Local University"}],
        )
        self.assertEqual(len(generator.calls), 2)
        self.assertIn("previous extraction was rejected", generator.calls[1][0])
        self.assertEqual(generator.calls[1][1], generator.calls[0][1])

    def test_rejects_placeholder_when_local_retry_is_also_incomplete(self) -> None:
        incomplete = json.dumps(
            {
                "document_type": "resume",
                "summary": "A resume",
                "expiry_date": None,
                "issue_date": None,
                "extracted_data": {"education": "[{"},
            }
        )
        generator = SequencedGenerator([incomplete, incomplete])

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")

        self.assertEqual(len(generator.calls), 2)

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
        self.assertEqual(len(generator.calls), 2)

    def test_retries_missing_required_field_with_corrected_output(self) -> None:
        corrected = {
            "document_type": "invoice",
            "summary": "An invoice",
            "expiry_date": None,
            "issue_date": None,
            "extracted_data": {},
        }
        generator = SequencedGenerator(
            [
                json.dumps(
                    {key: value for key, value in corrected.items() if key != "summary"}
                ),
                json.dumps(corrected),
            ]
        )

        document = DocumentParser(generator).parse("OCR contents")

        self.assertEqual(document.summary, "An invoice")
        self.assertEqual(len(generator.calls), 2)

    def test_rejects_each_missing_required_field(self) -> None:
        complete = {
            "document_type": "invoice",
            "summary": "An invoice",
            "expiry_date": None,
            "issue_date": None,
            "extracted_data": {},
        }
        for missing in ("document_type", "summary"):
            with self.subTest(missing=missing):
                response = json.dumps(
                    {key: value for key, value in complete.items() if key != missing}
                )
                generator = FakeGenerator(response)

                with self.assertRaisesRegex(
                    DocumentParsingError, "not valid structured output"
                ) as raised:
                    DocumentParser(generator).parse("OCR contents")

                self.assertEqual(raised.exception.generated_response, response)
                self.assertEqual(len(generator.calls), 2)

    def test_accepts_omitted_optional_fields_without_retry(self) -> None:
        complete = {
            "document_type": "invoice",
            "summary": "An invoice",
            "expiry_date": "2031-04-15",
            "issue_date": "2026-04-15",
            "extracted_data": {"invoice_number": "42"},
        }
        for omitted in (
            ("expiry_date",),
            ("issue_date",),
            ("extracted_data",),
            ("expiry_date", "issue_date", "extracted_data"),
        ):
            with self.subTest(omitted=omitted):
                generator = FakeGenerator(
                    json.dumps(
                        {
                            key: value
                            for key, value in complete.items()
                            if key not in omitted
                        }
                    )
                )

                document = DocumentParser(generator).parse("OCR contents")

                self.assertEqual(document.document_type, "invoice")
                self.assertEqual(document.summary, "An invoice")
                self.assertEqual(
                    document.expiry_date,
                    None if "expiry_date" in omitted else date(2031, 4, 15),
                )
                self.assertEqual(
                    document.issue_date,
                    None if "issue_date" in omitted else date(2026, 4, 15),
                )
                self.assertEqual(
                    document.extracted_data,
                    {} if "extracted_data" in omitted else {"invoice_number": "42"},
                )
                self.assertEqual(len(generator.calls), 1)

    def test_rejects_generated_notification_settings(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "document_type": "invoice",
                    "summary": "An invoice",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {},
                    "notification_days_before": 14,
                }
            )
        )

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")

        self.assertEqual(len(generator.calls), 2)

    def test_rejects_invalid_keys_inside_encoded_nested_containers(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "document_type": "invoice",
                    "summary": "An invoice",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {"items": '[{"Invoice Number":"42"}]'},
                }
            )
        )

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")

        self.assertEqual(len(generator.calls), 2)

    def test_rejects_text_before_generated_json(self) -> None:
        generator = FakeGenerator(
            'Here is the result: {"document_type":"invoice",'
            '"summary":"An invoice","expiry_date":null,'
            '"issue_date":null,"extracted_data":{}}'
        )

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")

        self.assertEqual(len(generator.calls), 2)

    def test_enforces_local_input_size_limit(self) -> None:
        generator = FakeGenerator("{}")

        with self.assertRaisesRegex(DocumentParsingError, "exceeds"):
            DocumentParser(generator, max_ocr_characters=3).parse("four")

        self.assertEqual(generator.calls, [])

    def test_accepts_input_at_exact_size_limit(self) -> None:
        generator = FakeGenerator(
            json.dumps(
                {
                    "document_type": "invoice",
                    "summary": "An invoice",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {},
                }
            )
        )

        document = DocumentParser(generator, max_ocr_characters=4).parse("four")

        self.assertEqual(document.document_type, "invoice")
        self.assertEqual(len(generator.calls), 1)
        self.assertEqual(generator.calls[0][1].count("four"), 1)

    def test_rejects_duplicate_generated_keys(self) -> None:
        generator = FakeGenerator(
            '{"document_type":"invoice","document_type":"contract",'
            '"summary":"Document","expiry_date":null,"issue_date":null,'
            '"extracted_data":{}}'
        )

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")

        self.assertEqual(len(generator.calls), 2)

    def test_rejects_duplicate_keys_in_nested_objects(self) -> None:
        generator = FakeGenerator(
            '{"document_type":"invoice","summary":"An invoice",'
            '"expiry_date":null,"issue_date":null,'
            '"extracted_data":{"address":{"city":"Rome","city":"Milan"}}}'
        )

        with self.assertRaisesRegex(DocumentParsingError, "not valid structured"):
            DocumentParser(generator).parse("OCR contents")

        self.assertEqual(len(generator.calls), 2)
