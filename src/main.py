"""Command-line entry point for local document OCR."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Protocol, TextIO

from core.ocr import OCRDependencyError, OCRInputError, OCRProcessingError, TesseractOCR


class OCRService(Protocol):
    """Narrow interface required by the Phase 1 command-line workflow."""

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str: ...


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract raw text from a local image with Tesseract OCR."
    )
    parser.add_argument("image", type=Path, help="Path to a local image file.")
    parser.add_argument(
        "--language",
        default="eng",
        help="Installed Tesseract language code (default: eng).",
    )
    return parser


def run(
    argv: Sequence[str] | None = None,
    *,
    ocr: OCRService | None = None,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
) -> int:
    args = build_parser().parse_args(argv)
    service = ocr or TesseractOCR()

    try:
        raw_text = service.extract_text(args.image, language=args.language)
    except (OCRInputError, OCRDependencyError, OCRProcessingError) as exc:
        print(f"OCR failed: {exc}", file=stderr)
        return 1

    stdout.write(raw_text)
    if raw_text and not raw_text.endswith("\n"):
        stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
