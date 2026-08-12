from __future__ import annotations

from datetime import UTC, date, datetime
from unittest import TestCase

from db.database import StoredDocument
from models.document import DocumentData
from notifier.desktop import ExpirationNotification
from pipeline import ExpirationTrackingPipeline


class FakeExpirationRepository:
    def __init__(self, documents: list[StoredDocument]) -> None:
        self.documents = documents
        self.calls: list[tuple[int, date | None]] = []

    def get_expiring_documents(
        self, days_threshold: int, *, today: date | None = None
    ) -> list[StoredDocument]:
        self.calls.append((days_threshold, today))
        return list(self.documents)


class FakeNotifier:
    def __init__(self) -> None:
        self.notifications: list[ExpirationNotification] = []

    def send(self, notification: ExpirationNotification) -> None:
        self.notifications.append(notification)


def _stored_document() -> StoredDocument:
    return StoredDocument(
        id="64b64b64b64b64b64b64b64b",
        file_hash="a" * 64,
        document=DocumentData(
            document_type="insurance_policy",
            summary="Policy for a private vehicle",
            expiry_date="2026-08-30",
            issue_date="2025-08-30",
            extracted_data={"policy_number": "PRIVATE-123"},
        ),
        created_at=datetime(2026, 8, 1, tzinfo=UTC),
    )


class ExpirationTrackingPipelineTests(TestCase):
    def test_queries_inclusive_window_and_sends_minimal_alert(self) -> None:
        repository = FakeExpirationRepository([_stored_document()])
        notifier = FakeNotifier()
        today = date(2026, 8, 12)

        result = ExpirationTrackingPipeline(
            repository,
            notifier,
            today_provider=lambda: today,
        ).check(30)

        self.assertEqual(repository.calls, [(30, today)])
        self.assertEqual(result.documents_found, 1)
        self.assertEqual(result.notifications_sent, 1)
        self.assertEqual(
            notifier.notifications,
            [
                ExpirationNotification(
                    title="Document expiration reminder",
                    message="Insurance Policy expires on 2026-08-30.",
                )
            ],
        )
        self.assertNotIn("PRIVATE-123", notifier.notifications[0].message)

    def test_rejects_negative_threshold_before_querying(self) -> None:
        repository = FakeExpirationRepository([])

        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            ExpirationTrackingPipeline(repository, FakeNotifier()).check(-1)

        self.assertEqual(repository.calls, [])
