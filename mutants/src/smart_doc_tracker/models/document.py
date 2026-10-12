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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentDataǁensure_complete_dynamic_values__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut: MutantDict = {}  # type: ignore


class DocumentData(BaseModel):
    """Validated common metadata plus document-specific extracted values."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    document_type: str = Field(min_length=1, max_length=100)
    summary: str = Field(min_length=1, max_length=1000)
    expiry_date: date | None = None
    issue_date: date | None = None
    notification_days_before: int | None = Field(default=None, ge=0, le=3_650)
    extracted_data: dict[str, Any] = Field(default_factory=dict)

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
    @_mutmut_mutated(mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut, is_classmethod = True)
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

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_orig(cls, value: object) -> None:
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

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_1(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) and not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_2(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_3(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_4(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(None):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_5(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError(None)
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_6(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("XXextracted_data keys must use English snake_caseXX")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_7(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use english snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_8(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("EXTRACTED_DATA KEYS MUST USE ENGLISH SNAKE_CASE")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_9(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(None)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_10(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(None)
        elif isinstance(value, float) and not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_11(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) or not isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_12(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and isfinite(value):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_13(cls, value: object) -> None:
        """Recursively validate dynamic keys and JSON-compatible values."""
        if isinstance(value, dict):
            for key, nested_value in value.items():
                if not isinstance(key, str) or not _SNAKE_CASE_KEY.fullmatch(key):
                    raise ValueError("extracted_data keys must use English snake_case")
                cls._validate_mapping_keys(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._validate_mapping_keys(item)
        elif isinstance(value, float) and not isfinite(None):
            raise ValueError("extracted_data numbers must be finite")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_14(cls, value: object) -> None:
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
            raise ValueError(None)
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_15(cls, value: object) -> None:
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
            raise ValueError("XXextracted_data numbers must be finiteXX")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_16(cls, value: object) -> None:
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
            raise ValueError("EXTRACTED_DATA NUMBERS MUST BE FINITE")
        elif value is not None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_17(cls, value: object) -> None:
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
        elif value is not None or not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_18(cls, value: object) -> None:
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
        elif value is None and not isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_19(cls, value: object) -> None:
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
        elif value is not None and isinstance(value, (str, int, float, bool)):
            raise ValueError("extracted_data values must be JSON-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_20(cls, value: object) -> None:
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
            raise ValueError(None)

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_21(cls, value: object) -> None:
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
            raise ValueError("XXextracted_data values must be JSON-compatibleXX")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_22(cls, value: object) -> None:
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
            raise ValueError("extracted_data values must be json-compatible")

    @classmethod
    def xǁDocumentDataǁ_validate_mapping_keys__mutmut_23(cls, value: object) -> None:
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
            raise ValueError("EXTRACTED_DATA VALUES MUST BE JSON-COMPATIBLE")

    @_mutmut_mutated(mutants_xǁDocumentDataǁensure_complete_dynamic_values__mutmut)
    def ensure_complete_dynamic_values(self) -> None:
        """Reject literal opening delimiters emitted as incomplete containers."""
        self._ensure_complete_value(self.extracted_data)

    def xǁDocumentDataǁensure_complete_dynamic_values__mutmut_orig(self) -> None:
        """Reject literal opening delimiters emitted as incomplete containers."""
        self._ensure_complete_value(self.extracted_data)

    def xǁDocumentDataǁensure_complete_dynamic_values__mutmut_1(self) -> None:
        """Reject literal opening delimiters emitted as incomplete containers."""
        self._ensure_complete_value(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut, is_classmethod = True)
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

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_orig(cls, value: object) -> None:
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

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_1(cls, value: object) -> None:
        """Validate dynamic values without disclosing their contents in errors."""
        if isinstance(value, dict):
            for nested_value in value.values():
                cls._ensure_complete_value(None)
        elif isinstance(value, list):
            for item in value:
                cls._ensure_complete_value(item)
        elif isinstance(value, str) and _INCOMPLETE_CONTAINER_PLACEHOLDER.fullmatch(
            value.strip()
        ):
            raise ValueError(
                "extracted_data contains an incomplete JSON container placeholder"
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_2(cls, value: object) -> None:
        """Validate dynamic values without disclosing their contents in errors."""
        if isinstance(value, dict):
            for nested_value in value.values():
                cls._ensure_complete_value(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._ensure_complete_value(None)
        elif isinstance(value, str) and _INCOMPLETE_CONTAINER_PLACEHOLDER.fullmatch(
            value.strip()
        ):
            raise ValueError(
                "extracted_data contains an incomplete JSON container placeholder"
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_3(cls, value: object) -> None:
        """Validate dynamic values without disclosing their contents in errors."""
        if isinstance(value, dict):
            for nested_value in value.values():
                cls._ensure_complete_value(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._ensure_complete_value(item)
        elif isinstance(value, str) or _INCOMPLETE_CONTAINER_PLACEHOLDER.fullmatch(
            value.strip()
        ):
            raise ValueError(
                "extracted_data contains an incomplete JSON container placeholder"
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_4(cls, value: object) -> None:
        """Validate dynamic values without disclosing their contents in errors."""
        if isinstance(value, dict):
            for nested_value in value.values():
                cls._ensure_complete_value(nested_value)
        elif isinstance(value, list):
            for item in value:
                cls._ensure_complete_value(item)
        elif isinstance(value, str) and _INCOMPLETE_CONTAINER_PLACEHOLDER.fullmatch(
            None
        ):
            raise ValueError(
                "extracted_data contains an incomplete JSON container placeholder"
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_5(cls, value: object) -> None:
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
                None
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_6(cls, value: object) -> None:
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
                "XXextracted_data contains an incomplete JSON container placeholderXX"
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_7(cls, value: object) -> None:
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
                "extracted_data contains an incomplete json container placeholder"
            )

    @classmethod
    def xǁDocumentDataǁ_ensure_complete_value__mutmut_8(cls, value: object) -> None:
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
                "EXTRACTED_DATA CONTAINS AN INCOMPLETE JSON CONTAINER PLACEHOLDER"
            )

mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['_mutmut_orig'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_1'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_2'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_3'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_4'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_5'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_6'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_7'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_8'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_9'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_10'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_11'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_12'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_13'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_14'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_15'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_16'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_17'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_18'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_19'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_20'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_21'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_22'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_validate_mapping_keys__mutmut['xǁDocumentDataǁ_validate_mapping_keys__mutmut_23'] = DocumentData.xǁDocumentDataǁ_validate_mapping_keys__mutmut_23 # type: ignore # mutmut generated

mutants_xǁDocumentDataǁensure_complete_dynamic_values__mutmut['_mutmut_orig'] = DocumentData.xǁDocumentDataǁensure_complete_dynamic_values__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentDataǁensure_complete_dynamic_values__mutmut['xǁDocumentDataǁensure_complete_dynamic_values__mutmut_1'] = DocumentData.xǁDocumentDataǁensure_complete_dynamic_values__mutmut_1 # type: ignore # mutmut generated

mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['_mutmut_orig'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_1'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_2'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_3'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_4'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_5'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_6'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_7'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentDataǁ_ensure_complete_value__mutmut['xǁDocumentDataǁ_ensure_complete_value__mutmut_8'] = DocumentData.xǁDocumentDataǁ_ensure_complete_value__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut: MutantDict = {}  # type: ignore


@dataclass(frozen=True, slots=True)
class StructuredDocumentSection:
    """Validated partial document data associated with a PDF page range."""

    chunk_number: int
    page_from: int
    page_to: int
    document: DocumentData

    @_mutmut_mutated(mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut)
    def __post_init__(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_orig(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_1(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number < 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_2(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 1:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_3(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError(None)
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_4(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("XXchunk_number must be positiveXX")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_5(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("CHUNK_NUMBER MUST BE POSITIVE")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_6(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 and self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_7(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from < 0 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_8(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 1 or self.page_to < self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_9(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to <= self.page_from:
            raise ValueError("The section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_10(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError(None)

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_11(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("XXThe section page range is invalidXX")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_12(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("the section page range is invalid")

    def xǁStructuredDocumentSectionǁ__post_init____mutmut_13(self) -> None:
        """Validate chunk numbering and the associated page range."""
        if self.chunk_number <= 0:
            raise ValueError("chunk_number must be positive")
        if self.page_from <= 0 or self.page_to < self.page_from:
            raise ValueError("THE SECTION PAGE RANGE IS INVALID")

mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['_mutmut_orig'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_1'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_2'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_3'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_4'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_5'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_6'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_7'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_8'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_9'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_10'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_11'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_12'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁStructuredDocumentSectionǁ__post_init____mutmut['xǁStructuredDocumentSectionǁ__post_init____mutmut_13'] = StructuredDocumentSection.xǁStructuredDocumentSectionǁ__post_init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁParsedLongDocumentǁ__post_init____mutmut: MutantDict = {}  # type: ignore


@dataclass(frozen=True, slots=True)
class ParsedLongDocument:
    """Consolidated document data and its page-aware structured sections."""

    document: DocumentData
    sections: tuple[StructuredDocumentSection, ...]

    @_mutmut_mutated(mutants_xǁParsedLongDocumentǁ__post_init____mutmut)
    def __post_init__(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError("A parsed long document must contain sections")

    def xǁParsedLongDocumentǁ__post_init____mutmut_orig(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError("A parsed long document must contain sections")

    def xǁParsedLongDocumentǁ__post_init____mutmut_1(self) -> None:
        """Require at least one structured section in a parsed document."""
        if self.sections:
            raise ValueError("A parsed long document must contain sections")

    def xǁParsedLongDocumentǁ__post_init____mutmut_2(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError(None)

    def xǁParsedLongDocumentǁ__post_init____mutmut_3(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError("XXA parsed long document must contain sectionsXX")

    def xǁParsedLongDocumentǁ__post_init____mutmut_4(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError("a parsed long document must contain sections")

    def xǁParsedLongDocumentǁ__post_init____mutmut_5(self) -> None:
        """Require at least one structured section in a parsed document."""
        if not self.sections:
            raise ValueError("A PARSED LONG DOCUMENT MUST CONTAIN SECTIONS")

mutants_xǁParsedLongDocumentǁ__post_init____mutmut['_mutmut_orig'] = ParsedLongDocument.xǁParsedLongDocumentǁ__post_init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁParsedLongDocumentǁ__post_init____mutmut['xǁParsedLongDocumentǁ__post_init____mutmut_1'] = ParsedLongDocument.xǁParsedLongDocumentǁ__post_init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁParsedLongDocumentǁ__post_init____mutmut['xǁParsedLongDocumentǁ__post_init____mutmut_2'] = ParsedLongDocument.xǁParsedLongDocumentǁ__post_init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁParsedLongDocumentǁ__post_init____mutmut['xǁParsedLongDocumentǁ__post_init____mutmut_3'] = ParsedLongDocument.xǁParsedLongDocumentǁ__post_init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁParsedLongDocumentǁ__post_init____mutmut['xǁParsedLongDocumentǁ__post_init____mutmut_4'] = ParsedLongDocument.xǁParsedLongDocumentǁ__post_init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁParsedLongDocumentǁ__post_init____mutmut['xǁParsedLongDocumentǁ__post_init____mutmut_5'] = ParsedLongDocument.xǁParsedLongDocumentǁ__post_init____mutmut_5 # type: ignore # mutmut generated
