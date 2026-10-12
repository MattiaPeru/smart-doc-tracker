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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
