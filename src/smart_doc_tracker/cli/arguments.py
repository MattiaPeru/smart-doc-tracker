"""Command-line argument definitions and validation."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from ..scheduler import parse_daily_time


class CliArgumentParser:
    """Build and evaluate arguments accepted by the local command-line app."""

    def __init__(self) -> None:
        """Create the underlying argument parser."""
        self._parser = self._build_parser()

    def parse(self, argv: Sequence[str] | None = None) -> argparse.Namespace:
        """Return validated command-line arguments."""
        return self._parser.parse_args(argv)

    @staticmethod
    def _build_parser() -> argparse.ArgumentParser:
        """Define all supported command-line arguments."""
        parser = argparse.ArgumentParser(
            description="Run privacy-first local document processing workflows."
        )
        parser.add_argument(
            "image", nargs="?", type=Path, help="Path to a local image file."
        )
        parser.add_argument(
            "--language",
            default="eng",
            help="Installed Tesseract language code (default: eng).",
        )
        parser.add_argument(
            "--structured",
            action="store_true",
            help="Parse OCR text into validated JSON with a local Ollama model.",
        )
        parser.add_argument(
            "--store",
            action="store_true",
            help="Store validated structured data in the local MongoDB database.",
        )
        operation_group = parser.add_mutually_exclusive_group()
        operation_group.add_argument(
            "--list-stored",
            action="store_true",
            help="Print every document stored by this project as JSON.",
        )
        operation_group.add_argument(
            "--get-stored",
            metavar="DOCUMENT_ID",
            help="Print one stored document by its MongoDB identifier.",
        )
        operation_group.add_argument(
            "--check-expirations",
            action="store_true",
            help="Check upcoming expirations and send local desktop alerts once.",
        )
        operation_group.add_argument(
            "--monitor-expirations",
            action="store_true",
            help="Run the expiration check every day in the foreground.",
        )
        operation_group.add_argument(
            "--process-inbox",
            action="store_true",
            help="Process all supported images currently in the local inbox.",
        )
        parser.add_argument(
            "--inbox-dir",
            type=Path,
            default=Path("data/inbox"),
            help=(
                "Local inbox folder used by automated processing (default: data/inbox)."
            ),
        )
        parser.add_argument(
            "--processed-dir",
            type=Path,
            default=Path("data/processed"),
            help=(
                "Local archive folder for processed files (default: data/processed)."
            ),
        )
        parser.add_argument(
            "--days-threshold",
            type=CliArgumentParser._non_negative_integer,
            default=None,
            help=(
                "Run the complete inbox and expiration pipeline using this inclusive "
                "expiration window. Expiration-only modes default to 30 days."
            ),
        )
        parser.add_argument(
            "--check-time",
            type=parse_daily_time,
            default=parse_daily_time("09:00"),
            metavar="HH:MM",
            help="Local daily check time for monitoring mode (default: 09:00).",
        )
        parser.add_argument(
            "--model",
            default="qwen2.5:3b",
            help="Locally installed Ollama model (default: qwen2.5:3b).",
        )
        parser.add_argument(
            "--ollama-url",
            default="http://127.0.0.1:11434",
            help="Loopback-only Ollama endpoint (default: http://127.0.0.1:11434).",
        )
        return parser

    @staticmethod
    def _non_negative_integer(value: str) -> int:
        """Parse an integer value and reject negative numbers."""
        try:
            parsed = int(value)
        except ValueError as exc:
            raise argparse.ArgumentTypeError("must be a non-negative integer") from exc
        if parsed < 0:
            raise argparse.ArgumentTypeError("must be a non-negative integer")
        return parsed
