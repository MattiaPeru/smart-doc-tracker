"""Validated models for local document retrieval and answers."""

from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, Field


@dataclass(frozen=True, slots=True)
class RetrievedDocumentChunk:
    """One semantically retrieved local document fragment."""

    document_id: str
    content: str
    source: str
    distance: float


@dataclass(frozen=True, slots=True)
class IndexedDocumentFragment:
    """One persisted local fragment belonging to a specific document."""

    fragment_id: str
    content: str
    source: str


class DocumentAnswer(BaseModel):
    """Grounded answer produced from retrieved local document fragments."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    answer: str = Field(min_length=1, max_length=8_000)
    document_ids: list[str] = Field(default_factory=list, max_length=50)
