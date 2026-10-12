from __future__ import annotations

from unittest import TestCase

from smart_doc_tracker.models.rag import ConversationTurn
from smart_doc_tracker.web.chat_memory import TemporaryChatMemory


class TemporaryChatMemoryTests(TestCase):
    def test_keeps_only_the_most_recent_bounded_turns(self) -> None:
        memory = TemporaryChatMemory(max_turns=2)

        memory.remember("conversation", self._turn("First"))
        memory.remember("conversation", self._turn("Second"))
        memory.remember("conversation", self._turn("Third"))

        self.assertEqual(
            [turn.question for turn in memory.history("conversation")],
            ["Second", "Third"],
        )

    def test_expires_and_clears_conversations_without_persistence(self) -> None:
        current_time = [10.0]
        memory = TemporaryChatMemory(
            ttl_seconds=5,
            clock=lambda: current_time[0],
        )
        memory.remember("expired", self._turn("Sensitive question"))
        memory.remember("cleared", self._turn("Another question"))

        memory.clear("cleared")
        current_time[0] = 15.0

        self.assertEqual(memory.history("expired"), ())
        self.assertEqual(memory.history("cleared"), ())

    @staticmethod
    def _turn(question: str) -> ConversationTurn:
        return ConversationTurn(question, "Local answer", ("doc-1",))
