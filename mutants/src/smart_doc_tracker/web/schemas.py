"""HTTP response schemas for the local dashboard."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from ..db.database import StoredDocument
from ..models.document import DocumentData
from ..models.rag import AnswerClaim, IndexedDocumentFragment
from ..settings import ReminderSettings
from .index_jobs import IndexUpdateJob
from .jobs import UploadJob
from .pending import PendingDocument


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ChatRequest(BaseModel):
    """One bounded natural-language question for the local document assistant."""

    model_config = ConfigDict(extra="forbid")

    question: str = Field(min_length=1, max_length=4_000)
    conversation_id: str | None = Field(
        default=None,
        min_length=1,
        max_length=64,
        pattern=r"^[A-Za-z0-9_-]+$",
    )
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut: MutantDict = {}  # type: ignore


class ChatDocumentReference(BaseModel):
    """Browser-safe document citation attached to one grounded answer."""

    model_config = ConfigDict(extra="forbid")

    id: str
    document_type: str
    summary: str

    @classmethod
    @_mutmut_mutated(mutants_xǁChatDocumentReferenceǁfrom_record__mutmut, is_classmethod = True)
    def from_record(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_orig(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_1(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=None,
            document_type=record.document.document_type,
            summary=record.document.summary,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_2(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=record.id,
            document_type=None,
            summary=record.document.summary,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_3(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=None,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_4(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            document_type=record.document.document_type,
            summary=record.document.summary,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_5(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=record.id,
            summary=record.document.summary,
        )

    @classmethod
    def xǁChatDocumentReferenceǁfrom_record__mutmut_6(cls, record: StoredDocument) -> ChatDocumentReference:
        """Create a citation without exposing hashes or document contents."""
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            )

mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['_mutmut_orig'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['xǁChatDocumentReferenceǁfrom_record__mutmut_1'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['xǁChatDocumentReferenceǁfrom_record__mutmut_2'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['xǁChatDocumentReferenceǁfrom_record__mutmut_3'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['xǁChatDocumentReferenceǁfrom_record__mutmut_4'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['xǁChatDocumentReferenceǁfrom_record__mutmut_5'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChatDocumentReferenceǁfrom_record__mutmut['xǁChatDocumentReferenceǁfrom_record__mutmut_6'] = ChatDocumentReference.xǁChatDocumentReferenceǁfrom_record__mutmut_6 # type: ignore # mutmut generated


class ChatResponse(BaseModel):
    """Grounded answer and the locally stored documents that support it."""

    model_config = ConfigDict(extra="forbid")

    answer: str
    claims: list[AnswerClaim]
    documents: list[ChatDocumentReference]
    insufficient_information: bool
mutants_xǁDocumentResponseǁfrom_record__mutmut: MutantDict = {}  # type: ignore


class DocumentResponse(BaseModel):
    """Browser-safe representation of a validated stored document."""

    model_config = ConfigDict(extra="forbid")

    id: str
    document_type: str
    summary: str
    expiry_date: date | None
    issue_date: date | None
    notification_days_before: int | None
    effective_notification_days_before: int
    extracted_data: dict[str, Any]
    created_at: datetime
    expiration_status: Literal["expired", "soon", "valid", "none"]
    original_file_name: str | None

    @classmethod
    @_mutmut_mutated(mutants_xǁDocumentResponseǁfrom_record__mutmut, is_classmethod = True)
    def from_record(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_orig(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_1(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = None
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_2(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = None
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_3(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if (record.document.notification_days_before is not None) and False
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_4(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if (record.document.notification_days_before is not None) or True
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_5(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_6(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is not None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_7(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = None
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_8(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "XXnoneXX"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_9(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "NONE"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_10(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date <= today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_11(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = None
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_12(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "XXexpiredXX"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_13(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "EXPIRED"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_14(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date + today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_15(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days < effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_16(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = None
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_17(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "XXsoonXX"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_18(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "SOON"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_19(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = None
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_20(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "XXvalidXX"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_21(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "VALID"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_22(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=None,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_23(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=None,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_24(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=None,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_25(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=None,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_26(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=None,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_27(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=None,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_28(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=None,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_29(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=None,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_30(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=None,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_31(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=None,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_32(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=None,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_33(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_34(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_35(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_36(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_37(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_38(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_39(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_40(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            created_at=record.created_at,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_41(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            expiration_status=status,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_42(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            original_file_name=record.source_file_name,
        )

    @classmethod
    def xǁDocumentResponseǁfrom_record__mutmut_43(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        effective_days = (
            record.document.notification_days_before
            if record.document.notification_days_before is not None
            else alert_days
        )
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= effective_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            notification_days_before=record.document.notification_days_before,
            effective_notification_days_before=effective_days,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
            )

mutants_xǁDocumentResponseǁfrom_record__mutmut['_mutmut_orig'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_1'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_2'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_3'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_4'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_5'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_6'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_7'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_8'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_9'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_10'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_11'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_12'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_13'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_14'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_15'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_16'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_17'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_18'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_19'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_20'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_21'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_22'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_23'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_24'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_25'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_26'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_27'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_28'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_29'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_30'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_31'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_32'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_33'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_34'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_35'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_36'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_37'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_38'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_39'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_40'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_41'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_42'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDocumentResponseǁfrom_record__mutmut['xǁDocumentResponseǁfrom_record__mutmut_43'] = DocumentResponse.xǁDocumentResponseǁfrom_record__mutmut_43 # type: ignore # mutmut generated


class ReminderSettingsResponse(ReminderSettings):
    """Browser-visible reminder defaults stored only on the local host."""
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut: MutantDict = {}  # type: ignore


class DocumentUpdateResponse(DocumentResponse):
    """Stored document plus its accepted background refresh identifier."""

    index_update_id: str

    @classmethod
    @_mutmut_mutated(mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut, is_classmethod = True)
    def from_update(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_orig(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_1(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = None
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_2(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            None,
            today=today,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_3(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=None,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_4(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            alert_days=None,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_5(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            today=today,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_6(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_7(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            )
        return cls(**response.model_dump(), index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_8(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), index_update_id=None)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_9(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            alert_days=alert_days,
        )
        return cls(index_update_id=index_update_id)

    @classmethod
    def xǁDocumentUpdateResponseǁfrom_update__mutmut_10(
        cls,
        record: StoredDocument,
        *,
        index_update_id: str,
        today: date,
        alert_days: int,
    ) -> DocumentUpdateResponse:
        """Create an update response after durable local queueing."""
        response = DocumentResponse.from_record(
            record,
            today=today,
            alert_days=alert_days,
        )
        return cls(**response.model_dump(), )

mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['_mutmut_orig'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_1'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_2'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_3'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_4'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_5'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_6'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_7'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_8'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_9'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentUpdateResponseǁfrom_update__mutmut['xǁDocumentUpdateResponseǁfrom_update__mutmut_10'] = DocumentUpdateResponse.xǁDocumentUpdateResponseǁfrom_update__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIndexUpdateJobResponseǁfrom_job__mutmut: MutantDict = {}  # type: ignore


class IndexUpdateJobResponse(BaseModel):
    """Minimal browser-visible state for one background refresh."""

    model_config = ConfigDict(from_attributes=True, extra="forbid")

    id: str
    status: str

    @classmethod
    @_mutmut_mutated(mutants_xǁIndexUpdateJobResponseǁfrom_job__mutmut, is_classmethod = True)
    def from_job(cls, job: IndexUpdateJob) -> IndexUpdateJobResponse:
        """Hide internal document and persistence metadata from the browser."""
        return cls.model_validate(job)

    @classmethod
    def xǁIndexUpdateJobResponseǁfrom_job__mutmut_orig(cls, job: IndexUpdateJob) -> IndexUpdateJobResponse:
        """Hide internal document and persistence metadata from the browser."""
        return cls.model_validate(job)

    @classmethod
    def xǁIndexUpdateJobResponseǁfrom_job__mutmut_1(cls, job: IndexUpdateJob) -> IndexUpdateJobResponse:
        """Hide internal document and persistence metadata from the browser."""
        return cls.model_validate(None)

mutants_xǁIndexUpdateJobResponseǁfrom_job__mutmut['_mutmut_orig'] = IndexUpdateJobResponse.xǁIndexUpdateJobResponseǁfrom_job__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIndexUpdateJobResponseǁfrom_job__mutmut['xǁIndexUpdateJobResponseǁfrom_job__mutmut_1'] = IndexUpdateJobResponse.xǁIndexUpdateJobResponseǁfrom_job__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUploadJobResponseǁfrom_job__mutmut: MutantDict = {}  # type: ignore


class UploadJobResponse(BaseModel):
    """Public status for one process-local upload job."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    file_name: str
    status: str
    created_at: datetime
    updated_at: datetime
    document_id: str | None
    pending_id: str | None
    inserted: bool | None
    error: str | None

    @classmethod
    @_mutmut_mutated(mutants_xǁUploadJobResponseǁfrom_job__mutmut, is_classmethod = True)
    def from_job(cls, job: UploadJob) -> UploadJobResponse:
        """Convert an immutable job snapshot to JSON output."""
        return cls.model_validate(job)

    @classmethod
    def xǁUploadJobResponseǁfrom_job__mutmut_orig(cls, job: UploadJob) -> UploadJobResponse:
        """Convert an immutable job snapshot to JSON output."""
        return cls.model_validate(job)

    @classmethod
    def xǁUploadJobResponseǁfrom_job__mutmut_1(cls, job: UploadJob) -> UploadJobResponse:
        """Convert an immutable job snapshot to JSON output."""
        return cls.model_validate(None)

mutants_xǁUploadJobResponseǁfrom_job__mutmut['_mutmut_orig'] = UploadJobResponse.xǁUploadJobResponseǁfrom_job__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUploadJobResponseǁfrom_job__mutmut['xǁUploadJobResponseǁfrom_job__mutmut_1'] = UploadJobResponse.xǁUploadJobResponseǁfrom_job__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut: MutantDict = {}  # type: ignore


class PendingDocumentResponse(BaseModel):
    """Editable extracted data for one upload awaiting confirmation."""

    model_config = ConfigDict(extra="forbid")

    id: str
    file_name: str
    document: DocumentData
    created_at: datetime

    @classmethod
    @_mutmut_mutated(mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut, is_classmethod = True)
    def from_pending(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            document=pending.document,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_orig(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            document=pending.document,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_1(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=None,
            file_name=pending.file_name,
            document=pending.document,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_2(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=None,
            document=pending.document,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_3(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            document=None,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_4(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            document=pending.document,
            created_at=None,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_5(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            file_name=pending.file_name,
            document=pending.document,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_6(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            document=pending.document,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_7(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            created_at=pending.created_at,
        )

    @classmethod
    def xǁPendingDocumentResponseǁfrom_pending__mutmut_8(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            document=pending.document,
            )

mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['_mutmut_orig'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_1'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_2'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_3'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_4'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_5'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_6'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_7'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPendingDocumentResponseǁfrom_pending__mutmut['xǁPendingDocumentResponseǁfrom_pending__mutmut_8'] = PendingDocumentResponse.xǁPendingDocumentResponseǁfrom_pending__mutmut_8 # type: ignore # mutmut generated


class IndexedFragmentResponse(BaseModel):
    """Browser-safe representation of one local Chroma content fragment."""

    model_config = ConfigDict(from_attributes=True, extra="forbid")

    fragment_id: str
    source: str
    content: str
mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut: MutantDict = {}  # type: ignore


class DocumentIndexedContentResponse(BaseModel):
    """Complete indexed content for one locally stored document."""

    model_config = ConfigDict(extra="forbid")

    document_id: str
    fragments: list[IndexedFragmentResponse]

    @classmethod
    @_mutmut_mutated(mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut, is_classmethod = True)
    def from_fragments(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            document_id=document_id,
            fragments=[
                IndexedFragmentResponse.model_validate(fragment)
                for fragment in fragments
            ],
        )

    @classmethod
    def xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_orig(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            document_id=document_id,
            fragments=[
                IndexedFragmentResponse.model_validate(fragment)
                for fragment in fragments
            ],
        )

    @classmethod
    def xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_1(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            document_id=None,
            fragments=[
                IndexedFragmentResponse.model_validate(fragment)
                for fragment in fragments
            ],
        )

    @classmethod
    def xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_2(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            document_id=document_id,
            fragments=None,
        )

    @classmethod
    def xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_3(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            fragments=[
                IndexedFragmentResponse.model_validate(fragment)
                for fragment in fragments
            ],
        )

    @classmethod
    def xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_4(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            document_id=document_id,
            )

    @classmethod
    def xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_5(
        cls,
        document_id: str,
        fragments: list[IndexedDocumentFragment],
    ) -> DocumentIndexedContentResponse:
        """Create an HTTP response without exposing stored embeddings."""
        return cls(
            document_id=document_id,
            fragments=[
                IndexedFragmentResponse.model_validate(None)
                for fragment in fragments
            ],
        )

mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut['_mutmut_orig'] = DocumentIndexedContentResponse.xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut['xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_1'] = DocumentIndexedContentResponse.xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut['xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_2'] = DocumentIndexedContentResponse.xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut['xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_3'] = DocumentIndexedContentResponse.xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut['xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_4'] = DocumentIndexedContentResponse.xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut['xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_5'] = DocumentIndexedContentResponse.xǁDocumentIndexedContentResponseǁfrom_fragments__mutmut_5 # type: ignore # mutmut generated
