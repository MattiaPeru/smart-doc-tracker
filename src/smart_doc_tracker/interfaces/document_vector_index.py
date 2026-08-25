"""Persistence interface for local document vector search."""

from __future__ import annotations

from typing import Protocol

from ..models.document import DocumentData
from ..models.rag import RetrievedDocumentChunk


class DocumentVectorIndex(Protocol):
    """Store and retrieve sensitive document content in a local vector index."""

    def upsert_document(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace the indexed fragments belonging to one document."""
        ...

    def query(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Return the fragments most semantically relevant to a question."""
        ...
