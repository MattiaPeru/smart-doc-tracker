"""Text recognition interface for decoded images."""

from __future__ import annotations

from typing import Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class TextReader(Protocol):
    """Extract text from a decoded local image."""

    def __call__(self, image: object, *, lang: str) -> str:
        """Extract text using the requested language."""
        ...
