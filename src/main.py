"""Minimal command-line entry point for Smart Doc Tracker."""

from __future__ import annotations

from collections.abc import Sequence

from cli.arguments import CliArgumentParser
from cli.dependencies import CliDependencies
from controllers.document_workflow_controller import DocumentWorkflowController


def run(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(dependencies).execute(arguments)


if __name__ == "__main__":
    raise SystemExit(run())
