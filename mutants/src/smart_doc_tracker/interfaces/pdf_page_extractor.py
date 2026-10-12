"""Page extraction interface for local PDF files."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from ..core.pdf import ExtractedPage


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPDFPageExtractorǁextract_pages__mutmut: MutantDict = {}  # type: ignore


class PDFPageExtractor(Protocol):
    """Extract page-aware text from local PDF files."""

    @_mutmut_mutated(mutants_xǁPDFPageExtractorǁextract_pages__mutmut)
    def extract_pages(
        self,
        pdf_path: str | Path,
        *,
        language: str = "eng",
    ) -> tuple[ExtractedPage, ...]:
        """Extract page-aware text from one local PDF."""
        ...

    def xǁPDFPageExtractorǁextract_pages__mutmut_orig(
        self,
        pdf_path: str | Path,
        *,
        language: str = "eng",
    ) -> tuple[ExtractedPage, ...]:
        """Extract page-aware text from one local PDF."""
        ...

    def xǁPDFPageExtractorǁextract_pages__mutmut_1(
        self,
        pdf_path: str | Path,
        *,
        language: str = "XXengXX",
    ) -> tuple[ExtractedPage, ...]:
        """Extract page-aware text from one local PDF."""
        ...

    def xǁPDFPageExtractorǁextract_pages__mutmut_2(
        self,
        pdf_path: str | Path,
        *,
        language: str = "ENG",
    ) -> tuple[ExtractedPage, ...]:
        """Extract page-aware text from one local PDF."""
        ...

mutants_xǁPDFPageExtractorǁextract_pages__mutmut['_mutmut_orig'] = PDFPageExtractor.xǁPDFPageExtractorǁextract_pages__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPDFPageExtractorǁextract_pages__mutmut['xǁPDFPageExtractorǁextract_pages__mutmut_1'] = PDFPageExtractor.xǁPDFPageExtractorǁextract_pages__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPDFPageExtractorǁextract_pages__mutmut['xǁPDFPageExtractorǁextract_pages__mutmut_2'] = PDFPageExtractor.xǁPDFPageExtractorǁextract_pages__mutmut_2 # type: ignore # mutmut generated
