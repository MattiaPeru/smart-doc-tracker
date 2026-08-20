"""Command-line application and command dispatch for local document workflows."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import time
from pathlib import Path
from typing import TextIO

from cli.dependencies import CliDependencies
from cli.interfaces import (
    DocumentFoldersFactory,
    OCRService,
    ParserService,
    RepositoryFactory,
    SchedulerFactory,
)
from cli.serializer import JsonResultSerializer

from core.file_hash import FileHashingError
from core.ocr import OCRDependencyError, OCRInputError, OCRProcessingError, TesseractOCR
from core.parser import DocumentParser, DocumentParsingError, LongDocumentParser
from core.pdf import (
    ExtractedPage,
    LocalPDFTextExtractor,
    PDFDependencyError,
    PDFInputError,
    PDFProcessingError,
)
from db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)
from infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from inbox import InboxError
from models.document import ParsedLongDocument
from notifier.desktop import DesktopNotificationError, PlyerDesktopNotifier
from pipeline import (
    DocumentStoragePipeline,
    ExpirationCheckResult,
    ExpirationTrackingPipeline,
    InboxProcessingPipeline,
    InboxProcessingResult,
    LongStructuredDocumentParser,
    NotificationSender,
    PDFPageExtractor,
)
from scheduler import (
    DailyTaskScheduler,
    SchedulerConfigurationError,
    SchedulerError,
)

@dataclass(slots=True)
class CliApplication:
    """Dispatch parsed arguments to focused local workflow commands."""

    dependencies: CliDependencies

    def execute(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments to the matching command workflow."""
        dependencies = self.dependencies
        create_repository = (
            dependencies.repository_factory or MongoDocumentRepository.connect
        )
        notifier = dependencies.notifier or PlyerDesktopNotifier()
        days_threshold = args.days_threshold if args.days_threshold is not None else 30

        if args.list_stored:
            return _list_stored_documents(
                create_repository,
                stdout=dependencies.stdout,
                stderr=dependencies.stderr,
            )
        if args.get_stored is not None:
            return _get_stored_document(
                args.get_stored,
                create_repository,
                stdout=dependencies.stdout,
                stderr=dependencies.stderr,
            )
        if args.check_expirations:
            return _check_expirations(
            create_repository,
            notifier,
            days_threshold=days_threshold,
            stdout=dependencies.stdout,
            stderr=dependencies.stderr,
        )
        if args.monitor_expirations:
            return _monitor_expirations(
            create_repository,
            notifier,
            days_threshold=days_threshold,
            check_time=args.check_time,
            scheduler_factory=dependencies.scheduler_factory,
            stderr=dependencies.stderr,
        )
        if args.process_inbox:
            return _process_inbox(
            create_repository,
            dependencies.ocr or TesseractOCR(),
            dependencies.document_parser,
            language=args.language,
            model=args.model,
            ollama_url=args.ollama_url,
            inbox_dir=args.inbox_dir,
            processed_dir=args.processed_dir,
            folders_factory=dependencies.folders_factory,
            pdf_extractor=dependencies.pdf_extractor,
            long_document_parser=dependencies.long_document_parser,
            stdout=dependencies.stdout,
            stderr=dependencies.stderr,
        )
        if args.image is None and args.days_threshold is not None:
            return _run_complete_pipeline(
                create_repository,
                dependencies.ocr or TesseractOCR(),
                dependencies.document_parser,
                notifier,
                days_threshold=days_threshold,
                language=args.language,
                model=args.model,
                ollama_url=args.ollama_url,
                inbox_dir=args.inbox_dir,
                processed_dir=args.processed_dir,
                folders_factory=dependencies.folders_factory,
                pdf_extractor=dependencies.pdf_extractor,
                long_document_parser=dependencies.long_document_parser,
                stdout=dependencies.stdout,
                stderr=dependencies.stderr,
            )
        if args.image is None:
            print("Input error: an image path is required.", file=dependencies.stderr)
            return 2
        if args.store and not args.structured:
            print("Input error: --store requires --structured.", file=dependencies.stderr)
            return 2

        return _process_single_document(
            args,
            create_repository,
            dependencies,
        )


def _process_single_document(
    args: argparse.Namespace,
    create_repository: RepositoryFactory,
    dependencies: CliDependencies,
) -> int:
    """Extract, optionally parse, and optionally store one local document."""
    stdout = dependencies.stdout
    stderr = dependencies.stderr
    service = dependencies.ocr or TesseractOCR()
    document_parser = dependencies.document_parser
    pdf_extractor = dependencies.pdf_extractor
    long_document_parser = dependencies.long_document_parser
    is_pdf = args.image.suffix.lower() == ".pdf"
    total_steps = 3 if args.store else (2 if args.structured else 1)
    pages: tuple[ExtractedPage, ...] | None = None

    try:
        if is_pdf:
            print(
                f"[1/{total_steps}] Extracting PDF text page by page locally...",
                file=stderr,
                flush=True,
            )
            pages = (pdf_extractor or LocalPDFTextExtractor()).extract_pages(
                args.image,
                language=args.language,
            )
            raw_text = "\n\n".join(
                f"[Page {page.page_number}]\n{page.text}" for page in pages
            )
        else:
            print(
                f"[1/{total_steps}] Waiting for local Tesseract OCR to extract text...",
                file=stderr,
                flush=True,
            )
            raw_text = service.extract_text(args.image, language=args.language)
    except (
        OCRInputError,
        OCRDependencyError,
        OCRProcessingError,
        PDFInputError,
        PDFDependencyError,
        PDFProcessingError,
    ) as exc:
        failure_label = "PDF extraction" if is_pdf else "OCR"
        print(f"{failure_label} failed: {exc}", file=stderr)
        return 1

    extraction_label = "PDF extraction" if is_pdf else "OCR"
    print(
        f"[1/{total_steps}] {extraction_label} completed.",
        file=stderr,
        flush=True,
    )

    if not args.structured:
        stdout.write(raw_text)
        if raw_text and not raw_text.endswith("\n"):
            stdout.write("\n")
        return 0

    try:
        generator = OllamaClient(base_url=args.ollama_url, model=args.model)
        print(
            f"[2/{total_steps}] Waiting for local Ollama model '{args.model}' to generate "
            "structured data...",
            file=stderr,
            flush=True,
        )
        parsed_long_document: ParsedLongDocument | None = None
        if pages is not None:
            parsed_long_document = (
                long_document_parser
                or LongDocumentParser(
                    generator,
                    progress_callback=lambda current, total: print(
                        f"[2/{total_steps}] Analyzing PDF section {current}/{total}...",
                        file=stderr,
                        flush=True,
                    ),
                )
            ).parse_pages(pages)
            document = parsed_long_document.document
        else:
            parser_service = document_parser or DocumentParser(generator)
            document = parser_service.parse(raw_text)
    except DocumentParsingError as exc:
        print(f"Parsing failed: {exc}", file=stderr)
        return 1
    except (
        OllamaConfigurationError,
        OllamaConnectionError,
        OllamaResponseError,
    ) as exc:
        print(f"Parsing failed: {exc}", file=stderr)
        return 1

    print(f"[2/{total_steps}] Structured parsing completed.", file=stderr, flush=True)

    if not args.store:
        JsonResultSerializer.write(
            JsonResultSerializer.document(document),
            stdout,
        )
        return 0

    try:
        print(
            "[3/3] Storing validated data in local MongoDB...",
            file=stderr,
            flush=True,
        )
        with create_repository() as repository:
            result = DocumentStoragePipeline(repository).store(args.image, document)
            if parsed_long_document is not None:
                repository.upsert_document_sections(
                    result.record.id,
                    parsed_long_document.sections,
                )
    except (FileHashingError, DatabaseConfigurationError, DatabaseError) as exc:
        print(f"Storage failed: {exc}", file=stderr)
        return 1

    status = "inserted" if result.inserted else "already present"
    print(f"[3/3] MongoDB storage completed ({status}).", file=stderr, flush=True)
    JsonResultSerializer.write(JsonResultSerializer.insert_result(result), stdout)
    return 0


def _list_stored_documents(
    repository_factory: RepositoryFactory,
    *,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    """Print every locally stored document as JSON."""
    try:
        print(
            "[1/1] Reading stored documents from local MongoDB...",
            file=stderr,
            flush=True,
        )
        with repository_factory() as repository:
            documents = repository.get_all_documents()
    except (DatabaseConfigurationError, DatabaseError) as exc:
        print(f"Database read failed: {exc}", file=stderr)
        return 1
    print(
        f"[1/1] Database read completed ({len(documents)} document(s)).",
        file=stderr,
        flush=True,
    )
    JsonResultSerializer.write(
        [JsonResultSerializer.stored_document(item) for item in documents],
        stdout,
    )
    return 0


def _get_stored_document(
    document_id: str,
    repository_factory: RepositoryFactory,
    *,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    """Print one locally stored document selected by identifier."""
    try:
        print(
            "[1/1] Reading the stored document from local MongoDB...",
            file=stderr,
            flush=True,
        )
        with repository_factory() as repository:
            document = repository.get_document_by_id(document_id)
    except (DatabaseConfigurationError, DatabaseError) as exc:
        print(f"Database read failed: {exc}", file=stderr)
        return 1
    if document is None:
        print("Stored document not found.", file=stderr)
        return 1
    print("[1/1] Database read completed.", file=stderr, flush=True)
    JsonResultSerializer.write(JsonResultSerializer.stored_document(document), stdout)
    return 0


def _check_expirations(
    repository_factory: RepositoryFactory,
    notifier: NotificationSender,
    *,
    days_threshold: int,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    """Run one expiration check and print its summary."""
    try:
        print(
            f"[1/1] Checking documents expiring within {days_threshold} day(s)...",
            file=stderr,
            flush=True,
        )
        result = _perform_expiration_check(
            repository_factory,
            notifier,
            days_threshold=days_threshold,
        )
    except (DatabaseConfigurationError, DatabaseError, DesktopNotificationError) as exc:
        print(f"Expiration check failed: {exc}", file=stderr)
        return 1
    print(
        "[1/1] Expiration check completed: "
        f"{result.documents_found} document(s), "
        f"{result.notifications_sent} notification(s).",
        file=stderr,
        flush=True,
    )
    JsonResultSerializer.write(JsonResultSerializer.expiration_result(result), stdout)
    return 0


def _monitor_expirations(
    repository_factory: RepositoryFactory,
    notifier: NotificationSender,
    *,
    days_threshold: int,
    check_time: time,
    scheduler_factory: SchedulerFactory | None,
    stderr: TextIO,
) -> int:
    """Schedule recurring local expiration checks in the foreground."""
    def scheduled_check() -> None:
        """Execute one scheduled check and report its outcome."""
        try:
            result = _perform_expiration_check(
                repository_factory,
                notifier,
                days_threshold=days_threshold,
            )
            print(
                "Daily expiration check completed: "
                f"{result.documents_found} document(s), "
                f"{result.notifications_sent} notification(s).",
                file=stderr,
                flush=True,
            )
        except (
            DatabaseConfigurationError,
            DatabaseError,
            DesktopNotificationError,
        ) as exc:
            print(f"Daily expiration check failed: {exc}", file=stderr, flush=True)

    create_scheduler = scheduler_factory or (
        lambda task, scheduled_time: DailyTaskScheduler(
            task,
            check_time=scheduled_time,
        )
    )
    print(
        f"Expiration monitoring scheduled daily at {check_time.strftime('%H:%M')}.",
        file=stderr,
        flush=True,
    )
    try:
        create_scheduler(scheduled_check, check_time).run()
    except KeyboardInterrupt:
        print("Expiration monitoring stopped.", file=stderr)
        return 0
    except (SchedulerConfigurationError, SchedulerError) as exc:
        print(f"Expiration monitoring failed: {exc}", file=stderr)
        return 1
    return 0


def _perform_expiration_check(
    repository_factory: RepositoryFactory,
    notifier: NotificationSender,
    *,
    days_threshold: int,
) -> ExpirationCheckResult:
    """Open the repository and execute the expiration pipeline once."""
    with repository_factory() as repository:
        return ExpirationTrackingPipeline(repository, notifier).check(days_threshold)


def _process_inbox(
    repository_factory: RepositoryFactory,
    ocr: OCRService,
    document_parser: ParserService | None,
    *,
    language: str,
    model: str,
    ollama_url: str,
    inbox_dir: Path,
    processed_dir: Path,
    folders_factory: DocumentFoldersFactory,
    pdf_extractor: PDFPageExtractor | None,
    long_document_parser: LongStructuredDocumentParser | None,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    """Process supported documents currently present in the local inbox."""
    try:
        generator = OllamaClient(base_url=ollama_url, model=model)
        parser_service = document_parser or DocumentParser(generator)
        long_parser_service = long_document_parser or LongDocumentParser(
            generator,
            progress_callback=lambda current, total: print(
                f"Analyzing PDF section {current}/{total}...",
                file=stderr,
                flush=True,
            ),
        )
        folders = folders_factory(inbox_dir, processed_dir)
        print(
            "[1/1] Scanning and processing the local document inbox...",
            file=stderr,
            flush=True,
        )
        with repository_factory() as repository:
            result = InboxProcessingPipeline(
                ocr=ocr,
                parser=parser_service,
                repository=repository,
                folders=folders,
                language=language,
                pdf_extractor=pdf_extractor or LocalPDFTextExtractor(),
                long_document_parser=long_parser_service,
            ).process()
    except (
        InboxError,
        DatabaseConfigurationError,
        DatabaseError,
        OllamaConfigurationError,
    ) as exc:
        print(f"Inbox processing failed: {exc}", file=stderr)
        return 1

    JsonResultSerializer.write(JsonResultSerializer.inbox_result(result), stdout)
    if result.failed:
        print(
            f"[1/1] Inbox processing completed with {result.failed} failed file(s).",
            file=stderr,
            flush=True,
        )
        return 1
    print(
        f"[1/1] Inbox processing completed for {result.processed} file(s).",
        file=stderr,
        flush=True,
    )
    return 0


def _run_complete_pipeline(
    repository_factory: RepositoryFactory,
    ocr: OCRService,
    document_parser: ParserService | None,
    notifier: NotificationSender,
    *,
    days_threshold: int,
    language: str,
    model: str,
    ollama_url: str,
    inbox_dir: Path,
    processed_dir: Path,
    folders_factory: DocumentFoldersFactory,
    pdf_extractor: PDFPageExtractor | None,
    long_document_parser: LongStructuredDocumentParser | None,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    """Process the inbox and then check stored document expirations."""
    try:
        generator = OllamaClient(base_url=ollama_url, model=model)
        parser_service = document_parser or DocumentParser(generator)
        long_parser_service = long_document_parser or LongDocumentParser(
            generator,
            progress_callback=lambda current, total: print(
                f"Analyzing PDF section {current}/{total}...",
                file=stderr,
                flush=True,
            ),
        )
        folders = folders_factory(inbox_dir, processed_dir)
        print("Starting the complete local document pipeline...", file=stderr, flush=True)
        with repository_factory() as repository:
            try:
                print(
                    "[1/2] Scanning and processing the local document inbox...",
                    file=stderr,
                    flush=True,
                )
                inbox_result = InboxProcessingPipeline(
                    ocr=ocr,
                    parser=parser_service,
                    repository=repository,
                    folders=folders,
                    language=language,
                    pdf_extractor=pdf_extractor or LocalPDFTextExtractor(),
                    long_document_parser=long_parser_service,
                ).process()
                print(
                    "[1/2] Inbox processing completed: "
                    f"{inbox_result.processed} processed, "
                    f"{inbox_result.already_present} already present, "
                    f"{inbox_result.failed} failed.",
                    file=stderr,
                    flush=True,
                )
            except InboxError as exc:
                print(f"Inbox processing failed: {exc}", file=stderr)
                inbox_result = InboxProcessingResult(
                    discovered=0,
                    processed=0,
                    already_present=0,
                    failed=1,
                    skipped=0,
                )

            print(
                f"[2/2] Checking documents expiring within {days_threshold} day(s)...",
                file=stderr,
                flush=True,
            )
            expiration_result = ExpirationTrackingPipeline(
                repository,
                notifier,
            ).check(days_threshold)
            print(
                "[2/2] Expiration check completed: "
                f"{expiration_result.documents_found} document(s), "
                f"{expiration_result.notifications_sent} notification(s).",
                file=stderr,
                flush=True,
            )
    except (
        DatabaseConfigurationError,
        DatabaseError,
        DesktopNotificationError,
        OllamaConfigurationError,
    ) as exc:
        print(f"Complete pipeline failed: {exc}", file=stderr)
        return 1

    JsonResultSerializer.write(
        {
            "inbox": JsonResultSerializer.inbox_result(inbox_result),
            "expirations": JsonResultSerializer.expiration_result(expiration_result),
        },
        stdout,
    )
    print(
        "Complete local document pipeline finished.",
        file=stderr,
        flush=True,
    )
    return 1 if inbox_result.failed else 0
