"""Parsing interface for extracted document text."""

from __future__ import annotations

from typing import Protocol

from ..models.document import DocumentData


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class StructuredDocumentParser(Protocol):
    """Convert extracted text into validated document data."""

    def parse(self, raw_text: str) -> DocumentData:
        """Convert raw text into validated document data."""
        ...
