"""Single-document extraction, parsing, and storage workflow."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from cli.dependencies import CliDependencies
from cli.serializer import JsonResultSerializer
from controllers.document_manager import DocumentManager
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
from db.database import DatabaseConfigurationError, DatabaseError, MongoDocumentRepository
from infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from models.document import ParsedLongDocument


@dataclass(slots=True)
class DocumentProcessingController:
    """Coordinate components needed to process one local document."""

    dependencies: CliDependencies

    def process_document(self, args: argparse.Namespace) -> int:
        """Extract, optionally parse, and optionally store one local document."""
        dependencies = self.dependencies
        stdout = dependencies.stdout
        stderr = dependencies.stderr
        ocr = dependencies.ocr or TesseractOCR()
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
                pages = (
                    dependencies.pdf_extractor or LocalPDFTextExtractor()
                ).extract_pages(args.image, language=args.language)
                raw_text = "\n\n".join(
                    f"[Page {page.page_number}]\n{page.text}" for page in pages
                )
            else:
                print(
                    f"[1/{total_steps}] Waiting for local Tesseract OCR to extract text...",
                    file=stderr,
                    flush=True,
                )
                raw_text = ocr.extract_text(args.image, language=args.language)
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
                f"[2/{total_steps}] Waiting for local Ollama model '{args.model}' "
                "to generate structured data...",
                file=stderr,
                flush=True,
            )
            parsed_long_document: ParsedLongDocument | None = None
            if pages is not None:
                parsed_long_document = (
                    dependencies.long_document_parser
                    or LongDocumentParser(
                        generator,
                        progress_callback=lambda current, total: print(
                            f"[2/{total_steps}] Analyzing PDF section "
                            f"{current}/{total}...",
                            file=stderr,
                            flush=True,
                        ),
                    )
                ).parse_pages(pages)
                document = parsed_long_document.document
            else:
                parser = dependencies.document_parser or DocumentParser(generator)
                document = parser.parse(raw_text)
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

        print(
            f"[2/{total_steps}] Structured parsing completed.",
            file=stderr,
            flush=True,
        )
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
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                result = DocumentManager(repository).insert_document(
                    args.image,
                    document,
                    sections=(
                        parsed_long_document.sections
                        if parsed_long_document is not None
                        else ()
                    ),
                )
        except (FileHashingError, DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Storage failed: {exc}", file=stderr)
            return 1

        status = "inserted" if result.inserted else "already present"
        print(
            f"[3/3] MongoDB storage completed ({status}).",
            file=stderr,
            flush=True,
        )
        JsonResultSerializer.write(JsonResultSerializer.insert_result(result), stdout)
        return 0
