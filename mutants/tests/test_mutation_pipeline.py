from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from unittest import TestCase

from smart_doc_tracker.db.database import DocumentInsertResult, StoredDocument
from smart_doc_tracker.models.document import DocumentData
from smart_doc_tracker.mutation_pipeline import (
    CoordinatedMutationError,
    DocumentMutationPipeline,
)


def _document(summary: str) -> DocumentData:
    return DocumentData(
        document_type="identity_card",
        summary=summary,
        expiry_date=None,
        issue_date=None,
        extracted_data={"card_number": "A-1"},
    )


class FakeRepository:
    def __init__(self) -> None:
        self.record: StoredDocument | None = StoredDocument(
            id="doc-1",
            file_hash="a" * 64,
            document=_document("Original"),
            created_at=datetime(2026, 8, 26, tzinfo=UTC),
        )
        self.fail_delete = False
        self.inserted_hashes: list[str] = []

    def __enter__(self) -> FakeRepository:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def get_document_by_id(self, document_id: str) -> StoredDocument | None:
        return self.record if self.record and self.record.id == document_id else None

    def insert_document(
        self,
        document: DocumentData,
        *,
        file_hash: str,
    ) -> DocumentInsertResult:
        self.inserted_hashes.append(file_hash)
        self.record = StoredDocument(
            id="doc-1",
            file_hash=file_hash,
            document=document,
            created_at=datetime(2026, 8, 26, tzinfo=UTC),
        )
        return DocumentInsertResult(self.record, True)

    def upsert_document_sections(self, document_id: str, sections: Any) -> None:
        return None

    def update_document(
        self,
        document_id: str,
        document: DocumentData,
    ) -> StoredDocument | None:
        if self.record is None or self.record.id != document_id:
            return None
        self.record = StoredDocument(
            id=self.record.id,
            file_hash=self.record.file_hash,
            document=document,
            created_at=self.record.created_at,
        )
        return self.record

    def set_source_file_name(
        self,
        document_id: str,
        source_file_name: str,
    ) -> StoredDocument | None:
        if self.record is None or self.record.id != document_id:
            return None
        self.record = StoredDocument(
            id=self.record.id,
            file_hash=self.record.file_hash,
            document=self.record.document,
            created_at=self.record.created_at,
            source_file_name=source_file_name,
        )
        return self.record

    def delete_document(self, document_id: str) -> StoredDocument | None:
        if self.fail_delete:
            raise RuntimeError("Local delete failed")
        previous = self.get_document_by_id(document_id)
        self.record = None
        return previous


class FakeVectorIndex:
    def __init__(self) -> None:
        self.fail_upsert = False
        self.fail_update = False
        self.restored: list[dict[str, Any]] = []
        self.deleted: list[str] = []
        self.upserts: list[tuple[str, str, DocumentData]] = []

    def snapshot_document(self, document_id: str) -> dict[str, Any]:
        return {"ids": [f"{document_id}:summary"]}

    def restore_document(self, snapshot: dict[str, Any]) -> None:
        self.restored.append(snapshot)

    def upsert_document(
        self,
        document_id: str,
        *,
        raw_text: str,
        document: DocumentData,
    ) -> None:
        if self.fail_upsert:
            raise RuntimeError("Local index failed")
        self.upserts.append((document_id, raw_text, document))

    def update_document_data(
        self,
        document_id: str,
        document: DocumentData,
    ) -> None:
        if self.fail_update:
            raise RuntimeError("Local index update failed")

    def delete_document(self, document_id: str) -> None:
        self.deleted.append(document_id)


class DocumentMutationPipelineTests(TestCase):
    def setUp(self) -> None:
        self.repository = FakeRepository()
        self.vector = FakeVectorIndex()
        self.scheduled: list[str] = []

        def schedule(document_id: str) -> str:
            self.scheduled.append(document_id)
            return "update-job"

        self.pipeline = DocumentMutationPipeline(
            lambda: self.repository,
            self.vector,
            schedule,
        )

    def test_rolls_back_mongo_when_durable_queueing_fails(self) -> None:
        def fail(_document_id: str) -> str:
            raise RuntimeError("Local queue failed")

        self.pipeline.index_update_submitter = fail

        with self.assertRaises(CoordinatedMutationError):
            self.pipeline.update("doc-1", _document("Changed"))

        assert self.repository.record is not None
        self.assertEqual(self.repository.record.document.summary, "Original")
        self.assertEqual(self.vector.restored, [])

    def test_updates_storage_without_waiting_for_vector_refresh(self) -> None:
        result = self.pipeline.update("doc-1", _document("Changed"))

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result.index_update_id, "update-job")
        self.assertEqual(self.scheduled, ["doc-1"])
        self.assertEqual(self.vector.restored, [])

    def test_creates_manual_document_without_ocr_source_text(self) -> None:
        document = _document("Entered by the user")

        result = self.pipeline.create_manual(document)

        self.assertTrue(result.inserted)
        self.assertEqual(len(self.repository.inserted_hashes[0]), 64)
        self.assertRegex(self.repository.inserted_hashes[0], r"^[0-9a-f]{64}$")
        self.assertEqual(self.vector.upserts, [("doc-1", "", document)])

    def test_links_the_archived_source_after_confirmation(self) -> None:
        result = self.pipeline.confirm(
            _document("Confirmed"),
            file_hash="b" * 64,
            raw_text="Local source text",
            finalize=lambda: Path("data/processed/identity-card.pdf"),
        )

        self.assertEqual(result.record.source_file_name, "identity-card.pdf")

    def test_restores_vector_snapshot_when_mongo_delete_fails(self) -> None:
        self.repository.fail_delete = True

        with self.assertRaises(CoordinatedMutationError):
            self.pipeline.delete("doc-1")

        self.assertIsNotNone(self.repository.record)
        self.assertEqual(self.vector.restored, [{"ids": ["doc-1:summary"]}])

    def test_removes_partial_insert_when_vector_indexing_fails(self) -> None:
        self.repository.record = None
        self.vector.fail_upsert = True
        finalized: list[bool] = []

        with self.assertRaises(CoordinatedMutationError):
            self.pipeline.confirm(
                _document("Confirmed"),
                file_hash="b" * 64,
                raw_text="Local source text",
                finalize=lambda: finalized.append(True),
            )

        self.assertIsNone(self.repository.record)
        self.assertEqual(self.vector.deleted, ["doc-1"])
        self.assertEqual(finalized, [])

    def test_rejects_incomplete_container_before_persistence(self) -> None:
        document = _document("Malformed")
        document.extracted_data["education"] = "[{"
        original = self.repository.record

        with self.assertRaisesRegex(ValueError, "incomplete JSON container"):
            self.pipeline.confirm(
                document,
                file_hash="b" * 64,
                raw_text="Local source text",
            )

        self.assertIs(self.repository.record, original)
        self.assertEqual(self.vector.deleted, [])
