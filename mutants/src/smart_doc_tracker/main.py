"""Minimal command-line entry point for Smart Doc Tracker."""

from __future__ import annotations

from collections.abc import Sequence

from .cli.arguments import CliArgumentParser
from .cli.dependencies import CliDependencies
from .controllers.document_workflow_controller import DocumentWorkflowController


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_run__mutmut)
def run(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(dependencies).execute(arguments)


def x_run__mutmut_orig(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(dependencies).execute(arguments)


def x_run__mutmut_1(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = None
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(dependencies).execute(arguments)


def x_run__mutmut_2(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(None)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(dependencies).execute(arguments)


def x_run__mutmut_3(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = None
    return DocumentWorkflowController(dependencies).execute(arguments)


def x_run__mutmut_4(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(dependencies).execute(None)


def x_run__mutmut_5(argv: Sequence[str] | None = None, **dependency_overrides: object) -> int:
    """Parse arguments and dispatch the selected local command."""
    arguments = CliArgumentParser().parse(argv)
    dependencies = CliDependencies.with_overrides(**dependency_overrides)
    return DocumentWorkflowController(None).execute(arguments)

mutants_x_run__mutmut['_mutmut_orig'] = x_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_1'] = x_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_2'] = x_run__mutmut_2 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_3'] = x_run__mutmut_3 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_4'] = x_run__mutmut_4 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_5'] = x_run__mutmut_5 # type: ignore # mutmut generated


if __name__ == "__main__":
    raise SystemExit(run())
