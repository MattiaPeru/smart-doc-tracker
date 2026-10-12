"""Text generation interface for a local language model."""

from __future__ import annotations

from typing import Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class TextGenerator(Protocol):
    """Generate text using a locally hosted model."""

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Generate text from system and user prompts."""
        ...
