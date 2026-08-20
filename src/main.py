"""Minimal command-line entry point for Smart Doc Tracker."""

from __future__ import annotations

from collections.abc import Sequence

from cli.application import CliApplication
from cli.arguments import CliArgumentParser
from cli.dependencies import CliDependencies


def run(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return CliApplication(dependencies).execute(arguments)


if __name__ == "__main__":
    raise SystemExit(run())
