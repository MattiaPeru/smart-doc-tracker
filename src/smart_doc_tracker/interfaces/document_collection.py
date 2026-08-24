"""Collection interface for local MongoDB persistence."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Protocol


class DocumentCollection(Protocol):
    """Expose the MongoDB collection operations used by the repository."""

    def create_index(self, keys: Any, **kwargs: Any) -> str:
        """Create an index for the collection."""
        ...

    def update_one(
        self,
        filter: Mapping[str, Any],
        update: Mapping[str, Any] | Sequence[Mapping[str, Any]],
        **kwargs: Any,
    ) -> Any:
        """Update or upsert one matching record."""
        ...

    def find_one(self, filter: Mapping[str, Any]) -> dict[str, Any] | None:
        """Return one matching record when present."""
        ...

    def find(self, filter: Mapping[str, Any]) -> Any:
        """Return a cursor over matching records."""
        ...
