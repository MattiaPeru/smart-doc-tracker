"""Local documents HTTP endpoints."""

import json
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse

from ...db.database import DatabaseError
from ...db.vector_database import VectorDatabaseError
from ...interfaces.document_repository import DocumentRepository
from ...models.document import DocumentData
from ...mutation_pipeline import CoordinatedMutationError
from ..pending import PendingDocumentError
from ..schemas import (
    DocumentIndexedContentResponse,
    DocumentResponse,
    DocumentUpdateResponse,
    IndexUpdateJobResponse,
)
from .context import WebRouteContext
from .helpers import require_index_jobs, require_mutation_service


def register_documents_routes(context: WebRouteContext) -> APIRouter:
    """Register the documents endpoints with explicit local services."""
    router = APIRouter()
    resolved = context.dependencies
    pending_documents = context.pending_documents
    mutations = context.mutations
    insertion = context.insertion
    index_jobs = context.index_jobs
    default_reminder_days = context.default_reminder_days
    Repository = Annotated[DocumentRepository, Depends(context.repository)]

    @router.get("/api/documents", response_model=list[DocumentResponse])
    def list_documents(
        repository: Repository,
        field_key: Annotated[str | None, Query(max_length=200)] = None,
        field_value: Annotated[str | None, Query(max_length=10_000)] = None,
    ) -> list[DocumentResponse]:
        """List documents or exactly match one validated dynamic JSON path."""
        if (field_key is None) != (field_value is None):
            raise HTTPException(
                status_code=422,
                detail="field_key and field_value must be provided together.",
            )
        try:
            records = (
                repository.search_by_dynamic_field(
                    field_key,
                    _parse_query_value(field_value),
                )
                if field_key is not None and field_value is not None
                else repository.get_all_documents()
            )
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        today = resolved.today_provider()
        alert_days = default_reminder_days()
        pending_ids = pending_documents.insertion_ids()
        pending_hashes = pending_documents.insertion_hashes()
        return [
            DocumentResponse.from_record(
                record,
                today=today,
                alert_days=alert_days,
            )
            for record in records
            if record.id not in pending_ids and record.file_hash not in pending_hashes
        ]

    @router.get("/api/documents/{document_id}", response_model=DocumentResponse)
    def get_document(
        document_id: str,
        repository: Repository,
    ) -> DocumentResponse:
        """Return one locally stored document."""
        record = repository.get_document_by_id(document_id)
        if record is None or record.file_hash in pending_documents.insertion_hashes():
            raise HTTPException(status_code=404, detail="Document not found.")
        alert_days = default_reminder_days()
        return DocumentResponse.from_record(
            record,
            today=resolved.today_provider(),
            alert_days=alert_days,
        )

    @router.get("/api/documents/{document_id}/original")
    def get_document_original(
        document_id: str,
        repository: Repository,
        download: bool = False,
    ) -> FileResponse:
        """Open or download the original file from the local processed archive."""
        record = repository.get_document_by_id(document_id)
        if record is None or record.file_hash in pending_documents.insertion_hashes():
            raise HTTPException(status_code=404, detail="Document not found.")
        if record.source_file_name is None:
            raise HTTPException(
                status_code=404,
                detail="The original file is not available for this document.",
            )
        processed_root = resolved.processed_path.expanduser().resolve()
        source_path = (processed_root / record.source_file_name).resolve()
        if source_path.parent != processed_root or not source_path.is_file():
            raise HTTPException(
                status_code=404,
                detail="The original file is not available for this document.",
            )
        return FileResponse(
            source_path,
            filename=record.source_file_name,
            content_disposition_type="attachment" if download else "inline",
        )

    @router.get(
        "/api/documents/{document_id}/indexed-content",
        response_model=DocumentIndexedContentResponse,
    )
    def get_document_indexed_content(
        document_id: str,
        repository: Repository,
    ) -> DocumentIndexedContentResponse:
        """Return every local Chroma content fragment for one stored document."""
        record = repository.get_document_by_id(document_id)
        if record is None or record.file_hash in pending_documents.insertion_hashes():
            raise HTTPException(status_code=404, detail="Document not found.")
        if resolved.vector_index is None:
            raise HTTPException(
                status_code=503,
                detail="The local vector database is unavailable.",
            )
        try:
            fragments = resolved.vector_index.get_document_fragments(document_id)
        except (ValueError, VectorDatabaseError) as exc:
            raise HTTPException(
                status_code=503,
                detail="The indexed document content is unavailable.",
            ) from exc
        return DocumentIndexedContentResponse.from_fragments(
            document_id,
            fragments,
        )

    @router.put("/api/documents/{document_id}", response_model=DocumentUpdateResponse)
    def update_document(
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResponse:
        """Store one document update and queue its local search refresh."""
        alert_days = default_reminder_days()
        if document_id in pending_documents.insertion_ids():
            raise HTTPException(status_code=404, detail="Document not found.")
        service = require_mutation_service(mutations)
        try:
            updated = service.update(document_id, document)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except CoordinatedMutationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        if updated is None:
            raise HTTPException(status_code=404, detail="Document not found.")
        return DocumentUpdateResponse.from_update(
            updated.record,
            index_update_id=updated.index_update_id,
            today=resolved.today_provider(),
            alert_days=alert_days,
        )

    @router.post("/api/documents/manual", response_model=DocumentResponse)
    def create_manual_document(document: DocumentData) -> DocumentResponse:
        """Validate, persist, and index a document entered entirely by the user."""
        alert_days = default_reminder_days()
        try:
            document.ensure_complete_dynamic_values()
            with insertion.lock:
                pending = pending_documents.add_manual(document)
                result = insertion.complete(pending.id)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except (
            CoordinatedMutationError,
            DatabaseError,
            PendingDocumentError,
            VectorDatabaseError,
        ) as exc:
            raise HTTPException(
                status_code=503,
                detail=(
                    "There were problems inserting the document. "
                    "Please try again later, or discard it from pending documents."
                ),
            ) from exc
        return DocumentResponse.from_record(
            result.record,
            today=resolved.today_provider(),
            alert_days=alert_days,
        )

    @router.get(
        "/api/document-updates/{update_id}",
        response_model=IndexUpdateJobResponse,
    )
    def get_document_update(update_id: str) -> IndexUpdateJobResponse:
        """Return simple progress for one accepted background refresh."""
        job = require_index_jobs(index_jobs).get(update_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Update not found.")
        return IndexUpdateJobResponse.from_job(job)

    @router.delete("/api/documents/{document_id}", status_code=204)
    def delete_document(document_id: str) -> None:
        """Delete one document consistently from MongoDB and ChromaDB."""
        if document_id in pending_documents.insertion_ids():
            raise HTTPException(status_code=404, detail="Document not found.")
        service = require_mutation_service(mutations)
        try:
            deleted = service.delete(document_id)
        except CoordinatedMutationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        if deleted is None:
            raise HTTPException(status_code=404, detail="Document not found.")

    return router


def _parse_query_value(value: str) -> Any:
    """Interpret JSON scalars and structures, falling back to a plain string."""
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value
