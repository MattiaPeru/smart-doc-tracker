"""Persistence interface for local document vector search."""

from __future__ import annotations

from typing import Any, Protocol

from ..models.document import DocumentData
from ..models.rag import IndexedDocumentFragment, RetrievedDocumentChunk


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDocumentVectorIndexǁquery__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁDocumentVectorIndexǁquery__mutmut)
    def query(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Return the fragments most semantically relevant to a question."""
        ...

    def xǁDocumentVectorIndexǁquery__mutmut_orig(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Return the fragments most semantically relevant to a question."""
        ...

    def xǁDocumentVectorIndexǁquery__mutmut_1(self, question: str, *, limit: int = 6) -> list[RetrievedDocumentChunk]:
        """Return the fragments most semantically relevant to a question."""
        ...

    def get_document_fragments(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return every stored content fragment for one document."""
        ...

    def snapshot_document(self, document_id: str) -> dict[str, Any]:
        """Return an opaque restorable snapshot for one document."""
        ...

    def restore_document(self, snapshot: dict[str, Any]) -> None:
        """Restore a previously captured document snapshot."""
        ...

    def update_document_data(self, document_id: str, document: DocumentData) -> None:
        """Update structured fragments while preserving raw-text fragments."""
        ...

    def delete_document(self, document_id: str) -> None:
        """Delete every vector fragment belonging to one document."""
        ...

mutants_xǁDocumentVectorIndexǁquery__mutmut['_mutmut_orig'] = DocumentVectorIndex.xǁDocumentVectorIndexǁquery__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentVectorIndexǁquery__mutmut['xǁDocumentVectorIndexǁquery__mutmut_1'] = DocumentVectorIndex.xǁDocumentVectorIndexǁquery__mutmut_1 # type: ignore # mutmut generated
