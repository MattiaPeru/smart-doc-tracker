"""Core document-processing components."""

from ..core.ocr import (
    OCRDependencyError,
    OCRInputError,
    OCRProcessingError,
    TesseractOCR,
)

__all__ = [
    "OCRDependencyError",
    "OCRInputError",
    "OCRProcessingError",
    "TesseractOCR",
]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
