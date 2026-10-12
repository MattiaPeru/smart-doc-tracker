"""OCR extraction interface for local images."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOCRExtractorǁextract_text__mutmut: MutantDict = {}  # type: ignore


class OCRExtractor(Protocol):
    """Extract raw text from local images."""

    @_mutmut_mutated(mutants_xǁOCRExtractorǁextract_text__mutmut)
    def extract_text(
        self,
        image_path: str | Path,
        *,
        language: str = "eng",
    ) -> str:
        """Extract raw text from one local image."""
        ...

    def xǁOCRExtractorǁextract_text__mutmut_orig(
        self,
        image_path: str | Path,
        *,
        language: str = "eng",
    ) -> str:
        """Extract raw text from one local image."""
        ...

    def xǁOCRExtractorǁextract_text__mutmut_1(
        self,
        image_path: str | Path,
        *,
        language: str = "XXengXX",
    ) -> str:
        """Extract raw text from one local image."""
        ...

    def xǁOCRExtractorǁextract_text__mutmut_2(
        self,
        image_path: str | Path,
        *,
        language: str = "ENG",
    ) -> str:
        """Extract raw text from one local image."""
        ...

mutants_xǁOCRExtractorǁextract_text__mutmut['_mutmut_orig'] = OCRExtractor.xǁOCRExtractorǁextract_text__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOCRExtractorǁextract_text__mutmut['xǁOCRExtractorǁextract_text__mutmut_1'] = OCRExtractor.xǁOCRExtractorǁextract_text__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOCRExtractorǁextract_text__mutmut['xǁOCRExtractorǁextract_text__mutmut_2'] = OCRExtractor.xǁOCRExtractorǁextract_text__mutmut_2 # type: ignore # mutmut generated
