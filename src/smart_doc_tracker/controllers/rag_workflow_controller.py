"""CLI presentation and dependency composition for local document RAG."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..core.parser import DocumentParsingError
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
from ..pipeline import DocumentQuestionPipeline


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
            print(
                "[1/1] Searching indexed documents and generating a local answer...",
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
        except (
            VectorDatabaseError,
            DocumentParsingError,
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
