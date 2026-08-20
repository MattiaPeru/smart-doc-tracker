"""Expiration checks and local notifications for stored documents."""

from __future__ import annotations

from dataclasses import dataclass

from controllers.document_manager import DocumentManager
from notifier.desktop import ExpirationNotification
from pipeline import ExpirationCheckResult, NotificationSender


@dataclass(slots=True)
class ExpirationController:
    """Check document dates and deliver prepared local expiration alerts."""

    document_manager: DocumentManager
    notifier: NotificationSender

    def check(self, days_threshold: int = 30) -> ExpirationCheckResult:
        """Notify once for each document expiring inside the requested window."""
        documents = self.document_manager.get_expiring_documents(days_threshold)
        notifications_sent = 0
        for record in documents:
            expiry_date = record.document.expiry_date
            if expiry_date is None:
                continue
            document_label = record.document.document_type.replace("_", " ").title()
            self.notifier.send(
                ExpirationNotification(
                    title="Document expiration reminder",
                    message=f"{document_label} expires on {expiry_date.isoformat()}.",
                )
            )
            notifications_sent += 1

        return ExpirationCheckResult(
            documents_found=len(documents),
            notifications_sent=notifications_sent,
        )
