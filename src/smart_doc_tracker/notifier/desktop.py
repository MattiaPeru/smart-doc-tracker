"""Native desktop notifications that never leave the local machine."""

from __future__ import annotations

from dataclasses import dataclass

from ..interfaces.plyer_notification_backend import PlyerNotificationBackend


class DesktopNotificationError(RuntimeError):
    """Raised when a native desktop notification cannot be delivered."""


@dataclass(frozen=True, slots=True)
class ExpirationNotification:
    """Prepared, non-sensitive data for one expiration alert."""

    title: str
    message: str


class PlyerDesktopNotifier:
    """Deliver native notifications through the local plyer backend."""

    def __init__(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def send(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                message=notification.message,
                app_name=self._app_name,
                timeout=self._timeout_seconds,
            )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc


def _load_plyer_backend() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return notification
