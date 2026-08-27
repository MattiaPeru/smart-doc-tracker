from __future__ import annotations

from pathlib import Path
from unittest import TestCase

MANAGER_SCRIPT_PATH = (
    Path(__file__).resolve().parents[2] / "scripts" / "manage_expiration_task.ps1"
)
RUNNER_SCRIPT_PATH = (
    Path(__file__).resolve().parents[2] / "scripts" / "run_expiration_check.ps1"
)


class WindowsSchedulerScriptTests(TestCase):
    def test_task_invokes_local_prerequisite_runner(self) -> None:
        script = MANAGER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("scripts\\run_expiration_check.ps1", script)
        self.assertIn("-ExecutionPolicy Bypass -File", script)
        self.assertIn("-DaysThreshold", script)
        self.assertIn("-OcrLanguage", script)
        self.assertIn("-WaitForInput", script)
        self.assertIn("-WindowStyle Normal", script)
        self.assertIn("-WorkingDirectory $projectRoot", script)

    def test_task_recovers_missed_runs_and_supports_uninstall(self) -> None:
        script = MANAGER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("-StartWhenAvailable", script)
        self.assertIn("-LogonType Interactive", script)
        self.assertIn("Unregister-ScheduledTask", script)
        self.assertIn('[ValidateSet("Install", "Uninstall")]', script)

    def test_runner_starts_services_before_the_complete_pipeline(self) -> None:
        script = RUNNER_SCRIPT_PATH.read_text(encoding="utf-8")

        docker_position = script.index("Start-DockerDaemon -DockerCli")
        storage_position = script.index("Start-StorageServices -DockerCli")
        pipeline_position = script.index("--days-threshold $DaysThreshold")
        self.assertLess(docker_position, storage_position)
        self.assertLess(storage_position, pipeline_position)
        self.assertIn("up -d --pull never mongodb chromadb", script)
        self.assertIn("db.adminCommand('ping')", script)
        self.assertIn("/dev/tcp/127.0.0.1/8000", script)
        self.assertIn("--language $OcrLanguage", script)

    def test_runner_reports_failures_and_waits_only_when_requested(self) -> None:
        script = RUNNER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("[switch]$WaitForInput", script)
        self.assertIn('Write-Host ("Reason: {0}"', script)
        self.assertIn('Read-Host "Press Enter to close"', script)
        self.assertIn("if ($WaitForInput)", script)
        self.assertIn("exit $exitCode", script)

    def test_runner_invokes_main_once_for_daily_processing(self) -> None:
        script = RUNNER_SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertEqual(script.count("& $pythonPath -m smart_doc_tracker"), 1)
        self.assertNotIn("--process-inbox", script)
        self.assertNotIn("--check-expirations", script)

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
        self.assertIn("$chromaIsReady = $LASTEXITCODE -eq 0", script)
        self.assertEqual(
            script.count("$ErrorActionPreference = $previousErrorActionPreference"),
            2,
        )
