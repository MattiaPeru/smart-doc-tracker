"""Hybrid document envelope and dynamic payload model."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime
from math import isfinite
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

_SNAKE_CASE_KEY = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")
_DATE_FORMATS = ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d")
_MISSING_DATE_VALUES = frozenset(
    {"", "none", "null", "n/a", "unknown", "not_applicable"}
)
_INCOMPLETE_CONTAINER_PLACEHOLDER = re.compile(r"^[\[{]+$")


class DocumentData(BaseModel):
    """Validated common metadata plus document-specific extracted values."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    document_type: str = Field(min_length=1, max_length=100)
    summary: str = Field(min_length=1, max_length=1000)
    expiry_date: date | None
    issue_date: date | None
    notification_days_before: int | None = Field(default=None, ge=0, le=3_650)
    extracted_data: dict[str, Any]

    @field_validator("document_type")
    @classmethod
    def normalize_document_type(cls, value: str) -> str:
        """Normalize the document category to a stable snake_case value."""
        normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
        if not normalized:
            raise ValueError("document_type must contain letters or numbers")
        return normalized

    @field_validator("expiry_date", "issue_date", mode="before")
    @classmethod
    def normalize_date(cls, value: object) -> object:
        """Accept common unambiguous date forms and normalize them to a date."""
        if value is None or isinstance(value, date):
            return value
        if not isinstance(value, str):
            raise ValueError("date values must be strings or null")

        candidate = value.strip()
        if candidate.lower() in _MISSING_DATE_VALUES:
            return None
        for date_format in _DATE_FORMATS:
            try:
                return datetime.strptime(candidate, date_format).date()
            except ValueError:
                continue
        raise ValueError(
            "date values must use YYYY-MM-DD or a supported numeric format"
        )

    @field_validator("extracted_data")
    @classmethod
    def validate_dynamic_keys(cls, value: dict[str, Any]) -> dict[str, Any]:
        """Require stable snake_case keys at every level of the dynamic payload."""
        cls._validate_mapping_keys(value)
        return value

    @classmethod
    def _validate_mapping_keys(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    def ensure_complete_dynamic_values(self) -> None:
        """Reject literal opening delimiters emitted as incomplete containers."""
        self._ensure_complete_value(self.extracted_data)

    @classmethod
    def _ensure_complete_value(cls, value: object) -> None:
        """Validate dynamic values without disclosing their contents in errors."""
        if isinstance(value, dict):
            for nested_value in value.values():
                cls._ensure_complete_value(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._ensure_complete_value(item)
        elif isinstance(value, str) and _INCOMPLETE_CONTAINER_PLACEHOLDER.fullmatch(
            value.strip()
        ):
            raise ValueError(
                "extracted_data contains an incomplete JSON container placeholder"
            )


@dataclass(frozen=True, slots=True)
class StructuredDocumentSection:
    """Validated partial document data associated with a PDF page range."""

    chunk_number: int
    page_from: int
    page_to: int
    document: DocumentData

    def __post_init__(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")


@dataclass(frozen=True, slots=True)
class ParsedLongDocument:
    """Consolidated document data and its page-aware structured sections."""

    document: DocumentData
    sections: tuple[StructuredDocumentSection, ...]

    def __post_init__(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError("A parsed long document must contain sections")
