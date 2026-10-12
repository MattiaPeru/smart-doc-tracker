"""Backend interface for native desktop notifications."""

from __future__ import annotations

from typing import Any, Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PlyerNotificationBackend(Protocol):
    """Expose the native notification operation used by the adapter."""

    def notify(self, **kwargs: Any) -> None:
        """Deliver one native desktop notification."""
        ...
