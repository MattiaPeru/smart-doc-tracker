"""HTTP response schemas for the local dashboard."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

from ..db.database import StoredDocument
from ..models.document import DocumentData
from ..models.rag import IndexedDocumentFragment
from .jobs import UploadJob
from .pending import PendingDocument


class DocumentResponse(BaseModel):
    """Browser-safe representation of a validated stored document."""

    model_config = ConfigDict(extra="forbid")

    id: str
    document_type: str
    summary: str
    expiry_date: date | None
    issue_date: date | None
    extracted_data: dict[str, Any]
    created_at: datetime
    expiration_status: Literal["expired", "soon", "valid", "none"]

    @classmethod
    def from_record(
        cls,
        record: StoredDocument,
        *,
        today: date,
        alert_days: int,
    ) -> DocumentResponse:
        """Create a response and classify its expiration color."""
        expiry_date = record.document.expiry_date
        status: Literal["expired", "soon", "valid", "none"]
        if expiry_date is None:
            status = "none"
        elif expiry_date < today:
            status = "expired"
        elif (expiry_date - today).days <= alert_days:
            status = "soon"
        else:
            status = "valid"
        return cls(
            id=record.id,
            document_type=record.document.document_type,
            summary=record.document.summary,
            expiry_date=expiry_date,
            issue_date=record.document.issue_date,
            extracted_data=record.document.extracted_data,
            created_at=record.created_at,
            expiration_status=status,
        )


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
    def from_job(cls, job: UploadJob) -> UploadJobResponse:
        """Convert an immutable job snapshot to JSON output."""
        return cls.model_validate(job)


class PendingDocumentResponse(BaseModel):
    """Editable extracted data for one upload awaiting confirmation."""

    model_config = ConfigDict(extra="forbid")

    id: str
    file_name: str
    document: DocumentData
    created_at: datetime

    @classmethod
    def from_pending(cls, pending: PendingDocument) -> PendingDocumentResponse:
        """Create a response without exposing raw OCR text or temporary paths."""
        return cls(
            id=pending.id,
            file_name=pending.file_name,
            document=pending.document,
            created_at=pending.created_at,
        )


class IndexedFragmentResponse(BaseModel):
    """Browser-safe representation of one local Chroma content fragment."""

    model_config = ConfigDict(from_attributes=True, extra="forbid")

    fragment_id: str
    source: str
    content: str


class DocumentIndexedContentResponse(BaseModel):
    """Complete indexed content for one locally stored document."""

    model_config = ConfigDict(extra="forbid")

    document_id: str
    fragments: list[IndexedFragmentResponse]

    @classmethod
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
