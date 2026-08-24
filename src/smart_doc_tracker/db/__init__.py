"""Local persistence and document queries."""

from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    DocumentInsertResult,
    MongoDocumentRepository,
    StoredDocument,
)

__all__ = [
    "DatabaseConfigurationError",
    "DatabaseError",
    "DocumentInsertResult",
    "MongoDocumentRepository",
    "StoredDocument",
]
