from __future__ import annotations

from datetime import date
from unittest import TestCase

from pydantic import ValidationError

from models.document import DocumentData


class DocumentDataTests(TestCase):
    def test_normalizes_envelope_and_common_date_formats(self) -> None:
        document = DocumentData.model_validate(
            {
                "document_type": "Identity Card",
                "summary": "  Local identity document  ",
                "expiry_date": "31/12/2030",
                "issue_date": "2020-01-02",
                "extracted_data": {"tax_code": "ABC", "address": {"city": "Rome"}},
            }
        )

        self.assertEqual(document.document_type, "identity_card")
        self.assertEqual(document.summary, "Local identity document")
        self.assertEqual(document.expiry_date, date(2030, 12, 31))
        self.assertEqual(document.issue_date, date(2020, 1, 2))

    def test_missing_dates_are_explicitly_null(self) -> None:
        document = DocumentData.model_validate(
            {
                "document_type": "invoice",
                "summary": "An invoice",
                "expiry_date": "unknown",
                "issue_date": None,
                "extracted_data": {},
            }
        )

        self.assertIsNone(document.expiry_date)
        self.assertIsNone(document.issue_date)

    def test_rejects_non_snake_case_dynamic_keys(self) -> None:
        with self.assertRaisesRegex(ValidationError, "English snake_case"):
            DocumentData.model_validate(
                {
                    "document_type": "invoice",
                    "summary": "An invoice",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {"Invoice Number": "42"},
                }
            )

    def test_rejects_unknown_envelope_fields(self) -> None:
        with self.assertRaises(ValidationError):
            DocumentData.model_validate(
                {
                    "document_type": "invoice",
                    "summary": "An invoice",
                    "expiry_date": None,
                    "issue_date": None,
                    "extracted_data": {},
                    "raw_text": "sensitive contents",
                }
            )
