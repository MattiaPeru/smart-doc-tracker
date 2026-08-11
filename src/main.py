"""Command-line entry point for local OCR and structured document parsing."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Protocol, TextIO

from core.file_hash import FileHashingError
from core.ocr import OCRDependencyError, OCRInputError, OCRProcessingError, TesseractOCR
from core.parser import DocumentParser, DocumentParsingError
from db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    DocumentInsertResult,
    MongoDocumentRepository,
    StoredDocument,
)
from infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from models.document import DocumentData
from pipeline import DocumentStoragePipeline


class OCRService(Protocol):
    """Narrow interface required by the Phase 1 command-line workflow."""

    def extract_text(self, image_path: str | Path, *, language: str = "eng") -> str: ...


class ParserService(Protocol):
    """Narrow interface required by the structured parsing workflow."""

    def parse(self, raw_text: str) -> DocumentData: ...


class RepositoryService(Protocol):
    """Persistence operations required by the command-line interface."""

    def __enter__(self) -> RepositoryService: ...
    def __exit__(self, *args: object) -> None: ...
    def insert_document(
        self, document: DocumentData, *, file_hash: str
    ) -> DocumentInsertResult: ...
    def get_all_documents(self) -> list[StoredDocument]: ...
    def get_document_by_id(self, document_id: str) -> StoredDocument | None: ...


RepositoryFactory = Callable[[], RepositoryService]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract raw text from a local image with Tesseract OCR."
    )
    parser.add_argument("image", nargs="?", type=Path, help="Path to a local image file.")
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
    read_group = parser.add_mutually_exclusive_group()
    read_group.add_argument(
        "--list-stored",
        action="store_true",
        help="Print every document stored by this project as JSON.",
    )
    read_group.add_argument(
        "--get-stored",
        metavar="DOCUMENT_ID",
        help="Print one stored document by its MongoDB identifier.",
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


def run(
    argv: Sequence[str] | None = None,
    *,
    ocr: OCRService | None = None,
    document_parser: ParserService | None = None,
    repository_factory: RepositoryFactory | None = None,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
) -> int:
    args = build_parser().parse_args(argv)
    create_repository = repository_factory or MongoDocumentRepository.connect

    if args.list_stored:
        return _list_stored_documents(create_repository, stdout=stdout, stderr=stderr)
    if args.get_stored is not None:
        return _get_stored_document(
            args.get_stored,
            create_repository,
            stdout=stdout,
            stderr=stderr,
        )
    if args.image is None:
        print("Input error: an image path is required.", file=stderr)
        return 2
    if args.store and not args.structured:
        print("Input error: --store requires --structured.", file=stderr)
        return 2

    service = ocr or TesseractOCR()
    total_steps = 3 if args.store else (2 if args.structured else 1)

    try:
        print(
            f"[1/{total_steps}] Waiting for local Tesseract OCR to extract text...",
            file=stderr,
            flush=True,
        )
        raw_text = service.extract_text(args.image, language=args.language)
    except (OCRInputError, OCRDependencyError, OCRProcessingError) as exc:
        print(f"OCR failed: {exc}", file=stderr)
        return 1

    print(f"[1/{total_steps}] OCR completed.", file=stderr, flush=True)

    if not args.structured:
        stdout.write(raw_text)
        if raw_text and not raw_text.endswith("\n"):
            stdout.write("\n")
        return 0

    try:
        parser_service = document_parser or DocumentParser(
            OllamaClient(base_url=args.ollama_url, model=args.model)
        )
        print(
            f"[2/{total_steps}] Waiting for local Ollama model '{args.model}' to generate "
            "structured data...",
            file=stderr,
            flush=True,
        )
        document = parser_service.parse(raw_text)
    except DocumentParsingError as exc:
        print(f"Parsing failed: {exc}", file=stderr)
        if exc.generated_response is not None:
            print("Raw LLM response:", file=stderr)
            print("---", file=stderr)
            print(exc.generated_response, file=stderr)
            print("---", file=stderr, flush=True)
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
        stdout.write(json.dumps(document.model_dump(mode="json"), indent=2))
        stdout.write("\n")
        return 0

    try:
        print(
            "[3/3] Storing validated data in local MongoDB...",
            file=stderr,
            flush=True,
        )
        with create_repository() as repository:
            result = DocumentStoragePipeline(repository).store(args.image, document)
    except (FileHashingError, DatabaseConfigurationError, DatabaseError) as exc:
        print(f"Storage failed: {exc}", file=stderr)
        return 1

    status = "inserted" if result.inserted else "already present"
    print(f"[3/3] MongoDB storage completed ({status}).", file=stderr, flush=True)
    stdout.write(json.dumps(_serialize_insert_result(result), indent=2))
    stdout.write("\n")
    return 0


def _list_stored_documents(
    repository_factory: RepositoryFactory,
    *,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    try:
        with repository_factory() as repository:
            documents = repository.get_all_documents()
    except (DatabaseConfigurationError, DatabaseError) as exc:
        print(f"Database read failed: {exc}", file=stderr)
        return 1
    stdout.write(json.dumps([_serialize_stored(item) for item in documents], indent=2))
    stdout.write("\n")
    return 0


def _get_stored_document(
    document_id: str,
    repository_factory: RepositoryFactory,
    *,
    stdout: TextIO,
    stderr: TextIO,
) -> int:
    try:
        with repository_factory() as repository:
            document = repository.get_document_by_id(document_id)
    except (DatabaseConfigurationError, DatabaseError) as exc:
        print(f"Database read failed: {exc}", file=stderr)
        return 1
    if document is None:
        print("Stored document not found.", file=stderr)
        return 1
    stdout.write(json.dumps(_serialize_stored(document), indent=2))
    stdout.write("\n")
    return 0


def _serialize_insert_result(result: DocumentInsertResult) -> dict[str, object]:
    return {"inserted": result.inserted, **_serialize_stored(result.record)}


def _serialize_stored(record: StoredDocument) -> dict[str, object]:
    return {
        "id": record.id,
        "file_hash": record.file_hash,
        "created_at": record.created_at.isoformat(),
        "document": record.document.model_dump(mode="json"),
    }


if __name__ == "__main__":
    raise SystemExit(run())
