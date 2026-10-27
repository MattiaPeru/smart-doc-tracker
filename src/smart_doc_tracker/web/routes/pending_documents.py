"""Local pending HTTP endpoints."""

from fastapi import APIRouter, HTTPException

from ...core.file_hash import FileHashingError, calculate_file_sha256
from ...db.database import DatabaseError
from ...db.vector_database import VectorDatabaseError
from ...models.document import DocumentData
from ...mutation_pipeline import CoordinatedMutationError
from ..insertion import PendingSourceRemovalError
from ..pending import PendingDocumentError
from ..schemas import DocumentResponse, PendingDocumentResponse
from .context import WebRouteContext


def register_pending_document_routes(context: WebRouteContext) -> APIRouter:
    """Register the pending endpoints with explicit local services."""
    router = APIRouter()
    resolved = context.dependencies
    pending_documents = context.pending_documents
    insertion = context.insertion
    default_reminder_days = context.default_reminder_days

    @router.get("/api/pending-documents", response_model=list[PendingDocumentResponse])
    def list_pending_documents() -> list[PendingDocumentResponse]:
        """List uploads that have not yet been explicitly confirmed."""
        return [
            PendingDocumentResponse.from_pending(item)
            for item in pending_documents.list()
        ]

    @router.get(
        "/api/pending-documents/{pending_id}",
        response_model=PendingDocumentResponse,
    )
    def get_pending_document(pending_id: str) -> PendingDocumentResponse:
        """Return one editable pending upload."""
        pending = pending_documents.get(pending_id)
        if pending is None:
            raise HTTPException(status_code=404, detail="Pending document not found.")
        return PendingDocumentResponse.from_pending(pending)

    @router.post(
        "/api/pending-documents/{pending_id}/confirm",
        response_model=DocumentResponse,
    )
    def confirm_pending_document(
        pending_id: str,
        document: DocumentData,
    ) -> DocumentResponse:
        """Validate user edits before persistence, indexing, and archiving."""
        alert_days = default_reminder_days()
        try:
            with insertion.lock:
                pending = pending_documents.get(pending_id)
                if pending is None:
                    raise HTTPException(
                        status_code=404, detail="Pending document not found."
                    )
                file_hash = pending.file_hash or calculate_file_sha256(
                    pending.source_path
                )
                pending_documents.begin_insertion(
                    pending_id, document, file_hash=file_hash
                )
                result = insertion.complete(pending_id)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except (
            CoordinatedMutationError,
            DatabaseError,
            FileHashingError,
            PendingDocumentError,
            VectorDatabaseError,
        ) as exc:
            raise HTTPException(
                status_code=503,
                detail=(
                    "There were problems inserting the document. "
                    "Please try again later, or discard it."
                ),
            ) from exc
        return DocumentResponse.from_record(
            result.record,
            today=resolved.today_provider(),
            alert_days=alert_days,
        )

    @router.delete("/api/pending-documents/{pending_id}", status_code=204)
    def reject_pending_document(pending_id: str) -> None:
        """Reject and securely discard one staged upload."""
        try:
            insertion.reject(pending_id)
        except PendingDocumentError as exc:
            raise HTTPException(
                status_code=404, detail="Pending document not found."
            ) from exc
        except PendingSourceRemovalError as exc:
            raise HTTPException(
                status_code=503,
                detail="The pending source could not be removed. Try again later.",
            ) from exc
        except OSError as exc:
            raise HTTPException(
                status_code=503,
                detail="The cancellation could not be recorded locally.",
            ) from exc
        except (DatabaseError, CoordinatedMutationError) as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc

    return router
