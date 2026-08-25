"""Embedding interface for a local semantic model."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol


class EmbeddingGenerator(Protocol):
    """Create vector embeddings without transmitting text off the host."""

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        """Return one embedding for each input text in the same order."""
        ...
