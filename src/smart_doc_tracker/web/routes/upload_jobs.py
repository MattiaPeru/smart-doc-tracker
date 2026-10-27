"""Local uploads HTTP endpoints."""

from typing import Annotated

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from ..schemas import UploadJobResponse
from .context import WebRouteContext


def register_upload_job_routes(context: WebRouteContext) -> APIRouter:
    """Register the uploads endpoints with explicit local services."""
    router = APIRouter()
    upload_intake = context.upload_intake
    jobs = context.jobs

    @router.post(
        "/api/uploads",
        response_model=UploadJobResponse,
        status_code=202,
    )
    async def upload_document(
        file: Annotated[UploadFile, File(description="A local image or PDF")],
        language: Annotated[str, Form(min_length=1, max_length=32)] = "eng",
    ) -> UploadJobResponse:
        """Validate, spool, and queue one document for local processing."""
        return await upload_intake.submit(file, language)

    @router.get("/api/jobs", response_model=list[UploadJobResponse])
    def list_upload_jobs() -> list[UploadJobResponse]:
        """List documents queued, processing, or failed."""
        return [UploadJobResponse.from_job(job) for job in jobs.list_processing()]

    @router.post("/api/jobs/retry-all")
    def retry_all_failed_upload_jobs() -> dict[str, int]:
        """Retry all failed uploads with available local source files."""
        return {"retried": jobs.retry_all_failed()}

    @router.delete("/api/jobs/failed")
    def discard_all_failed_upload_jobs() -> dict[str, int]:
        """Discard all failed uploads and their local source files."""
        return {"removed": jobs.discard_all_failed()}

    @router.get("/api/jobs/{job_id}", response_model=UploadJobResponse)
    def get_upload_job(job_id: str) -> UploadJobResponse:
        """Return the current status of one process-local upload job."""
        job = jobs.get(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        return UploadJobResponse.from_job(job)

    @router.post("/api/jobs/{job_id}/retry", response_model=UploadJobResponse)
    def retry_failed_upload_job(job_id: str) -> UploadJobResponse:
        """Retry one failed upload using its retained local source."""
        job = jobs.get(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        if not jobs.retry_failed(job_id):
            raise HTTPException(
                status_code=409,
                detail="Only failed uploads with a local source file can be retried.",
            )
        queued = jobs.get(job_id)
        if queued is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        return UploadJobResponse.from_job(queued)

    @router.delete("/api/jobs/{job_id}", status_code=204)
    def discard_failed_upload_job(job_id: str) -> None:
        """Discard one failed job and its locally queued source file."""
        job = jobs.get(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Upload job not found.")
        if not jobs.discard_failed(job_id):
            raise HTTPException(
                status_code=409,
                detail="Only failed upload jobs can be removed.",
            )

    return router
