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


class VectorDatabaseError(RuntimeError):
    """Raised when the local vector index cannot complete an operation."""


class VectorDatabaseDependencyError(VectorDatabaseError):
    """Raised when Chroma is not installed in the local environment."""


class VectorDatabaseConfigurationError(VectorDatabaseError, ValueError):
    """Raised when the Chroma endpoint is not explicitly local and safe."""


ChromaClientFactory = Callable[[str, int], Any]


class ChromaDocumentVectorIndex:
    """Persist document fragments through a loopback-only Chroma server."""

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


def collection_name_for_embedding_model(model: str) -> str:
    """Return a stable collection name isolated to one embedding model."""
    candidate = model.strip()
    if not candidate:
        raise ValueError("model cannot be empty")
    digest = sha256(candidate.encode("utf-8")).hexdigest()[:12]
    return f"{_COLLECTION_PREFIX}_{digest}"


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


def _optional_list(value: Any) -> list[Any]:
    """Convert an optional Chroma sequence without testing array truthiness."""
    return [] if value is None else list(value)
