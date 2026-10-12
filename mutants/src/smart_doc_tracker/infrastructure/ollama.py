"""Minimal local-only client for an Ollama text generation server."""

from __future__ import annotations

import json
from collections.abc import Callable, Sequence
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from ..interfaces.http_response import HTTPResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class OllamaConfigurationError(ValueError):
    """Raised when the configured Ollama endpoint is not local and safe."""


class OllamaConnectionError(RuntimeError):
    """Raised when the local Ollama service cannot be reached."""


class OllamaResponseError(RuntimeError):
    """Raised when Ollama returns an invalid response."""


Transport = Callable[..., HTTPResponse]
mutants_xǁOllamaClientǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOllamaClientǁgenerate__mutmut: MutantDict = {}  # type: ignore


class OllamaClient:
    """Generate JSON with an Ollama server bound to the loopback interface."""

    @_mutmut_mutated(mutants_xǁOllamaClientǁ__init____mutmut)
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
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_orig(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_1(
        self,
        *,
        base_url: str = "XXhttp://127.0.0.1:11434XX",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_2(
        self,
        *,
        base_url: str = "HTTP://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_3(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "XXqwen2.5:3bXX",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_4(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "QWEN2.5:3B",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_5(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8193,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_6(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2049,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_7(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 121.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_8(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = None
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_9(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(None)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_10(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_11(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(None)
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_12(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("XXThe Ollama model name cannot be empty.XX")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_13(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("the ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_14(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("THE OLLAMA MODEL NAME CANNOT BE EMPTY.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_15(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds < 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_16(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 1:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_17(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError(None)
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_18(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("XXThe Ollama timeout must be positive.XX")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_19(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("the ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_20(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("THE OLLAMA TIMEOUT MUST BE POSITIVE.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_21(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length < 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_22(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 1:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_23(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                None
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_24(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "XXThe Ollama context length must be positive.XX"
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_25(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "the ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_26(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "THE OLLAMA CONTEXT LENGTH MUST BE POSITIVE."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_27(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 and max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_28(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens < 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_29(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 1 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_30(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens > context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_31(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                None
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_32(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "XXThe Ollama output limit must be positive and smaller than the context.XX"
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_33(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "the ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_34(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "THE OLLAMA OUTPUT LIMIT MUST BE POSITIVE AND SMALLER THAN THE CONTEXT."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_35(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = None
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_36(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = None
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_37(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = None
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_38(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = None
        self._transport = transport

    def xǁOllamaClientǁ__init____mutmut_39(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "qwen2.5:3b",
        context_length: int = 8_192,
        max_output_tokens: int = 2_048,
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a loopback-only Ollama generation client."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError("The Ollama model name cannot be empty.")
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        if context_length <= 0:
            raise OllamaConfigurationError(
                "The Ollama context length must be positive."
            )
        if max_output_tokens <= 0 or max_output_tokens >= context_length:
            raise OllamaConfigurationError(
                "The Ollama output limit must be positive and smaller than the context."
            )
        self._model = model
        self._context_length = context_length
        self._max_output_tokens = max_output_tokens
        self._timeout_seconds = timeout_seconds
        self._transport = None

    @_mutmut_mutated(mutants_xǁOllamaClientǁgenerate__mutmut)
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_orig(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_1(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = None
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_2(self, *, system_prompt: str, user_prompt: str) -> str:
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
        ).encode(None)
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_3(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            None
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_4(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "XXmodelXX": self._model,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_5(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "MODEL": self._model,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_6(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "XXsystemXX": system_prompt,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_7(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "SYSTEM": system_prompt,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_8(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "XXpromptXX": user_prompt,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_9(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "PROMPT": user_prompt,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_10(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "XXformatXX": "json",
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_11(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "FORMAT": "json",
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_12(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "XXjsonXX",
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_13(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "JSON",
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_14(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "XXstreamXX": False,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_15(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "STREAM": False,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_16(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": True,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_17(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": False,
                "XXoptionsXX": {
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_18(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": False,
                "OPTIONS": {
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_19(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": False,
                "options": {
                    "XXtemperatureXX": 0.1,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_20(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": False,
                "options": {
                    "TEMPERATURE": 0.1,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_21(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a non-streaming JSON response from the local model."""
        body = json.dumps(
            {
                "model": self._model,
                "system": system_prompt,
                "prompt": user_prompt,
                "format": "json",
                "stream": False,
                "options": {
                    "temperature": 1.1,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_22(self, *, system_prompt: str, user_prompt: str) -> str:
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
                    "XXnum_ctxXX": self._context_length,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_23(self, *, system_prompt: str, user_prompt: str) -> str:
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
                    "NUM_CTX": self._context_length,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_24(self, *, system_prompt: str, user_prompt: str) -> str:
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
                    "XXnum_predictXX": self._max_output_tokens,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_25(self, *, system_prompt: str, user_prompt: str) -> str:
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
                    "NUM_PREDICT": self._max_output_tokens,
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_26(self, *, system_prompt: str, user_prompt: str) -> str:
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
        ).encode("XXutf-8XX")
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_27(self, *, system_prompt: str, user_prompt: str) -> str:
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
        ).encode("UTF-8")
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_28(self, *, system_prompt: str, user_prompt: str) -> str:
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
        request = None

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_29(self, *, system_prompt: str, user_prompt: str) -> str:
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
            None,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_30(self, *, system_prompt: str, user_prompt: str) -> str:
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
            data=None,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_31(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers=None,
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_32(self, *, system_prompt: str, user_prompt: str) -> str:
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
            method=None,
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_33(self, *, system_prompt: str, user_prompt: str) -> str:
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
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_34(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_35(self, *, system_prompt: str, user_prompt: str) -> str:
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
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_36(self, *, system_prompt: str, user_prompt: str) -> str:
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
            )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_37(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers={"XXContent-TypeXX": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_38(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers={"content-type": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_39(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers={"CONTENT-TYPE": "application/json"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_40(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers={"Content-Type": "XXapplication/jsonXX"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_41(self, *, system_prompt: str, user_prompt: str) -> str:
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
            headers={"Content-Type": "APPLICATION/JSON"},
            method="POST",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_42(self, *, system_prompt: str, user_prompt: str) -> str:
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
            method="XXPOSTXX",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_43(self, *, system_prompt: str, user_prompt: str) -> str:
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
            method="post",
        )

        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_44(self, *, system_prompt: str, user_prompt: str) -> str:
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
            with self._transport(None, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_45(self, *, system_prompt: str, user_prompt: str) -> str:
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
            with self._transport(request, timeout=None) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_46(self, *, system_prompt: str, user_prompt: str) -> str:
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
            with self._transport(timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_47(self, *, system_prompt: str, user_prompt: str) -> str:
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
            with self._transport(request, ) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_48(self, *, system_prompt: str, user_prompt: str) -> str:
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
                response_body = None
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_49(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                None
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_50(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "XXThe local Ollama service is unavailable.XX"
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_51(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "the local ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_52(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "THE LOCAL OLLAMA SERVICE IS UNAVAILABLE."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_53(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = None
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_54(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(None)
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_55(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode(None))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_56(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("XXutf-8XX"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_57(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("UTF-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_58(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = None
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_59(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["XXresponseXX"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_60(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["RESPONSE"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_61(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                None
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_62(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "XXThe local Ollama service returned an invalid response.XX"
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_63(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "the local ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_64(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "THE LOCAL OLLAMA SERVICE RETURNED AN INVALID RESPONSE."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_65(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) and not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_66(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_67(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or generated_text.strip():
            raise OllamaResponseError(
                "The local Ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_68(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                None
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_69(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "XXThe local Ollama service returned an empty response.XX"
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_70(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "the local ollama service returned an empty response."
            )
        return generated_text

    def xǁOllamaClientǁgenerate__mutmut_71(self, *, system_prompt: str, user_prompt: str) -> str:
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
            raise OllamaConnectionError(
                "The local Ollama service is unavailable."
            ) from exc

        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            generated_text = payload["response"]
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama service returned an invalid response."
            ) from exc
        if not isinstance(generated_text, str) or not generated_text.strip():
            raise OllamaResponseError(
                "THE LOCAL OLLAMA SERVICE RETURNED AN EMPTY RESPONSE."
            )
        return generated_text

mutants_xǁOllamaClientǁ__init____mutmut['_mutmut_orig'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_1'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_2'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_3'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_4'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_5'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_6'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_7'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_8'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_9'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_10'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_11'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_12'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_13'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_14'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_15'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_16'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_17'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_18'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_19'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_20'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_21'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_22'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_23'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_24'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_25'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_26'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_27'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_28'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_29'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_30'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_31'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_32'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_33'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_34'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_34 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_35'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_35 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_36'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_36 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_37'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_37 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_38'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_38 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁ__init____mutmut['xǁOllamaClientǁ__init____mutmut_39'] = OllamaClient.xǁOllamaClientǁ__init____mutmut_39 # type: ignore # mutmut generated

mutants_xǁOllamaClientǁgenerate__mutmut['_mutmut_orig'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_1'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_2'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_3'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_4'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_5'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_6'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_7'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_8'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_9'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_10'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_11'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_12'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_13'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_14'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_15'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_16'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_17'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_18'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_19'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_20'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_21'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_22'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_23'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_24'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_25'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_26'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_27'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_28'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_29'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_30'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_31'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_32'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_33'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_34'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_35'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_36'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_37'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_38'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_39'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_40'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_41'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_42'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_43'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_44'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_45'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_46'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_47'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_48'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_49'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_50'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_51'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_52'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_53'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_54'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_55'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_56'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_57'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_58'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_59'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_60'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_61'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_62'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_63'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_64'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_65'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_66'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_67'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_68'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_69'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_70'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOllamaClientǁgenerate__mutmut['xǁOllamaClientǁgenerate__mutmut_71'] = OllamaClient.xǁOllamaClientǁgenerate__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOllamaEmbeddingClientǁembed__mutmut: MutantDict = {}  # type: ignore


class OllamaEmbeddingClient:
    """Generate embeddings through an Ollama server bound to loopback."""

    @_mutmut_mutated(mutants_xǁOllamaEmbeddingClientǁ__init____mutmut)
    def __init__(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_orig(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_1(
        self,
        *,
        base_url: str = "XXhttp://127.0.0.1:11434XX",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_2(
        self,
        *,
        base_url: str = "HTTP://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_3(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "XXembeddinggemmaXX",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_4(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "EMBEDDINGGEMMA",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_5(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 121.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_6(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = None
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_7(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(None)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_8(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_9(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                None
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_10(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "XXThe Ollama embedding model cannot be empty.XX"
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_11(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "the ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_12(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "THE OLLAMA EMBEDDING MODEL CANNOT BE EMPTY."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_13(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds < 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_14(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 1:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_15(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError(None)
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_16(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("XXThe Ollama timeout must be positive.XX")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_17(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("the ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_18(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("THE OLLAMA TIMEOUT MUST BE POSITIVE.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_19(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = None
        self._timeout_seconds = timeout_seconds
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_20(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = None
        self._transport = transport

    def xǁOllamaEmbeddingClientǁ__init____mutmut_21(
        self,
        *,
        base_url: str = "http://127.0.0.1:11434",
        model: str = "embeddinggemma",
        timeout_seconds: float = 120.0,
        transport: Transport = urlopen,
    ) -> None:
        """Configure a local embedding model without remote fallbacks."""
        self._base_url = _validate_loopback_url(base_url)
        if not model.strip():
            raise OllamaConfigurationError(
                "The Ollama embedding model cannot be empty."
            )
        if timeout_seconds <= 0:
            raise OllamaConfigurationError("The Ollama timeout must be positive.")
        self._model = model
        self._timeout_seconds = timeout_seconds
        self._transport = None

    @_mutmut_mutated(mutants_xǁOllamaEmbeddingClientǁembed__mutmut)
    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_orig(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_1(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = None
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_2(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(None)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_3(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs and any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_4(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_5(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(None):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_6(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_7(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError(None)
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_8(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("XXEmbedding inputs cannot be empty.XX")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_9(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_10(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("EMBEDDING INPUTS CANNOT BE EMPTY.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_11(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = None
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_12(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode(None)
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_13(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            None
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_14(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"XXmodelXX": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_15(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"MODEL": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_16(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "XXinputXX": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_17(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "INPUT": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_18(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "XXtruncateXX": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_19(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "TRUNCATE": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_20(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": False}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_21(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("XXutf-8XX")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_22(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("UTF-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_23(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = None
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_24(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            None,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_25(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=None,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_26(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers=None,
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_27(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method=None,
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_28(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_29(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_30(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_31(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_32(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"XXContent-TypeXX": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_33(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"content-type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_34(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"CONTENT-TYPE": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_35(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "XXapplication/jsonXX"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_36(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "APPLICATION/JSON"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_37(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="XXPOSTXX",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_38(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="post",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_39(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(None, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_40(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=None) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_41(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_42(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, ) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_43(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = None
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_44(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                None
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_45(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "XXThe local Ollama embedding service is unavailable.XX"
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_46(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "the local ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_47(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "THE LOCAL OLLAMA EMBEDDING SERVICE IS UNAVAILABLE."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_48(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = None
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_49(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(None)
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_50(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode(None))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_51(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("XXutf-8XX"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_52(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("UTF-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_53(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = None
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_54(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["XXembeddingsXX"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_55(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["EMBEDDINGS"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_56(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs) and any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_57(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list) and len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_58(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_59(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) == len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_60(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    None
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_61(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector and any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_62(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list) and not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_63(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_64(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_65(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(None)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_66(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_67(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                None
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_68(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "XXThe local Ollama embedding service returned an invalid response.XX"
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_69(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "the local ollama embedding service returned an invalid response."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_70(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "THE LOCAL OLLAMA EMBEDDING SERVICE RETURNED AN INVALID RESPONSE."
            ) from exc
        return [[float(value) for value in vector] for vector in embeddings]

    def xǁOllamaEmbeddingClientǁembed__mutmut_71(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one normalized embedding per input using the local model."""
        inputs = list(texts)
        if not inputs or any(not value.strip() for value in inputs):
            raise ValueError("Embedding inputs cannot be empty.")
        body = json.dumps(
            {"model": self._model, "input": inputs, "truncate": True}
        ).encode("utf-8")
        request = Request(
            f"{self._base_url}/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with self._transport(request, timeout=self._timeout_seconds) as response:
                response_body = response.read()
        except (HTTPError, URLError, OSError) as exc:
            raise OllamaConnectionError(
                "The local Ollama embedding service is unavailable."
            ) from exc
        try:
            payload: Any = json.loads(response_body.decode("utf-8"))
            embeddings = payload["embeddings"]
            if (
                not isinstance(embeddings, list)
                or len(embeddings) != len(inputs)
                or any(
                    not isinstance(vector, list)
                    or not vector
                    or any(not isinstance(value, (int, float)) for value in vector)
                    for vector in embeddings
                )
            ):
                raise TypeError
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise OllamaResponseError(
                "The local Ollama embedding service returned an invalid response."
            ) from exc
        return [[float(None) for value in vector] for vector in embeddings]

mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['_mutmut_orig'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_1'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_2'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_3'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_4'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_5'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_6'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_7'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_8'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_9'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_10'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_11'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_12'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_13'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_14'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_15'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_16'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_17'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_18'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_19'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_20'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁ__init____mutmut['xǁOllamaEmbeddingClientǁ__init____mutmut_21'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁ__init____mutmut_21 # type: ignore # mutmut generated

mutants_xǁOllamaEmbeddingClientǁembed__mutmut['_mutmut_orig'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_1'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_2'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_3'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_4'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_5'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_6'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_7'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_8'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_9'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_10'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_11'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_12'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_13'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_14'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_15'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_16'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_17'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_18'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_19'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_20'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_21'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_22'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_23'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_24'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_25'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_26'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_27'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_28'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_29'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_30'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_31'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_32'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_33'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_34'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_35'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_36'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_37'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_38'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_39'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_40'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_41'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_42'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_43'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_44'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_45'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_46'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_47'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_48'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_49'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_50'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_51'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_52'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_53'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_54'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_55'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_56'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_57'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_58'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_59'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_60'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_61'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_62'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_63'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_64'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_65'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_66'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_67'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_68'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_69'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_70'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOllamaEmbeddingClientǁembed__mutmut['xǁOllamaEmbeddingClientǁembed__mutmut_71'] = OllamaEmbeddingClient.xǁOllamaEmbeddingClientǁembed__mutmut_71 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_loopback_url__mutmut)
def _validate_loopback_url(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_orig(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_1(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = None
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_2(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(None)
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_3(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment and parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_4(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query and parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_5(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None and parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_6(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None and parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_7(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"} and parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_8(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http" and parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_9(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme == "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_10(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "XXhttpXX"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_11(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "HTTP"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_12(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_13(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"XX127.0.0.1XX", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_14(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "XXlocalhostXX", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_15(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "LOCALHOST", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_16(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "XX::1XX"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_17(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_18(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_19(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path in {"", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_20(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"XXXX", "/"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_21(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "XX/XX"}
    ):
        raise OllamaConfigurationError(
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_22(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            None
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_23(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "XXOllama must use a plain HTTP loopback endpoint without credentials XX"
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_24(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "ollama must use a plain http loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_25(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "OLLAMA MUST USE A PLAIN HTTP LOOPBACK ENDPOINT WITHOUT CREDENTIALS "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_26(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "XXor a path.XX"
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_27(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "OR A PATH."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_28(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = None
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_29(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            None
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_30(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "XXThe Ollama endpoint has an invalid port.XX"
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_31(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "the ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_32(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "THE OLLAMA ENDPOINT HAS AN INVALID PORT."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_33(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is not None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_34(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            None
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_35(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "XXThe Ollama endpoint must include an explicit port.XX"
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_36(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "the ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_37(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "THE OLLAMA ENDPOINT MUST INCLUDE AN EXPLICIT PORT."
        )
    return base_url.rstrip("/")


def x__validate_loopback_url__mutmut_38(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip(None)


def x__validate_loopback_url__mutmut_39(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.lstrip("/")


def x__validate_loopback_url__mutmut_40(base_url: str) -> str:
    """Validate and normalize a safe loopback-only Ollama URL."""
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
            "Ollama must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise OllamaConfigurationError(
            "The Ollama endpoint has an invalid port."
        ) from exc
    if port is None:
        raise OllamaConfigurationError(
            "The Ollama endpoint must include an explicit port."
        )
    return base_url.rstrip("XX/XX")

mutants_x__validate_loopback_url__mutmut['_mutmut_orig'] = x__validate_loopback_url__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_1'] = x__validate_loopback_url__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_2'] = x__validate_loopback_url__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_3'] = x__validate_loopback_url__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_4'] = x__validate_loopback_url__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_5'] = x__validate_loopback_url__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_6'] = x__validate_loopback_url__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_7'] = x__validate_loopback_url__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_8'] = x__validate_loopback_url__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_9'] = x__validate_loopback_url__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_10'] = x__validate_loopback_url__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_11'] = x__validate_loopback_url__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_12'] = x__validate_loopback_url__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_13'] = x__validate_loopback_url__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_14'] = x__validate_loopback_url__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_15'] = x__validate_loopback_url__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_16'] = x__validate_loopback_url__mutmut_16 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_17'] = x__validate_loopback_url__mutmut_17 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_18'] = x__validate_loopback_url__mutmut_18 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_19'] = x__validate_loopback_url__mutmut_19 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_20'] = x__validate_loopback_url__mutmut_20 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_21'] = x__validate_loopback_url__mutmut_21 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_22'] = x__validate_loopback_url__mutmut_22 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_23'] = x__validate_loopback_url__mutmut_23 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_24'] = x__validate_loopback_url__mutmut_24 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_25'] = x__validate_loopback_url__mutmut_25 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_26'] = x__validate_loopback_url__mutmut_26 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_27'] = x__validate_loopback_url__mutmut_27 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_28'] = x__validate_loopback_url__mutmut_28 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_29'] = x__validate_loopback_url__mutmut_29 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_30'] = x__validate_loopback_url__mutmut_30 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_31'] = x__validate_loopback_url__mutmut_31 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_32'] = x__validate_loopback_url__mutmut_32 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_33'] = x__validate_loopback_url__mutmut_33 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_34'] = x__validate_loopback_url__mutmut_34 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_35'] = x__validate_loopback_url__mutmut_35 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_36'] = x__validate_loopback_url__mutmut_36 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_37'] = x__validate_loopback_url__mutmut_37 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_38'] = x__validate_loopback_url__mutmut_38 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_39'] = x__validate_loopback_url__mutmut_39 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_40'] = x__validate_loopback_url__mutmut_40 # type: ignore # mutmut generated
