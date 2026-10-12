from __future__ import annotations

from typing import Any
from unittest import TestCase

from smart_doc_tracker.notifier.desktop import (
    DesktopNotificationError,
    ExpirationNotification,
    PlyerDesktopNotifier,
)


class FakeBackend:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error
        self.calls: list[dict[str, Any]] = []

    def notify(self, **kwargs: Any) -> None:
        if self.error is not None:
            raise self.error
        self.calls.append(kwargs)


class PlyerDesktopNotifierTests(TestCase):
    def test_sends_prepared_notification_to_native_backend(self) -> None:
        backend = FakeBackend()
        notifier = PlyerDesktopNotifier(backend, timeout_seconds=7)

        notifier.send(ExpirationNotification("Reminder", "A document expires soon."))

        self.assertEqual(
            backend.calls,
            [
                {
                    "title": "Reminder",
                    "message": "A document expires soon.",
                    "app_name": "Smart Doc Tracker",
                    "timeout": 7,
                }
            ],
        )

    def test_wraps_backend_failure_without_notification_contents(self) -> None:
        notifier = PlyerDesktopNotifier(FakeBackend(RuntimeError("private payload")))

        with self.assertRaises(DesktopNotificationError) as context:
            notifier.send(ExpirationNotification("Reminder", "Sensitive message"))

        self.assertNotIn("Sensitive", str(context.exception))
        self.assertNotIn("private payload", str(context.exception))
