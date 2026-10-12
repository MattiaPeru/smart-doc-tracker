"""Local FastAPI dashboard adapter."""

from .app import create_app

__all__ = ["create_app"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
