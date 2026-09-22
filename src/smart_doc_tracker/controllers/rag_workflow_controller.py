"""CLI presentation and dependency composition for local document RAG."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..core.parser import DocumentParsingError
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)
from ..db.vector_database import (
    ChromaDocumentVectorIndex,
    VectorDatabaseError,
    collection_name_for_embedding_model,
)
from ..infrastructure.ollama import (
    OllamaClient,
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaEmbeddingClient,
    OllamaResponseError,
)
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..pipeline import (
    DocumentQuestionPipeline,
    ExpirationYearQuestionPipeline,
    StructuredFieldQuestionPipeline,
    requested_expiry_year,
    requested_structured_field,
)


def create_document_vector_index(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


@dataclass(slots=True)
class RagWorkflowController:
    """Run local retrieval and render a grounded JSON answer."""

    dependencies: CliDependencies

    def ask_documents(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] Querying normalized local expiration dates...",
                    file=self.dependencies.stderr,
                    flush=True,
                )
                create_repository = (
                    self.dependencies.repository_factory
                    or MongoDocumentRepository.connect
                )
                with create_repository() as repository:
                    answer = ExpirationYearQuestionPipeline(repository).ask(expiry_year)
            elif structured_field is not None:
                print(
                    "[1/1] Reading validated local document data...",
                    file=self.dependencies.stderr,
                    flush=True,
                )
                create_repository = (
                    self.dependencies.repository_factory
                    or MongoDocumentRepository.connect
                )
                with create_repository() as repository:
                    answer = StructuredFieldQuestionPipeline(
                        repository,
                        create_document_vector_index(self.dependencies, args),
                    ).ask(
                        args.ask_documents,
                        structured_field,
                        limit=args.rag_results,
                    )
            else:
                print(
                    "[1/1] Searching indexed documents and generating "
                    "a local answer...",
                    file=self.dependencies.stderr,
                    flush=True,
                )
                answer = DocumentQuestionPipeline(
                    vector_index=create_document_vector_index(self.dependencies, args),
                    generator=(
                        self.dependencies.rag_generator
                        or OllamaClient(base_url=args.ollama_url, model=args.model)
                    ),
                ).ask(args.ask_documents, limit=args.rag_results)
        except DocumentParsingError as exc:
            print(f"Document question failed: {exc}", file=self.dependencies.stderr)
            if args.show_rag_validation_details:
                self._write_validation_details(exc)
            return 1
        except (
            DatabaseConfigurationError,
            DatabaseError,
            VectorDatabaseError,
            OllamaConfigurationError,
            OllamaConnectionError,
            OllamaResponseError,
        ) as exc:
            print(f"Document question failed: {exc}", file=self.dependencies.stderr)
            return 1
        JsonResultSerializer.write(
            answer.model_dump(mode="json"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def _write_validation_details(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.response,
                    diagnostic.reason,
                )
            return
        if exc.generated_response is not None or exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def _write_rejected_generation(
        self,
        attempt: int,
        response: str | None,
        reason: str | None,
    ) -> None:
        """Render one explicitly requested rejected generation."""
        if response is not None:
            print(
                f"--- Rejected local model response (attempt {attempt}) ---",
                file=self.dependencies.stderr,
            )
            print(response, file=self.dependencies.stderr)
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)
