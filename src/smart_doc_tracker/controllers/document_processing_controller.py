"""CLI presentation for single-document processing."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..core.file_hash import FileHashingError
from ..core.ocr import (
    OCRDependencyError,
    OCRInputError,
    OCRProcessingError,
    TesseractOCR,
)
from ..core.parser import DocumentParser, DocumentParsingError, LongDocumentParser
from ..core.pdf import (
    LocalPDFTextExtractor,
    PDFDependencyError,
    PDFInputError,
    PDFProcessingError,
)
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)
from ..infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from ..pipeline import DocumentProcessingPipeline, DocumentProcessingStage


@dataclass(slots=True)
class DocumentProcessingController:
    """Prepare dependencies and render one document workflow for the CLI."""

    dependencies: CliDependencies

    def process_document(self, args: argparse.Namespace) -> int:
        """Run one document pipeline and render its output or sanitized failure."""
        dependencies = self.dependencies
        stdout = dependencies.stdout
        stderr = dependencies.stderr
        is_pdf = args.image.suffix.lower() == ".pdf"
        extraction_label = "PDF extraction" if is_pdf else "OCR"
        total_steps = 3 if args.store else (2 if args.structured else 1)

        def report_progress(stage: DocumentProcessingStage) -> None:
            """Render pipeline stage transitions without handling workflow logic."""
            if stage is DocumentProcessingStage.EXTRACTION_STARTED:
                action = (
                    "Extracting PDF text page by page locally"
                    if is_pdf
                    else "Waiting for local Tesseract OCR to extract text"
                )
                print(f"[1/{total_steps}] {action}...", file=stderr, flush=True)
            elif stage is DocumentProcessingStage.EXTRACTION_COMPLETED:
                print(
                    f"[1/{total_steps}] {extraction_label} completed.",
                    file=stderr,
                    flush=True,
                )
            elif stage is DocumentProcessingStage.PARSING_STARTED:
                print(
                    f"[2/{total_steps}] Waiting for local Ollama model "
                    f"'{args.model}' to generate structured data...",
                    file=stderr,
                    flush=True,
                )
            elif stage is DocumentProcessingStage.PARSING_COMPLETED:
                print(
                    f"[2/{total_steps}] Structured parsing completed.",
                    file=stderr,
                    flush=True,
                )
            elif stage is DocumentProcessingStage.STORAGE_STARTED:
                print(
                    "[3/3] Storing validated data in local MongoDB...",
                    file=stderr,
                    flush=True,
                )

        try:
            parser = None
            long_parser = None
            if args.structured:
                generator = OllamaClient(base_url=args.ollama_url, model=args.model)
                parser = dependencies.document_parser or DocumentParser(generator)
                long_parser = dependencies.long_document_parser or LongDocumentParser(
                    generator,
                    progress_callback=lambda current, total: print(
                        f"[2/{total_steps}] Analyzing PDF section {current}/{total}...",
                        file=stderr,
                        flush=True,
                    ),
                )

            result = DocumentProcessingPipeline(
                ocr=dependencies.ocr or TesseractOCR(),
                parser=parser,
                pdf_extractor=dependencies.pdf_extractor or LocalPDFTextExtractor(),
                long_document_parser=long_parser,
                repository_factory=(
                    dependencies.repository_factory or MongoDocumentRepository.connect
                    if args.store
                    else None
                ),
                language=args.language,
                progress_reporter=report_progress,
            ).process(
                args.image,
                structured=args.structured,
                store=args.store,
            )
        except (
            OCRInputError,
            OCRDependencyError,
            OCRProcessingError,
            PDFInputError,
            PDFDependencyError,
            PDFProcessingError,
        ) as exc:
            print(f"{extraction_label} failed: {exc}", file=stderr)
            return 1
        except (
            DocumentParsingError,
            OllamaConfigurationError,
            OllamaConnectionError,
            OllamaResponseError,
        ) as exc:
            print(f"Parsing failed: {exc}", file=stderr)
            return 1
        except (FileHashingError, DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Storage failed: {exc}", file=stderr)
            return 1

        if not args.structured:
            stdout.write(result.raw_text)
            if result.raw_text and not result.raw_text.endswith("\n"):
                stdout.write("\n")
            return 0

        if result.document is None:
            raise RuntimeError("Structured processing did not return document data")
        if not args.store:
            JsonResultSerializer.write(
                JsonResultSerializer.document(result.document),
                stdout,
            )
            return 0

        if result.insert_result is None:
            raise RuntimeError("Stored processing did not return a persistence result")
        status = "inserted" if result.insert_result.inserted else "already present"
        print(
            f"[3/3] MongoDB storage completed ({status}).",
            file=stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.insert_result(result.insert_result),
            stdout,
        )
        return 0
