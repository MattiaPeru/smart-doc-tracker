"""Local Chroma persistence for sensitive document search content."""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from hashlib import sha256
from importlib import import_module
from typing import Any
from urllib.parse import urlparse

from ..interfaces.embedding_generator import EmbeddingGenerator
from ..models.document import DocumentData
from ..models.rag import IndexedDocumentFragment, RetrievedDocumentChunk

_COLLECTION_PREFIX = "smart_doc_tracker_documents"
_PAGE_HEADER = re.compile(r"(?m)^\[Page (?P<page>[1-9]\d*)\]\r?\n")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class VectorDatabaseError(RuntimeError):
    """Raised when the local vector index cannot complete an operation."""


class VectorDatabaseDependencyError(VectorDatabaseError):
    """Raised when Chroma is not installed in the local environment."""


class VectorDatabaseConfigurationError(VectorDatabaseError, ValueError):
    """Raised when the Chroma endpoint is not explicitly local and safe."""


ChromaClientFactory = Callable[[str, int], Any]
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut: MutantDict = {}  # type: ignore
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut: MutantDict = {}  # type: ignore


class ChromaDocumentVectorIndex:
    """Persist document fragments through a loopback-only Chroma server."""

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut)
    def __init__(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_orig(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_1(
        self,
        *,
        base_url: str = "XXhttp://127.0.0.1:8000XX",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_2(
        self,
        *,
        base_url: str = "HTTP://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_3(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2001,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_4(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 201,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_5(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters < 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_6(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 1:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_7(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError(None)
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_8(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("XXchunk_characters must be positiveXX")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_9(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("CHUNK_CHARACTERS MUST BE POSITIVE")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_10(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 and chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_11(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap <= 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_12(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 1 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_13(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap > chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_14(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError(None)
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_15(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("XXchunk_overlap must be smaller than chunk_charactersXX")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_16(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("CHUNK_OVERLAP MUST BE SMALLER THAN CHUNK_CHARACTERS")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_17(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_18(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError(None)
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_19(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("XXcollection_name cannot be emptyXX")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_20(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("COLLECTION_NAME CANNOT BE EMPTY")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_21(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = None
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_22(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(None)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_23(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = None
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_24(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory and _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_25(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = None
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_26(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(None, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_27(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, None)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_28(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_29(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, )
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_30(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = None
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_31(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=None,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_32(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata=None,
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_33(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_34(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_35(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_36(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"XXhnsw:spaceXX": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_37(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"HNSW:SPACE": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_38(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "XXcosineXX"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_39(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "COSINE"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_40(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_41(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe local vector database could not be opened.XX"
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_42(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "the local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_43(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE COULD NOT BE OPENED."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_44(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = None
        self._chunk_characters = chunk_characters
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_45(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = None
        self._chunk_overlap = chunk_overlap

    def xǁChromaDocumentVectorIndexǁ__init____mutmut_46(
        self,
        *,
        base_url: str = "http://127.0.0.1:8000",
        embedding_generator: EmbeddingGenerator,
        collection_name: str = _COLLECTION_PREFIX,
        client_factory: ChromaClientFactory | None = None,
        chunk_characters: int = 2_000,
        chunk_overlap: int = 200,
    ) -> None:
        """Configure a local server index with explicitly generated embeddings."""
        if chunk_characters <= 0:
            raise ValueError("chunk_characters must be positive")
        if chunk_overlap < 0 or chunk_overlap >= chunk_characters:
            raise ValueError("chunk_overlap must be smaller than chunk_characters")
        if not collection_name.strip():
            raise ValueError("collection_name cannot be empty")
        host, port = _validate_loopback_url(base_url)
        factory = client_factory or _http_client
        try:
            client = factory(host, port)
            self._collection = client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be opened."
            ) from exc
        self._embedding_generator = embedding_generator
        self._chunk_characters = chunk_characters
        self._chunk_overlap = None

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut)
    def upsert_document(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_orig(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_1(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_2(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError(None)
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_3(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("XXdocument_id cannot be emptyXX")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_4(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("DOCUMENT_ID CANNOT BE EMPTY")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_5(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = None
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_6(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(None, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_7(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, None)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_8(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_9(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, )
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_10(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = None
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_11(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            None
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_12(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) == len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_13(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                None
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_14(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "XXThe local embedding model returned an unexpected result count.XX"
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_15(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "the local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_16(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "THE LOCAL EMBEDDING MODEL RETURNED AN UNEXPECTED RESULT COUNT."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_17(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = None
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_18(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = None
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_19(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = None
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_20(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(None, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_21(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, None, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_22(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, None)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_23(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_24(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_25(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, )
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_26(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = None
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_27(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where=None, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_28(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=None
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_29(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_30(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_31(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"XXdocument_idXX": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_32(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"DOCUMENT_ID": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_33(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = None
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_34(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(None)
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_35(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["XXidsXX"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_36(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["IDS"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_37(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=None,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_38(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=None,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_39(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=None,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_40(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=None,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_41(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_42(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_43(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_44(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_45(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = None
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_46(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(None)
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_47(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(None))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_48(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=None)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_49(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_50(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe document could not be indexed locally.XX"
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_51(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "the document could not be indexed locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupsert_document__mutmut_52(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        """Replace all raw, summary, and structured fragments for one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(raw_text, document)
        embeddings = self._embedding_generator.embed(
            [content for _, content, _, _ in fragments]
        )
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        ids = [f"{document_id}:{suffix}" for suffix, _, _, _ in fragments]
        documents = [content for _, content, _, _ in fragments]
        metadatas = [
            _fragment_metadata(document_id, source, page)
            for _, _, source, page in fragments
        ]
        try:
            existing = self._collection.get(
                where={"document_id": document_id}, include=[]
            )
            existing_ids = set(existing["ids"])
            self._collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas,
            )
            stale_ids = sorted(existing_ids.difference(ids))
            if stale_ids:
                self._collection.delete(ids=stale_ids)
        except Exception as exc:
            raise VectorDatabaseError(
                "THE DOCUMENT COULD NOT BE INDEXED LOCALLY."
            ) from exc

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut)
    def snapshot_document(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_orig(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_1(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_2(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError(None)
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_3(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("XXdocument_id cannot be emptyXX")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_4(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("DOCUMENT_ID CANNOT BE EMPTY")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_5(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = None
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_6(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where=None,
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_7(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=None,
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_8(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_9(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_10(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"XXdocument_idXX": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_11(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"DOCUMENT_ID": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_12(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["XXdocumentsXX", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_13(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["DOCUMENTS", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_14(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "XXmetadatasXX", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_15(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "METADATAS", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_16(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "XXembeddingsXX"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_17(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "EMBEDDINGS"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_18(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "XXdocument_idXX": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_19(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "DOCUMENT_ID": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_20(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "XXidsXX": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_21(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "IDS": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_22(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(None),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_23(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get(None)),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_24(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("XXidsXX")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_25(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("IDS")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_26(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "XXdocumentsXX": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_27(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "DOCUMENTS": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_28(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(None),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_29(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get(None)),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_30(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("XXdocumentsXX")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_31(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("DOCUMENTS")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_32(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "XXmetadatasXX": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_33(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "METADATAS": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_34(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(None),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_35(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get(None)),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_36(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("XXmetadatasXX")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_37(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("METADATAS")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_38(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "XXembeddingsXX": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_39(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "EMBEDDINGS": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_40(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(None),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_41(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get(None)),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_42(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("XXembeddingsXX")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_43(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("EMBEDDINGS")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_44(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_45(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe document index snapshot could not be created.XX"
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_46(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "the document index snapshot could not be created."
            ) from exc

    def xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_47(self, document_id: str) -> dict[str, Any]:
        """Capture all fragments needed for compensating local index operations."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas", "embeddings"],
            )
            return {
                "document_id": document_id,
                "ids": _optional_list(result.get("ids")),
                "documents": _optional_list(result.get("documents")),
                "metadatas": _optional_list(result.get("metadatas")),
                "embeddings": _optional_list(result.get("embeddings")),
            }
        except Exception as exc:
            raise VectorDatabaseError(
                "THE DOCUMENT INDEX SNAPSHOT COULD NOT BE CREATED."
            ) from exc

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut)
    def restore_document(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_orig(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_1(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = None
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_2(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get(None)
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_3(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("XXidsXX")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_4(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("IDS")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_5(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = None
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_6(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get(None)
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_7(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("XXdocument_idXX")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_8(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("DOCUMENT_ID")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_9(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) and not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_10(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_11(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_12(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError(None)
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_13(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("XXThe document index snapshot is invalid.XX")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_14(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("the document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_15(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("THE DOCUMENT INDEX SNAPSHOT IS INVALID.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_16(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where=None)
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_17(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"XXdocument_idXX": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_18(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"DOCUMENT_ID": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_19(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_20(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=None,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_21(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=None,
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_22(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=None,
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_23(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=None,
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_24(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_25(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_26(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_27(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_28(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["XXdocumentsXX"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_29(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["DOCUMENTS"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_30(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["XXmetadatasXX"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_31(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["METADATAS"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_32(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["XXembeddingsXX"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_33(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["EMBEDDINGS"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_34(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError(None) from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_35(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("XXThe document index snapshot is invalid.XX") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_36(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("the document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_37(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("THE DOCUMENT INDEX SNAPSHOT IS INVALID.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_38(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_39(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe document index snapshot could not be restored.XX"
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_40(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "the document index snapshot could not be restored."
            ) from exc

    def xǁChromaDocumentVectorIndexǁrestore_document__mutmut_41(self, snapshot: dict[str, Any]) -> None:
        """Restore an index snapshot after a coordinated operation fails."""
        ids = snapshot.get("ids")
        document_id = snapshot.get("document_id")
        if not isinstance(ids, list) or not isinstance(document_id, str):
            raise ValueError("The document index snapshot is invalid.")
        try:
            self._collection.delete(where={"document_id": document_id})
            if not ids:
                return
            self._collection.upsert(
                ids=ids,
                documents=snapshot["documents"],
                metadatas=snapshot["metadatas"],
                embeddings=snapshot["embeddings"],
            )
        except (KeyError, TypeError) as exc:
            raise ValueError("The document index snapshot is invalid.") from exc
        except Exception as exc:
            raise VectorDatabaseError(
                "THE DOCUMENT INDEX SNAPSHOT COULD NOT BE RESTORED."
            ) from exc

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut)
    def update_document_data(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_orig(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_1(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_2(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError(None)
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_3(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("XXdocument_id cannot be emptyXX")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_4(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("DOCUMENT_ID CANNOT BE EMPTY")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_5(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = None
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_6(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(None, document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_7(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", None)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_8(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments(document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_9(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", )[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_10(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("XXXX", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_11(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:3]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_12(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = None
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_13(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = None
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_14(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(None)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_15(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) == len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_16(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                None
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_17(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "XXThe local embedding model returned an unexpected result count.XX"
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_18(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "the local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_19(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "THE LOCAL EMBEDDING MODEL RETURNED AN UNEXPECTED RESULT COUNT."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_20(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=None,
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_21(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=None,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_22(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=None,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_23(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=None,
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_24(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_25(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_26(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_27(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_28(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(None, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_29(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, None, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_30(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, None)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_31(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_32(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_33(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, )
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_34(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_35(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe document index could not be updated locally.XX"
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_36(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "the document index could not be updated locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_37(self, document_id: str, document: DocumentData) -> None:
        """Replace summary and structured fragments without touching raw OCR text."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        fragments = self._fragments("", document)[:2]
        contents = [content for _, content, _source, _page in fragments]
        embeddings = self._embedding_generator.embed(contents)
        if len(embeddings) != len(fragments):
            raise VectorDatabaseError(
                "The local embedding model returned an unexpected result count."
            )
        try:
            self._collection.upsert(
                ids=[f"{document_id}:{suffix}" for suffix, _, _, _ in fragments],
                embeddings=embeddings,
                documents=contents,
                metadatas=[
                    _fragment_metadata(document_id, source, page)
                    for _, _, source, page in fragments
                ],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "THE DOCUMENT INDEX COULD NOT BE UPDATED LOCALLY."
            ) from exc

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut)
    def delete_document(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_orig(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_1(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_2(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError(None)
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_3(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("XXdocument_id cannot be emptyXX")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_4(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("DOCUMENT_ID CANNOT BE EMPTY")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_5(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where=None)
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_6(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"XXdocument_idXX": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_7(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"DOCUMENT_ID": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "The document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_8(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_9(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe document index could not be deleted locally.XX"
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_10(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "the document index could not be deleted locally."
            ) from exc

    def xǁChromaDocumentVectorIndexǁdelete_document__mutmut_11(self, document_id: str) -> None:
        """Delete all fragments belonging to one document."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            self._collection.delete(where={"document_id": document_id})
        except Exception as exc:
            raise VectorDatabaseError(
                "THE DOCUMENT INDEX COULD NOT BE DELETED LOCALLY."
            ) from exc

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁquery__mutmut)
    def query(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_orig(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_1(self, question: str, *, limit: int = 6) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_2(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = None
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_3(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_4(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError(None)
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_5(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("XXquestion cannot be emptyXX")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_6(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("QUESTION CANNOT BE EMPTY")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_7(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit < 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_8(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 1:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_9(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError(None)
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_10(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("XXlimit must be positiveXX")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_11(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("LIMIT MUST BE POSITIVE")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_12(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = None
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_13(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(None)
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_14(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count != 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_15(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 1:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_16(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = None
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_17(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed(None)
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_18(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) == 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_19(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 2:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_20(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    None
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_21(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "XXThe local embedding model returned an unexpected result count.XX"
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_22(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "the local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_23(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "THE LOCAL EMBEDDING MODEL RETURNED AN UNEXPECTED RESULT COUNT."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_24(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = None
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_25(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=None,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_26(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=None,
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_27(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=None,
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_28(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_29(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_30(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_31(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(None, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_32(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, None),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_33(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_34(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, ),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_35(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["XXdocumentsXX", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_36(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["DOCUMENTS", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_37(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "XXmetadatasXX", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_38(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "METADATAS", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_39(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "XXdistancesXX"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_40(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "DISTANCES"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_41(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_42(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe local vector database could not be queried.XX"
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_43(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "the local vector database could not be queried."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_44(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE COULD NOT BE QUERIED."
            ) from exc
        return _decode_query_result(result)

    def xǁChromaDocumentVectorIndexǁquery__mutmut_45(self, question: str, *, limit: int = 5) -> list[RetrievedDocumentChunk]:
        """Retrieve nearest document fragments using a locally embedded question."""
        candidate = question.strip()
        if not candidate:
            raise ValueError("question cannot be empty")
        if limit <= 0:
            raise ValueError("limit must be positive")
        try:
            count = int(self._collection.count())
            if count == 0:
                return []
            query_embedding = self._embedding_generator.embed([candidate])
            if len(query_embedding) != 1:
                raise VectorDatabaseError(
                    "The local embedding model returned an unexpected result count."
                )
            result = self._collection.query(
                query_embeddings=query_embedding,
                n_results=min(limit, count),
                include=["documents", "metadatas", "distances"],
            )
        except VectorDatabaseError:
            raise
        except Exception as exc:
            raise VectorDatabaseError(
                "The local vector database could not be queried."
            ) from exc
        return _decode_query_result(None)

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut)
    def get_document_fragments(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_orig(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_1(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_2(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError(None)
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_3(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("XXdocument_id cannot be emptyXX")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_4(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("DOCUMENT_ID CANNOT BE EMPTY")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_5(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = None
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_6(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where=None,
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_7(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=None,
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_8(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_9(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_10(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"XXdocument_idXX": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_11(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"DOCUMENT_ID": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_12(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["XXdocumentsXX", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_13(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["DOCUMENTS", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_14(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "XXmetadatasXX"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_15(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "METADATAS"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_16(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                None
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_17(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "XXThe indexed document content could not be read locally.XX"
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_18(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "the indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_19(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "THE INDEXED DOCUMENT CONTENT COULD NOT BE READ LOCALLY."
            ) from exc
        return _decode_document_fragments(result)

    def xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_20(self, document_id: str) -> list[IndexedDocumentFragment]:
        """Return all persisted content for one document without embeddings."""
        if not document_id.strip():
            raise ValueError("document_id cannot be empty")
        try:
            result = self._collection.get(
                where={"document_id": document_id},
                include=["documents", "metadatas"],
            )
        except Exception as exc:
            raise VectorDatabaseError(
                "The indexed document content could not be read locally."
            ) from exc
        return _decode_document_fragments(None)

    @_mutmut_mutated(mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut)
    def _fragments(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_orig(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_1(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = None
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_2(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("XXsummaryXX", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_3(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("SUMMARY", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_4(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "XXsummaryXX", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_5(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "SUMMARY", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_6(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "XXstructuredXX",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_7(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "STRUCTURED",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_8(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    None,
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_9(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=None,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_10(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=None,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_11(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_12(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_13(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_14(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode=None),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_15(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="XXjsonXX"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_16(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="JSON"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_17(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=False,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_18(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=False,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_19(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "XXstructured_dataXX",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_20(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "STRUCTURED_DATA",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_21(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = None
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_22(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            None,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_23(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            None,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_24(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            None,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_25(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_26(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_27(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_28(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(None, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_29(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=None):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_30(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(start=1):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_31(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, ):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_32(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=2):
            fragments.append((f"raw:{index:04d}", chunk, "raw_text", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_33(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append(None)
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_34(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "XXraw_textXX", page))
        return fragments

    def xǁChromaDocumentVectorIndexǁ_fragments__mutmut_35(
        self, raw_text: str, document: DocumentData
    ) -> list[tuple[str, str, str, int | None]]:
        """Build deterministic fragments for every requested content category."""
        fragments: list[tuple[str, str, str, int | None]] = [
            ("summary", document.summary, "summary", None),
            (
                "structured",
                json.dumps(
                    document.model_dump(mode="json"),
                    ensure_ascii=True,
                    sort_keys=True,
                ),
                "structured_data",
                None,
            ),
        ]
        raw_chunks = _page_aware_chunks(
            raw_text,
            self._chunk_characters,
            self._chunk_overlap,
        )
        for index, (chunk, page) in enumerate(raw_chunks, start=1):
            fragments.append((f"raw:{index:04d}", chunk, "RAW_TEXT", page))
        return fragments

mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_35 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_36'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_36 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_37'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_37 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_38'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_38 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_39'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_39 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_40'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_40 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_41'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_41 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_42'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_42 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_43'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_43 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_44'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_44 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_45'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_45 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ__init____mutmut['xǁChromaDocumentVectorIndexǁ__init____mutmut_46'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ__init____mutmut_46 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_35 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_36'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_36 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_37'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_37 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_38'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_38 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_39'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_39 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_40'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_40 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_41'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_41 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_42'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_42 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_43'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_43 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_44'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_44 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_45'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_45 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_46'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_46 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_47'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_47 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_48'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_48 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_49'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_49 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_50'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_50 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_51'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_51 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupsert_document__mutmut['xǁChromaDocumentVectorIndexǁupsert_document__mutmut_52'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupsert_document__mutmut_52 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_35 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_36'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_36 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_37'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_37 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_38'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_38 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_39'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_39 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_40'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_40 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_41'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_41 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_42'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_42 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_43'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_43 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_44'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_44 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_45'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_45 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_46'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_46 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut['xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_47'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁsnapshot_document__mutmut_47 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_35 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_36'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_36 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_37'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_37 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_38'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_38 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_39'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_39 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_40'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_40 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁrestore_document__mutmut['xǁChromaDocumentVectorIndexǁrestore_document__mutmut_41'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁrestore_document__mutmut_41 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_36'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_36 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut['xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_37'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁupdate_document_data__mutmut_37 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁdelete_document__mutmut['xǁChromaDocumentVectorIndexǁdelete_document__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁdelete_document__mutmut_11 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_35 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_36'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_36 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_37'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_37 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_38'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_38 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_39'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_39 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_40'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_40 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_41'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_41 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_42'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_42 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_43'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_43 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_44'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_44 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁquery__mutmut['xǁChromaDocumentVectorIndexǁquery__mutmut_45'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁquery__mutmut_45 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut['xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁget_document_fragments__mutmut_20 # type: ignore # mutmut generated

mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['_mutmut_orig'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_orig # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_1'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_1 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_2'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_2 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_3'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_3 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_4'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_4 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_5'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_5 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_6'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_6 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_7'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_7 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_8'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_8 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_9'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_9 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_10'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_10 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_11'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_11 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_12'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_12 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_13'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_13 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_14'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_14 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_15'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_15 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_16'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_16 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_17'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_17 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_18'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_18 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_19'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_19 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_20'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_20 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_21'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_21 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_22'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_22 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_23'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_23 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_24'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_24 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_25'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_25 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_26'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_26 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_27'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_27 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_28'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_28 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_29'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_29 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_30'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_30 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_31'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_31 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_32'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_32 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_33'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_33 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_34'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_34 # type: ignore # mutmut generated
mutants_xǁChromaDocumentVectorIndexǁ_fragments__mutmut['xǁChromaDocumentVectorIndexǁ_fragments__mutmut_35'] = ChromaDocumentVectorIndex.xǁChromaDocumentVectorIndexǁ_fragments__mutmut_35 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__fragment_metadata__mutmut)
def _fragment_metadata(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "source": source,
    }
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_orig(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "source": source,
    }
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_1(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = None
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_2(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "XXdocument_idXX": document_id,
        "source": source,
    }
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_3(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "DOCUMENT_ID": document_id,
        "source": source,
    }
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_4(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "XXsourceXX": source,
    }
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_5(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "SOURCE": source,
    }
    if page is not None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_6(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "source": source,
    }
    if page is None:
        metadata["page"] = page
    return metadata


def x__fragment_metadata__mutmut_7(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "source": source,
    }
    if page is not None:
        metadata["page"] = None
    return metadata


def x__fragment_metadata__mutmut_8(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "source": source,
    }
    if page is not None:
        metadata["XXpageXX"] = page
    return metadata


def x__fragment_metadata__mutmut_9(
    document_id: str,
    source: str,
    page: int | None,
) -> dict[str, str | int]:
    """Build Chroma metadata without claiming an unknown page number."""
    metadata: dict[str, str | int] = {
        "document_id": document_id,
        "source": source,
    }
    if page is not None:
        metadata["PAGE"] = page
    return metadata

mutants_x__fragment_metadata__mutmut['_mutmut_orig'] = x__fragment_metadata__mutmut_orig # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_1'] = x__fragment_metadata__mutmut_1 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_2'] = x__fragment_metadata__mutmut_2 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_3'] = x__fragment_metadata__mutmut_3 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_4'] = x__fragment_metadata__mutmut_4 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_5'] = x__fragment_metadata__mutmut_5 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_6'] = x__fragment_metadata__mutmut_6 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_7'] = x__fragment_metadata__mutmut_7 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_8'] = x__fragment_metadata__mutmut_8 # type: ignore # mutmut generated
mutants_x__fragment_metadata__mutmut['x__fragment_metadata__mutmut_9'] = x__fragment_metadata__mutmut_9 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_collection_name_for_embedding_model__mutmut)
def collection_name_for_embedding_model(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_orig(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_1(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = None
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_2(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_3(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError(None)
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_4(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("XXmodel cannot be emptyXX")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_5(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("MODEL CANNOT BE EMPTY")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_6(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = None
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_7(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(None).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_8(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode(None)).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_9(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("XXutf-8XX")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_10(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("UTF-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


def x_collection_name_for_embedding_model__mutmut_11(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:13]
    return f"{_COLLECTION_PREFIX}_{digest}"

mutants_x_collection_name_for_embedding_model__mutmut['_mutmut_orig'] = x_collection_name_for_embedding_model__mutmut_orig # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_1'] = x_collection_name_for_embedding_model__mutmut_1 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_2'] = x_collection_name_for_embedding_model__mutmut_2 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_3'] = x_collection_name_for_embedding_model__mutmut_3 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_4'] = x_collection_name_for_embedding_model__mutmut_4 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_5'] = x_collection_name_for_embedding_model__mutmut_5 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_6'] = x_collection_name_for_embedding_model__mutmut_6 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_7'] = x_collection_name_for_embedding_model__mutmut_7 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_8'] = x_collection_name_for_embedding_model__mutmut_8 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_9'] = x_collection_name_for_embedding_model__mutmut_9 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_10'] = x_collection_name_for_embedding_model__mutmut_10 # type: ignore # mutmut generated
mutants_x_collection_name_for_embedding_model__mutmut['x_collection_name_for_embedding_model__mutmut_11'] = x_collection_name_for_embedding_model__mutmut_11 # type: ignore # mutmut generated
mutants_x__http_client__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__http_client__mutmut)
def _http_client(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_orig(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_1(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = None
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_2(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module(None)
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_3(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("XXchromadbXX")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_4(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("CHROMADB")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_5(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = None
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_6(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module(None)
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_7(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("XXchromadb.configXX")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_8(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("CHROMADB.CONFIG")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_9(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            None
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_10(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "XXChromaDB is required for local document search.XX"
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_11(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "chromadb is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_12(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "CHROMADB IS REQUIRED FOR LOCAL DOCUMENT SEARCH."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_13(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=None,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_14(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=None,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_15(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=None,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_16(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=None,
    )


def x__http_client__mutmut_17(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_18(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_19(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_20(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        )


def x__http_client__mutmut_21(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=True,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_22(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=None,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_23(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=None,
        ),
    )


def x__http_client__mutmut_24(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_25(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            ),
    )


def x__http_client__mutmut_26(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=True,
            allow_reset=False,
        ),
    )


def x__http_client__mutmut_27(host: str, port: int) -> Any:
    """Create the Chroma HTTP client lazily for unrelated local workflows."""
    try:
        chromadb = import_module("chromadb")
        settings_module = import_module("chromadb.config")
    except ImportError as exc:
        raise VectorDatabaseDependencyError(
            "ChromaDB is required for local document search."
        ) from exc
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=False,
        settings=settings_module.Settings(
            anonymized_telemetry=False,
            allow_reset=True,
        ),
    )

mutants_x__http_client__mutmut['_mutmut_orig'] = x__http_client__mutmut_orig # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_1'] = x__http_client__mutmut_1 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_2'] = x__http_client__mutmut_2 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_3'] = x__http_client__mutmut_3 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_4'] = x__http_client__mutmut_4 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_5'] = x__http_client__mutmut_5 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_6'] = x__http_client__mutmut_6 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_7'] = x__http_client__mutmut_7 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_8'] = x__http_client__mutmut_8 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_9'] = x__http_client__mutmut_9 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_10'] = x__http_client__mutmut_10 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_11'] = x__http_client__mutmut_11 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_12'] = x__http_client__mutmut_12 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_13'] = x__http_client__mutmut_13 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_14'] = x__http_client__mutmut_14 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_15'] = x__http_client__mutmut_15 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_16'] = x__http_client__mutmut_16 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_17'] = x__http_client__mutmut_17 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_18'] = x__http_client__mutmut_18 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_19'] = x__http_client__mutmut_19 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_20'] = x__http_client__mutmut_20 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_21'] = x__http_client__mutmut_21 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_22'] = x__http_client__mutmut_22 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_23'] = x__http_client__mutmut_23 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_24'] = x__http_client__mutmut_24 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_25'] = x__http_client__mutmut_25 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_26'] = x__http_client__mutmut_26 # type: ignore # mutmut generated
mutants_x__http_client__mutmut['x__http_client__mutmut_27'] = x__http_client__mutmut_27 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_loopback_url__mutmut)
def _validate_loopback_url(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_orig(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_1(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = None
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_2(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(None)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_3(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query and parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_4(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"} and parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_5(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None and parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_6(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None and parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_7(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"} and parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_8(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http" and parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_9(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme == "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_10(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "XXhttpXX"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_11(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "HTTP"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_12(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_13(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"XX127.0.0.1XX", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_14(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "XXlocalhostXX", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_15(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "LOCALHOST", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_16(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "XX::1XX"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_17(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_18(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_19(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_20(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"XXXX", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_21(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "XX/XX"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_22(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            None
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_23(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "XXChromaDB must use a plain HTTP loopback endpoint without credentials XX"
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_24(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "chromadb must use a plain http loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_25(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "CHROMADB MUST USE A PLAIN HTTP LOOPBACK ENDPOINT WITHOUT CREDENTIALS "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_26(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "XXor a path.XX"
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_27(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "OR A PATH."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_28(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = None
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_29(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            None
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_30(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "XXThe ChromaDB endpoint has an invalid port.XX"
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_31(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "the chromadb endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_32(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "THE CHROMADB ENDPOINT HAS AN INVALID PORT."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_33(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is not None:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_34(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            None
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_35(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "XXThe ChromaDB endpoint must include an explicit port.XX"
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_36(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "the chromadb endpoint must include an explicit port."
        )
    return parsed.hostname, port


def x__validate_loopback_url__mutmut_37(base_url: str) -> tuple[str, int]:
    """Validate a plain HTTP Chroma URL with an explicit loopback host and port."""
    parsed = urlparse(base_url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise VectorDatabaseConfigurationError(
            "ChromaDB must use a plain HTTP loopback endpoint without credentials "
            "or a path."
        )
    try:
        port = parsed.port
    except ValueError as exc:
        raise VectorDatabaseConfigurationError(
            "The ChromaDB endpoint has an invalid port."
        ) from exc
    if port is None:
        raise VectorDatabaseConfigurationError(
            "THE CHROMADB ENDPOINT MUST INCLUDE AN EXPLICIT PORT."
        )
    return parsed.hostname, port

mutants_x__validate_loopback_url__mutmut['_mutmut_orig'] = x__validate_loopback_url__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_1'] = x__validate_loopback_url__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_2'] = x__validate_loopback_url__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_3'] = x__validate_loopback_url__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_4'] = x__validate_loopback_url__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_5'] = x__validate_loopback_url__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_6'] = x__validate_loopback_url__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_7'] = x__validate_loopback_url__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_8'] = x__validate_loopback_url__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_9'] = x__validate_loopback_url__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_10'] = x__validate_loopback_url__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_11'] = x__validate_loopback_url__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_12'] = x__validate_loopback_url__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_13'] = x__validate_loopback_url__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_14'] = x__validate_loopback_url__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_15'] = x__validate_loopback_url__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_16'] = x__validate_loopback_url__mutmut_16 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_17'] = x__validate_loopback_url__mutmut_17 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_18'] = x__validate_loopback_url__mutmut_18 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_19'] = x__validate_loopback_url__mutmut_19 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_20'] = x__validate_loopback_url__mutmut_20 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_21'] = x__validate_loopback_url__mutmut_21 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_22'] = x__validate_loopback_url__mutmut_22 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_23'] = x__validate_loopback_url__mutmut_23 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_24'] = x__validate_loopback_url__mutmut_24 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_25'] = x__validate_loopback_url__mutmut_25 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_26'] = x__validate_loopback_url__mutmut_26 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_27'] = x__validate_loopback_url__mutmut_27 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_28'] = x__validate_loopback_url__mutmut_28 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_29'] = x__validate_loopback_url__mutmut_29 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_30'] = x__validate_loopback_url__mutmut_30 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_31'] = x__validate_loopback_url__mutmut_31 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_32'] = x__validate_loopback_url__mutmut_32 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_33'] = x__validate_loopback_url__mutmut_33 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_34'] = x__validate_loopback_url__mutmut_34 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_35'] = x__validate_loopback_url__mutmut_35 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_36'] = x__validate_loopback_url__mutmut_36 # type: ignore # mutmut generated
mutants_x__validate_loopback_url__mutmut['x__validate_loopback_url__mutmut_37'] = x__validate_loopback_url__mutmut_37 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__chunk_text__mutmut)
def _chunk_text(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_orig(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_1(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = None
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_2(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_3(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = None
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_4(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = None
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_5(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 1
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_6(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start <= len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_7(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = None
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_8(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(None, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_9(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, None)
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_10(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_11(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, )
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_12(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start - size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_13(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(None)
        if end == len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_14(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end != len(candidate):
            break
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_15(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            return
        start = end - overlap
    return chunks


def x__chunk_text__mutmut_16(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = None
    return chunks


def x__chunk_text__mutmut_17(text: str, size: int, overlap: int) -> list[str]:
    """Split non-empty text into stable overlapping character windows."""
    candidate = text.strip()
    if not candidate:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(candidate):
        end = min(start + size, len(candidate))
        chunks.append(candidate[start:end])
        if end == len(candidate):
            break
        start = end + overlap
    return chunks

mutants_x__chunk_text__mutmut['_mutmut_orig'] = x__chunk_text__mutmut_orig # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_1'] = x__chunk_text__mutmut_1 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_2'] = x__chunk_text__mutmut_2 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_3'] = x__chunk_text__mutmut_3 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_4'] = x__chunk_text__mutmut_4 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_5'] = x__chunk_text__mutmut_5 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_6'] = x__chunk_text__mutmut_6 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_7'] = x__chunk_text__mutmut_7 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_8'] = x__chunk_text__mutmut_8 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_9'] = x__chunk_text__mutmut_9 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_10'] = x__chunk_text__mutmut_10 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_11'] = x__chunk_text__mutmut_11 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_12'] = x__chunk_text__mutmut_12 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_13'] = x__chunk_text__mutmut_13 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_14'] = x__chunk_text__mutmut_14 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_15'] = x__chunk_text__mutmut_15 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_16'] = x__chunk_text__mutmut_16 # type: ignore # mutmut generated
mutants_x__chunk_text__mutmut['x__chunk_text__mutmut_17'] = x__chunk_text__mutmut_17 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__page_aware_chunks__mutmut)
def _page_aware_chunks(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_orig(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_1(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = None
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_2(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(None)
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_3(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(None))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_4(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_5(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(None, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_6(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, None, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_7(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, None)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_8(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_9(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_10(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, )]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_11(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = None
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_12(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(None):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_13(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = None
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_14(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if (index + 1 < len(matches)) and False else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_15(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if (index + 1 < len(matches)) or True else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_16(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index - 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_17(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 2].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_18(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index - 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_19(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 2 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_20(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 <= len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_21(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = None
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_22(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = None
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_23(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(None)
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_24(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group(None))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_25(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("XXpageXX"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_26(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("PAGE"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_27(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            None
        )
    return chunks


def x__page_aware_chunks__mutmut_28(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(None, size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_29(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, None, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_30(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, None)
        )
    return chunks


def x__page_aware_chunks__mutmut_31(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(size, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_32(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, overlap)
        )
    return chunks


def x__page_aware_chunks__mutmut_33(
    text: str,
    size: int,
    overlap: int,
) -> list[tuple[str, int | None]]:
    """Chunk OCR text without allowing one fragment to cross known PDF pages."""
    matches = list(_PAGE_HEADER.finditer(text))
    if not matches:
        return [(chunk, None) for chunk in _chunk_text(text, size, overlap)]
    chunks: list[tuple[str, int | None]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_text = text[match.start() : end]
        page = int(match.group("page"))
        chunks.extend(
            (chunk, page) for chunk in _chunk_text(page_text, size, )
        )
    return chunks

mutants_x__page_aware_chunks__mutmut['_mutmut_orig'] = x__page_aware_chunks__mutmut_orig # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_1'] = x__page_aware_chunks__mutmut_1 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_2'] = x__page_aware_chunks__mutmut_2 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_3'] = x__page_aware_chunks__mutmut_3 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_4'] = x__page_aware_chunks__mutmut_4 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_5'] = x__page_aware_chunks__mutmut_5 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_6'] = x__page_aware_chunks__mutmut_6 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_7'] = x__page_aware_chunks__mutmut_7 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_8'] = x__page_aware_chunks__mutmut_8 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_9'] = x__page_aware_chunks__mutmut_9 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_10'] = x__page_aware_chunks__mutmut_10 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_11'] = x__page_aware_chunks__mutmut_11 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_12'] = x__page_aware_chunks__mutmut_12 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_13'] = x__page_aware_chunks__mutmut_13 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_14'] = x__page_aware_chunks__mutmut_14 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_15'] = x__page_aware_chunks__mutmut_15 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_16'] = x__page_aware_chunks__mutmut_16 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_17'] = x__page_aware_chunks__mutmut_17 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_18'] = x__page_aware_chunks__mutmut_18 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_19'] = x__page_aware_chunks__mutmut_19 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_20'] = x__page_aware_chunks__mutmut_20 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_21'] = x__page_aware_chunks__mutmut_21 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_22'] = x__page_aware_chunks__mutmut_22 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_23'] = x__page_aware_chunks__mutmut_23 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_24'] = x__page_aware_chunks__mutmut_24 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_25'] = x__page_aware_chunks__mutmut_25 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_26'] = x__page_aware_chunks__mutmut_26 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_27'] = x__page_aware_chunks__mutmut_27 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_28'] = x__page_aware_chunks__mutmut_28 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_29'] = x__page_aware_chunks__mutmut_29 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_30'] = x__page_aware_chunks__mutmut_30 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_31'] = x__page_aware_chunks__mutmut_31 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_32'] = x__page_aware_chunks__mutmut_32 # type: ignore # mutmut generated
mutants_x__page_aware_chunks__mutmut['x__page_aware_chunks__mutmut_33'] = x__page_aware_chunks__mutmut_33 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decode_query_result__mutmut)
def _decode_query_result(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_orig(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_1(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = None
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_2(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["XXdocumentsXX"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_3(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["DOCUMENTS"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_4(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][1]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_5(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = None
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_6(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["XXmetadatasXX"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_7(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["METADATAS"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_8(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][1]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_9(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = None
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_10(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["XXdistancesXX"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_11(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["DISTANCES"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_12(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][1]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_13(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            None
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_14(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "XXThe local vector database returned invalid query results.XX"
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_15(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "the local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_16(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "THE LOCAL VECTOR DATABASE RETURNED INVALID QUERY RESULTS."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_17(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = None
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_18(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        None, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_19(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, None, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_20(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, None, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_21(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=None
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_22(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_23(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_24(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_25(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_26(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=False
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_27(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) and not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_28(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_29(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_30(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                None
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_31(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "XXThe local vector database returned invalid query results.XX"
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_32(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "the local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_33(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE RETURNED INVALID QUERY RESULTS."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_34(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = None
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_35(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get(None)
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_36(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("XXdocument_idXX")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_37(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("DOCUMENT_ID")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_38(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = None
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_39(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get(None)
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_40(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("XXsourceXX")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_41(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("SOURCE")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_42(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) and not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_43(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_44(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_45(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                None
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_46(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "XXThe local vector database returned invalid query results.XX"
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_47(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "the local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_48(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE RETURNED INVALID QUERY RESULTS."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_49(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = None
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_50(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get(None)
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_51(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("XXpageXX")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_52(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("PAGE")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_53(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None or (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_54(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_55(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) and page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_56(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_57(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page < 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_58(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 1):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_59(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                None
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_60(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "XXThe local vector database returned invalid query results.XX"
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_61(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "the local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_62(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE RETURNED INVALID QUERY RESULTS."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_63(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            None
        )
    return chunks


def x__decode_query_result__mutmut_64(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                None,
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_65(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                None,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_66(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                None,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_67(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                None,
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_68(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                None,
            )
        )
    return chunks


def x__decode_query_result__mutmut_69(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                content,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_70(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                source,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_71(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                float(distance),
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_72(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                page,
            )
        )
    return chunks


def x__decode_query_result__mutmut_73(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(distance),
                )
        )
    return chunks


def x__decode_query_result__mutmut_74(result: Any) -> list[RetrievedDocumentChunk]:
    """Validate the first Chroma result batch without exposing stored contents."""
    try:
        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]
    except (KeyError, IndexError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid query results."
        ) from exc
    chunks: list[RetrievedDocumentChunk] = []
    for content, metadata, distance in zip(
        documents, metadatas, distances, strict=True
    ):
        if not isinstance(content, str) or not isinstance(metadata, dict):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        document_id = metadata.get("document_id")
        source = metadata.get("source")
        if not isinstance(document_id, str) or not isinstance(source, str):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid query results."
            )
        chunks.append(
            RetrievedDocumentChunk(
                document_id,
                content,
                source,
                float(None),
                page,
            )
        )
    return chunks

mutants_x__decode_query_result__mutmut['_mutmut_orig'] = x__decode_query_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_1'] = x__decode_query_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_2'] = x__decode_query_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_3'] = x__decode_query_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_4'] = x__decode_query_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_5'] = x__decode_query_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_6'] = x__decode_query_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_7'] = x__decode_query_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_8'] = x__decode_query_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_9'] = x__decode_query_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_10'] = x__decode_query_result__mutmut_10 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_11'] = x__decode_query_result__mutmut_11 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_12'] = x__decode_query_result__mutmut_12 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_13'] = x__decode_query_result__mutmut_13 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_14'] = x__decode_query_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_15'] = x__decode_query_result__mutmut_15 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_16'] = x__decode_query_result__mutmut_16 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_17'] = x__decode_query_result__mutmut_17 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_18'] = x__decode_query_result__mutmut_18 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_19'] = x__decode_query_result__mutmut_19 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_20'] = x__decode_query_result__mutmut_20 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_21'] = x__decode_query_result__mutmut_21 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_22'] = x__decode_query_result__mutmut_22 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_23'] = x__decode_query_result__mutmut_23 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_24'] = x__decode_query_result__mutmut_24 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_25'] = x__decode_query_result__mutmut_25 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_26'] = x__decode_query_result__mutmut_26 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_27'] = x__decode_query_result__mutmut_27 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_28'] = x__decode_query_result__mutmut_28 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_29'] = x__decode_query_result__mutmut_29 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_30'] = x__decode_query_result__mutmut_30 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_31'] = x__decode_query_result__mutmut_31 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_32'] = x__decode_query_result__mutmut_32 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_33'] = x__decode_query_result__mutmut_33 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_34'] = x__decode_query_result__mutmut_34 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_35'] = x__decode_query_result__mutmut_35 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_36'] = x__decode_query_result__mutmut_36 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_37'] = x__decode_query_result__mutmut_37 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_38'] = x__decode_query_result__mutmut_38 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_39'] = x__decode_query_result__mutmut_39 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_40'] = x__decode_query_result__mutmut_40 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_41'] = x__decode_query_result__mutmut_41 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_42'] = x__decode_query_result__mutmut_42 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_43'] = x__decode_query_result__mutmut_43 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_44'] = x__decode_query_result__mutmut_44 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_45'] = x__decode_query_result__mutmut_45 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_46'] = x__decode_query_result__mutmut_46 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_47'] = x__decode_query_result__mutmut_47 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_48'] = x__decode_query_result__mutmut_48 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_49'] = x__decode_query_result__mutmut_49 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_50'] = x__decode_query_result__mutmut_50 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_51'] = x__decode_query_result__mutmut_51 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_52'] = x__decode_query_result__mutmut_52 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_53'] = x__decode_query_result__mutmut_53 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_54'] = x__decode_query_result__mutmut_54 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_55'] = x__decode_query_result__mutmut_55 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_56'] = x__decode_query_result__mutmut_56 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_57'] = x__decode_query_result__mutmut_57 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_58'] = x__decode_query_result__mutmut_58 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_59'] = x__decode_query_result__mutmut_59 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_60'] = x__decode_query_result__mutmut_60 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_61'] = x__decode_query_result__mutmut_61 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_62'] = x__decode_query_result__mutmut_62 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_63'] = x__decode_query_result__mutmut_63 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_64'] = x__decode_query_result__mutmut_64 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_65'] = x__decode_query_result__mutmut_65 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_66'] = x__decode_query_result__mutmut_66 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_67'] = x__decode_query_result__mutmut_67 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_68'] = x__decode_query_result__mutmut_68 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_69'] = x__decode_query_result__mutmut_69 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_70'] = x__decode_query_result__mutmut_70 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_71'] = x__decode_query_result__mutmut_71 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_72'] = x__decode_query_result__mutmut_72 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_73'] = x__decode_query_result__mutmut_73 # type: ignore # mutmut generated
mutants_x__decode_query_result__mutmut['x__decode_query_result__mutmut_74'] = x__decode_query_result__mutmut_74 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decode_document_fragments__mutmut)
def _decode_document_fragments(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_orig(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_1(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = None
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_2(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(None)
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_3(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["XXidsXX"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_4(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["IDS"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_5(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = None
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_6(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(None)
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_7(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["XXdocumentsXX"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_8(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["DOCUMENTS"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_9(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = None
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_10(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(None)
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_11(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["XXmetadatasXX"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_12(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["METADATAS"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_13(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            None
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_14(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "XXThe local vector database returned invalid document content.XX"
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_15(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "the local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_16(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "THE LOCAL VECTOR DATABASE RETURNED INVALID DOCUMENT CONTENT."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_17(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_18(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) != len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_19(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) != len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_20(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            None
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_21(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "XXThe local vector database returned invalid document content.XX"
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_22(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "the local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_23(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "THE LOCAL VECTOR DATABASE RETURNED INVALID DOCUMENT CONTENT."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_24(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = None
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_25(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        None, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_26(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, None, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_27(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, None, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_28(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=None
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_29(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_30(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_31(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_32(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_33(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=False
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_34(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict) and not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_35(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str) and not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_36(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str) and not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_37(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_38(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_39(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_40(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_41(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                None
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_42(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "XXThe local vector database returned invalid document content.XX"
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_43(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "the local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_44(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE RETURNED INVALID DOCUMENT CONTENT."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_45(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = None
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_46(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get(None)
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_47(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("XXpageXX")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_48(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("PAGE")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_49(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None or (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_50(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_51(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) and page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_52(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_53(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page < 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_54(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 1):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_55(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                None
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_56(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "XXThe local vector database returned invalid document content.XX"
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_57(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "the local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_58(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "THE LOCAL VECTOR DATABASE RETURNED INVALID DOCUMENT CONTENT."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_59(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            None
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_60(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(None, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_61(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, None, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_62(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, None, page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_63(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], None)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_64(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_65(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_66(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_67(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], )
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_68(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["XXsourceXX"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_69(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["SOURCE"], page)
        )
    return sorted(fragments, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_70(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(None, key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_71(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=None)


def x__decode_document_fragments__mutmut_72(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(key=lambda fragment: fragment.fragment_id)


def x__decode_document_fragments__mutmut_73(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, )


def x__decode_document_fragments__mutmut_74(result: Any) -> list[IndexedDocumentFragment]:
    """Validate and order the content returned by a filtered Chroma lookup."""
    try:
        identifiers = list(result["ids"])
        documents = list(result["documents"])
        metadatas = list(result["metadatas"])
    except (KeyError, TypeError) as exc:
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        ) from exc
    if not (len(identifiers) == len(documents) == len(metadatas)):
        raise VectorDatabaseError(
            "The local vector database returned invalid document content."
        )

    fragments: list[IndexedDocumentFragment] = []
    for fragment_id, content, metadata in zip(
        identifiers, documents, metadatas, strict=True
    ):
        if (
            not isinstance(fragment_id, str)
            or not isinstance(content, str)
            or not isinstance(metadata, dict)
            or not isinstance(metadata.get("source"), str)
        ):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        page = metadata.get("page")
        if page is not None and (not isinstance(page, int) or page <= 0):
            raise VectorDatabaseError(
                "The local vector database returned invalid document content."
            )
        fragments.append(
            IndexedDocumentFragment(fragment_id, content, metadata["source"], page)
        )
    return sorted(fragments, key=lambda fragment: None)

mutants_x__decode_document_fragments__mutmut['_mutmut_orig'] = x__decode_document_fragments__mutmut_orig # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_1'] = x__decode_document_fragments__mutmut_1 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_2'] = x__decode_document_fragments__mutmut_2 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_3'] = x__decode_document_fragments__mutmut_3 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_4'] = x__decode_document_fragments__mutmut_4 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_5'] = x__decode_document_fragments__mutmut_5 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_6'] = x__decode_document_fragments__mutmut_6 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_7'] = x__decode_document_fragments__mutmut_7 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_8'] = x__decode_document_fragments__mutmut_8 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_9'] = x__decode_document_fragments__mutmut_9 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_10'] = x__decode_document_fragments__mutmut_10 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_11'] = x__decode_document_fragments__mutmut_11 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_12'] = x__decode_document_fragments__mutmut_12 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_13'] = x__decode_document_fragments__mutmut_13 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_14'] = x__decode_document_fragments__mutmut_14 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_15'] = x__decode_document_fragments__mutmut_15 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_16'] = x__decode_document_fragments__mutmut_16 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_17'] = x__decode_document_fragments__mutmut_17 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_18'] = x__decode_document_fragments__mutmut_18 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_19'] = x__decode_document_fragments__mutmut_19 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_20'] = x__decode_document_fragments__mutmut_20 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_21'] = x__decode_document_fragments__mutmut_21 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_22'] = x__decode_document_fragments__mutmut_22 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_23'] = x__decode_document_fragments__mutmut_23 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_24'] = x__decode_document_fragments__mutmut_24 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_25'] = x__decode_document_fragments__mutmut_25 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_26'] = x__decode_document_fragments__mutmut_26 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_27'] = x__decode_document_fragments__mutmut_27 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_28'] = x__decode_document_fragments__mutmut_28 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_29'] = x__decode_document_fragments__mutmut_29 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_30'] = x__decode_document_fragments__mutmut_30 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_31'] = x__decode_document_fragments__mutmut_31 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_32'] = x__decode_document_fragments__mutmut_32 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_33'] = x__decode_document_fragments__mutmut_33 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_34'] = x__decode_document_fragments__mutmut_34 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_35'] = x__decode_document_fragments__mutmut_35 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_36'] = x__decode_document_fragments__mutmut_36 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_37'] = x__decode_document_fragments__mutmut_37 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_38'] = x__decode_document_fragments__mutmut_38 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_39'] = x__decode_document_fragments__mutmut_39 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_40'] = x__decode_document_fragments__mutmut_40 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_41'] = x__decode_document_fragments__mutmut_41 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_42'] = x__decode_document_fragments__mutmut_42 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_43'] = x__decode_document_fragments__mutmut_43 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_44'] = x__decode_document_fragments__mutmut_44 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_45'] = x__decode_document_fragments__mutmut_45 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_46'] = x__decode_document_fragments__mutmut_46 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_47'] = x__decode_document_fragments__mutmut_47 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_48'] = x__decode_document_fragments__mutmut_48 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_49'] = x__decode_document_fragments__mutmut_49 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_50'] = x__decode_document_fragments__mutmut_50 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_51'] = x__decode_document_fragments__mutmut_51 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_52'] = x__decode_document_fragments__mutmut_52 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_53'] = x__decode_document_fragments__mutmut_53 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_54'] = x__decode_document_fragments__mutmut_54 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_55'] = x__decode_document_fragments__mutmut_55 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_56'] = x__decode_document_fragments__mutmut_56 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_57'] = x__decode_document_fragments__mutmut_57 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_58'] = x__decode_document_fragments__mutmut_58 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_59'] = x__decode_document_fragments__mutmut_59 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_60'] = x__decode_document_fragments__mutmut_60 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_61'] = x__decode_document_fragments__mutmut_61 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_62'] = x__decode_document_fragments__mutmut_62 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_63'] = x__decode_document_fragments__mutmut_63 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_64'] = x__decode_document_fragments__mutmut_64 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_65'] = x__decode_document_fragments__mutmut_65 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_66'] = x__decode_document_fragments__mutmut_66 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_67'] = x__decode_document_fragments__mutmut_67 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_68'] = x__decode_document_fragments__mutmut_68 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_69'] = x__decode_document_fragments__mutmut_69 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_70'] = x__decode_document_fragments__mutmut_70 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_71'] = x__decode_document_fragments__mutmut_71 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_72'] = x__decode_document_fragments__mutmut_72 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_73'] = x__decode_document_fragments__mutmut_73 # type: ignore # mutmut generated
mutants_x__decode_document_fragments__mutmut['x__decode_document_fragments__mutmut_74'] = x__decode_document_fragments__mutmut_74 # type: ignore # mutmut generated
mutants_x__optional_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__optional_list__mutmut)
def _optional_list(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if value is None else list(value)


def x__optional_list__mutmut_orig(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if value is None else list(value)


def x__optional_list__mutmut_1(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if (value is None) and False else list(value)


def x__optional_list__mutmut_2(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if (value is None) or True else list(value)


def x__optional_list__mutmut_3(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if value is not None else list(value)


def x__optional_list__mutmut_4(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if value is None else list(None)

mutants_x__optional_list__mutmut['_mutmut_orig'] = x__optional_list__mutmut_orig # type: ignore # mutmut generated
mutants_x__optional_list__mutmut['x__optional_list__mutmut_1'] = x__optional_list__mutmut_1 # type: ignore # mutmut generated
mutants_x__optional_list__mutmut['x__optional_list__mutmut_2'] = x__optional_list__mutmut_2 # type: ignore # mutmut generated
mutants_x__optional_list__mutmut['x__optional_list__mutmut_3'] = x__optional_list__mutmut_3 # type: ignore # mutmut generated
mutants_x__optional_list__mutmut['x__optional_list__mutmut_4'] = x__optional_list__mutmut_4 # type: ignore # mutmut generated
