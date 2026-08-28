"""Lifecycle management for services required by the local web dashboard."""

from __future__ import annotations

import logging
import os
import socket
import subprocess
import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

_LOGGER = logging.getLogger(__name__)
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
_COMPOSE_PORTS = {"mongodb": 27017, "chromadb": 8000}
_OLLAMA_PORT = 11434


class LocalServiceStartupError(RuntimeError):
    """Raised when a required loopback-only service cannot be started."""


@dataclass(frozen=True, slots=True)
class _CommandResult:
    returncode: int
    stdout: str = ""
    stderr: str = ""


class _ManagedProcess(Protocol):
    def poll(self) -> int | None:
        """Return the exit code, or None while the process is running."""

    def terminate(self) -> None:
        """Request a graceful process shutdown."""

    def wait(self, timeout: float | None = None) -> int:
        """Wait for the process to exit."""

    def kill(self) -> None:
        """Force the process to exit."""


_CommandExecutor = Callable[[Sequence[str], Path], _CommandResult]
_ProcessLauncher = Callable[[Sequence[str]], _ManagedProcess]
_PortProbe = Callable[[str, int], bool]


def _execute_command(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def _launch_process(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def _probe_loopback_port(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=0.25):
            return True
    except OSError:
        return False


@dataclass(slots=True)
class LocalWebServiceManager:
    """Start and stop only the local services owned by one web server run."""

    project_root: Path = _PROJECT_ROOT
    startup_timeout_seconds: float = 60.0
    poll_interval_seconds: float = 0.25
    command_executor: _CommandExecutor = _execute_command
    process_launcher: _ProcessLauncher = _launch_process
    port_probe: _PortProbe = _probe_loopback_port
    sleeper: Callable[[float], None] = time.sleep
    monotonic: Callable[[], float] = time.monotonic
    _started_compose_services: list[str] = field(default_factory=list, init=False)
    _ollama_process: _ManagedProcess | None = field(default=None, init=False)

    def start(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("startup_timeout_seconds must be positive")
        if self.poll_interval_seconds < 0:
            raise ValueError("poll_interval_seconds cannot be negative")
        try:
            self._start_compose_services()
            self._start_ollama()
        except OSError as exc:
            self.stop()
            raise LocalServiceStartupError(
                "A required local service command is unavailable. "
                "Ensure Docker Desktop and Ollama are installed."
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def stop(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "compose", "stop", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def _start_compose_services(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "-d", "--pull", "never", *missing),
                self.project_root,
            )
            if result.returncode != 0:
                self._record_started_compose_services(missing)
                raise LocalServiceStartupError(
                    "MongoDB and ChromaDB could not be started. "
                    "Ensure Docker Desktop is running and the local images exist."
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def _running_compose_services(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def _record_started_compose_services(self, candidates: Sequence[str]) -> None:
        """Record partial Compose startup so failure cleanup remains precise."""
        try:
            running = self._running_compose_services()
        except LocalServiceStartupError:
            return
        self._started_compose_services.extend(
            service for service in candidates if service in running
        )

    def _start_ollama(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "serve"))
        except OSError as exc:
            raise LocalServiceStartupError(
                "Ollama could not be started. Ensure it is installed locally."
            ) from exc
        self._wait_for_port(
            _OLLAMA_PORT,
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def _wait_for_port(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() < deadline:
            if self.port_probe("127.0.0.1", port):
                return
            if process is not None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def _stop_ollama(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = None
        if process is None or process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
