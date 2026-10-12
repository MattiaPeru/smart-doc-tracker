"""Validated models for local document retrieval and answers."""

from __future__ import annotations

from dataclasses import dataclass
from html import unescape

from pydantic import BaseModel, ConfigDict, Field, field_validator


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True, slots=True)
class RetrievedDocumentChunk:
    """One semantically retrieved local document fragment."""

    document_id: str
    content: str
    source: str
    distance: float
    page: int | None = None


@dataclass(frozen=True, slots=True)
class IndexedDocumentFragment:
    """One persisted local fragment belonging to a specific document."""

    fragment_id: str
    content: str
    source: str
    page: int | None = None


@dataclass(frozen=True, slots=True)
class ConversationTurn:
    """One bounded in-memory exchange used to resolve follow-up questions."""

    question: str
    answer: str
    document_ids: tuple[str, ...]


class AnswerEvidence(BaseModel):
    """One short verbatim quote supporting a concrete answer claim."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    document_id: str = Field(min_length=1, max_length=200)
    quote: str = Field(min_length=1, max_length=500)
    source: str = Field(min_length=1, max_length=100)
    page: int | None = Field(default=None, ge=1)

    @field_validator("quote", mode="before")
    @classmethod
    def decode_quote_entities(cls, value: object) -> object:
        """Decode text entities before literal evidence validation and display."""
        return unescape(value) if isinstance(value, str) else value


class AnswerClaim(BaseModel):
    """One concrete conclusion with bounded supporting evidence."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    claim: str = Field(min_length=1, max_length=1_000)
    evidence: list[AnswerEvidence] = Field(min_length=1, max_length=5)

    @field_validator("claim", mode="before")
    @classmethod
    def decode_claim_entities(cls, value: object) -> object:
        """Decode harmless text entities for safe text-only rendering."""
        return unescape(value) if isinstance(value, str) else value


class DocumentAnswer(BaseModel):
    """Grounded answer produced from retrieved local document fragments."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    answer: str = Field(min_length=1, max_length=8_000)
    claims: list[AnswerClaim] = Field(default_factory=list, max_length=10)
    document_ids: list[str] = Field(default_factory=list, max_length=50)
    insufficient_information: bool = False

    @field_validator("answer", mode="before")
    @classmethod
    def decode_answer_entities(cls, value: object) -> object:
        """Decode text entities while leaving browser escaping to textContent."""
        return unescape(value) if isinstance(value, str) else value
