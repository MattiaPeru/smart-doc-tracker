"""Local notification interfaces and adapters."""

from ..notifier.desktop import (
    DesktopNotificationError,
    ExpirationNotification,
    PlyerDesktopNotifier,
)

__all__ = [
    "DesktopNotificationError",
    "ExpirationNotification",
    "PlyerDesktopNotifier",
]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
