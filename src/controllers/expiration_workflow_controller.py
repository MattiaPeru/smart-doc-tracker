"""CLI workflows for one-time and scheduled expiration checks."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import time

from cli.dependencies import CliDependencies
from cli.serializer import JsonResultSerializer
from controllers.document_manager import DocumentManager
from controllers.expiration_controller import ExpirationController
from db.database import DatabaseConfigurationError, DatabaseError, MongoDocumentRepository
from notifier.desktop import DesktopNotificationError, PlyerDesktopNotifier
from scheduler import DailyTaskScheduler, SchedulerConfigurationError, SchedulerError


@dataclass(slots=True)
class ExpirationWorkflowController:
    """Coordinate repositories, notifications, scheduling, and CLI output."""

    dependencies: CliDependencies

    def check_expirations(self, days_threshold: int = 30) -> int:
        """Run one expiration check and print its summary."""
        dependencies = self.dependencies
        try:
            print(
                f"[1/1] Checking documents expiring within {days_threshold} day(s)...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            notifier = dependencies.notifier or PlyerDesktopNotifier()
            with create_repository() as repository:
                result = ExpirationController(
                    DocumentManager(repository),
                    notifier,
                ).check(days_threshold)
        except (
            DatabaseConfigurationError,
            DatabaseError,
            DesktopNotificationError,
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
        days_threshold: int = 30,
        *,
        check_time: time,
    ) -> int:
        """Schedule recurring local expiration checks in the foreground."""
        dependencies = self.dependencies
        create_repository = (
            dependencies.repository_factory or MongoDocumentRepository.connect
        )
        notifier = dependencies.notifier or PlyerDesktopNotifier()

        def scheduled_check() -> None:
            """Execute one scheduled expiration check and report its outcome."""
            try:
                with create_repository() as repository:
                    result = ExpirationController(
                        DocumentManager(repository),
                        notifier,
                    ).check(days_threshold)
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
            ) as exc:
                print(
                    f"Daily expiration check failed: {exc}",
                    file=dependencies.stderr,
                    flush=True,
                )

        create_scheduler = dependencies.scheduler_factory or (
            lambda task, scheduled_time: DailyTaskScheduler(
                task,
                check_time=scheduled_time,
            )
        )
        print(
            f"Expiration monitoring scheduled daily at {check_time.strftime('%H:%M')}.",
            file=dependencies.stderr,
            flush=True,
        )
        try:
            create_scheduler(scheduled_check, check_time).run()
        except KeyboardInterrupt:
            print("Expiration monitoring stopped.", file=dependencies.stderr)
            return 0
        except (SchedulerConfigurationError, SchedulerError) as exc:
            print(f"Expiration monitoring failed: {exc}", file=dependencies.stderr)
            return 1
        return 0
