"""Native desktop notifications that never leave the local machine."""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from ..interfaces.plyer_notification_backend import PlyerNotificationBackend


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DesktopNotificationError(RuntimeError):
    """Raised when a native desktop notification cannot be delivered."""


@dataclass(frozen=True, slots=True)
class ExpirationNotification:
    """Prepared, non-sensitive data for one expiration alert."""

    title: str
    message: str
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPlyerDesktopNotifierǁsend__mutmut: MutantDict = {}  # type: ignore


class PlyerDesktopNotifier:
    """Deliver native notifications through the local plyer backend."""

    @_mutmut_mutated(mutants_xǁPlyerDesktopNotifierǁ__init____mutmut)
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

    def xǁPlyerDesktopNotifierǁ__init____mutmut_orig(
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

    def xǁPlyerDesktopNotifierǁ__init____mutmut_1(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "XXSmart Doc TrackerXX",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_2(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "smart doc tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_3(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "SMART DOC TRACKER",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_4(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 11,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_5(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds < 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_6(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 1:
            raise ValueError("timeout_seconds must be positive")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_7(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError(None)
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_8(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("XXtimeout_seconds must be positiveXX")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_9(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("TIMEOUT_SECONDS MUST BE POSITIVE")
        self._backend = backend
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_10(
        self,
        backend: PlyerNotificationBackend | None = None,
        *,
        app_name: str = "Smart Doc Tracker",
        timeout_seconds: int = 10,
    ) -> None:
        """Configure the local notification backend and display options."""
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        self._backend = None
        self._app_name = app_name
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_11(
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
        self._app_name = None
        self._timeout_seconds = timeout_seconds

    def xǁPlyerDesktopNotifierǁ__init____mutmut_12(
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
        self._timeout_seconds = None

    @_mutmut_mutated(mutants_xǁPlyerDesktopNotifierǁsend__mutmut)
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

    def xǁPlyerDesktopNotifierǁsend__mutmut_orig(self, notification: ExpirationNotification) -> None:
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

    def xǁPlyerDesktopNotifierǁsend__mutmut_1(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = None
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

    def xǁPlyerDesktopNotifierǁsend__mutmut_2(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend and _load_plyer_backend()
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

    def xǁPlyerDesktopNotifierǁsend__mutmut_3(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=None,
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

    def xǁPlyerDesktopNotifierǁsend__mutmut_4(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                message=None,
                app_name=self._app_name,
                timeout=self._timeout_seconds,
            )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_5(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                message=notification.message,
                app_name=None,
                timeout=self._timeout_seconds,
            )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_6(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                message=notification.message,
                app_name=self._app_name,
                timeout=None,
            )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_7(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
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

    def xǁPlyerDesktopNotifierǁsend__mutmut_8(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                app_name=self._app_name,
                timeout=self._timeout_seconds,
            )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_9(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                message=notification.message,
                timeout=self._timeout_seconds,
            )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_10(self, notification: ExpirationNotification) -> None:
        """Send one prepared alert without logging its contents."""
        try:
            backend = self._backend or _load_plyer_backend()
            backend.notify(
                title=notification.title,
                message=notification.message,
                app_name=self._app_name,
                )
        except DesktopNotificationError:
            raise
        except Exception as exc:
            raise DesktopNotificationError(
                "The local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_11(self, notification: ExpirationNotification) -> None:
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
                None
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_12(self, notification: ExpirationNotification) -> None:
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
                "XXThe local desktop notification could not be delivered.XX"
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_13(self, notification: ExpirationNotification) -> None:
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
                "the local desktop notification could not be delivered."
            ) from exc

    def xǁPlyerDesktopNotifierǁsend__mutmut_14(self, notification: ExpirationNotification) -> None:
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
                "THE LOCAL DESKTOP NOTIFICATION COULD NOT BE DELIVERED."
            ) from exc

mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['_mutmut_orig'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_1'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_2'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_3'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_4'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_5'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_6'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_7'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_8'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_9'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_10'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_11'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁ__init____mutmut['xǁPlyerDesktopNotifierǁ__init____mutmut_12'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁ__init____mutmut_12 # type: ignore # mutmut generated

mutants_xǁPlyerDesktopNotifierǁsend__mutmut['_mutmut_orig'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_1'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_2'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_3'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_4'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_5'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_6'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_7'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_8'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_9'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_10'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_11'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_12'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_13'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPlyerDesktopNotifierǁsend__mutmut['xǁPlyerDesktopNotifierǁsend__mutmut_14'] = PlyerDesktopNotifier.xǁPlyerDesktopNotifierǁsend__mutmut_14 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_plyer_backend__mutmut)
def _load_plyer_backend() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(PlyerNotificationBackend, notification)


def x__load_plyer_backend__mutmut_orig() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(PlyerNotificationBackend, notification)


def x__load_plyer_backend__mutmut_1() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            None
        ) from exc
    return cast(PlyerNotificationBackend, notification)


def x__load_plyer_backend__mutmut_2() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "XXDesktop notifications require the locally installed plyer package.XX"
        ) from exc
    return cast(PlyerNotificationBackend, notification)


def x__load_plyer_backend__mutmut_3() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(PlyerNotificationBackend, notification)


def x__load_plyer_backend__mutmut_4() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "DESKTOP NOTIFICATIONS REQUIRE THE LOCALLY INSTALLED PLYER PACKAGE."
        ) from exc
    return cast(PlyerNotificationBackend, notification)


def x__load_plyer_backend__mutmut_5() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(None, notification)


def x__load_plyer_backend__mutmut_6() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(PlyerNotificationBackend, None)


def x__load_plyer_backend__mutmut_7() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(notification)


def x__load_plyer_backend__mutmut_8() -> PlyerNotificationBackend:
    """Load the locally installed plyer notification backend."""
    try:
        from plyer import notification
    except ImportError as exc:
        raise DesktopNotificationError(
            "Desktop notifications require the locally installed plyer package."
        ) from exc
    return cast(PlyerNotificationBackend, )

mutants_x__load_plyer_backend__mutmut['_mutmut_orig'] = x__load_plyer_backend__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_1'] = x__load_plyer_backend__mutmut_1 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_2'] = x__load_plyer_backend__mutmut_2 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_3'] = x__load_plyer_backend__mutmut_3 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_4'] = x__load_plyer_backend__mutmut_4 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_5'] = x__load_plyer_backend__mutmut_5 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_6'] = x__load_plyer_backend__mutmut_6 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_7'] = x__load_plyer_backend__mutmut_7 # type: ignore # mutmut generated
mutants_x__load_plyer_backend__mutmut['x__load_plyer_backend__mutmut_8'] = x__load_plyer_backend__mutmut_8 # type: ignore # mutmut generated
