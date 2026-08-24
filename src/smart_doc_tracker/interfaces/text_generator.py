"""Text generation interface for a local language model."""

from __future__ import annotations

from typing import Protocol


class TextGenerator(Protocol):
    """Generate text using a locally hosted model."""

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Generate text from system and user prompts."""
        ...
