"""Local-only infrastructure adapters."""

from ..infrastructure.ollama import (
    OllamaClient,
    OllamaConnectionError,
    OllamaEmbeddingClient,
    OllamaResponseError,
)

__all__ = [
    "OllamaClient",
    "OllamaConnectionError",
    "OllamaEmbeddingClient",
    "OllamaResponseError",
]
