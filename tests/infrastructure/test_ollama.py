from __future__ import annotations

import json
from unittest import TestCase
from urllib.request import Request

from smart_doc_tracker.infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaResponseError,
)


class FakeResponse:
    def __init__(self, body: bytes) -> None:
        self.body = body

    def __enter__(self) -> FakeResponse:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def read(self) -> bytes:
        return self.body


class OllamaClientTests(TestCase):
    def test_sends_non_streaming_json_request_to_loopback(self) -> None:
        calls: list[tuple[Request, float]] = []

        def transport(request: Request, *, timeout: float) -> FakeResponse:
            calls.append((request, timeout))
            return FakeResponse(b'{"response":"{\\"document_type\\":\\"invoice\\"}"}')

        result = OllamaClient(transport=transport).generate(
            system_prompt="system", user_prompt="OCR data"
        )

        self.assertEqual(result, '{"document_type":"invoice"}')
        self.assertEqual(len(calls), 1)
        request, timeout = calls[0]
        self.assertEqual(request.full_url, "http://127.0.0.1:11434/api/generate")
        payload = json.loads(request.data or b"")
        self.assertEqual(payload["model"], "qwen2.5:3b")
        self.assertEqual(payload["format"], "json")
        self.assertFalse(payload["stream"])
        self.assertEqual(payload["options"]["num_ctx"], 8_192)
        self.assertEqual(payload["options"]["num_predict"], 2_048)
        self.assertEqual(timeout, 120.0)

    def test_rejects_non_loopback_endpoint(self) -> None:
        for endpoint in (
            "https://example.com:11434",
            "http://192.168.1.5:11434",
            "http://localhost:11434/proxy",
        ):
            with self.subTest(endpoint=endpoint):
                with self.assertRaises(OllamaConfigurationError):
                    OllamaClient(base_url=endpoint)

    def test_rejects_invalid_service_response(self) -> None:
        def transport(request: Request, *, timeout: float) -> FakeResponse:
            return FakeResponse(b'{"unexpected": true}')

        with self.assertRaisesRegex(OllamaResponseError, "invalid response"):
            OllamaClient(transport=transport).generate(
                system_prompt="system", user_prompt="OCR data"
            )
