"""Delivery interface for prepared notifications."""

from __future__ import annotations

from typing import Protocol

from ..notifier.desktop import ExpirationNotification


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class NotificationSender(Protocol):
    """Send prepared local notifications."""

    def send(self, notification: ExpirationNotification) -> None:
        """Deliver one prepared local notification."""
        ...
