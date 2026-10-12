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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_create_document_vector_index__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_document_vector_index__mutmut)
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


def x_create_document_vector_index__mutmut_orig(
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


def x_create_document_vector_index__mutmut_1(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_2(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=None,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_3(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=None,
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_4(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=None,
    )


def x_create_document_vector_index__mutmut_5(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_6(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_7(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        )


def x_create_document_vector_index__mutmut_8(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(None),
        embedding_generator=OllamaEmbeddingClient(
            base_url=args.ollama_url,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_9(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=OllamaEmbeddingClient(
            base_url=None,
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_10(
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
            model=None,
        ),
    )


def x_create_document_vector_index__mutmut_11(
    dependencies: CliDependencies, args: argparse.Namespace
) -> DocumentVectorIndex:
    """Return an injected index or compose the default entirely local adapter."""
    if dependencies.document_vector_index is not None:
        return dependencies.document_vector_index
    return ChromaDocumentVectorIndex(
        base_url=args.chroma_url,
        collection_name=collection_name_for_embedding_model(args.embedding_model),
        embedding_generator=OllamaEmbeddingClient(
            model=args.embedding_model,
        ),
    )


def x_create_document_vector_index__mutmut_12(
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
            ),
    )

mutants_x_create_document_vector_index__mutmut['_mutmut_orig'] = x_create_document_vector_index__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_1'] = x_create_document_vector_index__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_2'] = x_create_document_vector_index__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_3'] = x_create_document_vector_index__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_4'] = x_create_document_vector_index__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_5'] = x_create_document_vector_index__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_6'] = x_create_document_vector_index__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_7'] = x_create_document_vector_index__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_8'] = x_create_document_vector_index__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_9'] = x_create_document_vector_index__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_10'] = x_create_document_vector_index__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_11'] = x_create_document_vector_index__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_document_vector_index__mutmut['x_create_document_vector_index__mutmut_12'] = x_create_document_vector_index__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut: MutantDict = {}  # type: ignore


@dataclass(slots=True)
class RagWorkflowController:
    """Run local retrieval and render a grounded JSON answer."""

    dependencies: CliDependencies

    @_mutmut_mutated(mutants_xǁRagWorkflowControllerǁask_documents__mutmut)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_orig(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_1(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_2(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_3(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_4(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_5(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is None:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_6(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_7(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] Querying normalized local expiration dates...",
                    file=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_8(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] Querying normalized local expiration dates...",
                    file=self.dependencies.stderr,
                    flush=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_9(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_10(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] Querying normalized local expiration dates...",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_11(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] Querying normalized local expiration dates...",
                    file=self.dependencies.stderr,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_12(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "XX[1/1] Querying normalized local expiration dates...XX",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_13(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] querying normalized local expiration dates...",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_14(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] QUERYING NORMALIZED LOCAL EXPIRATION DATES...",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_15(self, args: argparse.Namespace) -> int:
        """Answer one question from the local Chroma document index."""
        try:
            expiry_year = requested_expiry_year(args.ask_documents)
            structured_field = requested_structured_field(args.ask_documents)
            if expiry_year is not None:
                print(
                    "[1/1] Querying normalized local expiration dates...",
                    file=self.dependencies.stderr,
                    flush=False,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_16(self, args: argparse.Namespace) -> int:
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
                create_repository = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_17(self, args: argparse.Namespace) -> int:
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
                    self.dependencies.repository_factory and MongoDocumentRepository.connect
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_18(self, args: argparse.Namespace) -> int:
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
                    answer = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_19(self, args: argparse.Namespace) -> int:
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
                    answer = ExpirationYearQuestionPipeline(repository).ask(None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_20(self, args: argparse.Namespace) -> int:
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
                    answer = ExpirationYearQuestionPipeline(None).ask(expiry_year)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_21(self, args: argparse.Namespace) -> int:
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
            elif structured_field is None:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_22(self, args: argparse.Namespace) -> int:
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
                    None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_23(self, args: argparse.Namespace) -> int:
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
                    file=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_24(self, args: argparse.Namespace) -> int:
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
                    flush=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_25(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_26(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_27(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_28(self, args: argparse.Namespace) -> int:
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
                    "XX[1/1] Reading validated local document data...XX",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_29(self, args: argparse.Namespace) -> int:
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
                    "[1/1] reading validated local document data...",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_30(self, args: argparse.Namespace) -> int:
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
                    "[1/1] READING VALIDATED LOCAL DOCUMENT DATA...",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_31(self, args: argparse.Namespace) -> int:
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
                    flush=False,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_32(self, args: argparse.Namespace) -> int:
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
                create_repository = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_33(self, args: argparse.Namespace) -> int:
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
                    self.dependencies.repository_factory and MongoDocumentRepository.connect
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_34(self, args: argparse.Namespace) -> int:
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
                    answer = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_35(self, args: argparse.Namespace) -> int:
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
                        None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_36(self, args: argparse.Namespace) -> int:
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
                        None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_37(self, args: argparse.Namespace) -> int:
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
                        limit=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_38(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_39(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_40(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_41(self, args: argparse.Namespace) -> int:
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
                        None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_42(self, args: argparse.Namespace) -> int:
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
                        None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_43(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_44(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_45(self, args: argparse.Namespace) -> int:
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
                        create_document_vector_index(None, args),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_46(self, args: argparse.Namespace) -> int:
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
                        create_document_vector_index(self.dependencies, None),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_47(self, args: argparse.Namespace) -> int:
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
                        create_document_vector_index(args),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_48(self, args: argparse.Namespace) -> int:
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
                        create_document_vector_index(self.dependencies, ),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_49(self, args: argparse.Namespace) -> int:
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
                    None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_50(self, args: argparse.Namespace) -> int:
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
                    file=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_51(self, args: argparse.Namespace) -> int:
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
                    flush=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_52(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_53(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_54(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_55(self, args: argparse.Namespace) -> int:
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
                    "XX[1/1] Searching indexed documents and generating XX"
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_56(self, args: argparse.Namespace) -> int:
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
                    "[1/1] searching indexed documents and generating "
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_57(self, args: argparse.Namespace) -> int:
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
                    "[1/1] SEARCHING INDEXED DOCUMENTS AND GENERATING "
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_58(self, args: argparse.Namespace) -> int:
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
                    "XXa local answer...XX",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_59(self, args: argparse.Namespace) -> int:
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
                    "A LOCAL ANSWER...",
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_60(self, args: argparse.Namespace) -> int:
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
                    flush=False,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_61(self, args: argparse.Namespace) -> int:
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
                answer = None
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_62(self, args: argparse.Namespace) -> int:
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
                ).ask(None, limit=args.rag_results)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_63(self, args: argparse.Namespace) -> int:
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
                ).ask(args.ask_documents, limit=None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_64(self, args: argparse.Namespace) -> int:
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
                ).ask(limit=args.rag_results)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_65(self, args: argparse.Namespace) -> int:
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
                ).ask(args.ask_documents, )
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_66(self, args: argparse.Namespace) -> int:
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
                    vector_index=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_67(self, args: argparse.Namespace) -> int:
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
                    generator=None,
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_68(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_69(self, args: argparse.Namespace) -> int:
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_70(self, args: argparse.Namespace) -> int:
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
                    vector_index=create_document_vector_index(None, args),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_71(self, args: argparse.Namespace) -> int:
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
                    vector_index=create_document_vector_index(self.dependencies, None),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_72(self, args: argparse.Namespace) -> int:
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
                    vector_index=create_document_vector_index(args),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_73(self, args: argparse.Namespace) -> int:
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
                    vector_index=create_document_vector_index(self.dependencies, ),
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_74(self, args: argparse.Namespace) -> int:
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
                        self.dependencies.rag_generator and OllamaClient(base_url=args.ollama_url, model=args.model)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_75(self, args: argparse.Namespace) -> int:
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
                        or OllamaClient(base_url=None, model=args.model)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_76(self, args: argparse.Namespace) -> int:
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
                        or OllamaClient(base_url=args.ollama_url, model=None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_77(self, args: argparse.Namespace) -> int:
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
                        or OllamaClient(model=args.model)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_78(self, args: argparse.Namespace) -> int:
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
                        or OllamaClient(base_url=args.ollama_url, )
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_79(self, args: argparse.Namespace) -> int:
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
            print(None, file=self.dependencies.stderr)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_80(self, args: argparse.Namespace) -> int:
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
            print(f"Document question failed: {exc}", file=None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_81(self, args: argparse.Namespace) -> int:
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
            print(file=self.dependencies.stderr)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_82(self, args: argparse.Namespace) -> int:
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
            print(f"Document question failed: {exc}", )
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_83(self, args: argparse.Namespace) -> int:
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
                self._write_validation_details(None)
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_84(self, args: argparse.Namespace) -> int:
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
            return 2
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

    def xǁRagWorkflowControllerǁask_documents__mutmut_85(self, args: argparse.Namespace) -> int:
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
            print(None, file=self.dependencies.stderr)
            return 1
        JsonResultSerializer.write(
            answer.model_dump(mode="json"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_86(self, args: argparse.Namespace) -> int:
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
            print(f"Document question failed: {exc}", file=None)
            return 1
        JsonResultSerializer.write(
            answer.model_dump(mode="json"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_87(self, args: argparse.Namespace) -> int:
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
            print(file=self.dependencies.stderr)
            return 1
        JsonResultSerializer.write(
            answer.model_dump(mode="json"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_88(self, args: argparse.Namespace) -> int:
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
            print(f"Document question failed: {exc}", )
            return 1
        JsonResultSerializer.write(
            answer.model_dump(mode="json"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_89(self, args: argparse.Namespace) -> int:
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
            return 2
        JsonResultSerializer.write(
            answer.model_dump(mode="json"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_90(self, args: argparse.Namespace) -> int:
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
            None, self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_91(self, args: argparse.Namespace) -> int:
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
            answer.model_dump(mode="json"), None
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_92(self, args: argparse.Namespace) -> int:
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
            self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_93(self, args: argparse.Namespace) -> int:
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
            answer.model_dump(mode="json"), )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_94(self, args: argparse.Namespace) -> int:
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
            answer.model_dump(mode=None), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_95(self, args: argparse.Namespace) -> int:
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
            answer.model_dump(mode="XXjsonXX"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_96(self, args: argparse.Namespace) -> int:
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
            answer.model_dump(mode="JSON"), self.dependencies.stdout
        )
        print("[1/1] Local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_97(self, args: argparse.Namespace) -> int:
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
        print(None, file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_98(self, args: argparse.Namespace) -> int:
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
        print("[1/1] Local document answer completed.", file=None)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_99(self, args: argparse.Namespace) -> int:
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
        print(file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_100(self, args: argparse.Namespace) -> int:
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
        print("[1/1] Local document answer completed.", )
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_101(self, args: argparse.Namespace) -> int:
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
        print("XX[1/1] Local document answer completed.XX", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_102(self, args: argparse.Namespace) -> int:
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
        print("[1/1] local document answer completed.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_103(self, args: argparse.Namespace) -> int:
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
        print("[1/1] LOCAL DOCUMENT ANSWER COMPLETED.", file=self.dependencies.stderr)
        return 0

    def xǁRagWorkflowControllerǁask_documents__mutmut_104(self, args: argparse.Namespace) -> int:
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
        return 1

    @_mutmut_mutated(mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut)
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_orig(self, exc: DocumentParsingError) -> None:
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_1(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(None, start=1):
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_2(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=None):
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_3(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(start=1):
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_4(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, ):
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_5(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=2):
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_6(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    None,
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_7(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    None,
                    diagnostic.reason,
                )
            return
        if exc.generated_response is not None or exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_8(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.response,
                    None,
                )
            return
        if exc.generated_response is not None or exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_9(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
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

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_10(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.reason,
                )
            return
        if exc.generated_response is not None or exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_11(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.response,
                    )
            return
        if exc.generated_response is not None or exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_12(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.response,
                    diagnostic.reason,
                )
            return
        if exc.generated_response is not None and exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_13(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.response,
                    diagnostic.reason,
                )
            return
        if exc.generated_response is None or exc.validation_reason is not None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_14(self, exc: DocumentParsingError) -> None:
        """Render explicitly requested sensitive local-model diagnostics."""
        if exc.validation_diagnostics:
            for attempt, diagnostic in enumerate(exc.validation_diagnostics, start=1):
                self._write_rejected_generation(
                    attempt,
                    diagnostic.response,
                    diagnostic.reason,
                )
            return
        if exc.generated_response is not None or exc.validation_reason is None:
            self._write_rejected_generation(
                1,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_15(self, exc: DocumentParsingError) -> None:
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
                None,
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_16(self, exc: DocumentParsingError) -> None:
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
                None,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_17(self, exc: DocumentParsingError) -> None:
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
                None,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_18(self, exc: DocumentParsingError) -> None:
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
                exc.generated_response,
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_19(self, exc: DocumentParsingError) -> None:
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
                exc.validation_reason,
            )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_20(self, exc: DocumentParsingError) -> None:
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
                )

    def xǁRagWorkflowControllerǁ_write_validation_details__mutmut_21(self, exc: DocumentParsingError) -> None:
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
                2,
                exc.generated_response,
                exc.validation_reason,
            )

    @_mutmut_mutated(mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut)
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

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_orig(
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

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_1(
        self,
        attempt: int,
        response: str | None,
        reason: str | None,
    ) -> None:
        """Render one explicitly requested rejected generation."""
        if response is None:
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

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_2(
        self,
        attempt: int,
        response: str | None,
        reason: str | None,
    ) -> None:
        """Render one explicitly requested rejected generation."""
        if response is not None:
            print(
                None,
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

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_3(
        self,
        attempt: int,
        response: str | None,
        reason: str | None,
    ) -> None:
        """Render one explicitly requested rejected generation."""
        if response is not None:
            print(
                f"--- Rejected local model response (attempt {attempt}) ---",
                file=None,
            )
            print(response, file=self.dependencies.stderr)
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_4(
        self,
        attempt: int,
        response: str | None,
        reason: str | None,
    ) -> None:
        """Render one explicitly requested rejected generation."""
        if response is not None:
            print(
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

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_5(
        self,
        attempt: int,
        response: str | None,
        reason: str | None,
    ) -> None:
        """Render one explicitly requested rejected generation."""
        if response is not None:
            print(
                f"--- Rejected local model response (attempt {attempt}) ---",
                )
            print(response, file=self.dependencies.stderr)
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_6(
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
            print(None, file=self.dependencies.stderr)
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_7(
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
            print(response, file=None)
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_8(
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
            print(file=self.dependencies.stderr)
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_9(
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
            print(response, )
            print(
                "--- End rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_10(
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
                None,
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_11(
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
                file=None,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_12(
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
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_13(
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
                )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_14(
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
                "XX--- End rejected local model response ---XX",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_15(
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
                "--- end rejected local model response ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_16(
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
                "--- END REJECTED LOCAL MODEL RESPONSE ---",
                file=self.dependencies.stderr,
            )
        if reason is not None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_17(
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
        if reason is None:
            print("Validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_18(
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
            print(None, file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_19(
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
            print("Validation reason:", file=None)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_20(
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
            print(file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_21(
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
            print("Validation reason:", )
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_22(
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
            print("XXValidation reason:XX", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_23(
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
            print("validation reason:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_24(
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
            print("VALIDATION REASON:", file=self.dependencies.stderr)
            print(reason, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_25(
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
            print(None, file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_26(
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
            print(reason, file=None)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_27(
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
            print(file=self.dependencies.stderr)

    def xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_28(
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
            print(reason, )

mutants_xǁRagWorkflowControllerǁask_documents__mutmut['_mutmut_orig'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_1'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_2'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_3'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_4'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_5'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_6'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_7'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_8'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_9'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_10'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_11'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_12'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_13'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_14'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_15'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_16'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_17'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_18'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_19'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_20'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_21'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_22'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_23'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_24'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_25'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_26'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_27'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_28'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_29'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_30'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_31'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_32'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_33'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_34'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_35'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_36'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_37'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_38'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_39'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_40'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_41'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_42'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_43'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_44'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_45'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_46'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_47'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_48'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_49'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_50'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_51'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_52'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_53'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_53 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_54'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_54 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_55'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_55 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_56'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_56 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_57'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_57 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_58'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_58 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_59'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_59 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_60'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_60 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_61'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_61 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_62'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_62 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_63'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_63 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_64'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_64 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_65'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_65 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_66'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_66 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_67'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_67 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_68'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_68 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_69'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_69 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_70'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_70 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_71'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_71 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_72'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_72 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_73'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_73 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_74'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_74 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_75'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_75 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_76'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_76 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_77'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_77 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_78'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_78 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_79'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_79 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_80'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_80 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_81'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_81 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_82'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_82 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_83'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_83 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_84'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_84 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_85'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_85 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_86'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_86 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_87'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_87 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_88'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_88 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_89'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_89 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_90'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_90 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_91'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_91 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_92'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_92 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_93'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_93 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_94'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_94 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_95'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_95 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_96'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_96 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_97'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_97 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_98'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_98 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_99'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_99 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_100'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_100 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_101'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_101 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_102'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_102 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_103'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_103 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁask_documents__mutmut['xǁRagWorkflowControllerǁask_documents__mutmut_104'] = RagWorkflowController.xǁRagWorkflowControllerǁask_documents__mutmut_104 # type: ignore # mutmut generated

mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['_mutmut_orig'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_1'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_2'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_3'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_4'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_5'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_6'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_7'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_8'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_9'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_10'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_11'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_12'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_13'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_14'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_15'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_16'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_17'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_18'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_19'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_20'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_validation_details__mutmut['xǁRagWorkflowControllerǁ_write_validation_details__mutmut_21'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_validation_details__mutmut_21 # type: ignore # mutmut generated

mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['_mutmut_orig'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_1'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_2'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_3'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_4'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_5'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_6'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_7'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_8'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_9'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_10'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_11'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_12'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_13'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_14'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_15'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_16'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_17'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_18'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_19'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_20'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_21'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_22'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_23'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_24'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_25'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_26'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_27'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut['xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_28'] = RagWorkflowController.xǁRagWorkflowControllerǁ_write_rejected_generation__mutmut_28 # type: ignore # mutmut generated
