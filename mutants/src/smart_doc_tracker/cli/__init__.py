"""Command-line adapters for Smart Doc Tracker."""

from ..cli.arguments import CliArgumentParser
from ..cli.dependencies import CliDependencies

__all__ = ["CliArgumentParser", "CliDependencies"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
