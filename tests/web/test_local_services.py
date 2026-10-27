from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from subprocess import TimeoutExpired
from unittest import TestCase
from unittest.mock import Mock, patch

from smart_doc_tracker.web.local_services import (
    LocalServiceStartupError,
    LocalWebServiceManager,
    _CommandResult,
)


class FakeProcess:
    def __init__(self) -> None:
        self.running = True
        self.terminated = False
        self.killed = False

    def poll(self) -> int | None:
        return None if self.running else 0

    def terminate(self) -> None:
        self.terminated = True
        self.running = False

    def wait(self, timeout: float | None = None) -> int:
        return 0

    def kill(self) -> None:
        self.killed = True
        self.running = False


class FakeLocalServices:
    def __init__(
        self,
        *,
        running: set[str] | None = None,
        ollama_running: bool = False,
        fail_ollama_start: bool = False,
    ) -> None:
        self.running = set(running or ())
        self.ollama_running = ollama_running
        self.fail_ollama_start = fail_ollama_start
        self.commands: list[tuple[str, ...]] = []
        self.process = FakeProcess()
        self.launches: list[tuple[str, ...]] = []

    def execute(self, command: Sequence[str], cwd: Path) -> _CommandResult:
        normalized = tuple(command)
        self.commands.append(normalized)
        if normalized[2:4] == ("ps", "--status"):
            return _CommandResult(0, "\n".join(sorted(self.running)))
        if normalized[2:4] == ("up", "-d"):
            self.running.update(normalized[6:])
            return _CommandResult(0)
        if normalized[2] == "stop":
            self.running.difference_update(normalized[3:])
            return _CommandResult(0)
        raise AssertionError(f"Unexpected command: {normalized}")

    def launch(self, command: Sequence[str]) -> FakeProcess:
        normalized = tuple(command)
        self.launches.append(normalized)
        if self.fail_ollama_start:
            raise OSError("ollama unavailable")
        self.ollama_running = True
        return self.process

    def probe(self, host: str, port: int) -> bool:
        if host != "127.0.0.1":
            return False
        if port == 27017:
            return "mongodb" in self.running
        if port == 8000:
            return "chromadb" in self.running
        if port == 11434:
            return self.ollama_running
        return False

    def manager(self) -> LocalWebServiceManager:
        return LocalWebServiceManager(
            project_root=Path("project"),
            startup_timeout_seconds=1,
            poll_interval_seconds=0,
            command_executor=self.execute,
            process_launcher=self.launch,
            port_probe=self.probe,
            sleeper=lambda _seconds: None,
        )


class LocalWebServiceManagerTests(TestCase):
    def test_starts_and_stops_only_missing_services(self) -> None:
        services = FakeLocalServices(running={"mongodb"})
        manager = services.manager()

        manager.start()
        manager.stop()

        self.assertIn(
            ("docker", "compose", "up", "-d", "--pull", "never", "chromadb"),
            services.commands,
        )
        self.assertIn(
            ("docker", "compose", "stop", "chromadb"),
            services.commands,
        )
        self.assertIn("mongodb", services.running)
        self.assertNotIn("chromadb", services.running)
        self.assertEqual(services.launches, [("ollama", "serve")])
        self.assertTrue(services.process.terminated)

    def test_leaves_preexisting_services_running(self) -> None:
        services = FakeLocalServices(
            running={"mongodb", "chromadb"},
            ollama_running=True,
        )
        manager = services.manager()

        manager.start()
        manager.stop()

        self.assertEqual(services.running, {"mongodb", "chromadb"})
        self.assertEqual(services.launches, [])
        self.assertFalse(any(command[2] == "stop" for command in services.commands))

    def test_cleans_up_compose_services_when_ollama_cannot_start(self) -> None:
        services = FakeLocalServices(fail_ollama_start=True)
        manager = services.manager()

        with self.assertRaisesRegex(
            LocalServiceStartupError,
            "Ollama could not be started",
        ):
            manager.start()

        self.assertEqual(services.running, set())
        self.assertIn(
            ("docker", "compose", "stop", "chromadb", "mongodb"),
            services.commands,
        )

    def test_forces_ollama_to_stop_after_a_graceful_timeout(self) -> None:
        services = FakeLocalServices()
        manager = services.manager()
        manager.start()

        def wait(timeout: float | None = None) -> int:
            if not services.process.killed:
                raise TimeoutExpired("ollama", timeout)
            return 0

        services.process.wait = wait  # type: ignore[method-assign]
        manager.stop()

        self.assertTrue(services.process.terminated)
        self.assertTrue(services.process.killed)

    @patch("smart_doc_tracker.web.app.LocalWebServiceManager")
    @patch("uvicorn.run", side_effect=RuntimeError("server stopped"))
    def test_web_command_always_stops_owned_services(
        self,
        _run_server: Mock,
        manager_type: Mock,
    ) -> None:
        from smart_doc_tracker.web.app import run

        manager = manager_type.return_value

        with self.assertRaisesRegex(RuntimeError, "server stopped"):
            run([])

        manager.start.assert_called_once_with()
        manager.stop.assert_called_once_with()

    @patch("smart_doc_tracker.web.app.LocalWebServiceManager")
    @patch("uvicorn.run")
    def test_chat_debug_flag_is_scoped_to_the_server_run(
        self,
        run_server: Mock,
        _manager_type: Mock,
    ) -> None:
        import os

        from smart_doc_tracker.web.app import run

        previous = os.environ.pop("SMART_DOC_TRACKER_CHAT_DEBUG", None)
        try:
            run_server.side_effect = lambda *_args, **_kwargs: self.assertEqual(
                os.environ.get("SMART_DOC_TRACKER_CHAT_DEBUG"), "1"
            )
            run(["--chat-debug"])
            self.assertNotIn("SMART_DOC_TRACKER_CHAT_DEBUG", os.environ)
        finally:
            if previous is not None:
                os.environ["SMART_DOC_TRACKER_CHAT_DEBUG"] = previous
