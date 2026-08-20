from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import UTC, date, datetime
from typing import Any
from unittest import TestCase
from unittest.mock import patch

from bson import ObjectId

from db.database import DatabaseConfigurationError, MongoDocumentRepository
from models.document import DocumentData, StructuredDocumentSection


@dataclass
class FakeUpdateResult:
    upserted_id: ObjectId | None


class FakeCursor(list[dict[str, Any]]):
    def sort(self, keys: list[tuple[str, int]]) -> FakeCursor:
        for key, _direction in reversed(keys):
            super().sort(key=lambda item: item[key])
        return self


class FakeCollection:
    def __init__(self) -> None:
        self.documents: list[dict[str, Any]] = []
        self.queries: list[dict[str, Any]] = []
        self.indexes: list[tuple[Any, dict[str, Any]]] = []

    def create_index(self, keys: Any, **kwargs: Any) -> str:
        self.indexes.append((keys, kwargs))
        return str(kwargs["name"])

    def update_one(
        self,
        filter: dict[str, Any],
        update: dict[str, Any],
        **kwargs: Any,
    ) -> FakeUpdateResult:
        existing = self.find_one(filter)
        if existing is not None:
            return FakeUpdateResult(None)
        identifier = ObjectId()
        self.documents.append({"_id": identifier, **deepcopy(update["$setOnInsert"])})
        return FakeUpdateResult(identifier)

    def find_one(self, filter: dict[str, Any]) -> dict[str, Any] | None:
        return next(
            (deepcopy(item) for item in self.documents if _matches(item, filter)),
            None,
        )

    def find(self, filter: dict[str, Any]) -> FakeCursor:
        self.queries.append(deepcopy(filter))
        return FakeCursor(
            deepcopy(item) for item in self.documents if _matches(item, filter)
        )


def _matches(document: dict[str, Any], query: dict[str, Any]) -> bool:
    for key, expected in query.items():
        value: Any = document
        for segment in key.split("."):
            if not isinstance(value, dict) or segment not in value:
                return False
            value = value[segment]
        if isinstance(expected, dict) and set(expected) <= {"$gte", "$lt"}:
            if "$gte" in expected and value < expected["$gte"]:
                return False
            if "$lt" in expected and value >= expected["$lt"]:
                return False
        elif value != expected:
            return False
    return True


def _document(*, expiry_date: str | None = "2030-01-10") -> DocumentData:
    return DocumentData(
        document_type="insurance_policy",
        summary="A vehicle insurance policy",
        expiry_date=expiry_date,
        issue_date="2025-01-10",
        extracted_data={
            "policy_number": "P-123",
            "holder": {"city": "Rome"},
        },
    )


class MongoDocumentRepositoryTests(TestCase):
    def setUp(self) -> None:
        self.collection = FakeCollection()
        self.sections_collection = FakeCollection()
        self.repository = MongoDocumentRepository(
            self.collection,
            sections_collection=self.sections_collection,
        )
        self.file_hash = "a" * 64
        self.created_at = datetime(2026, 8, 11, 12, 30, tzinfo=UTC)

    def test_insert_is_idempotent_and_preserves_dynamic_payload(self) -> None:
        first = self.repository.insert_document(
            _document(), file_hash=self.file_hash, created_at=self.created_at
        )
        second = self.repository.insert_document(
            _document(), file_hash=self.file_hash, created_at=self.created_at
        )

        self.assertTrue(first.inserted)
        self.assertFalse(second.inserted)
        self.assertEqual(first.record.id, second.record.id)
        self.assertEqual(len(self.collection.documents), 1)
        self.assertEqual(first.record.document.expiry_date, date(2030, 1, 10))
        self.assertEqual(
            first.record.document.extracted_data["policy_number"], "P-123"
        )
        self.assertIsInstance(self.collection.documents[0]["expiry_date"], datetime)

    def test_get_document_by_id_and_get_all_documents(self) -> None:
        inserted = self.repository.insert_document(
            _document(), file_hash=self.file_hash, created_at=self.created_at
        )

        found = self.repository.get_document_by_id(inserted.record.id)

        self.assertEqual(found, inserted.record)
        self.assertEqual(self.repository.get_all_documents(), [inserted.record])
        self.assertIsNone(self.repository.get_document_by_id("not-an-object-id"))

    def test_get_expiring_documents_uses_inclusive_day_threshold(self) -> None:
        expected = self.repository.insert_document(
            _document(expiry_date="2030-01-10"),
            file_hash=self.file_hash,
            created_at=self.created_at,
        ).record
        self.repository.insert_document(
            _document(expiry_date="2030-01-11"),
            file_hash="b" * 64,
            created_at=self.created_at,
        )

        results = self.repository.get_expiring_documents(
            2, today=date(2030, 1, 8)
        )

        self.assertEqual(results, [expected])
        expiry_query = self.collection.queries[-1]["expiry_date"]
        self.assertEqual(expiry_query["$gte"].date(), date(2030, 1, 8))
        self.assertEqual(expiry_query["$lt"].date(), date(2030, 1, 11))

    def test_searches_nested_dynamic_field_and_rejects_operator_paths(self) -> None:
        expected = self.repository.insert_document(
            _document(), file_hash=self.file_hash, created_at=self.created_at
        ).record

        results = self.repository.search_by_dynamic_field("holder.city", "Rome")

        self.assertEqual(results, [expected])
        self.assertEqual(
            self.collection.queries[-1], {"extracted_data.holder.city": "Rome"}
        )
        with self.assertRaises(ValueError):
            self.repository.search_by_dynamic_field("$where", "unsafe")

    def test_rejects_invalid_file_hash(self) -> None:
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self.repository.insert_document(_document(), file_hash="invalid")

    def test_persists_structured_pdf_sections_idempotently(self) -> None:
        inserted = self.repository.insert_document(
            _document(), file_hash=self.file_hash, created_at=self.created_at
        )
        section = StructuredDocumentSection(
            chunk_number=1,
            page_from=1,
            page_to=3,
            document=_document(),
        )

        self.repository.upsert_document_sections(inserted.record.id, [section])
        self.repository.upsert_document_sections(inserted.record.id, [section])

        self.assertEqual(len(self.sections_collection.documents), 1)
        stored = self.sections_collection.documents[0]
        self.assertEqual(stored["page_from"], 1)
        self.assertEqual(stored["page_to"], 3)
        self.assertEqual(
            stored["structured_data"]["document_type"],
            "insurance_policy",
        )
        self.assertNotIn("raw_text", stored)

    def test_rejects_remote_mongodb_uri_before_connecting(self) -> None:
        for uri in (
            "mongodb://example.com:27017",
            "mongodb://127.0.0.1:27017/database",
            "mongodb://user:password@127.0.0.1:27017",
            "mongodb+srv://localhost:27017",
        ):
            with self.subTest(uri=uri):
                with self.assertRaises(DatabaseConfigurationError):
                    MongoDocumentRepository.connect(uri=uri)

    def test_connect_pings_local_service_and_creates_query_indexes(self) -> None:
        collection = FakeCollection()

        class FakeMongoClient:
            def __init__(self) -> None:
                self.admin = self
                self.pinged = False
                self.closed = False

            def command(self, command_name: str) -> None:
                self.pinged = command_name == "ping"

            def __getitem__(self, name: str) -> FakeDatabase:
                return FakeDatabase()

            def close(self) -> None:
                self.closed = True

        client = FakeMongoClient()

        class FakeDatabase:
            def __getitem__(self, name: str) -> FakeCollection:
                return collection

        with patch("db.database.MongoClient", return_value=client) as constructor:
            repository = MongoDocumentRepository.connect()

        self.assertTrue(client.pinged)
        self.assertEqual(
            [options["name"] for _keys, options in collection.indexes],
            [
                "unique_file_hash",
                "expiry_date_lookup",
                "unique_document_chunk",
                "document_page_lookup",
            ],
        )
        self.assertTrue(collection.indexes[0][1]["unique"])
        constructor.assert_called_once_with(
            "mongodb://127.0.0.1:27017",
            connect=False,
            serverSelectionTimeoutMS=5_000,
            tz_aware=True,
        )
        repository.close()
        self.assertTrue(client.closed)
