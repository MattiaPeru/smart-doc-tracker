from __future__ import annotations

from unittest import TestCase

from smart_doc_tracker.db.vector_database import (
    ChromaDocumentVectorIndex,
    VectorDatabaseConfigurationError,
    VectorDatabaseUnavailableError,
    collection_name_for_embedding_model,
)
from smart_doc_tracker.models.document import DocumentData


class FakeEmbeddingGenerator:
    def __init__(self) -> None:
        self.calls: list[list[str]] = []

    def embed(self, texts: list[str]) -> list[list[float]]:
        self.calls.append(list(texts))
        return [[float(index), 1.0] for index, _ in enumerate(texts, start=1)]


class FakeCollection:
    def __init__(self) -> None:
        self.delete_calls: list[list[str]] = []
        self.delete_where_calls: list[dict[str, str]] = []
        self.existing_ids: list[str] = []
        self.get_payload: dict[str, object] | None = None
        self.upsert_payload: dict[str, object] = {}
        self.query_payload: dict[str, object] = {}
        self.record_count = 3

    def get(self, **payload: object) -> dict[str, object]:
        if self.get_payload is not None:
            return self.get_payload
        return {"ids": self.existing_ids}

    def delete(
        self,
        *,
        ids: list[str] | None = None,
        where: dict[str, str] | None = None,
    ) -> None:
        if ids is not None:
            self.delete_calls.append(ids)
        if where is not None:
            self.delete_where_calls.append(where)

    def upsert(self, **payload: object) -> None:
        self.upsert_payload = payload

    def count(self) -> int:
        return self.record_count

    def query(self, **payload: object) -> dict[str, object]:
        self.query_payload = payload
        return {
            "documents": [["Relevant policy"]],
            "metadatas": [[{"document_id": "doc-1", "source": "raw_text"}]],
            "distances": [[0.125]],
        }


class FakeClient:
    def __init__(self, collection: FakeCollection) -> None:
        self.collection = collection
        self.calls: list[dict[str, object]] = []

    def get_or_create_collection(self, **kwargs: object) -> FakeCollection:
        self.calls.append(kwargs)
        return self.collection


def _document() -> DocumentData:
    return DocumentData(
        document_type="insurance_policy",
        summary="A vehicle insurance policy",
        expiry_date="2030-01-01",
        issue_date=None,
        extracted_data={"policy_number": "P-42"},
    )


class ChromaDocumentVectorIndexTests(TestCase):
    def test_reconnects_after_local_chroma_starts(self) -> None:
        collection = FakeCollection()
        available = False

        def create_client(_host: str, _port: int) -> FakeClient:
            if not available:
                raise OSError("Local service stopped")
            return FakeClient(collection)

        index = ChromaDocumentVectorIndex(
            embedding_generator=FakeEmbeddingGenerator(),
            client_factory=create_client,
        )
        with self.assertRaises(VectorDatabaseUnavailableError):
            index.upsert_document("doc-1", raw_text="Local text", document=_document())

        available = True
        index.upsert_document("doc-1", raw_text="Local text", document=_document())
        self.assertTrue(collection.upsert_payload["ids"])

    def test_classifies_a_stopped_service_after_connection(self) -> None:
        class StoppedCollection(FakeCollection):
            def get(self, **payload: object) -> dict[str, object]:
                raise OSError("Connection refused")

        class StoppedClient(FakeClient):
            def heartbeat(self) -> None:
                raise OSError("Connection refused")

        index = ChromaDocumentVectorIndex(
            embedding_generator=FakeEmbeddingGenerator(),
            client_factory=lambda _host, _port: StoppedClient(StoppedCollection()),
        )
        with self.assertRaises(VectorDatabaseUnavailableError):
            index.upsert_document("doc-1", raw_text="Local text", document=_document())

    def test_indexes_raw_summary_and_structured_data_with_explicit_embeddings(
        self,
    ) -> None:
        collection = FakeCollection()
        client = FakeClient(collection)
        embedder = FakeEmbeddingGenerator()
        client_calls: list[tuple[str, int]] = []

        def create_client(host: str, port: int) -> FakeClient:
            client_calls.append((host, port))
            return client

        index = ChromaDocumentVectorIndex(
            base_url="http://localhost:9000",
            embedding_generator=embedder,
            client_factory=create_client,
            chunk_characters=12,
            chunk_overlap=2,
        )
        index.upsert_document(
            "doc-1", raw_text="A sufficiently long raw text", document=_document()
        )

        self.assertEqual(client_calls, [("localhost", 9000)])
        self.assertEqual(client.calls[0]["name"], "smart_doc_tracker_documents")
        self.assertIsNone(client.calls[0]["embedding_function"])
        self.assertEqual(collection.delete_calls, [])
        documents = collection.upsert_payload["documents"]
        metadatas = collection.upsert_payload["metadatas"]
        self.assertIsInstance(documents, list)
        self.assertIsInstance(metadatas, list)
        assert isinstance(documents, list)
        assert isinstance(metadatas, list)
        self.assertIn("A vehicle insurance policy", documents)
        self.assertTrue(any('"policy_number": "P-42"' in item for item in documents))
        self.assertEqual(
            {item["source"] for item in metadatas},
            {"summary", "structured_data", "raw_text"},
        )
        self.assertEqual(len(embedder.calls[0]), len(documents))

    def test_deletes_only_stale_fragment_ids_after_upsert(self) -> None:
        collection = FakeCollection()
        collection.existing_ids = ["doc-1:summary", "doc-1:raw:9999"]
        index = ChromaDocumentVectorIndex(
            embedding_generator=FakeEmbeddingGenerator(),
            client_factory=lambda _host, _port: FakeClient(collection),
        )
        index.upsert_document(
            "doc-1", raw_text="Current raw text", document=_document()
        )

        self.assertEqual(collection.delete_calls, [["doc-1:raw:9999"]])

    def test_indexes_reliable_pdf_page_metadata_without_cross_page_chunks(self) -> None:
        collection = FakeCollection()
        index = ChromaDocumentVectorIndex(
            embedding_generator=FakeEmbeddingGenerator(),
            client_factory=lambda _host, _port: FakeClient(collection),
            chunk_characters=100,
            chunk_overlap=10,
        )

        index.upsert_document(
            "doc-1",
            raw_text="[Page 1]\nFirst page text\n\n[Page 2]\nSecond page text",
            document=_document(),
        )

        documents = collection.upsert_payload["documents"]
        metadatas = collection.upsert_payload["metadatas"]
        assert isinstance(documents, list)
        assert isinstance(metadatas, list)
        raw_pairs = [
            (content, metadata)
            for content, metadata in zip(documents, metadatas, strict=True)
            if metadata["source"] == "raw_text"
        ]
        self.assertEqual([metadata["page"] for _, metadata in raw_pairs], [1, 2])
        self.assertNotIn("Second page text", raw_pairs[0][0])

    def test_queries_with_precomputed_embedding_and_decodes_metadata(self) -> None:
        collection = FakeCollection()
        embedder = FakeEmbeddingGenerator()
        index = ChromaDocumentVectorIndex(
            embedding_generator=embedder,
            client_factory=lambda _host, _port: FakeClient(collection),
        )
        results = index.query("When does the policy expire?", limit=8)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].document_id, "doc-1")
        self.assertEqual(results[0].source, "raw_text")
        self.assertEqual(collection.query_payload["n_results"], 3)
        self.assertIn("query_embeddings", collection.query_payload)

    def test_returns_every_document_fragment_in_stable_identifier_order(self) -> None:
        collection = FakeCollection()
        collection.get_payload = {
            "ids": ["doc-1:raw:0002", "doc-1:summary", "doc-1:raw:0001"],
            "documents": ["second", "Summary", "first"],
            "metadatas": [
                {"document_id": "doc-1", "source": "raw_text"},
                {"document_id": "doc-1", "source": "summary"},
                {"document_id": "doc-1", "source": "raw_text"},
            ],
        }
        index = ChromaDocumentVectorIndex(
            embedding_generator=FakeEmbeddingGenerator(),
            client_factory=lambda _host, _port: FakeClient(collection),
        )

        fragments = index.get_document_fragments("doc-1")

        self.assertEqual(
            [fragment.fragment_id for fragment in fragments],
            ["doc-1:raw:0001", "doc-1:raw:0002", "doc-1:summary"],
        )
        self.assertEqual(
            [fragment.content for fragment in fragments], ["first", "second", "Summary"]
        )

    def test_snapshots_deletes_and_restores_all_document_fragments(self) -> None:
        collection = FakeCollection()
        collection.get_payload = {
            "ids": ["doc-1:summary"],
            "documents": ["A vehicle insurance policy"],
            "metadatas": [{"document_id": "doc-1", "source": "summary"}],
            "embeddings": [[1.0, 2.0]],
        }
        index = ChromaDocumentVectorIndex(
            embedding_generator=FakeEmbeddingGenerator(),
            client_factory=lambda _host, _port: FakeClient(collection),
        )

        snapshot = index.snapshot_document("doc-1")
        index.delete_document("doc-1")
        index.restore_document(snapshot)

        self.assertEqual(
            collection.delete_where_calls,
            [{"document_id": "doc-1"}, {"document_id": "doc-1"}],
        )
        self.assertEqual(collection.upsert_payload["ids"], ["doc-1:summary"])

    def test_builds_model_specific_collection_names(self) -> None:
        first = collection_name_for_embedding_model("embeddinggemma")
        second = collection_name_for_embedding_model("another-model")

        self.assertRegex(first, r"^smart_doc_tracker_documents_[0-9a-f]{12}$")
        self.assertNotEqual(first, second)
        self.assertEqual(first, collection_name_for_embedding_model(" embeddinggemma "))

        with self.assertRaises(ValueError):
            collection_name_for_embedding_model("  ")

    def test_rejects_non_loopback_chroma_endpoints_before_connecting(self) -> None:
        for endpoint in (
            "https://127.0.0.1:8000",
            "http://192.168.1.10:8000",
            "http://localhost:8000/path",
            "http://localhost",
        ):
            with self.subTest(endpoint=endpoint):
                with self.assertRaises(VectorDatabaseConfigurationError):
                    ChromaDocumentVectorIndex(
                        base_url=endpoint,
                        embedding_generator=FakeEmbeddingGenerator(),
                    )
