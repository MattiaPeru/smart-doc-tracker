"""Validated domain models for locally processed documents."""

from ..models.document import DocumentData

__all__ = ["DocumentData"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
