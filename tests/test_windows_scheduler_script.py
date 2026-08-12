from __future__ import annotations

from pathlib import Path
from unittest import TestCase


MANAGER_SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "manage_expiration_task.ps1"
)
RUNNER_SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "run_expiration_check.ps1"
)


class WindowsSchedulerScriptTests(TestCase):
    def test_task_invokes_local_prerequisite_runner(self) -> None:
        script = MANAGER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("scripts\\run_expiration_check.ps1", script)
        self.assertIn("-ExecutionPolicy Bypass -File", script)
        self.assertIn("-DaysThreshold", script)
        self.assertIn("-WorkingDirectory $projectRoot", script)

    def test_task_recovers_missed_runs_and_supports_uninstall(self) -> None:
        script = MANAGER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("-StartWhenAvailable", script)
        self.assertIn("-LogonType Interactive", script)
        self.assertIn("Unregister-ScheduledTask", script)
        self.assertIn('[ValidateSet("Install", "Uninstall")]', script)

    def test_runner_starts_local_services_before_expiration_check(self) -> None:
        script = RUNNER_SCRIPT_PATH.read_text(encoding="utf-8")

        docker_position = script.index("Start-DockerDaemon -DockerCli")
        mongo_position = script.index("Start-MongoService -DockerCli")
        check_position = script.index("--check-expirations --days-threshold")
        self.assertLess(docker_position, mongo_position)
        self.assertLess(mongo_position, check_position)
        self.assertIn("up -d --pull never mongodb", script)
        self.assertIn("db.adminCommand('ping')", script)

    def test_runner_uses_only_loopback_project_services(self) -> None:
        script = RUNNER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn('"docker-compose.yml"', script)
        self.assertIn("--pull never", script)
        self.assertNotIn("http://", script)
        self.assertNotIn("https://", script)

    def test_runner_treats_unready_service_probes_as_expected_states(self) -> None:
        script = RUNNER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertEqual(script.count('$ErrorActionPreference = "SilentlyContinue"'), 2)
        self.assertIn("$probeSucceeded = $LASTEXITCODE -eq 0", script)
        self.assertIn("$mongoIsReady = $LASTEXITCODE -eq 0", script)
        self.assertEqual(
            script.count(
                "$ErrorActionPreference = $previousErrorActionPreference"
            ),
            2,
        )
