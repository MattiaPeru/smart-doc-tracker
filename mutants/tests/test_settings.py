from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from smart_doc_tracker.settings import LocalReminderSettingsStore, ReminderSettings


class LocalReminderSettingsStoreTests(TestCase):
    def test_defaults_to_thirty_days_and_persists_a_validated_value(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "settings.json"
            store = LocalReminderSettingsStore(path)

            self.assertEqual(store.load().default_notification_days_before, 30)

            store.save(ReminderSettings(default_notification_days_before=14))

            self.assertEqual(store.load().default_notification_days_before, 14)
            self.assertFalse(list(path.parent.glob("*.tmp")))
