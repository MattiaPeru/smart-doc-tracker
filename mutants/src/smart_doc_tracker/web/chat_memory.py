"""Bounded, process-local memory for document chat conversations."""

from __future__ import annotations

import time
from collections import OrderedDict, deque
from collections.abc import Callable
from dataclasses import dataclass, field
from threading import Lock

from ..models.rag import ConversationTurn


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(slots=True)
class _Conversation:
    turns: deque[ConversationTurn]
    last_access: float
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTemporaryChatMemoryǁhistory__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTemporaryChatMemoryǁremember__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTemporaryChatMemoryǁclear__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTemporaryChatMemoryǁ_discard_expired__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut)
    def __post_init__(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_orig(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_1(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns < 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_2(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 1:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_3(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError(None)
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_4(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("XXmax_turns must be positiveXX")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_5(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("MAX_TURNS MUST BE POSITIVE")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_6(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations < 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_7(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 1:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_8(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError(None)
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_9(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("XXmax_conversations must be positiveXX")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_10(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("MAX_CONVERSATIONS MUST BE POSITIVE")
        if self.ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_11(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds < 0:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_12(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 1:
            raise ValueError("ttl_seconds must be positive")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_13(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError(None)

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_14(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("XXttl_seconds must be positiveXX")

    def xǁTemporaryChatMemoryǁ__post_init____mutmut_15(self) -> None:
        """Reject invalid bounds before the memory can accept sensitive turns."""
        if self.max_turns <= 0:
            raise ValueError("max_turns must be positive")
        if self.max_conversations <= 0:
            raise ValueError("max_conversations must be positive")
        if self.ttl_seconds <= 0:
            raise ValueError("TTL_SECONDS MUST BE POSITIVE")

    @_mutmut_mutated(mutants_xǁTemporaryChatMemoryǁhistory__mutmut)
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

    def xǁTemporaryChatMemoryǁhistory__mutmut_orig(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
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

    def xǁTemporaryChatMemoryǁhistory__mutmut_1(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = None
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_2(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(None)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_3(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = None
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_4(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(None)
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_5(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is not None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_6(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                return ()
            conversation.last_access = None
            self._conversations.move_to_end(conversation_id)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_7(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(None)
            return tuple(conversation.turns)

    def xǁTemporaryChatMemoryǁhistory__mutmut_8(self, conversation_id: str) -> tuple[ConversationTurn, ...]:
        """Return a stable snapshot of one active conversation."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                return ()
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)
            return tuple(None)

    @_mutmut_mutated(mutants_xǁTemporaryChatMemoryǁremember__mutmut)
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

    def xǁTemporaryChatMemoryǁremember__mutmut_orig(self, conversation_id: str, turn: ConversationTurn) -> None:
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

    def xǁTemporaryChatMemoryǁremember__mutmut_1(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = None
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

    def xǁTemporaryChatMemoryǁremember__mutmut_2(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(None)
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

    def xǁTemporaryChatMemoryǁremember__mutmut_3(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = None
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

    def xǁTemporaryChatMemoryǁremember__mutmut_4(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(None)
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

    def xǁTemporaryChatMemoryǁremember__mutmut_5(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is not None:
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

    def xǁTemporaryChatMemoryǁremember__mutmut_6(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) > self.max_conversations:
                    self._conversations.popitem(last=False)
                conversation = _Conversation(
                    turns=deque(maxlen=self.max_turns),
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_7(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=None)
                conversation = _Conversation(
                    turns=deque(maxlen=self.max_turns),
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_8(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=True)
                conversation = _Conversation(
                    turns=deque(maxlen=self.max_turns),
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_9(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=False)
                conversation = None
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_10(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=False)
                conversation = _Conversation(
                    turns=None,
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_11(self, conversation_id: str, turn: ConversationTurn) -> None:
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
                    last_access=None,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_12(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=False)
                conversation = _Conversation(
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_13(self, conversation_id: str, turn: ConversationTurn) -> None:
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
                    )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_14(self, conversation_id: str, turn: ConversationTurn) -> None:
        """Append one completed exchange and enforce all memory bounds."""
        with self._lock:
            now = self.clock()
            self._discard_expired(now)
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                while len(self._conversations) >= self.max_conversations:
                    self._conversations.popitem(last=False)
                conversation = _Conversation(
                    turns=deque(maxlen=None),
                    last_access=now,
                )
                self._conversations[conversation_id] = conversation
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_15(self, conversation_id: str, turn: ConversationTurn) -> None:
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
                self._conversations[conversation_id] = None
            conversation.turns.append(turn)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_16(self, conversation_id: str, turn: ConversationTurn) -> None:
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
            conversation.turns.append(None)
            conversation.last_access = now
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_17(self, conversation_id: str, turn: ConversationTurn) -> None:
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
            conversation.last_access = None
            self._conversations.move_to_end(conversation_id)

    def xǁTemporaryChatMemoryǁremember__mutmut_18(self, conversation_id: str, turn: ConversationTurn) -> None:
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
            self._conversations.move_to_end(None)

    @_mutmut_mutated(mutants_xǁTemporaryChatMemoryǁclear__mutmut)
    def clear(self, conversation_id: str) -> None:
        """Forget one conversation immediately."""
        with self._lock:
            self._conversations.pop(conversation_id, None)

    def xǁTemporaryChatMemoryǁclear__mutmut_orig(self, conversation_id: str) -> None:
        """Forget one conversation immediately."""
        with self._lock:
            self._conversations.pop(conversation_id, None)

    def xǁTemporaryChatMemoryǁclear__mutmut_1(self, conversation_id: str) -> None:
        """Forget one conversation immediately."""
        with self._lock:
            self._conversations.pop(None, None)

    def xǁTemporaryChatMemoryǁclear__mutmut_2(self, conversation_id: str) -> None:
        """Forget one conversation immediately."""
        with self._lock:
            self._conversations.pop(None)

    def xǁTemporaryChatMemoryǁclear__mutmut_3(self, conversation_id: str) -> None:
        """Forget one conversation immediately."""
        with self._lock:
            self._conversations.pop(conversation_id, )

    def clear_all(self) -> None:
        """Forget every conversation, including during application shutdown."""
        with self._lock:
            self._conversations.clear()

    @_mutmut_mutated(mutants_xǁTemporaryChatMemoryǁ_discard_expired__mutmut)
    def _discard_expired(self, now: float) -> None:
        """Remove conversations whose inactivity reached the configured TTL."""
        expired = [
            conversation_id
            for conversation_id, conversation in self._conversations.items()
            if now - conversation.last_access >= self.ttl_seconds
        ]
        for conversation_id in expired:
            del self._conversations[conversation_id]

    def xǁTemporaryChatMemoryǁ_discard_expired__mutmut_orig(self, now: float) -> None:
        """Remove conversations whose inactivity reached the configured TTL."""
        expired = [
            conversation_id
            for conversation_id, conversation in self._conversations.items()
            if now - conversation.last_access >= self.ttl_seconds
        ]
        for conversation_id in expired:
            del self._conversations[conversation_id]

    def xǁTemporaryChatMemoryǁ_discard_expired__mutmut_1(self, now: float) -> None:
        """Remove conversations whose inactivity reached the configured TTL."""
        expired = None
        for conversation_id in expired:
            del self._conversations[conversation_id]

    def xǁTemporaryChatMemoryǁ_discard_expired__mutmut_2(self, now: float) -> None:
        """Remove conversations whose inactivity reached the configured TTL."""
        expired = [
            conversation_id
            for conversation_id, conversation in self._conversations.items()
            if now + conversation.last_access >= self.ttl_seconds
        ]
        for conversation_id in expired:
            del self._conversations[conversation_id]

    def xǁTemporaryChatMemoryǁ_discard_expired__mutmut_3(self, now: float) -> None:
        """Remove conversations whose inactivity reached the configured TTL."""
        expired = [
            conversation_id
            for conversation_id, conversation in self._conversations.items()
            if now - conversation.last_access > self.ttl_seconds
        ]
        for conversation_id in expired:
            del self._conversations[conversation_id]

mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['_mutmut_orig'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_1'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_2'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_3'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_4'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_5'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_6'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_7'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_8'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_9'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_10'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_11'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_12'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_13'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_14'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ__post_init____mutmut['xǁTemporaryChatMemoryǁ__post_init____mutmut_15'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ__post_init____mutmut_15 # type: ignore # mutmut generated

mutants_xǁTemporaryChatMemoryǁhistory__mutmut['_mutmut_orig'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_1'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_2'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_3'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_4'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_5'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_6'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_7'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁhistory__mutmut['xǁTemporaryChatMemoryǁhistory__mutmut_8'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁhistory__mutmut_8 # type: ignore # mutmut generated

mutants_xǁTemporaryChatMemoryǁremember__mutmut['_mutmut_orig'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_1'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_2'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_3'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_4'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_5'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_6'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_7'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_8'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_9'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_10'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_11'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_12'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_13'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_14'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_15'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_16'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_17'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁremember__mutmut['xǁTemporaryChatMemoryǁremember__mutmut_18'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁremember__mutmut_18 # type: ignore # mutmut generated

mutants_xǁTemporaryChatMemoryǁclear__mutmut['_mutmut_orig'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁclear__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁclear__mutmut['xǁTemporaryChatMemoryǁclear__mutmut_1'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁclear__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁclear__mutmut['xǁTemporaryChatMemoryǁclear__mutmut_2'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁclear__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁclear__mutmut['xǁTemporaryChatMemoryǁclear__mutmut_3'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁclear__mutmut_3 # type: ignore # mutmut generated

mutants_xǁTemporaryChatMemoryǁ_discard_expired__mutmut['_mutmut_orig'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ_discard_expired__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ_discard_expired__mutmut['xǁTemporaryChatMemoryǁ_discard_expired__mutmut_1'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ_discard_expired__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ_discard_expired__mutmut['xǁTemporaryChatMemoryǁ_discard_expired__mutmut_2'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ_discard_expired__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTemporaryChatMemoryǁ_discard_expired__mutmut['xǁTemporaryChatMemoryǁ_discard_expired__mutmut_3'] = TemporaryChatMemory.xǁTemporaryChatMemoryǁ_discard_expired__mutmut_3 # type: ignore # mutmut generated
