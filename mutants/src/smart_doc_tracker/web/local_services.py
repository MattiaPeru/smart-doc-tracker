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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x__execute_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__execute_command__mutmut)
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


def x__execute_command__mutmut_orig(command: Sequence[str], cwd: Path) -> _CommandResult:
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


def x__execute_command__mutmut_1(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = None
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_2(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        None,
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


def x__execute_command__mutmut_3(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=None,
        check=False,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_4(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=None,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_5(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=None,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_6(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        text=None,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_7(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
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


def x__execute_command__mutmut_8(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        check=False,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_9(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_10(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_11(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_12(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(None),
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


def x__execute_command__mutmut_13(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_14(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=False,
        text=True,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_15(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        text=False,
    )
    return _CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_16(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        returncode=None,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_17(command: Sequence[str], cwd: Path) -> _CommandResult:
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
        stdout=None,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_18(command: Sequence[str], cwd: Path) -> _CommandResult:
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
        stderr=None,
    )


def x__execute_command__mutmut_19(command: Sequence[str], cwd: Path) -> _CommandResult:
    """Run one local command and capture only its operator diagnostics."""
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    return _CommandResult(
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_20(command: Sequence[str], cwd: Path) -> _CommandResult:
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
        stderr=completed.stderr,
    )


def x__execute_command__mutmut_21(command: Sequence[str], cwd: Path) -> _CommandResult:
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
        )

mutants_x__execute_command__mutmut['_mutmut_orig'] = x__execute_command__mutmut_orig # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_1'] = x__execute_command__mutmut_1 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_2'] = x__execute_command__mutmut_2 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_3'] = x__execute_command__mutmut_3 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_4'] = x__execute_command__mutmut_4 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_5'] = x__execute_command__mutmut_5 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_6'] = x__execute_command__mutmut_6 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_7'] = x__execute_command__mutmut_7 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_8'] = x__execute_command__mutmut_8 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_9'] = x__execute_command__mutmut_9 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_10'] = x__execute_command__mutmut_10 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_11'] = x__execute_command__mutmut_11 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_12'] = x__execute_command__mutmut_12 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_13'] = x__execute_command__mutmut_13 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_14'] = x__execute_command__mutmut_14 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_15'] = x__execute_command__mutmut_15 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_16'] = x__execute_command__mutmut_16 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_17'] = x__execute_command__mutmut_17 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_18'] = x__execute_command__mutmut_18 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_19'] = x__execute_command__mutmut_19 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_20'] = x__execute_command__mutmut_20 # type: ignore # mutmut generated
mutants_x__execute_command__mutmut['x__execute_command__mutmut_21'] = x__execute_command__mutmut_21 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__launch_process__mutmut)
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


def x__launch_process__mutmut_orig(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_1(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = None
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_2(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if (os.name == "nt") and False else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_3(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if (os.name == "nt") or True else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_4(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name != "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_5(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "XXntXX" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_6(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "NT" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_7(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 1
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_8(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        None,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_9(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=None,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_10(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=None,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_11(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=None,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_12(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=None,
    )


def x__launch_process__mutmut_13(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_14(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_15(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_16(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def x__launch_process__mutmut_17(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(command),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        )


def x__launch_process__mutmut_18(command: Sequence[str]) -> _ManagedProcess:
    """Start one hidden local service process without retaining its output."""
    creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    return subprocess.Popen(
        list(None),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )

mutants_x__launch_process__mutmut['_mutmut_orig'] = x__launch_process__mutmut_orig # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_1'] = x__launch_process__mutmut_1 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_2'] = x__launch_process__mutmut_2 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_3'] = x__launch_process__mutmut_3 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_4'] = x__launch_process__mutmut_4 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_5'] = x__launch_process__mutmut_5 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_6'] = x__launch_process__mutmut_6 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_7'] = x__launch_process__mutmut_7 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_8'] = x__launch_process__mutmut_8 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_9'] = x__launch_process__mutmut_9 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_10'] = x__launch_process__mutmut_10 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_11'] = x__launch_process__mutmut_11 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_12'] = x__launch_process__mutmut_12 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_13'] = x__launch_process__mutmut_13 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_14'] = x__launch_process__mutmut_14 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_15'] = x__launch_process__mutmut_15 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_16'] = x__launch_process__mutmut_16 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_17'] = x__launch_process__mutmut_17 # type: ignore # mutmut generated
mutants_x__launch_process__mutmut['x__launch_process__mutmut_18'] = x__launch_process__mutmut_18 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__probe_loopback_port__mutmut)
def _probe_loopback_port(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=0.25):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_orig(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=0.25):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_1(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection(None, timeout=0.25):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_2(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=None):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_3(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection(timeout=0.25):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_4(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), ):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_5(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=1.25):
            return True
    except OSError:
        return False


def x__probe_loopback_port__mutmut_6(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=0.25):
            return False
    except OSError:
        return False


def x__probe_loopback_port__mutmut_7(host: str, port: int) -> bool:
    """Return whether one explicit loopback TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=0.25):
            return True
    except OSError:
        return True

mutants_x__probe_loopback_port__mutmut['_mutmut_orig'] = x__probe_loopback_port__mutmut_orig # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_1'] = x__probe_loopback_port__mutmut_1 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_2'] = x__probe_loopback_port__mutmut_2 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_3'] = x__probe_loopback_port__mutmut_3 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_4'] = x__probe_loopback_port__mutmut_4 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_5'] = x__probe_loopback_port__mutmut_5 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_6'] = x__probe_loopback_port__mutmut_6 # type: ignore # mutmut generated
mutants_x__probe_loopback_port__mutmut['x__probe_loopback_port__mutmut_7'] = x__probe_loopback_port__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁstop__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut: MutantDict = {}  # type: ignore
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁstart__mutmut)
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

    def xǁLocalWebServiceManagerǁstart__mutmut_orig(self) -> None:
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

    def xǁLocalWebServiceManagerǁstart__mutmut_1(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds < 0:
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

    def xǁLocalWebServiceManagerǁstart__mutmut_2(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 1:
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

    def xǁLocalWebServiceManagerǁstart__mutmut_3(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError(None)
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

    def xǁLocalWebServiceManagerǁstart__mutmut_4(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("XXstartup_timeout_seconds must be positiveXX")
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

    def xǁLocalWebServiceManagerǁstart__mutmut_5(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("STARTUP_TIMEOUT_SECONDS MUST BE POSITIVE")
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

    def xǁLocalWebServiceManagerǁstart__mutmut_6(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("startup_timeout_seconds must be positive")
        if self.poll_interval_seconds <= 0:
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

    def xǁLocalWebServiceManagerǁstart__mutmut_7(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("startup_timeout_seconds must be positive")
        if self.poll_interval_seconds < 1:
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

    def xǁLocalWebServiceManagerǁstart__mutmut_8(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("startup_timeout_seconds must be positive")
        if self.poll_interval_seconds < 0:
            raise ValueError(None)
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

    def xǁLocalWebServiceManagerǁstart__mutmut_9(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("startup_timeout_seconds must be positive")
        if self.poll_interval_seconds < 0:
            raise ValueError("XXpoll_interval_seconds cannot be negativeXX")
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

    def xǁLocalWebServiceManagerǁstart__mutmut_10(self) -> None:
        """Start missing MongoDB, ChromaDB, and Ollama loopback services."""
        if self.startup_timeout_seconds <= 0:
            raise ValueError("startup_timeout_seconds must be positive")
        if self.poll_interval_seconds < 0:
            raise ValueError("POLL_INTERVAL_SECONDS CANNOT BE NEGATIVE")
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

    def xǁLocalWebServiceManagerǁstart__mutmut_11(self) -> None:
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
                None
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def xǁLocalWebServiceManagerǁstart__mutmut_12(self) -> None:
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
                "XXA required local service command is unavailable. XX"
                "Ensure Docker Desktop and Ollama are installed."
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def xǁLocalWebServiceManagerǁstart__mutmut_13(self) -> None:
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
                "a required local service command is unavailable. "
                "Ensure Docker Desktop and Ollama are installed."
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def xǁLocalWebServiceManagerǁstart__mutmut_14(self) -> None:
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
                "A REQUIRED LOCAL SERVICE COMMAND IS UNAVAILABLE. "
                "Ensure Docker Desktop and Ollama are installed."
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def xǁLocalWebServiceManagerǁstart__mutmut_15(self) -> None:
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
                "XXEnsure Docker Desktop and Ollama are installed.XX"
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def xǁLocalWebServiceManagerǁstart__mutmut_16(self) -> None:
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
                "ensure docker desktop and ollama are installed."
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    def xǁLocalWebServiceManagerǁstart__mutmut_17(self) -> None:
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
                "ENSURE DOCKER DESKTOP AND OLLAMA ARE INSTALLED."
            ) from exc
        except LocalServiceStartupError:
            self.stop()
            raise

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁstop__mutmut)
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

    def xǁLocalWebServiceManagerǁstop__mutmut_orig(self) -> None:
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

    def xǁLocalWebServiceManagerǁstop__mutmut_1(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if self._started_compose_services:
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

    def xǁLocalWebServiceManagerǁstop__mutmut_2(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = None
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

    def xǁLocalWebServiceManagerǁstop__mutmut_3(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(None)
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

    def xǁLocalWebServiceManagerǁstop__mutmut_4(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(None))
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

    def xǁLocalWebServiceManagerǁstop__mutmut_5(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = None
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_6(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                None,
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_7(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "compose", "stop", *services),
                None,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_8(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_9(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "compose", "stop", *services),
                )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_10(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("XXdockerXX", "compose", "stop", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_11(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("DOCKER", "compose", "stop", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_12(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "XXcomposeXX", "stop", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_13(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "COMPOSE", "stop", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_14(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "compose", "XXstopXX", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_15(self) -> None:
        """Stop only services that were started by this manager instance."""
        self._stop_ollama()
        if not self._started_compose_services:
            return
        services = list(reversed(self._started_compose_services))
        try:
            result = self.command_executor(
                ("docker", "compose", "STOP", *services),
                self.project_root,
            )
        except OSError:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_16(self) -> None:
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
            _LOGGER.warning(None)
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_17(self) -> None:
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
            _LOGGER.warning("XXLocally managed Docker services could not be stopped.XX")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_18(self) -> None:
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
            _LOGGER.warning("locally managed docker services could not be stopped.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_19(self) -> None:
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
            _LOGGER.warning("LOCALLY MANAGED DOCKER SERVICES COULD NOT BE STOPPED.")
            self._started_compose_services.clear()
            return
        if result.returncode != 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_20(self) -> None:
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
        if result.returncode == 0:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_21(self) -> None:
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
        if result.returncode != 1:
            _LOGGER.warning("Locally managed Docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_22(self) -> None:
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
            _LOGGER.warning(None)
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_23(self) -> None:
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
            _LOGGER.warning("XXLocally managed Docker services could not be stopped.XX")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_24(self) -> None:
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
            _LOGGER.warning("locally managed docker services could not be stopped.")
        self._started_compose_services.clear()

    def xǁLocalWebServiceManagerǁstop__mutmut_25(self) -> None:
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
            _LOGGER.warning("LOCALLY MANAGED DOCKER SERVICES COULD NOT BE STOPPED.")
        self._started_compose_services.clear()

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut)
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_orig(self) -> None:
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_1(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = None
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_2(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = None
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_3(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service in running]
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_4(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                None,
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_5(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                None,
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_6(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_7(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_8(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "XXStarting required Docker services: %s.XX",
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_9(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "starting required docker services: %s.",
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_10(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "STARTING REQUIRED DOCKER SERVICES: %S.",
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_11(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(None),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_12(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                "XX, XX".join(missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_13(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = None
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_14(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                None,
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_15(self) -> None:
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
                None,
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_16(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_17(self) -> None:
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_18(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("XXdockerXX", "compose", "up", "-d", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_19(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("DOCKER", "compose", "up", "-d", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_20(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "XXcomposeXX", "up", "-d", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_21(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "COMPOSE", "up", "-d", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_22(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "XXupXX", "-d", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_23(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "UP", "-d", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_24(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "XX-dXX", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_25(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "-D", "--pull", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_26(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "-d", "XX--pullXX", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_27(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "-d", "--PULL", "never", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_28(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "-d", "--pull", "XXneverXX", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_29(self) -> None:
        """Start missing persistence containers and wait for their loopback ports."""
        running = self._running_compose_services()
        missing = [service for service in _COMPOSE_PORTS if service not in running]
        if missing:
            _LOGGER.info(
                "Starting required Docker services: %s.",
                ", ".join(missing),
            )
            result = self.command_executor(
                ("docker", "compose", "up", "-d", "--pull", "NEVER", *missing),
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_30(self) -> None:
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
            if result.returncode == 0:
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_31(self) -> None:
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
            if result.returncode != 1:
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_32(self) -> None:
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
                self._record_started_compose_services(None)
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

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_33(self) -> None:
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
                    None
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_34(self) -> None:
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
                    "XXMongoDB and ChromaDB could not be started. XX"
                    "Ensure Docker Desktop is running and the local images exist."
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_35(self) -> None:
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
                    "mongodb and chromadb could not be started. "
                    "Ensure Docker Desktop is running and the local images exist."
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_36(self) -> None:
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
                    "MONGODB AND CHROMADB COULD NOT BE STARTED. "
                    "Ensure Docker Desktop is running and the local images exist."
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_37(self) -> None:
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
                    "XXEnsure Docker Desktop is running and the local images exist.XX"
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_38(self) -> None:
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
                    "ensure docker desktop is running and the local images exist."
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_39(self) -> None:
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
                    "ENSURE DOCKER DESKTOP IS RUNNING AND THE LOCAL IMAGES EXIST."
                )
            self._started_compose_services.extend(missing)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_40(self) -> None:
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
            self._started_compose_services.extend(None)
        for service, port in _COMPOSE_PORTS.items():
            self._wait_for_port(
                port,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_41(self) -> None:
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
                None,
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_42(self) -> None:
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
                service_name=None,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_43(self) -> None:
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
                service_name=service,
            )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_44(self) -> None:
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
                )
        _LOGGER.info("MongoDB and ChromaDB are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_45(self) -> None:
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
        _LOGGER.info(None)

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_46(self) -> None:
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
        _LOGGER.info("XXMongoDB and ChromaDB are ready on loopback.XX")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_47(self) -> None:
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
        _LOGGER.info("mongodb and chromadb are ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_48(self) -> None:
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
        _LOGGER.info("MONGODB AND CHROMADB ARE READY ON LOOPBACK.")

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut)
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

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_orig(self) -> set[str]:
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

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_1(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = None
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_2(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            None,
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_3(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            None,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_4(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_5(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_6(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("XXdockerXX", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_7(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("DOCKER", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_8(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "XXcomposeXX", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_9(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "COMPOSE", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_10(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "XXpsXX", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_11(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "PS", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_12(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "XX--statusXX", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_13(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--STATUS", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_14(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "XXrunningXX", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_15(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "RUNNING", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_16(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "XX--servicesXX"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_17(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--SERVICES"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_18(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode == 0:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_19(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 1:
            raise LocalServiceStartupError(
                "Docker Compose is unavailable. Ensure Docker Desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_20(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                None
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_21(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "XXDocker Compose is unavailable. Ensure Docker Desktop is running.XX"
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_22(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "docker compose is unavailable. ensure docker desktop is running."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    def xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_23(self) -> set[str]:
        """Return the Compose services already running for this project."""
        result = self.command_executor(
            ("docker", "compose", "ps", "--status", "running", "--services"),
            self.project_root,
        )
        if result.returncode != 0:
            raise LocalServiceStartupError(
                "DOCKER COMPOSE IS UNAVAILABLE. ENSURE DOCKER DESKTOP IS RUNNING."
            )
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut)
    def _record_started_compose_services(self, candidates: Sequence[str]) -> None:
        """Record partial Compose startup so failure cleanup remains precise."""
        try:
            running = self._running_compose_services()
        except LocalServiceStartupError:
            return
        self._started_compose_services.extend(
            service for service in candidates if service in running
        )

    def xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_orig(self, candidates: Sequence[str]) -> None:
        """Record partial Compose startup so failure cleanup remains precise."""
        try:
            running = self._running_compose_services()
        except LocalServiceStartupError:
            return
        self._started_compose_services.extend(
            service for service in candidates if service in running
        )

    def xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_1(self, candidates: Sequence[str]) -> None:
        """Record partial Compose startup so failure cleanup remains precise."""
        try:
            running = None
        except LocalServiceStartupError:
            return
        self._started_compose_services.extend(
            service for service in candidates if service in running
        )

    def xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_2(self, candidates: Sequence[str]) -> None:
        """Record partial Compose startup so failure cleanup remains precise."""
        try:
            running = self._running_compose_services()
        except LocalServiceStartupError:
            return
        self._started_compose_services.extend(
            None
        )

    def xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_3(self, candidates: Sequence[str]) -> None:
        """Record partial Compose startup so failure cleanup remains precise."""
        try:
            running = self._running_compose_services()
        except LocalServiceStartupError:
            return
        self._started_compose_services.extend(
            service for service in candidates if service not in running
        )

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut)
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_orig(self) -> None:
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_1(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe(None, _OLLAMA_PORT):
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_2(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", None):
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_3(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe(_OLLAMA_PORT):
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_4(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", ):
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_5(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("XX127.0.0.1XX", _OLLAMA_PORT):
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_6(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info(None)
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_7(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("XXUsing the Ollama service already running on loopback.XX")
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_8(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("using the ollama service already running on loopback.")
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_9(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("USING THE OLLAMA SERVICE ALREADY RUNNING ON LOOPBACK.")
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_10(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info(None)
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_11(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("XXStarting the required local Ollama service.XX")
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_12(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("starting the required local ollama service.")
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_13(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("STARTING THE REQUIRED LOCAL OLLAMA SERVICE.")
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_14(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = None
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_15(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(None)
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_16(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("XXollamaXX", "serve"))
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_17(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("OLLAMA", "serve"))
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_18(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "XXserveXX"))
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_19(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "SERVE"))
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

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_20(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "serve"))
        except OSError as exc:
            raise LocalServiceStartupError(
                None
            ) from exc
        self._wait_for_port(
            _OLLAMA_PORT,
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_21(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "serve"))
        except OSError as exc:
            raise LocalServiceStartupError(
                "XXOllama could not be started. Ensure it is installed locally.XX"
            ) from exc
        self._wait_for_port(
            _OLLAMA_PORT,
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_22(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "serve"))
        except OSError as exc:
            raise LocalServiceStartupError(
                "ollama could not be started. ensure it is installed locally."
            ) from exc
        self._wait_for_port(
            _OLLAMA_PORT,
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_23(self) -> None:
        """Reuse an existing Ollama endpoint or start one owned local process."""
        if self.port_probe("127.0.0.1", _OLLAMA_PORT):
            _LOGGER.info("Using the Ollama service already running on loopback.")
            return
        _LOGGER.info("Starting the required local Ollama service.")
        try:
            self._ollama_process = self.process_launcher(("ollama", "serve"))
        except OSError as exc:
            raise LocalServiceStartupError(
                "OLLAMA COULD NOT BE STARTED. ENSURE IT IS INSTALLED LOCALLY."
            ) from exc
        self._wait_for_port(
            _OLLAMA_PORT,
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_24(self) -> None:
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
            None,
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_25(self) -> None:
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
            service_name=None,
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_26(self) -> None:
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
            process=None,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_27(self) -> None:
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
            service_name="ollama",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_28(self) -> None:
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
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_29(self) -> None:
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
            )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_30(self) -> None:
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
            service_name="XXollamaXX",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_31(self) -> None:
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
            service_name="OLLAMA",
            process=self._ollama_process,
        )
        _LOGGER.info("Ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_32(self) -> None:
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
        _LOGGER.info(None)

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_33(self) -> None:
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
        _LOGGER.info("XXOllama is ready on loopback.XX")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_34(self) -> None:
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
        _LOGGER.info("ollama is ready on loopback.")

    def xǁLocalWebServiceManagerǁ_start_ollama__mutmut_35(self) -> None:
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
        _LOGGER.info("OLLAMA IS READY ON LOOPBACK.")

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut)
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

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_orig(
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

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_1(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = None
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

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_2(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() - self.startup_timeout_seconds
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

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_3(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() <= deadline:
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

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_4(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() < deadline:
            if self.port_probe(None, port):
                return
            if process is not None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_5(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() < deadline:
            if self.port_probe("127.0.0.1", None):
                return
            if process is not None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_6(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() < deadline:
            if self.port_probe(port):
                return
            if process is not None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_7(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() < deadline:
            if self.port_probe("127.0.0.1", ):
                return
            if process is not None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_8(
        self,
        port: int,
        *,
        service_name: str,
        process: _ManagedProcess | None = None,
    ) -> None:
        """Wait a bounded time for one required loopback service to become ready."""
        deadline = self.monotonic() + self.startup_timeout_seconds
        while self.monotonic() < deadline:
            if self.port_probe("XX127.0.0.1XX", port):
                return
            if process is not None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_9(
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
            if process is not None or process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_10(
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
            if process is None and process.poll() is not None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_11(
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
            if process is not None and process.poll() is None:
                raise LocalServiceStartupError(
                    f"The local {service_name} service exited during startup."
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_12(
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
                    None
                )
            self.sleeper(self.poll_interval_seconds)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_13(
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
            self.sleeper(None)
        raise LocalServiceStartupError(
            f"The local {service_name} service did not become ready in time."
        )

    def xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_14(
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
            None
        )

    @_mutmut_mutated(mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut)
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

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_orig(self) -> None:
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

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_1(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = None
        self._ollama_process = None
        if process is None or process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_2(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = ""
        if process is None or process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_3(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = None
        if process is None and process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_4(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = None
        if process is not None or process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_5(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = None
        if process is None or process.poll() is None:
            return
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_6(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = None
        if process is None or process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=None)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_7(self) -> None:
        """Stop the Ollama process owned by this manager, forcing it if necessary."""
        process = self._ollama_process
        self._ollama_process = None
        if process is None or process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=11)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_8(self) -> None:
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
            process.wait(timeout=None)

    def xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_9(self) -> None:
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
            process.wait(timeout=6)

mutants_xǁLocalWebServiceManagerǁstart__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_10'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_11'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_12'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_13'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_14'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_15'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_16'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstart__mutmut['xǁLocalWebServiceManagerǁstart__mutmut_17'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstart__mutmut_17 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁstop__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_10'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_11'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_12'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_13'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_14'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_15'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_16'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_17'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_18'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_19'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_20'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_21'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_22'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_23'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_24'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁstop__mutmut['xǁLocalWebServiceManagerǁstop__mutmut_25'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁstop__mutmut_25 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_10'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_11'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_12'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_13'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_14'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_15'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_16'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_17'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_18'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_19'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_20'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_21'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_22'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_23'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_24'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_25'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_26'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_27'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_28'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_29'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_30'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_30 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_31'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_31 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_32'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_32 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_33'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_33 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_34'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_34 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_35'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_35 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_36'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_36 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_37'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_37 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_38'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_38 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_39'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_39 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_40'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_40 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_41'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_41 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_42'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_42 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_43'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_43 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_44'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_44 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_45'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_45 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_46'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_46 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_47'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_47 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_compose_services__mutmut['xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_48'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_compose_services__mutmut_48 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_10'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_11'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_12'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_13'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_14'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_15'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_16'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_17'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_18'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_19'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_20'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_21'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_22'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_running_compose_services__mutmut['xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_23'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_running_compose_services__mutmut_23 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut['xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut['xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut['xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_record_started_compose_services__mutmut_3 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_10'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_11'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_12'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_13'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_14'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_15'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_16'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_17'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_18'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_19'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_20'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_21'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_22'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_23'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_24'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_25'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_26'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_27'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_28'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_29'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_30'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_30 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_31'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_31 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_32'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_32 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_33'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_33 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_34'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_34 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_start_ollama__mutmut['xǁLocalWebServiceManagerǁ_start_ollama__mutmut_35'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_start_ollama__mutmut_35 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_10'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_11'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_12'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_13'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_wait_for_port__mutmut['xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_14'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_wait_for_port__mutmut_14 # type: ignore # mutmut generated

mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['_mutmut_orig'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_1'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_2'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_3'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_4'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_5'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_6'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_7'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_8'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLocalWebServiceManagerǁ_stop_ollama__mutmut['xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_9'] = LocalWebServiceManager.xǁLocalWebServiceManagerǁ_stop_ollama__mutmut_9 # type: ignore # mutmut generated
