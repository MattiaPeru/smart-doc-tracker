from __future__ import annotations

from typing import Any
from unittest import TestCase

from smart_doc_tracker.scheduler import (
    DailyTaskScheduler,
    SchedulerConfigurationError,
    parse_daily_time,
)


class FakeSchedulerBackend:
    def __init__(self) -> None:
        self.jobs: list[tuple[object, dict[str, Any]]] = []
        self.started = False

    def add_job(self, function: object, **kwargs: Any) -> None:
        self.jobs.append((function, kwargs))

    def start(self) -> None:
        self.started = True


class DailyTaskSchedulerTests(TestCase):
    def test_registers_one_coalesced_daily_job(self) -> None:
        backend = FakeSchedulerBackend()

        def task() -> None:
            pass

        DailyTaskScheduler(backend=backend).run(
            task,
            check_time=parse_daily_time("08:45"),
        )

        self.assertTrue(backend.started)
        self.assertEqual(backend.jobs[0][0], task)
        self.assertEqual(backend.jobs[0][1]["trigger"], "cron")
        self.assertEqual(backend.jobs[0][1]["hour"], 8)
        self.assertEqual(backend.jobs[0][1]["minute"], 45)
        self.assertTrue(backend.jobs[0][1]["coalesce"])
        self.assertEqual(backend.jobs[0][1]["max_instances"], 1)

    def test_rejects_invalid_daily_times(self) -> None:
        for value in ("9:00", "24:00", "12:60", "noon"):
            with self.subTest(value=value):
                with self.assertRaises(SchedulerConfigurationError):
                    parse_daily_time(value)
