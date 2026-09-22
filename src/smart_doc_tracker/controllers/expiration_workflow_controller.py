"""CLI workflows for one-time and scheduled expiration checks."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import time

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)
from ..notifier.desktop import DesktopNotificationError, PlyerDesktopNotifier
from ..pipeline import ExpirationTrackingPipeline
from ..scheduler import DailyTaskScheduler, SchedulerConfigurationError, SchedulerError
from ..settings import LocalReminderSettingsStore, ReminderSettingsError


@dataclass(slots=True)
class ExpirationWorkflowController:
    """Coordinate repositories, notifications, scheduling, and CLI output."""

    dependencies: CliDependencies

    def check_expirations(self, days_threshold: int | None = None) -> int:
        """Run one expiration check and print its summary."""
        dependencies = self.dependencies
        try:
            effective_threshold = self._days_threshold(days_threshold)
            print(
                "[1/1] Checking documents expiring using "
                f"a {effective_threshold}-day default...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            notifier = dependencies.notifier or PlyerDesktopNotifier()
            with create_repository() as repository:
                result = ExpirationTrackingPipeline(
                    repository,
                    notifier,
                ).check(effective_threshold)
        except (
            DatabaseConfigurationError,
            DatabaseError,
            DesktopNotificationError,
            ReminderSettingsError,
        ) as exc:
            print(f"Expiration check failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Expiration check completed: "
            f"{result.documents_found} document(s), "
            f"{result.notifications_sent} notification(s).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.expiration_result(result),
            dependencies.stdout,
        )
        return 0

    def monitor_expirations(
        self,
        days_threshold: int | None = None,
        *,
        check_time: time,
    ) -> int:
        """Schedule recurring local expiration checks in the foreground."""
        dependencies = self.dependencies
        try:
            self._days_threshold(days_threshold)
        except ReminderSettingsError as exc:
            print(f"Expiration monitoring failed: {exc}", file=dependencies.stderr)
            return 1
        create_repository = (
            dependencies.repository_factory or MongoDocumentRepository.connect
        )
        notifier = dependencies.notifier or PlyerDesktopNotifier()

        def scheduled_check() -> None:
            """Execute one scheduled expiration check and report its outcome."""
            try:
                effective_threshold = self._days_threshold(days_threshold)
                with create_repository() as repository:
                    result = ExpirationTrackingPipeline(
                        repository,
                        notifier,
                    ).check(effective_threshold)
                print(
                    "Daily expiration check completed: "
                    f"{result.documents_found} document(s), "
                    f"{result.notifications_sent} notification(s).",
                    file=dependencies.stderr,
                    flush=True,
                )
            except (
                DatabaseConfigurationError,
                DatabaseError,
                DesktopNotificationError,
                ReminderSettingsError,
            ) as exc:
                print(
                    f"Daily expiration check failed: {exc}",
                    file=dependencies.stderr,
                    flush=True,
                )

        scheduler = dependencies.scheduler or DailyTaskScheduler()
        print(
            f"Expiration monitoring scheduled daily at {check_time.strftime('%H:%M')}.",
            file=dependencies.stderr,
            flush=True,
        )
        try:
            scheduler.run(scheduled_check, check_time=check_time)
        except KeyboardInterrupt:
            print("Expiration monitoring stopped.", file=dependencies.stderr)
            return 0
        except (SchedulerConfigurationError, SchedulerError) as exc:
            print(f"Expiration monitoring failed: {exc}", file=dependencies.stderr)
            return 1
        return 0

    def _days_threshold(self, override: int | None) -> int:
        """Resolve an explicit CLI override or the durable local default."""
        if override is not None:
            return override
        store = self.dependencies.reminder_settings or LocalReminderSettingsStore()
        return store.load().default_notification_days_before
