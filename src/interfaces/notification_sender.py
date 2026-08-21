"""Delivery interface for prepared notifications."""

from __future__ import annotations

from typing import Protocol

from notifier.desktop import ExpirationNotification


class NotificationSender(Protocol):
    """Send prepared local notifications."""

    def send(self, notification: ExpirationNotification) -> None:
        """Deliver one prepared local notification."""
        ...
