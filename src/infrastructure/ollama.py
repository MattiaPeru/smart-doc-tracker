"""Minimal local-only client for an Ollama text generation server."""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


class OllamaConfigurationError(ValueError):
    """Raised when the configured Ollama endpoint is not local and safe."""


class OllamaConnectionError(RuntimeError):
    """Raised when the local Ollama service cannot be reached."""


class OllamaResponseError(RuntimeError):
    """Raised when Ollama returns an invalid response."""


class HTTPResponse(Protocol):
    """Subset of an HTTP response used by the adapter."""

    def __enter__(self) -> HTTPResponse: ...
    def __exit__(self, *args: object) -> None: ...
    def read(self) -> bytes: ...


Transport = Callable[..., HTTPResponse]


class OllamaClient:
    """Generate JSON with an Ollama server bound to the loopback interface."""

    def __init__(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError("The Ollama context length must be positive.")
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_ctx": self._context_length,
                    "num_predict": self._max_output_tokens,
                },
            }
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/generate",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError("The local Ollama service is unavailable.") from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError("The local Ollama service returned an invalid response.") from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError("The local Ollama service returned an empty response.")
        return generated_text


def _validate_loopback_url(base_url: str) -> str:
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError("The Ollama endpoint has an invalid port.") from exc
    if port is None:
        raise OllamaConfigurationError("The Ollama endpoint must include an explicit port.")
    return base_url.rstrip("/")
