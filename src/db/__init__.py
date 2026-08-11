"""Local persistence and document queries."""

from db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    DocumentInsertResult,
    StoredDocument,
    MongoDocumentRepository,
)

__all__ = [
    "DatabaseConfigurationError",
    "DatabaseError",
    "DocumentInsertResult",
    "MongoDocumentRepository",
    "StoredDocument",
]
