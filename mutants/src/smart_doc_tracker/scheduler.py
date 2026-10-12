"""Local scheduling for recurring expiration checks."""

from __future__ import annotations

from collections.abc import Callable
from datetime import time
from typing import cast

from .interfaces.blocking_scheduler_backend import BlockingSchedulerBackend


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SchedulerConfigurationError(ValueError):
    """Raised when the daily schedule is invalid or unavailable."""


class SchedulerError(RuntimeError):
    """Raised when the local scheduler cannot run."""
mutants_x_parse_daily_time__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_daily_time__mutmut)
def parse_daily_time(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_orig(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_1(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = None
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_2(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(None)
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_3(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split("XX:XX")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_4(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 and len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_5(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) == 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_6(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 3 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_7(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) == 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_8(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 3:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_9(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=None, minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_10(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=None)
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_11(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_12(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), )
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_13(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(None), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_14(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(None))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour HH:MM format"
        ) from exc


def x_parse_daily_time__mutmut_15(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            None
        ) from exc


def x_parse_daily_time__mutmut_16(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "XXcheck_time must use 24-hour HH:MM formatXX"
        ) from exc


def x_parse_daily_time__mutmut_17(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "check_time must use 24-hour hh:mm format"
        ) from exc


def x_parse_daily_time__mutmut_18(value: str) -> time:
    """Parse a strict local 24-hour HH:MM value."""
    try:
        hour_text, minute_text = value.split(":")
        if len(hour_text) != 2 or len(minute_text) != 2:
            raise ValueError
        return time(hour=int(hour_text), minute=int(minute_text))
    except (AttributeError, TypeError, ValueError) as exc:
        raise SchedulerConfigurationError(
            "CHECK_TIME MUST USE 24-HOUR HH:MM FORMAT"
        ) from exc

mutants_x_parse_daily_time__mutmut['_mutmut_orig'] = x_parse_daily_time__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_1'] = x_parse_daily_time__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_2'] = x_parse_daily_time__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_3'] = x_parse_daily_time__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_4'] = x_parse_daily_time__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_5'] = x_parse_daily_time__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_6'] = x_parse_daily_time__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_7'] = x_parse_daily_time__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_8'] = x_parse_daily_time__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_9'] = x_parse_daily_time__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_10'] = x_parse_daily_time__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_11'] = x_parse_daily_time__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_12'] = x_parse_daily_time__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_13'] = x_parse_daily_time__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_14'] = x_parse_daily_time__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_15'] = x_parse_daily_time__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_16'] = x_parse_daily_time__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_17'] = x_parse_daily_time__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_daily_time__mutmut['x_parse_daily_time__mutmut_18'] = x_parse_daily_time__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDailyTaskSchedulerǁrun__mutmut: MutantDict = {}  # type: ignore


class DailyTaskScheduler:
    """Run one callable every day using the host's local timezone."""

    @_mutmut_mutated(mutants_xǁDailyTaskSchedulerǁ__init____mutmut)
    def __init__(
        self,
        backend: BlockingSchedulerBackend | None = None,
    ) -> None:
        """Configure the local scheduler backend."""
        self._backend = backend

    def xǁDailyTaskSchedulerǁ__init____mutmut_orig(
        self,
        backend: BlockingSchedulerBackend | None = None,
    ) -> None:
        """Configure the local scheduler backend."""
        self._backend = backend

    def xǁDailyTaskSchedulerǁ__init____mutmut_1(
        self,
        backend: BlockingSchedulerBackend | None = None,
    ) -> None:
        """Configure the local scheduler backend."""
        self._backend = None

    @_mutmut_mutated(mutants_xǁDailyTaskSchedulerǁrun__mutmut)
    def run(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_orig(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_1(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = None
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_2(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend and _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_3(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                None,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_4(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger=None,
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_5(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=None,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_6(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=None,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_7(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id=None,
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_8(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=None,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_9(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=None,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_10(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=None,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_11(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_12(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_13(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_14(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_15(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_16(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_17(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_18(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_19(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="XXcronXX",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_20(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="CRON",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_21(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="XXdaily_expiration_checkXX",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_22(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="DAILY_EXPIRATION_CHECK",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_23(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=False,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_24(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=False,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_25(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=2,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "The local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_26(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                None
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_27(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "XXThe local daily scheduler stopped unexpectedly.XX"
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_28(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "the local daily scheduler stopped unexpectedly."
            ) from exc

    def xǁDailyTaskSchedulerǁrun__mutmut_29(
        self,
        task: Callable[[], None],
        *,
        check_time: time,
    ) -> None:
        """Register one daily task and block until the process is interrupted."""
        scheduler = self._backend or _load_scheduler_backend()
        try:
            scheduler.add_job(
                task,
                trigger="cron",
                hour=check_time.hour,
                minute=check_time.minute,
                id="daily_expiration_check",
                replace_existing=True,
                coalesce=True,
                max_instances=1,
            )
            scheduler.start()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            raise SchedulerError(
                "THE LOCAL DAILY SCHEDULER STOPPED UNEXPECTEDLY."
            ) from exc

mutants_xǁDailyTaskSchedulerǁ__init____mutmut['_mutmut_orig'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁ__init____mutmut['xǁDailyTaskSchedulerǁ__init____mutmut_1'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDailyTaskSchedulerǁrun__mutmut['_mutmut_orig'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_1'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_2'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_3'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_4'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_5'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_6'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_7'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_8'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_9'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_10'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_11'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_12'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_13'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_14'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_15'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_16'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_17'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_18'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_19'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_20'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_21'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_22'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_23'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_24'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_25'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_26'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_27'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_28'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDailyTaskSchedulerǁrun__mutmut['xǁDailyTaskSchedulerǁrun__mutmut_29'] = DailyTaskScheduler.xǁDailyTaskSchedulerǁrun__mutmut_29 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_scheduler_backend__mutmut)
def _load_scheduler_backend() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return cast(BlockingSchedulerBackend, BlockingScheduler())


def x__load_scheduler_backend__mutmut_orig() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return cast(BlockingSchedulerBackend, BlockingScheduler())


def x__load_scheduler_backend__mutmut_1() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            None
        ) from exc
    return cast(BlockingSchedulerBackend, BlockingScheduler())


def x__load_scheduler_backend__mutmut_2() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "XXDaily scheduling requires the locally installed APScheduler package.XX"
        ) from exc
    return cast(BlockingSchedulerBackend, BlockingScheduler())


def x__load_scheduler_backend__mutmut_3() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "daily scheduling requires the locally installed apscheduler package."
        ) from exc
    return cast(BlockingSchedulerBackend, BlockingScheduler())


def x__load_scheduler_backend__mutmut_4() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "DAILY SCHEDULING REQUIRES THE LOCALLY INSTALLED APSCHEDULER PACKAGE."
        ) from exc
    return cast(BlockingSchedulerBackend, BlockingScheduler())


def x__load_scheduler_backend__mutmut_5() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return cast(None, BlockingScheduler())


def x__load_scheduler_backend__mutmut_6() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return cast(BlockingSchedulerBackend, None)


def x__load_scheduler_backend__mutmut_7() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return cast(BlockingScheduler())


def x__load_scheduler_backend__mutmut_8() -> BlockingSchedulerBackend:
    """Load the locally installed APScheduler backend."""
    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
    except ImportError as exc:
        raise SchedulerConfigurationError(
            "Daily scheduling requires the locally installed APScheduler package."
        ) from exc
    return cast(BlockingSchedulerBackend, )

mutants_x__load_scheduler_backend__mutmut['_mutmut_orig'] = x__load_scheduler_backend__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_1'] = x__load_scheduler_backend__mutmut_1 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_2'] = x__load_scheduler_backend__mutmut_2 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_3'] = x__load_scheduler_backend__mutmut_3 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_4'] = x__load_scheduler_backend__mutmut_4 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_5'] = x__load_scheduler_backend__mutmut_5 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_6'] = x__load_scheduler_backend__mutmut_6 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_7'] = x__load_scheduler_backend__mutmut_7 # type: ignore # mutmut generated
mutants_x__load_scheduler_backend__mutmut['x__load_scheduler_backend__mutmut_8'] = x__load_scheduler_backend__mutmut_8 # type: ignore # mutmut generated
