from __future__ import annotations

from pathlib import Path
from unittest import TestCase


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "manage_expiration_task.ps1"
)


class WindowsSchedulerScriptTests(TestCase):
    def test_task_runs_one_shot_check_from_project_virtual_environment(self) -> None:
        script = SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn(".venv\\Scripts\\python.exe", script)
        self.assertIn("src\\main.py", script)
        self.assertIn("--check-expirations --days-threshold", script)
        self.assertIn("-WorkingDirectory $projectRoot", script)

    def test_task_recovers_missed_runs_and_supports_uninstall(self) -> None:
        script = SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("-StartWhenAvailable", script)
        self.assertIn("-LogonType Interactive", script)
        self.assertIn("Unregister-ScheduledTask", script)
        self.assertIn('[ValidateSet("Install", "Uninstall")]', script)
