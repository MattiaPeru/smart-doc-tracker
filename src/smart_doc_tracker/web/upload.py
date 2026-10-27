"""Validate and stage browser uploads for local document processing."""

import os
import re
import tempfile
from pathlib import Path

from fastapi import HTTPException, UploadFile

from ..core.ocr import SUPPORTED_IMAGE_EXTENSIONS
from .jobs import UploadJobService
from .schemas import UploadJobResponse

_SUPPORTED_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS | {".pdf"}
_LANGUAGE_CODE = re.compile(r"^[A-Za-z][A-Za-z0-9_+-]{0,31}$")
_MAX_UPLOAD_BYTES = 25 * 1024 * 1024
_UPLOAD_CHUNK_BYTES = 1024 * 1024


class UploadIntake:
    """Spool a validated upload and transfer ownership to the local job queue."""

    def __init__(self, jobs: UploadJobService) -> None:
        """Transfer accepted local files to the upload job queue."""
        self._jobs = jobs

    async def submit(self, file: UploadFile, language: str) -> UploadJobResponse:
        """Validate, spool, and queue one document for local processing."""
        safe_name = Path(file.filename or "").name
        suffix = Path(safe_name).suffix.lower()
        if not safe_name or suffix not in _SUPPORTED_EXTENSIONS:
            raise HTTPException(status_code=415, detail="Unsupported document format.")
        if not _LANGUAGE_CODE.fullmatch(language):
            raise HTTPException(status_code=422, detail="Invalid OCR language code.")
        temporary_path: Path | None = None
        try:
            descriptor, raw_path = tempfile.mkstemp(
                prefix="smart-doc-upload-",
                suffix=suffix,
            )
            temporary_path = Path(raw_path)
            total = 0
            with os.fdopen(descriptor, "wb") as destination:
                while chunk := await file.read(_UPLOAD_CHUNK_BYTES):
                    total += len(chunk)
                    if total > _MAX_UPLOAD_BYTES:
                        raise HTTPException(
                            status_code=413,
                            detail="The upload exceeds the 25 MB limit.",
                        )
                    destination.write(chunk)
            if total == 0:
                raise HTTPException(status_code=422, detail="The upload is empty.")
            job = self._jobs.submit(
                temporary_path,
                file_name=safe_name,
                language=language,
            )
            temporary_path = None
            return UploadJobResponse.from_job(job)
        finally:
            await file.close()
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
