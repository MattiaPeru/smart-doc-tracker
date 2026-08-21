"""MongoDB persistence for validated documents on the local host."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import UTC, date, datetime, time, timedelta
from collections.abc import Sequence
from typing import Any
from urllib.parse import urlsplit

from bson import ObjectId
from pymongo import ASCENDING, MongoClient
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError, PyMongoError

from interfaces.document_collection import DocumentCollection
from models.document import DocumentData, StructuredDocumentSection


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_FIELD_PATH = re.compile(
    r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*"
    r"(?:\.[a-z][a-z0-9]*(?:_[a-z0-9]+)*)*$"
)


class DatabaseConfigurationError(ValueError):
    """Raised when MongoDB is not configured as a loopback-only service."""


class DatabaseError(RuntimeError):
    """Raised when a local database operation cannot be completed."""


@dataclass(frozen=True, slots=True)
class StoredDocument:
    """A validated document together with its persistence metadata."""

    id: str
    file_hash: str
    document: DocumentData
    created_at: datetime


@dataclass(frozen=True, slots=True)
class DocumentInsertResult:
    """Result of an idempotent document insertion."""

    record: StoredDocument
    inserted: bool


class MongoDocumentRepository:
    """Store and query hybrid documents in a local MongoDB collection."""

    def __init__(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = sections_collection
        self._client = client

    @classmethod
    def connect(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
    ) -> MongoDocumentRepository:
        """Connect to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=False,
            serverSelectionTimeoutMS=timeout_ms,
            tz_aware=True,
        )
        try:
            client.admin.command("ping")
            database = client[database_name]
            collection: Collection[dict[str, Any]] = database[collection_name]
            sections_collection: Collection[dict[str, Any]] = database[
                "document_sections"
            ]
            collection.create_index(
                [("file_hash", ASCENDING)], unique=True, name="unique_file_hash"
            )
            collection.create_index(
                [("expiry_date", ASCENDING)], name="expiry_date_lookup"
            )
            sections_collection.create_index(
                [("document_id", ASCENDING), ("chunk_number", ASCENDING)],
                unique=True,
                name="unique_document_chunk",
            )
            sections_collection.create_index(
                [("document_id", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            collection,
            sections_collection=sections_collection,
            client=client,
        )

    def close(self) -> None:
        """Close the owned MongoDB client, if this repository created one."""
        if self._client is not None:
            self._client.close()

    def __enter__(self) -> MongoDocumentRepository:
        """Return this repository for context-managed use."""
        return self

    def __exit__(self, *args: object) -> None:
        """Close the owned client when leaving the context."""
        self.close()

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at or datetime.now(UTC))
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        payload["file_hash"] = normalized_hash
        payload["created_at"] = timestamp

        try:
            try:
                result = self._collection.update_one(
                    {"file_hash": normalized_hash},
                    {"$setOnInsert": payload},
                    upsert=True,
                )
                inserted = result.upserted_id is not None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(record=_to_stored_document(stored), inserted=inserted)

    def upsert_document_sections(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                "Document section persistence is not configured."
            )
        if not ObjectId.is_valid(document_id):
            raise ValueError("document_id must be a valid MongoDB identifier")
        identifier = ObjectId(document_id)

        try:
            for section in sections:
                document_payload = section.document.model_dump(mode="python")
                document_payload["expiry_date"] = _date_to_datetime(
                    section.document.expiry_date
                )
                document_payload["issue_date"] = _date_to_datetime(
                    section.document.issue_date
                )
                self._sections_collection.update_one(
                    {
                        "document_id": identifier,
                        "chunk_number": section.chunk_number,
                    },
                    {
                        "$setOnInsert": {
                            "document_id": identifier,
                            "chunk_number": section.chunk_number,
                            "page_from": section.page_from,
                            "page_to": section.page_to,
                            "structured_data": document_payload,
                        }
                    },
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def get_all_documents(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def get_expiring_documents(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def search_by_dynamic_field(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError("field_key must be a dot-separated English snake_case path")
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def _find_documents(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc


def _validate_local_mongodb_uri(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError("The MongoDB endpoint has an invalid port.") from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def _validate_mongodb_name(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def _validate_file_hash(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def _date_to_datetime(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, time.min, tzinfo=UTC)


def _normalize_datetime(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError("created_at must include timezone information")
    return value.astimezone(UTC)


def _to_stored_document(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "expiry_date",
                "issue_date",
                "extracted_data",
            )
        }
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc
