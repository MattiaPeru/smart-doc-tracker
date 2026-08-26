"""Inbox processing and combined local-document workflows."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..core.ocr import TesseractOCR
from ..core.parser import DocumentParser, LongDocumentParser
from ..core.pdf import LocalPDFTextExtractor
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)
from ..db.vector_database import VectorDatabaseError
from ..inbox import InboxError
from ..infrastructure.ollama import OllamaClient, OllamaConfigurationError
from ..notifier.desktop import DesktopNotificationError, PlyerDesktopNotifier
from ..pipeline import (
    ExpirationTrackingPipeline,
    ExtractedTextReporter,
    InboxFailureReporter,
    InboxProcessingFailure,
    InboxProcessingPipeline,
    InboxProcessingResult,
)
from .rag_workflow_controller import create_document_vector_index


@dataclass(slots=True)
class InboxWorkflowController:
    """Coordinate multi-document inbox workflows and their CLI output."""

    dependencies: CliDependencies

    def _failure_reporter(self) -> InboxFailureReporter:
        """Build a terminal reporter for safe per-file failure diagnostics."""
        def report(failure: InboxProcessingFailure) -> None:
            """Print one safe and actionable per-file error."""
            print(
                f"[ERROR] File '{failure.file_name}' failed during "
                f"{failure.phase}: {failure.error_type}: {failure.reason}",
                file=self.dependencies.stderr,
                flush=True,
            )

        return report

    def _extracted_text_reporter(
        self, args: argparse.Namespace
    ) -> ExtractedTextReporter | None:
        """Build the opt-in terminal reporter for sensitive extracted text."""
        if not args.print_ocr_text:
            return None

        def report(source_path: Path, raw_text: str) -> None:
            """Print one explicitly requested extraction result locally."""
            print(
                f"--- Extracted text: {source_path.name} ---",
                file=self.dependencies.stderr,
                flush=True,
            )
            print(raw_text, file=self.dependencies.stderr, flush=True)
            print(
                "--- End extracted text ---",
                file=self.dependencies.stderr,
                flush=True,
            )

        return report

    def process_inbox(self, args: argparse.Namespace) -> int:
        """Process supported documents currently present in the local inbox."""
        dependencies = self.dependencies
        try:
            generator = OllamaClient(base_url=args.ollama_url, model=args.model)
            parser = dependencies.document_parser or DocumentParser(generator)
            long_parser = dependencies.long_document_parser or LongDocumentParser(
                generator,
                progress_callback=lambda current, total: print(
                    f"Analyzing PDF section {current}/{total}...",
                    file=dependencies.stderr,
                    flush=True,
                ),
            )
            folders = dependencies.folders_factory(args.inbox_dir, args.processed_dir)
            print(
                "[1/1] Scanning and processing the local document inbox...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                vector_index = dependencies.document_vector_index or (
                    create_document_vector_index(dependencies, args)
                    if dependencies.repository_factory is None
                    else None
                )
                result = InboxProcessingPipeline(
                    ocr=dependencies.ocr or TesseractOCR(),
                    parser=parser,
                    repository=repository,
                    folders=folders,
                    language=args.language,
                    pdf_extractor=(
                        dependencies.pdf_extractor or LocalPDFTextExtractor()
                    ),
                    long_document_parser=long_parser,
                    vector_index=vector_index,
                    extracted_text_reporter=self._extracted_text_reporter(args),
                    failure_reporter=self._failure_reporter(),
                ).process()
        except (
            InboxError,
            DatabaseConfigurationError,
            DatabaseError,
            OllamaConfigurationError,
            VectorDatabaseError,
        ) as exc:
            print(f"Inbox processing failed: {exc}", file=dependencies.stderr)
            return 1

        JsonResultSerializer.write(
            JsonResultSerializer.inbox_result(result),
            dependencies.stdout,
        )
        if result.failed:
            print(
                "[1/1] Inbox processing completed with "
                f"{result.failed} failed file(s).",
                file=dependencies.stderr,
                flush=True,
            )
            return 1
        print(
            f"[1/1] Inbox processing completed for {result.processed} file(s).",
            file=dependencies.stderr,
            flush=True,
        )
        return 0

    def run_complete_pipeline(self, args: argparse.Namespace) -> int:
        """Process the inbox and then check stored document expirations."""
        dependencies = self.dependencies
        days_threshold = args.days_threshold if args.days_threshold is not None else 30
        try:
            generator = OllamaClient(base_url=args.ollama_url, model=args.model)
            parser = dependencies.document_parser or DocumentParser(generator)
            long_parser = dependencies.long_document_parser or LongDocumentParser(
                generator,
                progress_callback=lambda current, total: print(
                    f"Analyzing PDF section {current}/{total}...",
                    file=dependencies.stderr,
                    flush=True,
                ),
            )
            folders = dependencies.folders_factory(args.inbox_dir, args.processed_dir)
            print(
                "Starting the complete local document pipeline...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                vector_index = dependencies.document_vector_index or (
                    create_document_vector_index(dependencies, args)
                    if dependencies.repository_factory is None
                    else None
                )
                try:
                    print(
                        "[1/2] Scanning and processing the local document inbox...",
                        file=dependencies.stderr,
                        flush=True,
                    )
                    inbox_result = InboxProcessingPipeline(
                        ocr=dependencies.ocr or TesseractOCR(),
                        parser=parser,
                        repository=repository,
                        folders=folders,
                        language=args.language,
                        pdf_extractor=(
                            dependencies.pdf_extractor or LocalPDFTextExtractor()
                        ),
                        long_document_parser=long_parser,
                        vector_index=vector_index,
                        extracted_text_reporter=self._extracted_text_reporter(args),
                        failure_reporter=self._failure_reporter(),
                    ).process()
                    print(
                        "[1/2] Inbox processing completed: "
                        f"{inbox_result.processed} processed, "
                        f"{inbox_result.already_present} already present, "
                        f"{inbox_result.failed} failed.",
                        file=dependencies.stderr,
                        flush=True,
                    )
                except InboxError as exc:
                    print(f"Inbox processing failed: {exc}", file=dependencies.stderr)
                    inbox_result = InboxProcessingResult(
                        discovered=0,
                        processed=0,
                        already_present=0,
                        failed=1,
                        skipped=0,
                    )

                print(
                    f"[2/2] Checking documents expiring within "
                    f"{days_threshold} day(s)...",
                    file=dependencies.stderr,
                    flush=True,
                )
                expiration_result = ExpirationTrackingPipeline(
                    repository,
                    dependencies.notifier or PlyerDesktopNotifier(),
                ).check(days_threshold)
                print(
                    "[2/2] Expiration check completed: "
                    f"{expiration_result.documents_found} document(s), "
                    f"{expiration_result.notifications_sent} notification(s).",
                    file=dependencies.stderr,
                    flush=True,
                )
        except (
            DatabaseConfigurationError,
            DatabaseError,
            DesktopNotificationError,
            OllamaConfigurationError,
            VectorDatabaseError,
        ) as exc:
            print(f"Complete pipeline failed: {exc}", file=dependencies.stderr)
            return 1

        JsonResultSerializer.write(
            {
                "inbox": JsonResultSerializer.inbox_result(inbox_result),
                "expirations": JsonResultSerializer.expiration_result(
                    expiration_result
                ),
            },
            dependencies.stdout,
        )
        print(
            "Complete local document pipeline finished.",
            file=dependencies.stderr,
            flush=True,
        )
        return 1 if inbox_result.failed else 0
