"""Local-only infrastructure adapters."""

from infrastructure.ollama import OllamaClient, OllamaConnectionError, OllamaResponseError

__all__ = ["OllamaClient", "OllamaConnectionError", "OllamaResponseError"]
