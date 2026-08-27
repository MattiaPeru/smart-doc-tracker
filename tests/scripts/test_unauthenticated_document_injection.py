from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

SCRIPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "scripts"
    / "simulate_unauthenticated_document_injection.py"
)
SPEC = importlib.util.spec_from_file_location(
    "document_injection_simulation",
    SCRIPT_PATH,
)
assert SPEC is not None and SPEC.loader is not None
simulation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(simulation)


class UnauthenticatedDocumentInjectionTests(TestCase):
    def test_accepts_only_explicit_loopback_http_endpoints(self) -> None:
        self.assertEqual(
            simulation.validate_endpoint("http://127.0.0.1:8080"),
            "http://127.0.0.1:8080",
        )
        self.assertEqual(
            simulation.validate_endpoint("http://[::1]:8080/"),
            "http://[::1]:8080",
        )

        rejected = (
            "https://127.0.0.1:8080",
            "http://192.168.1.10:8080",
            "http://127.0.0.1",
            "http://user@127.0.0.1:8080",
            "http://127.0.0.1:8080/api",
            "http://127.0.0.1:8080?target=other",
        )
        for endpoint in rejected:
            with self.subTest(endpoint=endpoint):
                with self.assertRaises(argparse.ArgumentTypeError):
                    simulation.validate_endpoint(endpoint)

    def test_creates_a_valid_synthetic_pdf_and_multipart_body(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.pdf"
            simulation.create_synthetic_pdf(path)
            body, boundary = simulation.encode_multipart_file(path)

        self.assertTrue(path.name.encode("ascii") in body)
        self.assertIn(b"application/pdf", body)
        self.assertIn(b"%PDF-", body)
        self.assertIn(boundary.encode("ascii"), body)

    def test_simulation_follows_upload_job_confirmation_and_verification(self) -> None:
        calls: list[tuple[str, str]] = []

        def fake_request(
            endpoint: str,
            path: str,
            *,
            method: str = "GET",
            body: bytes | None = None,
            content_type: str | None = None,
            timeout: float = 10.0,
        ) -> object:
            del endpoint, content_type, timeout
            calls.append((method, path))
            if path == "/api/uploads":
                self.assertIsNotNone(body)
                return {"id": "job-1"}
            if path == "/api/jobs/job-1":
                return {"status": "awaiting_confirmation", "pending_id": "pending-1"}
            if path == "/api/pending-documents/pending-1/confirm":
                self.assertIsNotNone(body)
                assert body is not None
                payload = json.loads(body)
                result_marker[0] = payload["extracted_data"]["synthetic_marker"]
                return {"id": "document-1"}
            if path == "/api/documents/document-1":
                return {
                    "extracted_data": {
                        "synthetic_marker": result_marker[0],
                    }
                }
            raise AssertionError(path)

        result_marker = [""]
        with patch.object(simulation, "request_json", side_effect=fake_request):
            result = simulation.run_simulation("http://127.0.0.1:8080", 1.0)

        self.assertEqual(result["document_id"], "document-1")
        self.assertEqual(result["synthetic_marker"], result_marker[0])
        self.assertEqual(
            calls,
            [
                ("POST", "/api/uploads"),
                ("GET", "/api/jobs/job-1"),
                ("POST", "/api/pending-documents/pending-1/confirm"),
                ("GET", "/api/documents/document-1"),
            ],
        )

    def test_requires_execute_flag_before_any_request(self) -> None:
        with patch.object(simulation, "run_simulation") as run_simulation:
            exit_code = simulation.main([])

        self.assertEqual(exit_code, 0)
        run_simulation.assert_not_called()
