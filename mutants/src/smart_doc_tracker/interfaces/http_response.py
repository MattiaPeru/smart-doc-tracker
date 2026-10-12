"""Response interface for the local Ollama HTTP transport."""

from __future__ import annotations

from typing import Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class HTTPResponse(Protocol):
    """Expose the response operations required by the Ollama adapter."""

    def __enter__(self) -> HTTPResponse:
        """Open the response context."""
        ...

    def __exit__(self, *args: object) -> None:
        """Close the response context."""
        ...

    def read(self) -> bytes:
        """Read the complete response body."""
        ...
