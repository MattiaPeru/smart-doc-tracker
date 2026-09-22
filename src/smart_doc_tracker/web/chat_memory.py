"""Bounded, process-local memory for document chat conversations."""

from __future__ import annotations

import time
from collections import OrderedDict, deque
from collections.abc import Callable
from dataclasses import dataclass, field
from threading import Lock

from ..models.rag import ConversationTurn


@dataclass(slots=True)
class _Conversation:
    turns: deque[ConversationTurn]
    last_access: float


@dataclass(slots=True)
class TemporaryChatMemory:
    """Keep a small number of recent chat turns in memory and never on disk."""

    max_turns: int = 6
    max_conversations: int = 100
    ttl_seconds: float = 30 * 60
    clock: Callable[[], float] = time.monotonic
    _conversations: OrderedDict[str, _Conversation] = field(
        default_factory=OrderedDict,
        init=False,
        repr=False,
    )
    _lock: Lock = field(default_factory=Lock, init=False, repr=False)

    def __post_init__(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def history(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def remember(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=False)
                conversation = _Conversation(
                    turns=deque(maxlen=self.max_turns),
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def clear(self, conversation_id: str) -> None:
        """Forget one conversation immediately."""
        with self._lock:
            self._conversations.pop(conversation_id, None)

    def clear_all(self) -> None:
        """Forget every conversation, including during application shutdown."""
        with self._lock:
            self._conversations.clear()

    def _discard_expired(self, now: float) -> None:
        """Remove conversations whose inactivity reached the configured TTL."""
        expired = [
            conversation_id
            for conversation_id, conversation in self._conversations.items()
            if now - conversation.last_access >= self.ttl_seconds
        ]
        for conversation_id in expired:
            del self._conversations[conversation_id]
