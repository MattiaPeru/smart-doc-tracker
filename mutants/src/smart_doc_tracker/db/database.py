"""MongoDB persistence for validated documents on the local host."""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, date, datetime, time, timedelta
from pathlib import Path
from typing import Any, cast
from urllib.parse import urlsplit

from bson import ObjectId
from pymongo import ASCENDING, MongoClient
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError, PyMongoError

from ..interfaces.document_collection import DocumentCollection
from ..models.document import DocumentData, StructuredDocumentSection

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_FIELD_PATH = re.compile(
    r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*"
    r"(?:\.[a-z][a-z0-9]*(?:_[a-z0-9]+)*)*$"
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
    source_file_name: str | None = None


@dataclass(frozen=True, slots=True)
class DocumentInsertResult:
    """Result of an idempotent document insertion."""

    record: StoredDocument
    inserted: bool
mutants_xǁMongoDocumentRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁclose__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut: MutantDict = {}  # type: ignore


class MongoDocumentRepository:
    """Store and query hybrid documents in a local MongoDB collection."""

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁ__init____mutmut)
    def __init__(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = True,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = sections_collection
        self._client = client
        self._close_on_exit = close_on_exit

    def xǁMongoDocumentRepositoryǁ__init____mutmut_orig(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = True,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = sections_collection
        self._client = client
        self._close_on_exit = close_on_exit

    def xǁMongoDocumentRepositoryǁ__init____mutmut_1(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = False,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = sections_collection
        self._client = client
        self._close_on_exit = close_on_exit

    def xǁMongoDocumentRepositoryǁ__init____mutmut_2(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = True,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = None
        self._sections_collection = sections_collection
        self._client = client
        self._close_on_exit = close_on_exit

    def xǁMongoDocumentRepositoryǁ__init____mutmut_3(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = True,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = None
        self._client = client
        self._close_on_exit = close_on_exit

    def xǁMongoDocumentRepositoryǁ__init____mutmut_4(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = True,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = sections_collection
        self._client = None
        self._close_on_exit = close_on_exit

    def xǁMongoDocumentRepositoryǁ__init____mutmut_5(
        self,
        collection: DocumentCollection,
        *,
        sections_collection: DocumentCollection | None = None,
        client: MongoClient[dict[str, Any]] | None = None,
        close_on_exit: bool = True,
    ) -> None:
        """Configure document collections and an optional owned client."""
        self._collection = collection
        self._sections_collection = sections_collection
        self._client = client
        self._close_on_exit = None

    @classmethod
    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁconnect__mutmut, is_classmethod = True)
    def connect(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_orig(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_1(
        cls,
        *,
        uri: str = "XXmongodb://127.0.0.1:27017XX",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_2(
        cls,
        *,
        uri: str = "MONGODB://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_3(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "XXsmart_doc_trackerXX",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_4(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "SMART_DOC_TRACKER",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_5(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "XXdocumentsXX",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_6(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "DOCUMENTS",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_7(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5001,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_8(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = False,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_9(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(None)
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_10(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(None, label="database_name")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_11(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label=None)
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_12(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(label="database_name")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_13(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, )
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_14(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="XXdatabase_nameXX")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_15(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="DATABASE_NAME")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_16(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(None, label="collection_name")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_17(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label=None)
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_18(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(label="collection_name")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_19(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, )
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_20(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="XXcollection_nameXX")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_21(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="COLLECTION_NAME")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_22(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms < 0:
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_23(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 1:
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_24(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError(None)

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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_25(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("XXtimeout_ms must be positiveXX")

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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_26(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("TIMEOUT_MS MUST BE POSITIVE")

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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_27(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = None
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_28(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            None,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_29(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=None,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_30(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=False,
            serverSelectionTimeoutMS=None,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_31(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=False,
            serverSelectionTimeoutMS=timeout_ms,
            tz_aware=None,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_32(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_33(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_34(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=False,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_35(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=False,
            serverSelectionTimeoutMS=timeout_ms,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_36(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=True,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_37(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
        _validate_local_mongodb_uri(uri)
        _validate_mongodb_name(database_name, label="database_name")
        _validate_mongodb_name(collection_name, label="collection_name")
        if timeout_ms <= 0:
            raise DatabaseConfigurationError("timeout_ms must be positive")

        client: MongoClient[dict[str, Any]] = MongoClient(
            uri,
            connect=False,
            serverSelectionTimeoutMS=timeout_ms,
            tz_aware=False,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_38(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            client.admin.command(None)
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_39(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            client.admin.command("XXpingXX")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_40(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            client.admin.command("PING")
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_41(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            database = None
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_42(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            collection: Collection[dict[str, Any]] = None
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_43(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            sections_collection: Collection[dict[str, Any]] = None
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_44(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                "XXdocument_sectionsXX"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_45(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                "DOCUMENT_SECTIONS"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_46(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                None, unique=True, name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_47(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], unique=None, name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_48(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], unique=True, name=None
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_49(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                unique=True, name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_50(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_51(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], unique=True, )
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_52(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("XXfile_hashXX", ASCENDING)], unique=True, name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_53(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("FILE_HASH", ASCENDING)], unique=True, name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_54(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], unique=False, name="unique_file_hash"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_55(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], unique=True, name="XXunique_file_hashXX"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_56(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("file_hash", ASCENDING)], unique=True, name="UNIQUE_FILE_HASH"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_57(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                None, name="expiry_date_lookup"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_58(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("expiry_date", ASCENDING)], name=None
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_59(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name="expiry_date_lookup"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_60(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("expiry_date", ASCENDING)], )
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_61(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("XXexpiry_dateXX", ASCENDING)], name="expiry_date_lookup"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_62(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("EXPIRY_DATE", ASCENDING)], name="expiry_date_lookup"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_63(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("expiry_date", ASCENDING)], name="XXexpiry_date_lookupXX"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_64(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("expiry_date", ASCENDING)], name="EXPIRY_DATE_LOOKUP"
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_65(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                None,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_66(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                unique=None,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_67(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name=None,
            )
            sections_collection.create_index(
                [("document_id", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_68(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_69(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_70(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                )
            sections_collection.create_index(
                [("document_id", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_71(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("XXdocument_idXX", ASCENDING), ("chunk_number", ASCENDING)],
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_72(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("DOCUMENT_ID", ASCENDING), ("chunk_number", ASCENDING)],
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_73(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("document_id", ASCENDING), ("XXchunk_numberXX", ASCENDING)],
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_74(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("document_id", ASCENDING), ("CHUNK_NUMBER", ASCENDING)],
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_75(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                unique=False,
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_76(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name="XXunique_document_chunkXX",
            )
            sections_collection.create_index(
                [("document_id", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_77(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name="UNIQUE_DOCUMENT_CHUNK",
            )
            sections_collection.create_index(
                [("document_id", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_78(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                None,
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_79(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name=None,
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_80(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_81(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_82(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("XXdocument_idXX", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_83(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("DOCUMENT_ID", ASCENDING), ("page_from", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_84(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("document_id", ASCENDING), ("XXpage_fromXX", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_85(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                [("document_id", ASCENDING), ("PAGE_FROM", ASCENDING)],
                name="document_page_lookup",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_86(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name="XXdocument_page_lookupXX",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_87(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
                name="DOCUMENT_PAGE_LOOKUP",
            )
        except PyMongoError as exc:
            client.close()
            raise DatabaseError("The local MongoDB service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_88(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            raise DatabaseError(None) from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_89(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            raise DatabaseError("XXThe local MongoDB service is unavailable.XX") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_90(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            raise DatabaseError("the local mongodb service is unavailable.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_91(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            raise DatabaseError("THE LOCAL MONGODB SERVICE IS UNAVAILABLE.") from exc
        return cls(
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_92(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            None,
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_93(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=None,
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_94(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=None,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_95(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=None,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_96(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_97(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_98(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_99(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_100(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(None, collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_101(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, None),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_102(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(collection),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_103(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, ),
            sections_collection=cast(DocumentCollection, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_104(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(None, sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_105(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, None),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_106(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(sections_collection),
            client=client,
            close_on_exit=close_on_exit,
        )

    @classmethod
    def xǁMongoDocumentRepositoryǁconnect__mutmut_107(
        cls,
        *,
        uri: str = "mongodb://127.0.0.1:27017",
        database_name: str = "smart_doc_tracker",
        collection_name: str = "documents",
        timeout_ms: int = 5_000,
        close_on_exit: bool = True,
    ) -> MongoDocumentRepository:
        """Connect once to MongoDB after enforcing a loopback-only configuration."""
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
            cast(DocumentCollection, collection),
            sections_collection=cast(DocumentCollection, ),
            client=client,
            close_on_exit=close_on_exit,
        )

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁclose__mutmut)
    def close(self) -> None:
        """Close the owned MongoDB client, if this repository created one."""
        if self._client is not None:
            self._client.close()

    def xǁMongoDocumentRepositoryǁclose__mutmut_orig(self) -> None:
        """Close the owned MongoDB client, if this repository created one."""
        if self._client is not None:
            self._client.close()

    def xǁMongoDocumentRepositoryǁclose__mutmut_1(self) -> None:
        """Close the owned MongoDB client, if this repository created one."""
        if self._client is None:
            self._client.close()

    def __enter__(self) -> MongoDocumentRepository:
        """Return this repository for context-managed use."""
        return self

    def __exit__(self, *args: object) -> None:
        """Close the owned client when leaving the context."""
        if self._close_on_exit:
            self.close()

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_orig(
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_1(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = None
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_2(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(None)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_3(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = None
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_4(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(None)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_5(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at and datetime.now(UTC))
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_6(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at or datetime.now(None))
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_7(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at or datetime.now(UTC))
        payload = None
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_8(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at or datetime.now(UTC))
        payload = document.model_dump(mode=None)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_9(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at or datetime.now(UTC))
        payload = document.model_dump(mode="XXpythonXX")
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_10(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        created_at: datetime | None = None,
    ) -> DocumentInsertResult:
        """Insert once by file hash and return the existing record on retries."""
        normalized_hash = _validate_file_hash(file_hash)
        timestamp = _normalize_datetime(created_at or datetime.now(UTC))
        payload = document.model_dump(mode="PYTHON")
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_11(
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
        payload["expiry_date"] = None
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_12(
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
        payload["XXexpiry_dateXX"] = _date_to_datetime(document.expiry_date)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_13(
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
        payload["EXPIRY_DATE"] = _date_to_datetime(document.expiry_date)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_14(
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
        payload["expiry_date"] = _date_to_datetime(None)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_15(
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
        payload["issue_date"] = None
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_16(
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
        payload["XXissue_dateXX"] = _date_to_datetime(document.issue_date)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_17(
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
        payload["ISSUE_DATE"] = _date_to_datetime(document.issue_date)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_18(
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
        payload["issue_date"] = _date_to_datetime(None)
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_19(
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
        payload["file_hash"] = None
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_20(
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
        payload["XXfile_hashXX"] = normalized_hash
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_21(
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
        payload["FILE_HASH"] = normalized_hash
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_22(
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
        payload["created_at"] = None

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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_23(
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
        payload["XXcreated_atXX"] = timestamp

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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_24(
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
        payload["CREATED_AT"] = timestamp

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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_25(
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
                result = None
                inserted = result.upserted_id is not None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_26(
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
                    None,
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_27(
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
                    None,
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_28(
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
                    upsert=None,
                )
                inserted = result.upserted_id is not None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_29(
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_30(
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_31(
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
                    )
                inserted = result.upserted_id is not None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_32(
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
                    {"XXfile_hashXX": normalized_hash},
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_33(
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
                    {"FILE_HASH": normalized_hash},
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_34(
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
                    {"XX$setOnInsertXX": payload},
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_35(
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
                    {"$setoninsert": payload},
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_36(
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
                    {"$SETONINSERT": payload},
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_37(
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
                    upsert=False,
                )
                inserted = result.upserted_id is not None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_38(
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
                inserted = None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_39(
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
                inserted = result.upserted_id is None
            except DuplicateKeyError:
                inserted = False
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_40(
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
                inserted = None
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_41(
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
                inserted = True
            stored = self._collection.find_one({"file_hash": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_42(
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
            stored = None
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_43(
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
            stored = self._collection.find_one(None)
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_44(
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
            stored = self._collection.find_one({"XXfile_hashXX": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_45(
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
            stored = self._collection.find_one({"FILE_HASH": normalized_hash})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_46(
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
            raise DatabaseError(None) from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_47(
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
            raise DatabaseError("XXThe document could not be stored locally.XX") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_48(
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
            raise DatabaseError("the document could not be stored locally.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_49(
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
            raise DatabaseError("THE DOCUMENT COULD NOT BE STORED LOCALLY.") from exc

        if stored is None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_50(
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

        if stored is not None:
            raise DatabaseError("The stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_51(
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
            raise DatabaseError(None)
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_52(
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
            raise DatabaseError("XXThe stored document could not be retrieved.XX")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_53(
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
            raise DatabaseError("the stored document could not be retrieved.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_54(
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
            raise DatabaseError("THE STORED DOCUMENT COULD NOT BE RETRIEVED.")
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_55(
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
        return DocumentInsertResult(
            record=None, inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_56(
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), inserted=None
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_57(
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
        return DocumentInsertResult(
            inserted=inserted
        )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_58(
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
        return DocumentInsertResult(
            record=_to_stored_document(stored), )

    def xǁMongoDocumentRepositoryǁinsert_document__mutmut_59(
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
        return DocumentInsertResult(
            record=_to_stored_document(None), inserted=inserted
        )

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut)
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_orig(
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_1(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is not None:
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_2(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                None
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_3(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                "XXDocument section persistence is not configured.XX"
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_4(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                "document section persistence is not configured."
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_5(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                "DOCUMENT SECTION PERSISTENCE IS NOT CONFIGURED."
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_6(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                "Document section persistence is not configured."
            )
        if ObjectId.is_valid(document_id):
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_7(
        self,
        document_id: str,
        sections: Sequence[StructuredDocumentSection],
    ) -> None:
        """Persist validated PDF section analyses without storing raw page text."""
        if self._sections_collection is None:
            raise DatabaseConfigurationError(
                "Document section persistence is not configured."
            )
        if not ObjectId.is_valid(None):
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_8(
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
            raise ValueError(None)
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_9(
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
            raise ValueError("XXdocument_id must be a valid MongoDB identifierXX")
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_10(
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
            raise ValueError("document_id must be a valid mongodb identifier")
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_11(
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
            raise ValueError("DOCUMENT_ID MUST BE A VALID MONGODB IDENTIFIER")
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_12(
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
        identifier = None

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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_13(
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
        identifier = ObjectId(None)

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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_14(
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
                document_payload = None
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_15(
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
                document_payload = section.document.model_dump(mode=None)
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_16(
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
                document_payload = section.document.model_dump(mode="XXpythonXX")
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_17(
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
                document_payload = section.document.model_dump(mode="PYTHON")
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_18(
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
                document_payload["expiry_date"] = None
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_19(
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
                document_payload["XXexpiry_dateXX"] = _date_to_datetime(
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_20(
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
                document_payload["EXPIRY_DATE"] = _date_to_datetime(
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_21(
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
                    None
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_22(
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
                document_payload["issue_date"] = None
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_23(
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
                document_payload["XXissue_dateXX"] = _date_to_datetime(
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_24(
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
                document_payload["ISSUE_DATE"] = _date_to_datetime(
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_25(
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
                    None
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_26(
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
                    None,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_27(
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
                    None,
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_28(
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
                    upsert=None,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_29(
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_30(
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
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_31(
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
                    )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_32(
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
                        "XXdocument_idXX": identifier,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_33(
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
                        "DOCUMENT_ID": identifier,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_34(
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
                        "XXchunk_numberXX": section.chunk_number,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_35(
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
                        "CHUNK_NUMBER": section.chunk_number,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_36(
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
                        "XX$setOnInsertXX": {
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_37(
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
                        "$setoninsert": {
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_38(
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
                        "$SETONINSERT": {
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_39(
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
                            "XXdocument_idXX": identifier,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_40(
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
                            "DOCUMENT_ID": identifier,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_41(
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
                            "XXchunk_numberXX": section.chunk_number,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_42(
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
                            "CHUNK_NUMBER": section.chunk_number,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_43(
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
                            "XXpage_fromXX": section.page_from,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_44(
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
                            "PAGE_FROM": section.page_from,
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

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_45(
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
                            "XXpage_toXX": section.page_to,
                            "structured_data": document_payload,
                        }
                    },
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_46(
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
                            "PAGE_TO": section.page_to,
                            "structured_data": document_payload,
                        }
                    },
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_47(
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
                            "XXstructured_dataXX": document_payload,
                        }
                    },
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_48(
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
                            "STRUCTURED_DATA": document_payload,
                        }
                    },
                    upsert=True,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_49(
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
                    upsert=False,
                )
        except PyMongoError as exc:
            raise DatabaseError(
                "The structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_50(
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
                None
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_51(
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
                "XXThe structured document sections could not be stored locally.XX"
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_52(
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
                "the structured document sections could not be stored locally."
            ) from exc

    def xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_53(
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
                "THE STRUCTURED DOCUMENT SECTIONS COULD NOT BE STORED LOCALLY."
            ) from exc

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut)
    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_orig(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_1(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_2(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(None):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_3(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = None
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_4(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one(None)
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_5(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"XX_idXX": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_6(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_ID": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_7(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(None)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_8(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError(None) from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_9(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("XXThe document could not be read locally.XX") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_10(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("the document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_11(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("THE DOCUMENT COULD NOT BE READ LOCALLY.") from exc
        return _to_stored_document(payload) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_12(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if (payload is not None) and False else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_13(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if (payload is not None) or True else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_14(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(None) if payload is not None else None

    def xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_15(self, document_id: str) -> StoredDocument | None:
        """Return one stored document, or None for an unknown or invalid identifier."""
        if not ObjectId.is_valid(document_id):
            return None
        try:
            payload = self._collection.find_one({"_id": ObjectId(document_id)})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be read locally.") from exc
        return _to_stored_document(payload) if payload is None else None

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut)
    def get_all_documents(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_orig(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_1(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = None
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_2(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                None
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_3(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find(None).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_4(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.rfind({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_5(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("XXcreated_atXX", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_6(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("CREATED_AT", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_7(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("XX_idXX", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_8(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_ID", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_9(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(None) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_10(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError(None) from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_11(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("XXDocuments could not be read locally.XX") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_12(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("documents could not be read locally.") from exc

    def xǁMongoDocumentRepositoryǁget_all_documents__mutmut_13(self) -> list[StoredDocument]:
        """Return every stored document in deterministic creation order."""
        try:
            cursor = self._collection.find({}).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("DOCUMENTS COULD NOT BE READ LOCALLY.") from exc

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut)
    def update_document(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_orig(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_1(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_2(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(None):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_3(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = None
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_4(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(None)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_5(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = None
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_6(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode=None)
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_7(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="XXpythonXX")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_8(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="PYTHON")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_9(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = None
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_10(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["XXexpiry_dateXX"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_11(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["EXPIRY_DATE"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_12(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(None)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_13(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = None
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_14(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["XXissue_dateXX"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_15(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["ISSUE_DATE"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_16(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(None)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_17(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                None,
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_18(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                None,
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_19(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_20(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_21(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"XX_idXX": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_22(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_ID": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_23(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"XX$setXX": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_24(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$SET": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_25(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = None
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_26(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one(None)
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_27(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"XX_idXX": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_28(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_ID": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_29(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(None) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_30(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("XXThe document could not be updated locally.XX") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_31(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("the document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_32(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("THE DOCUMENT COULD NOT BE UPDATED LOCALLY.") from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_33(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if (stored is not None) and False else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_34(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if (stored is not None) or True else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_35(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(None) if stored is not None else None

    def xǁMongoDocumentRepositoryǁupdate_document__mutmut_36(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        """Replace validated document fields and preserve persistence metadata."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        payload = document.model_dump(mode="python")
        payload["expiry_date"] = _date_to_datetime(document.expiry_date)
        payload["issue_date"] = _date_to_datetime(document.issue_date)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": payload},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be updated locally.") from exc
        return _to_stored_document(stored) if stored is None else None

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut)
    def set_source_file_name(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_orig(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_1(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_2(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(None):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_3(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = None
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_4(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(None)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_5(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = None
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_6(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(None)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_7(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                None,
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_8(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                None,
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_9(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_10(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_11(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"XX_idXX": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_12(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_ID": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_13(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"XX$setXX": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_14(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$SET": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_15(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"XXsource_file_nameXX": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_16(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"SOURCE_FILE_NAME": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_17(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = None
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_18(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one(None)
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_19(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"XX_idXX": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_20(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_ID": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_21(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                None
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_22(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "XXThe document source reference could not be stored locally.XX"
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_23(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "the document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_24(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "THE DOCUMENT SOURCE REFERENCE COULD NOT BE STORED LOCALLY."
            ) from exc
        return _to_stored_document(stored) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_25(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if (stored is not None) and False else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_26(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if (stored is not None) or True else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_27(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(None) if stored is not None else None

    def xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_28(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        """Attach the safe processed-file name to one stored document."""
        if not ObjectId.is_valid(document_id):
            return None
        normalized_name = _validate_source_file_name(source_file_name)
        identifier = ObjectId(document_id)
        try:
            self._collection.update_one(
                {"_id": identifier},
                {"$set": {"source_file_name": normalized_name}},
            )
            stored = self._collection.find_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(
                "The document source reference could not be stored locally."
            ) from exc
        return _to_stored_document(stored) if stored is None else None

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut)
    def delete_document(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_orig(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_1(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_2(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(None):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_3(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = None
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_4(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(None)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_5(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = None
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_6(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one(None)
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_7(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"XX_idXX": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_8(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_ID": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_9(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is not None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_10(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_11(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many(None)
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_12(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"XXdocument_idXX": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_13(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"DOCUMENT_ID": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_14(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one(None)
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_15(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"XX_idXX": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_16(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_ID": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_17(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError(None) from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_18(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("XXThe document could not be deleted locally.XX") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_19(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("the document could not be deleted locally.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_20(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("THE DOCUMENT COULD NOT BE DELETED LOCALLY.") from exc
        return _to_stored_document(stored)

    def xǁMongoDocumentRepositoryǁdelete_document__mutmut_21(self, document_id: str) -> StoredDocument | None:
        """Delete one document and its structured sections, returning its snapshot."""
        if not ObjectId.is_valid(document_id):
            return None
        identifier = ObjectId(document_id)
        try:
            stored = self._collection.find_one({"_id": identifier})
            if stored is None:
                return None
            if self._sections_collection is not None:
                self._sections_collection.delete_many({"document_id": identifier})
            self._collection.delete_one({"_id": identifier})
        except PyMongoError as exc:
            raise DatabaseError("The document could not be deleted locally.") from exc
        return _to_stored_document(None)

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut)
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

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_orig(
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

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_1(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold <= 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_2(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 1:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_3(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError(None)
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_4(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("XXdays_threshold cannot be negativeXX")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_5(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("DAYS_THRESHOLD CANNOT BE NEGATIVE")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_6(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = None
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_7(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today and date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_8(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = None
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_9(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(None)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_10(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = None
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_11(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(None)
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_12(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date - timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_13(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=None))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_14(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold - 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_15(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 2))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_16(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = None
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_17(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"XXexpiry_dateXX": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_18(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"EXPIRY_DATE": {"$gte": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_19(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"XX$gteXX": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_20(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$GTE": start, "$lt": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_21(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "XX$ltXX": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_22(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$LT": end}}
        return self._find_documents(query)

    def xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_23(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        """Return documents expiring from today through the inclusive threshold."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")
        start_date = today or date.today()
        start = _date_to_datetime(start_date)
        end = _date_to_datetime(start_date + timedelta(days=days_threshold + 1))
        query = {"expiry_date": {"$gte": start, "$lt": end}}
        return self._find_documents(None)

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut)
    def get_documents_expiring_in_year(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_orig(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_1(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 and year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_2(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year <= 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_3(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 2 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_4(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year > date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_5(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError(None)
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_6(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("XXyear must be between 1 and 9998XX")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_7(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("YEAR MUST BE BETWEEN 1 AND 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_8(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = None
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_9(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(None)
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_10(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(None, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_11(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, None, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_12(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, None))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_13(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_14(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_15(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, ))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_16(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 2, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_17(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 2))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_18(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = None
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_19(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(None)
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_20(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(None, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_21(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, None, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_22(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, None))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_23(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_24(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_25(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, ))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_26(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year - 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_27(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 2, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_28(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 2, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_29(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 2))
        return self._find_documents({"expiry_date": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_30(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents(None)

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_31(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"XXexpiry_dateXX": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_32(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"EXPIRY_DATE": {"$gte": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_33(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"XX$gteXX": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_34(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$GTE": start, "$lt": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_35(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "XX$ltXX": end}})

    def xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_36(self, year: int) -> list[StoredDocument]:
        """Return documents with an expiry date inside the requested calendar year."""
        if year < 1 or year >= date.max.year:
            raise ValueError("year must be between 1 and 9998")
        start = _date_to_datetime(date(year, 1, 1))
        end = _date_to_datetime(date(year + 1, 1, 1))
        return self._find_documents({"expiry_date": {"$gte": start, "$LT": end}})

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut)
    def search_by_dynamic_field(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_orig(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_1(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) and not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_2(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_3(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_4(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(None):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_5(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                None
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_6(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "XXfield_key must be a dot-separated English snake_case pathXX"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_7(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated english snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_8(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "FIELD_KEY MUST BE A DOT-SEPARATED ENGLISH SNAKE_CASE PATH"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_9(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys(None)
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_10(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"XXvalueXX": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_11(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"VALUE": field_value})
        return self._find_documents({f"extracted_data.{field_key}": field_value})

    def xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_12(
        self, field_key: str, field_value: Any
    ) -> list[StoredDocument]:
        """Find documents by an exact value at a validated dynamic field path."""
        if not isinstance(field_key, str) or not _FIELD_PATH.fullmatch(field_key):
            raise ValueError(
                "field_key must be a dot-separated English snake_case path"
            )
        DocumentData._validate_mapping_keys({"value": field_value})
        return self._find_documents(None)

    @_mutmut_mutated(mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut)
    def _find_documents(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_orig(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_1(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = None
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_2(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                None
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_3(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(None).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_4(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.rfind(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_5(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("XXcreated_atXX", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_6(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("CREATED_AT", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_7(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("XX_idXX", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_8(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_ID", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_9(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(None) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("Documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_10(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError(None) from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_11(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("XXDocuments could not be queried locally.XX") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_12(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("documents could not be queried locally.") from exc

    def xǁMongoDocumentRepositoryǁ_find_documents__mutmut_13(self, query: dict[str, Any]) -> list[StoredDocument]:
        """Execute a query and convert results into domain records."""
        try:
            cursor = self._collection.find(query).sort(
                [("created_at", ASCENDING), ("_id", ASCENDING)]
            )
            return [_to_stored_document(payload) for payload in cursor]
        except PyMongoError as exc:
            raise DatabaseError("DOCUMENTS COULD NOT BE QUERIED LOCALLY.") from exc

mutants_xǁMongoDocumentRepositoryǁ__init____mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ__init____mutmut['xǁMongoDocumentRepositoryǁ__init____mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ__init____mutmut['xǁMongoDocumentRepositoryǁ__init____mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ__init____mutmut['xǁMongoDocumentRepositoryǁ__init____mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ__init____mutmut['xǁMongoDocumentRepositoryǁ__init____mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ__init____mutmut['xǁMongoDocumentRepositoryǁ__init____mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ__init____mutmut_5 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_24'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_25'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_26'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_27'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_28'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_29'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_30'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_31'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_32'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_33'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_34'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_35'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_36'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_37'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_38'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_39'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_40'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_41'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_42'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_43'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_44'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_45'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_46'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_47'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_48'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_49'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_49 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_50'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_50 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_51'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_51 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_52'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_52 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_53'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_53 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_54'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_54 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_55'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_55 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_56'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_56 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_57'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_57 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_58'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_58 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_59'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_59 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_60'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_60 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_61'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_61 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_62'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_62 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_63'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_63 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_64'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_64 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_65'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_65 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_66'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_66 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_67'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_67 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_68'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_68 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_69'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_69 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_70'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_70 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_71'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_71 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_72'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_72 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_73'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_73 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_74'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_74 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_75'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_75 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_76'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_76 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_77'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_77 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_78'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_78 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_79'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_79 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_80'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_80 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_81'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_81 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_82'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_82 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_83'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_83 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_84'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_84 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_85'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_85 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_86'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_86 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_87'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_87 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_88'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_88 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_89'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_89 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_90'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_90 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_91'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_91 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_92'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_92 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_93'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_93 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_94'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_94 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_95'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_95 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_96'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_96 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_97'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_97 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_98'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_98 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_99'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_99 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_100'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_100 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_101'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_101 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_102'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_102 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_103'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_103 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_104'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_104 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_105'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_105 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_106'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_106 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁconnect__mutmut['xǁMongoDocumentRepositoryǁconnect__mutmut_107'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁconnect__mutmut_107 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁclose__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁclose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁclose__mutmut['xǁMongoDocumentRepositoryǁclose__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁclose__mutmut_1 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_24'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_25'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_26'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_27'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_28'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_29'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_30'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_31'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_32'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_33'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_34'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_35'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_36'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_37'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_38'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_39'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_40'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_41'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_42'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_43'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_44'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_45'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_46'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_47'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_48'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_49'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_49 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_50'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_50 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_51'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_51 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_52'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_52 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_53'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_53 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_54'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_54 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_55'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_55 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_56'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_56 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_57'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_57 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_58'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_58 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁinsert_document__mutmut['xǁMongoDocumentRepositoryǁinsert_document__mutmut_59'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁinsert_document__mutmut_59 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_24'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_25'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_26'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_27'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_28'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_29'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_30'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_31'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_32'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_33'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_34'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_35'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_36'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_37'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_38'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_39'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_40'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_41'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_42'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_43'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_44'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_45'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_46'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_47'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_48'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_49'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_49 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_50'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_50 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_51'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_51 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_52'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_52 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut['xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_53'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupsert_document_sections__mutmut_53 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_document_by_id__mutmut['xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_document_by_id__mutmut_15 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_all_documents__mutmut['xǁMongoDocumentRepositoryǁget_all_documents__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_all_documents__mutmut_13 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_24'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_25'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_26'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_27'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_28'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_29'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_30'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_31'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_32'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_33'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_34'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_35'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁupdate_document__mutmut['xǁMongoDocumentRepositoryǁupdate_document__mutmut_36'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁupdate_document__mutmut_36 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_24'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_25'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_26'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_27'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁset_source_file_name__mutmut['xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_28'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁset_source_file_name__mutmut_28 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁdelete_document__mutmut['xǁMongoDocumentRepositoryǁdelete_document__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁdelete_document__mutmut_21 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut['xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_expiring_documents__mutmut_23 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_14'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_15'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_16'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_17'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_18'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_19'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_20'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_21'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_22'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_23'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_24'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_25'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_26'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_27'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_28'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_29'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_30'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_31'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_32'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_33'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_34'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_35'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut['xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_36'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁget_documents_expiring_in_year__mutmut_36 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut['xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁsearch_by_dynamic_field__mutmut_12 # type: ignore # mutmut generated

mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['_mutmut_orig'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_1'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_2'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_3'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_4'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_5'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_6'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_7'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_8'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_9'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_10'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_11'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_12'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMongoDocumentRepositoryǁ_find_documents__mutmut['xǁMongoDocumentRepositoryǁ_find_documents__mutmut_13'] = MongoDocumentRepository.xǁMongoDocumentRepositoryǁ_find_documents__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_local_mongodb_uri__mutmut)
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_orig(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_1(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = None
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_2(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(None)
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_3(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query and parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_4(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"} and parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_5(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None and parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_6(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None and parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_7(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"} and parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_8(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb" and parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_9(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme == "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_10(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "XXmongodbXX"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_11(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "MONGODB"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_12(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_13(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"XX127.0.0.1XX", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_14(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "XXlocalhostXX", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_15(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "LOCALHOST", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_16(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "XX::1XX"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_17(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_18(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_19(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_20(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"XXXX", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_21(uri: str) -> str:
    """Validate a credential-free loopback MongoDB URI."""
    parsed = urlsplit(uri)
    if (
        parsed.scheme != "mongodb"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "XX/XX"}
        or parsed.query
        or parsed.fragment
    ):
        raise DatabaseConfigurationError(
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_22(uri: str) -> str:
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
            None
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_23(uri: str) -> str:
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
            "XXMongoDB must use a loopback endpoint without credentials, options, XX"
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_24(uri: str) -> str:
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
            "mongodb must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_25(uri: str) -> str:
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
            "MONGODB MUST USE A LOOPBACK ENDPOINT WITHOUT CREDENTIALS, OPTIONS, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_26(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "XXor a path.XX"
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_27(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "OR A PATH."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_28(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = None
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_29(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            None
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_30(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "XXThe MongoDB endpoint has an invalid port.XX"
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_31(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "the mongodb endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_32(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "THE MONGODB ENDPOINT HAS AN INVALID PORT."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_33(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is not None:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_34(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            None
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_35(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "XXThe MongoDB endpoint must include an explicit port.XX"
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_36(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "the mongodb endpoint must include an explicit port."
        )
    return uri


def x__validate_local_mongodb_uri__mutmut_37(uri: str) -> str:
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
            "MongoDB must use a loopback endpoint without credentials, options, "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise DatabaseConfigurationError(
            "The MongoDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise DatabaseConfigurationError(
            "THE MONGODB ENDPOINT MUST INCLUDE AN EXPLICIT PORT."
        )
    return uri

mutants_x__validate_local_mongodb_uri__mutmut['_mutmut_orig'] = x__validate_local_mongodb_uri__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_1'] = x__validate_local_mongodb_uri__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_2'] = x__validate_local_mongodb_uri__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_3'] = x__validate_local_mongodb_uri__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_4'] = x__validate_local_mongodb_uri__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_5'] = x__validate_local_mongodb_uri__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_6'] = x__validate_local_mongodb_uri__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_7'] = x__validate_local_mongodb_uri__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_8'] = x__validate_local_mongodb_uri__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_9'] = x__validate_local_mongodb_uri__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_10'] = x__validate_local_mongodb_uri__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_11'] = x__validate_local_mongodb_uri__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_12'] = x__validate_local_mongodb_uri__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_13'] = x__validate_local_mongodb_uri__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_14'] = x__validate_local_mongodb_uri__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_15'] = x__validate_local_mongodb_uri__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_16'] = x__validate_local_mongodb_uri__mutmut_16 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_17'] = x__validate_local_mongodb_uri__mutmut_17 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_18'] = x__validate_local_mongodb_uri__mutmut_18 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_19'] = x__validate_local_mongodb_uri__mutmut_19 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_20'] = x__validate_local_mongodb_uri__mutmut_20 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_21'] = x__validate_local_mongodb_uri__mutmut_21 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_22'] = x__validate_local_mongodb_uri__mutmut_22 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_23'] = x__validate_local_mongodb_uri__mutmut_23 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_24'] = x__validate_local_mongodb_uri__mutmut_24 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_25'] = x__validate_local_mongodb_uri__mutmut_25 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_26'] = x__validate_local_mongodb_uri__mutmut_26 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_27'] = x__validate_local_mongodb_uri__mutmut_27 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_28'] = x__validate_local_mongodb_uri__mutmut_28 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_29'] = x__validate_local_mongodb_uri__mutmut_29 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_30'] = x__validate_local_mongodb_uri__mutmut_30 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_31'] = x__validate_local_mongodb_uri__mutmut_31 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_32'] = x__validate_local_mongodb_uri__mutmut_32 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_33'] = x__validate_local_mongodb_uri__mutmut_33 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_34'] = x__validate_local_mongodb_uri__mutmut_34 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_35'] = x__validate_local_mongodb_uri__mutmut_35 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_36'] = x__validate_local_mongodb_uri__mutmut_36 # type: ignore # mutmut generated
mutants_x__validate_local_mongodb_uri__mutmut['x__validate_local_mongodb_uri__mutmut_37'] = x__validate_local_mongodb_uri__mutmut_37 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_mongodb_name__mutmut)
def _validate_mongodb_name(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_orig(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_1(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value and not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_2(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if value or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_3(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_4(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(None, value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_5(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-Za-z0-9_-]+", None):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_6(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_7(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-Za-z0-9_-]+", ):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_8(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"XX[A-Za-z0-9_-]+XX", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_9(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[a-za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_10(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-ZA-Z0-9_-]+", value):
        raise DatabaseConfigurationError(
            f"{label} must contain only letters, numbers, underscores, or hyphens"
        )


def x__validate_mongodb_name__mutmut_11(value: str, *, label: str) -> None:
    """Validate a database or collection name."""
    if not value or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise DatabaseConfigurationError(
            None
        )

mutants_x__validate_mongodb_name__mutmut['_mutmut_orig'] = x__validate_mongodb_name__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_1'] = x__validate_mongodb_name__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_2'] = x__validate_mongodb_name__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_3'] = x__validate_mongodb_name__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_4'] = x__validate_mongodb_name__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_5'] = x__validate_mongodb_name__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_6'] = x__validate_mongodb_name__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_7'] = x__validate_mongodb_name__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_8'] = x__validate_mongodb_name__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_9'] = x__validate_mongodb_name__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_10'] = x__validate_mongodb_name__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_mongodb_name__mutmut['x__validate_mongodb_name__mutmut_11'] = x__validate_mongodb_name__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_file_hash__mutmut)
def _validate_file_hash(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_orig(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_1(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = None
    if not _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_2(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().upper()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_3(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_4(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(None):
        raise ValueError("file_hash must be a 64-character SHA-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_5(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError(None)
    return normalized


def x__validate_file_hash__mutmut_6(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("XXfile_hash must be a 64-character SHA-256 hexadecimal digestXX")
    return normalized


def x__validate_file_hash__mutmut_7(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("file_hash must be a 64-character sha-256 hexadecimal digest")
    return normalized


def x__validate_file_hash__mutmut_8(value: str) -> str:
    """Normalize and validate a SHA-256 file hash."""
    normalized = value.strip().lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError("FILE_HASH MUST BE A 64-CHARACTER SHA-256 HEXADECIMAL DIGEST")
    return normalized

mutants_x__validate_file_hash__mutmut['_mutmut_orig'] = x__validate_file_hash__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_1'] = x__validate_file_hash__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_2'] = x__validate_file_hash__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_3'] = x__validate_file_hash__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_4'] = x__validate_file_hash__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_5'] = x__validate_file_hash__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_6'] = x__validate_file_hash__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_7'] = x__validate_file_hash__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_file_hash__mutmut['x__validate_file_hash__mutmut_8'] = x__validate_file_hash__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_source_file_name__mutmut)
def _validate_source_file_name(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_orig(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_1(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_2(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError(None)
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_3(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("XXsource_file_name must be a file nameXX")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_4(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("SOURCE_FILE_NAME MUST BE A FILE NAME")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_5(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = None
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_6(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized and "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_7(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized and "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_8(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."} and Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_9(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized and normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_10(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_11(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized not in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_12(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {"XX.XX", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_13(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", "XX..XX"}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_14(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(None).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_15(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name == normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_16(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "XX/XX" in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_17(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" not in normalized
        or "\\" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_18(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "XX\\XX" in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_19(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" not in normalized
    ):
        raise ValueError("source_file_name must not contain a directory path")
    return normalized


def x__validate_source_file_name__mutmut_20(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError(None)
    return normalized


def x__validate_source_file_name__mutmut_21(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("XXsource_file_name must not contain a directory pathXX")
    return normalized


def x__validate_source_file_name__mutmut_22(value: str) -> str:
    """Require one plain file name without directory traversal components."""
    if not isinstance(value, str):
        raise ValueError("source_file_name must be a file name")
    normalized = value.strip()
    if (
        not normalized
        or normalized in {".", ".."}
        or Path(normalized).name != normalized
        or "/" in normalized
        or "\\" in normalized
    ):
        raise ValueError("SOURCE_FILE_NAME MUST NOT CONTAIN A DIRECTORY PATH")
    return normalized

mutants_x__validate_source_file_name__mutmut['_mutmut_orig'] = x__validate_source_file_name__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_1'] = x__validate_source_file_name__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_2'] = x__validate_source_file_name__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_3'] = x__validate_source_file_name__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_4'] = x__validate_source_file_name__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_5'] = x__validate_source_file_name__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_6'] = x__validate_source_file_name__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_7'] = x__validate_source_file_name__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_8'] = x__validate_source_file_name__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_9'] = x__validate_source_file_name__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_10'] = x__validate_source_file_name__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_11'] = x__validate_source_file_name__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_12'] = x__validate_source_file_name__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_13'] = x__validate_source_file_name__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_14'] = x__validate_source_file_name__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_15'] = x__validate_source_file_name__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_16'] = x__validate_source_file_name__mutmut_16 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_17'] = x__validate_source_file_name__mutmut_17 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_18'] = x__validate_source_file_name__mutmut_18 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_19'] = x__validate_source_file_name__mutmut_19 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_20'] = x__validate_source_file_name__mutmut_20 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_21'] = x__validate_source_file_name__mutmut_21 # type: ignore # mutmut generated
mutants_x__validate_source_file_name__mutmut['x__validate_source_file_name__mutmut_22'] = x__validate_source_file_name__mutmut_22 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__date_to_datetime__mutmut)
def _date_to_datetime(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, time.min, tzinfo=UTC)


def x__date_to_datetime__mutmut_orig(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, time.min, tzinfo=UTC)


def x__date_to_datetime__mutmut_1(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is not None:
        return None
    return datetime.combine(value, time.min, tzinfo=UTC)


def x__date_to_datetime__mutmut_2(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(None, time.min, tzinfo=UTC)


def x__date_to_datetime__mutmut_3(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, None, tzinfo=UTC)


def x__date_to_datetime__mutmut_4(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, time.min, tzinfo=None)


def x__date_to_datetime__mutmut_5(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(time.min, tzinfo=UTC)


def x__date_to_datetime__mutmut_6(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, tzinfo=UTC)


def x__date_to_datetime__mutmut_7(value: date | None) -> datetime | None:
    """Convert a date to a UTC midnight datetime."""
    if value is None:
        return None
    return datetime.combine(value, time.min, )

mutants_x__date_to_datetime__mutmut['_mutmut_orig'] = x__date_to_datetime__mutmut_orig # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_1'] = x__date_to_datetime__mutmut_1 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_2'] = x__date_to_datetime__mutmut_2 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_3'] = x__date_to_datetime__mutmut_3 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_4'] = x__date_to_datetime__mutmut_4 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_5'] = x__date_to_datetime__mutmut_5 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_6'] = x__date_to_datetime__mutmut_6 # type: ignore # mutmut generated
mutants_x__date_to_datetime__mutmut['x__date_to_datetime__mutmut_7'] = x__date_to_datetime__mutmut_7 # type: ignore # mutmut generated
mutants_x__normalize_datetime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__normalize_datetime__mutmut)
def _normalize_datetime(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError("created_at must include timezone information")
    return value.astimezone(UTC)


def x__normalize_datetime__mutmut_orig(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError("created_at must include timezone information")
    return value.astimezone(UTC)


def x__normalize_datetime__mutmut_1(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is not None:
        raise ValueError("created_at must include timezone information")
    return value.astimezone(UTC)


def x__normalize_datetime__mutmut_2(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError(None)
    return value.astimezone(UTC)


def x__normalize_datetime__mutmut_3(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError("XXcreated_at must include timezone informationXX")
    return value.astimezone(UTC)


def x__normalize_datetime__mutmut_4(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError("CREATED_AT MUST INCLUDE TIMEZONE INFORMATION")
    return value.astimezone(UTC)


def x__normalize_datetime__mutmut_5(value: datetime) -> datetime:
    """Require timezone information and normalize a datetime to UTC."""
    if value.tzinfo is None:
        raise ValueError("created_at must include timezone information")
    return value.astimezone(None)

mutants_x__normalize_datetime__mutmut['_mutmut_orig'] = x__normalize_datetime__mutmut_orig # type: ignore # mutmut generated
mutants_x__normalize_datetime__mutmut['x__normalize_datetime__mutmut_1'] = x__normalize_datetime__mutmut_1 # type: ignore # mutmut generated
mutants_x__normalize_datetime__mutmut['x__normalize_datetime__mutmut_2'] = x__normalize_datetime__mutmut_2 # type: ignore # mutmut generated
mutants_x__normalize_datetime__mutmut['x__normalize_datetime__mutmut_3'] = x__normalize_datetime__mutmut_3 # type: ignore # mutmut generated
mutants_x__normalize_datetime__mutmut['x__normalize_datetime__mutmut_4'] = x__normalize_datetime__mutmut_4 # type: ignore # mutmut generated
mutants_x__normalize_datetime__mutmut['x__normalize_datetime__mutmut_5'] = x__normalize_datetime__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_stored_document__mutmut)
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_orig(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_1(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = None
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_2(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "XXdocument_typeXX",
                "summary",
                "expiry_date",
                "issue_date",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_3(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "DOCUMENT_TYPE",
                "summary",
                "expiry_date",
                "issue_date",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_4(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "XXsummaryXX",
                "expiry_date",
                "issue_date",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_5(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "SUMMARY",
                "expiry_date",
                "issue_date",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_6(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "XXexpiry_dateXX",
                "issue_date",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_7(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "EXPIRY_DATE",
                "issue_date",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_8(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "expiry_date",
                "XXissue_dateXX",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_9(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "expiry_date",
                "ISSUE_DATE",
                "extracted_data",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_10(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "expiry_date",
                "issue_date",
                "XXextracted_dataXX",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_11(payload: dict[str, Any]) -> StoredDocument:
    """Convert one database payload into a validated stored document."""
    try:
        document_payload = {
            key: payload[key]
            for key in (
                "document_type",
                "summary",
                "expiry_date",
                "issue_date",
                "EXTRACTED_DATA",
            )
        }
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_12(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = None
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_13(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["XXnotification_days_beforeXX"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_14(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["NOTIFICATION_DAYS_BEFORE"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_15(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            None
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_16(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "XXnotification_days_beforeXX"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_17(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "NOTIFICATION_DAYS_BEFORE"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_18(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = None
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_19(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["XXcreated_atXX"]
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_20(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["CREATED_AT"]
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_21(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_22(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError(None)
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_23(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("XXcreated_at must be a datetimeXX")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_24(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("CREATED_AT MUST BE A DATETIME")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_25(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is not None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_26(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = None
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_27(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=None)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_28(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = None
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_29(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(None)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_30(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=None,
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_31(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=None,
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_32(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=None,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_33(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            created_at=None,
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_34(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=None,
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_35(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_36(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_37(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_38(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_39(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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


def x__to_stored_document__mutmut_40(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(None),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_41(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["XX_idXX"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_42(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_ID"]),
            file_hash=_validate_file_hash(payload["file_hash"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_43(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(None),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_44(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["XXfile_hashXX"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_45(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
        created_at = payload["created_at"]
        if not isinstance(created_at, datetime):
            raise TypeError("created_at must be a datetime")
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        document = DocumentData.model_validate(document_payload)
        return StoredDocument(
            id=str(payload["_id"]),
            file_hash=_validate_file_hash(payload["FILE_HASH"]),
            document=document,
            created_at=created_at.astimezone(UTC),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_46(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            created_at=created_at.astimezone(None),
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_47(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if (payload.get("source_file_name") is not None) and False
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_48(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if (payload.get("source_file_name") is not None) or True
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_49(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(None)
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_50(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["XXsource_file_nameXX"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_51(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["SOURCE_FILE_NAME"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_52(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get(None) is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_53(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("XXsource_file_nameXX") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_54(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("SOURCE_FILE_NAME") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_55(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("The stored document data is invalid.") from exc


def x__to_stored_document__mutmut_56(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError(None) from exc


def x__to_stored_document__mutmut_57(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("XXThe stored document data is invalid.XX") from exc


def x__to_stored_document__mutmut_58(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("the stored document data is invalid.") from exc


def x__to_stored_document__mutmut_59(payload: dict[str, Any]) -> StoredDocument:
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
        document_payload["notification_days_before"] = payload.get(
            "notification_days_before"
        )
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
            source_file_name=(
                _validate_source_file_name(payload["source_file_name"])
                if payload.get("source_file_name") is not None
                else None
            ),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise DatabaseError("THE STORED DOCUMENT DATA IS INVALID.") from exc

mutants_x__to_stored_document__mutmut['_mutmut_orig'] = x__to_stored_document__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_1'] = x__to_stored_document__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_2'] = x__to_stored_document__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_3'] = x__to_stored_document__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_4'] = x__to_stored_document__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_5'] = x__to_stored_document__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_6'] = x__to_stored_document__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_7'] = x__to_stored_document__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_8'] = x__to_stored_document__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_9'] = x__to_stored_document__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_10'] = x__to_stored_document__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_11'] = x__to_stored_document__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_12'] = x__to_stored_document__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_13'] = x__to_stored_document__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_14'] = x__to_stored_document__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_15'] = x__to_stored_document__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_16'] = x__to_stored_document__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_17'] = x__to_stored_document__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_18'] = x__to_stored_document__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_19'] = x__to_stored_document__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_20'] = x__to_stored_document__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_21'] = x__to_stored_document__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_22'] = x__to_stored_document__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_23'] = x__to_stored_document__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_24'] = x__to_stored_document__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_25'] = x__to_stored_document__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_26'] = x__to_stored_document__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_27'] = x__to_stored_document__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_28'] = x__to_stored_document__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_29'] = x__to_stored_document__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_30'] = x__to_stored_document__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_31'] = x__to_stored_document__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_32'] = x__to_stored_document__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_33'] = x__to_stored_document__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_34'] = x__to_stored_document__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_35'] = x__to_stored_document__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_36'] = x__to_stored_document__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_37'] = x__to_stored_document__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_38'] = x__to_stored_document__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_39'] = x__to_stored_document__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_40'] = x__to_stored_document__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_41'] = x__to_stored_document__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_42'] = x__to_stored_document__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_43'] = x__to_stored_document__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_44'] = x__to_stored_document__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_45'] = x__to_stored_document__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_46'] = x__to_stored_document__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_47'] = x__to_stored_document__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_48'] = x__to_stored_document__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_49'] = x__to_stored_document__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_50'] = x__to_stored_document__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_51'] = x__to_stored_document__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_52'] = x__to_stored_document__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_53'] = x__to_stored_document__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_54'] = x__to_stored_document__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_55'] = x__to_stored_document__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_56'] = x__to_stored_document__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_57'] = x__to_stored_document__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_58'] = x__to_stored_document__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_stored_document__mutmut['x__to_stored_document__mutmut_59'] = x__to_stored_document__mutmut_59 # type: ignore # mutmut generated
