"""Embedding interface for a local semantic model."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class EmbeddingGenerator(Protocol):
    """Create vector embeddings without transmitting text off the host."""

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one embedding for each input text in the same order."""
        ...
