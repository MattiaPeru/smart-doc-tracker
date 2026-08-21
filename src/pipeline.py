"""Cross-component orchestration for local document workflows."""

from __future__ import annotations

from collections.abc import Callable
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date
from enum import StrEnum
from pathlib import Path

from core.file_hash import calculate_file_sha256
from core.file_hash import FileHashingError
from core.ocr import OCRDependencyError, OCRInputError, OCRProcessingError
from core.parser import DocumentParsingError
from core.pdf import (
    ExtractedPage,
    PDFDependencyError,
    PDFInputError,
    PDFProcessingError,
)
from db.database import DatabaseError
from db.database import DocumentInsertResult
from inbox import InboxError
from infrastructure.ollama import (
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from interfaces.document_folders import DocumentFolders
from interfaces.document_repository import DocumentRepository
from interfaces.long_structured_document_parser import LongStructuredDocumentParser
from interfaces.notification_sender import NotificationSender
from interfaces.ocr_extractor import OCRExtractor
from interfaces.pdf_page_extractor import PDFPageExtractor
from interfaces.structured_document_parser import StructuredDocumentParser
from models.document import (
    DocumentData,
    StructuredDocumentSection,
)
from notifier.desktop import ExpirationNotification


FileHasher = Callable[[str | Path], str]


@dataclass(slots=True)
class DocumentStoragePipeline:
    """Hash a local source file and persist its validated document data."""

    repository: DocumentRepository
    file_hasher: FileHasher = calculate_file_sha256

    def store(
        self,
        source_path: str | Path,
        document: DocumentData,
        *,
        sections: Sequence[StructuredDocumentSection] = (),
    ) -> DocumentInsertResult:
        """Persist document data and optional sections using the source file hash."""
        result = self.repository.insert_document(
            document,
            file_hash=self.file_hasher(source_path),
        )
        if sections:
            self.repository.upsert_document_sections(result.record.id, sections)
        return result


class DocumentProcessingStage(StrEnum):
    """Observable stages of local single-document processing."""

    EXTRACTION_STARTED = "extraction_started"
    EXTRACTION_COMPLETED = "extraction_completed"
    PARSING_STARTED = "parsing_started"
    PARSING_COMPLETED = "parsing_completed"
    STORAGE_STARTED = "storage_started"


ProcessingProgressReporter = Callable[[DocumentProcessingStage], None]


@dataclass(frozen=True, slots=True)
class DocumentProcessingResult:
    """Data produced by one local document-processing workflow."""

    raw_text: str
    document: DocumentData | None = None
    insert_result: DocumentInsertResult | None = None


@dataclass(slots=True)
class DocumentProcessingPipeline:
    """Extract, optionally parse, and optionally store one local document."""

    ocr: OCRExtractor
    parser: StructuredDocumentParser | None = None
    pdf_extractor: PDFPageExtractor | None = None
    long_document_parser: LongStructuredDocumentParser | None = None
    repository: DocumentRepository | None = None
    repository_factory: Callable[[], DocumentRepository] | None = None
    language: str = "eng"
    progress_reporter: ProcessingProgressReporter | None = None

    def process(
        self,
        source_path: str | Path,
        *,
        structured: bool = False,
        store: bool = False,
    ) -> DocumentProcessingResult:
        """Run the requested local stages in order and return prepared results."""
        if store and not structured:
            raise ValueError("Storage requires structured document processing.")

        path = Path(source_path)
        is_pdf = path.suffix.lower() == ".pdf"
        self._report(DocumentProcessingStage.EXTRACTION_STARTED)
        pages: tuple[ExtractedPage, ...] | None = None
        if is_pdf:
            if self.pdf_extractor is None:
                raise PDFDependencyError("PDF extraction is not configured.")
            pages = self.pdf_extractor.extract_pages(path, language=self.language)
            raw_text = "\n\n".join(
                f"[Page {page.page_number}]\n{page.text}" for page in pages
            )
        else:
            raw_text = self.ocr.extract_text(path, language=self.language)
        self._report(DocumentProcessingStage.EXTRACTION_COMPLETED)

        if not structured:
            return DocumentProcessingResult(raw_text=raw_text)

        self._report(DocumentProcessingStage.PARSING_STARTED)
        sections: Sequence[StructuredDocumentSection] = ()
        if pages is not None:
            if self.long_document_parser is None:
                raise PDFDependencyError("Long PDF parsing is not configured.")
            parsed = self.long_document_parser.parse_pages(pages)
            document = parsed.document
            sections = parsed.sections
        else:
            if self.parser is None:
                raise DocumentParsingError("Document parsing is not configured.")
            document = self.parser.parse(raw_text)
        self._report(DocumentProcessingStage.PARSING_COMPLETED)

        if not store:
            return DocumentProcessingResult(raw_text=raw_text, document=document)

        self._report(DocumentProcessingStage.STORAGE_STARTED)
        if self.repository is not None:
            insert_result = DocumentStoragePipeline(self.repository).store(
                path,
                document,
                sections=sections,
            )
        elif self.repository_factory is not None:
            with self.repository_factory() as repository:
                insert_result = DocumentStoragePipeline(repository).store(
                    path,
                    document,
                    sections=sections,
                )
        else:
            raise DatabaseError("Document storage is not configured.")

        return DocumentProcessingResult(
            raw_text=raw_text,
            document=document,
            insert_result=insert_result,
        )

    def _report(self, stage: DocumentProcessingStage) -> None:
        """Report a processing stage when an observer is configured."""
        if self.progress_reporter is not None:
            self.progress_reporter(stage)


@dataclass(frozen=True, slots=True)
class InboxProcessingResult:
    """Privacy-conscious summary of one inbox scan."""

    discovered: int
    processed: int
    already_present: int
    failed: int
    skipped: int


@dataclass(slots=True)
class InboxProcessingPipeline:
    """Run OCR, parsing, persistence, and archiving for local inbox files."""

    ocr: OCRExtractor
    parser: StructuredDocumentParser
    repository: DocumentRepository
    folders: DocumentFolders
    language: str = "eng"
    pdf_extractor: PDFPageExtractor | None = None
    long_document_parser: LongStructuredDocumentParser | None = None

    def process(self) -> InboxProcessingResult:
        """Process every supported inbox file, isolating expected per-file failures."""
        scan = self.folders.scan()
        processed = 0
        already_present = 0
        failed = 0

        document_pipeline = DocumentProcessingPipeline(
            ocr=self.ocr,
            parser=self.parser,
            pdf_extractor=self.pdf_extractor,
            long_document_parser=self.long_document_parser,
            repository=self.repository,
            language=self.language,
        )
        for source_path in scan.files:
            try:
                processing_result = document_pipeline.process(
                    source_path,
                    structured=True,
                    store=True,
                )
                self.folders.archive(source_path)
            except (
                OCRInputError,
                OCRDependencyError,
                OCRProcessingError,
                PDFInputError,
                PDFDependencyError,
                PDFProcessingError,
                DocumentParsingError,
                OllamaConfigurationError,
                OllamaConnectionError,
                OllamaResponseError,
                FileHashingError,
                DatabaseError,
                InboxError,
            ):
                failed += 1
                continue

            processed += 1
            insert_result = processing_result.insert_result
            if insert_result is None:
                raise RuntimeError(
                    "Stored processing did not return a persistence result"
                )
            if not insert_result.inserted:
                already_present += 1

        return InboxProcessingResult(
            discovered=len(scan.files),
            processed=processed,
            already_present=already_present,
            failed=failed,
            skipped=scan.skipped,
        )


@dataclass(frozen=True, slots=True)
class ExpirationCheckResult:
    """Summary of a completed expiration check."""

    documents_found: int
    notifications_sent: int


@dataclass(slots=True)
class ExpirationTrackingPipeline:
    """Query upcoming expirations and send privacy-conscious local alerts."""

    repository: DocumentRepository
    notifier: NotificationSender
    today_provider: Callable[[], date] = date.today

    def check(self, days_threshold: int = 30) -> ExpirationCheckResult:
        """Notify once for each document expiring inside the inclusive window."""
        if days_threshold < 0:
            raise ValueError("days_threshold cannot be negative")

        documents = self.repository.get_expiring_documents(
            days_threshold,
            today=self.today_provider(),
        )
        notifications_sent = 0
        for record in documents:
            expiry_date = record.document.expiry_date
            if expiry_date is None:
                continue
            document_label = record.document.document_type.replace("_", " ").title()
            self.notifier.send(
                ExpirationNotification(
                    title="Document expiration reminder",
                    message=f"{document_label} expires on {expiry_date.isoformat()}.",
                )
            )
            notifications_sent += 1

        return ExpirationCheckResult(
            documents_found=len(documents),
            notifications_sent=notifications_sent,
        )
