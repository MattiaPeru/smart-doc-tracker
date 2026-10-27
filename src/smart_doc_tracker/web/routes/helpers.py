"""Safe service checks shared by local document routes."""

from fastapi import HTTPException

from ...mutation_pipeline import DocumentMutationPipeline
from ..index_jobs import DocumentIndexJobService


def require_mutation_service(
    service: DocumentMutationPipeline | None,
) -> DocumentMutationPipeline:
    """Return configured mutation coordination or a safe service error."""
    if service is None:
        raise HTTPException(
            status_code=503,
            detail="The local vector database is unavailable.",
        )
    return service


def require_index_jobs(
    service: DocumentIndexJobService | None,
) -> DocumentIndexJobService:
    """Return the configured local refresh queue or a safe service error."""
    if service is None:
        raise HTTPException(
            status_code=503,
            detail="Document updates are temporarily unavailable.",
        )
    return service
