"""Core document-processing components."""

from core.ocr import OCRDependencyError, OCRInputError, OCRProcessingError, TesseractOCR

__all__ = [
    "OCRDependencyError",
    "OCRInputError",
    "OCRProcessingError",
    "TesseractOCR",
]
