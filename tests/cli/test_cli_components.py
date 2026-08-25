from __future__ import annotations

import json
from datetime import UTC, datetime
from io import StringIO
from unittest import TestCase

from smart_doc_tracker.cli.arguments import CliArgumentParser
from smart_doc_tracker.cli.serializer import JsonResultSerializer
from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.models.document import DocumentData


class CliArgumentParserTests(TestCase):
    def test_parses_local_document_command_options(self) -> None:
        arguments = CliArgumentParser().parse(
            [
                "document.pdf",
                "--structured",
                "--store",
                "--language",
                "ita",
                "--print-ocr-text",
            ]
        )

        self.assertEqual(arguments.image.name, "document.pdf")
        self.assertTrue(arguments.structured)
        self.assertTrue(arguments.store)
        self.assertEqual(arguments.language, "ita")
        self.assertTrue(arguments.print_ocr_text)


class JsonResultSerializerTests(TestCase):
    def test_serializes_insert_result_and_writes_one_json_value(self) -> None:
        document = DocumentData(
            document_type="invoice",
            summary="A local invoice",
            expiry_date=None,
            issue_date="2026-08-01",
            extracted_data={"invoice_number": "42"},
        )
        result = DocumentInsertResult(
            record=StoredDocument(
                id="64b64b64b64b64b64b64b64b",
                file_hash="a" * 64,
                document=document,
                created_at=datetime(2026, 8, 20, 10, 0, tzinfo=UTC),
            ),
            inserted=True,
        )
        output = StringIO()

        JsonResultSerializer.write(
            JsonResultSerializer.insert_result(result),
            output,
        )

        payload = json.loads(output.getvalue())
        self.assertTrue(payload["inserted"])
        self.assertEqual(payload["document"]["document_type"], "invoice")
        self.assertTrue(output.getvalue().endswith("\n"))
