"""Coordinate application-visible mutations across MongoDB and ChromaDB."""

from __future__ import annotations

from _thread import LockType
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from secrets import token_hex
from threading import Lock

from .db.database import DocumentInsertResult, StoredDocument
from .interfaces.document_repository import DocumentRepository
from .interfaces.document_vector_index import DocumentVectorIndex
from .models.document import DocumentData, StructuredDocumentSection


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CoordinatedMutationError(RuntimeError):
    """Raised when a coordinated mutation fails and is compensated."""


RepositoryFactory = Callable[[], DocumentRepository]
IndexUpdateSubmitter = Callable[[str], str]


@dataclass(frozen=True, slots=True)
class DocumentUpdateResult:
    """Stored document together with its durable local refresh job."""

    record: StoredDocument
    index_update_id: str
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentMutationPipelineǁupdate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentMutationPipelineǁdelete__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut: MutantDict = {}  # type: ignore


@dataclass(slots=True)
class DocumentMutationPipeline:
    """Apply local document mutations with compensating cross-store rollback."""

    repository_factory: RepositoryFactory
    vector_index: DocumentVectorIndex
    index_update_submitter: IndexUpdateSubmitter
    operation_lock: LockType = field(default_factory=Lock)

    @_mutmut_mutated(mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut)
    def create_manual(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(32),
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_orig(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(32),
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_1(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            None,
            file_hash=token_hex(32),
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_2(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=None,
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_3(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(32),
            raw_text=None,
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_4(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            file_hash=token_hex(32),
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_5(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_6(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(32),
            )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_7(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(None),
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_8(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(33),
            raw_text="",
        )

    def xǁDocumentMutationPipelineǁcreate_manual__mutmut_9(self, document: DocumentData) -> DocumentInsertResult:
        """Persist and index user-authored data without an OCR source file."""
        return self.confirm(
            document,
            file_hash=token_hex(32),
            raw_text="XXXX",
        )

    @_mutmut_mutated(mutants_xǁDocumentMutationPipelineǁconfirm__mutmut)
    def confirm(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_orig(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_1(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = ""
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_2(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = None
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_3(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(None, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_4(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=None)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_5(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_6(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, )
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_7(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            None,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_8(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            None,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_9(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_10(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_11(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        None,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_12(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=None,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_13(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=None,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_14(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_15(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_16(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_17(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_18(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = None
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_19(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = None
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_20(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        None,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_21(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        None,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_22(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_23(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_24(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is not None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_25(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            None
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_26(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "XXThe archived source could not be linked to its document.XX"
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_27(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "the archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_28(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "THE ARCHIVED SOURCE COULD NOT BE LINKED TO ITS DOCUMENT."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_29(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = None
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_30(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=None,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_31(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=None,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_32(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_33(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_34(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = None
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_35(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = False
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_36(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None or inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_37(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_38(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = None
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_39(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(None)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_40(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_41(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    None
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_42(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "XXThe confirmed document failed and automatic rollback was XX"
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_43(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "the confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_44(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "THE CONFIRMED DOCUMENT FAILED AND AUTOMATIC ROLLBACK WAS "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_45(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "XXincomplete.XX"
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_46(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "INCOMPLETE."
                ) from exc
            raise CoordinatedMutationError(
                "The confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_47(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                None
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_48(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "XXThe confirmed document was not committed to both local stores.XX"
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_49(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "the confirmed document was not committed to both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁconfirm__mutmut_50(
        self,
        document: DocumentData,
        *,
        file_hash: str,
        raw_text: str,
        sections: Sequence[StructuredDocumentSection] = (),
        finalize: Callable[[], Path] | None = None,
    ) -> DocumentInsertResult:
        """Persist and index one confirmed document before finalizing its source."""
        document.ensure_complete_dynamic_values()
        inserted: DocumentInsertResult | None = None
        try:
            with self.repository_factory() as repository:
                inserted = repository.insert_document(document, file_hash=file_hash)
                if inserted.inserted:
                    if sections:
                        repository.upsert_document_sections(
                            inserted.record.id,
                            sections,
                        )
                    self.vector_index.upsert_document(
                        inserted.record.id,
                        raw_text=raw_text,
                        document=document,
                    )
                if finalize is not None:
                    archived_path = finalize()
                    archived_record = repository.set_source_file_name(
                        inserted.record.id,
                        archived_path.name,
                    )
                    if archived_record is None:
                        raise CoordinatedMutationError(
                            "The archived source could not be linked to its document."
                        )
                    inserted = DocumentInsertResult(
                        record=archived_record,
                        inserted=inserted.inserted,
                    )
                return inserted
        except Exception as exc:
            compensated = True
            if inserted is not None and inserted.inserted:
                compensated = self._compensate_insert(inserted.record.id)
            if not compensated:
                raise CoordinatedMutationError(
                    "The confirmed document failed and automatic rollback was "
                    "incomplete."
                ) from exc
            raise CoordinatedMutationError(
                "THE CONFIRMED DOCUMENT WAS NOT COMMITTED TO BOTH LOCAL STORES."
            ) from exc

    @_mutmut_mutated(mutants_xǁDocumentMutationPipelineǁupdate__mutmut)
    def update(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_orig(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_1(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = None
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_2(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(None)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_3(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is not None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_4(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = None
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_5(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(None, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_6(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, None)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_7(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_8(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, )
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_9(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is not None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_10(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = None
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_11(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(None)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_12(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(None, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_13(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, None)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_14(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_15(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, )
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_16(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                None
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_17(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "XXThe document update failed and automatic rollback XX"
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_18(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "the document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_19(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "THE DOCUMENT UPDATE FAILED AND AUTOMATIC ROLLBACK "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_20(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "XXwas incomplete.XX"
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_21(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "WAS INCOMPLETE."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_22(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            None
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_23(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "XXThe document update was rolled back before local search XX"
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_24(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "the document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_25(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "THE DOCUMENT UPDATE WAS ROLLED BACK BEFORE LOCAL SEARCH "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_26(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "XXrefresh was scheduled.XX"
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_27(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "REFRESH WAS SCHEDULED."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_28(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(None, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_29(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, None)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_30(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_31(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, )
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_32(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                None
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_33(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "XXThe document could not be updated in both local stores.XX"
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_34(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "the document could not be updated in both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁupdate__mutmut_35(
        self,
        document_id: str,
        document: DocumentData,
    ) -> DocumentUpdateResult | None:
        """Store one update and durably schedule its local search refresh."""
        document.ensure_complete_dynamic_values()
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    previous = repository.get_document_by_id(document_id)
                    if previous is None:
                        return None
                    updated = repository.update_document(document_id, document)
                    if updated is None:
                        return None
                    try:
                        update_id = self.index_update_submitter(document_id)
                    except Exception as exc:
                        try:
                            repository.update_document(document_id, previous.document)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document update failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document update was rolled back before local search "
                            "refresh was scheduled."
                        ) from exc
                    return DocumentUpdateResult(updated, update_id)
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "THE DOCUMENT COULD NOT BE UPDATED IN BOTH LOCAL STORES."
            ) from exc

    @_mutmut_mutated(mutants_xǁDocumentMutationPipelineǁdelete__mutmut)
    def delete(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_orig(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_1(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(None) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_2(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is not None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_3(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = None
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_4(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(None)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_5(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(None)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_6(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = None
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_7(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(None)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_8(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(None)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_9(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                None
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_10(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "XXThe document deletion failed and automatic rollback XX"
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_11(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "the document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_12(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "THE DOCUMENT DELETION FAILED AND AUTOMATIC ROLLBACK "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_13(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "XXwas incomplete.XX"
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_14(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "WAS INCOMPLETE."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_15(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            None
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_16(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "XXThe document deletion was rolled back in both local XX"
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_17(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "the document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_18(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "THE DOCUMENT DELETION WAS ROLLED BACK IN BOTH LOCAL "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_19(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "XXstores.XX"
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_20(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "STORES."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "The document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_21(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                None
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_22(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "XXThe document could not be deleted from both local stores.XX"
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_23(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "the document could not be deleted from both local stores."
            ) from exc

    def xǁDocumentMutationPipelineǁdelete__mutmut_24(self, document_id: str) -> StoredDocument | None:
        """Delete from ChromaDB and MongoDB, restoring ChromaDB if MongoDB fails."""
        try:
            with self.operation_lock:
                with self.repository_factory() as repository:
                    if repository.get_document_by_id(document_id) is None:
                        return None
                    snapshot = self.vector_index.snapshot_document(document_id)
                    try:
                        self.vector_index.delete_document(document_id)
                        deleted = repository.delete_document(document_id)
                    except Exception as exc:
                        try:
                            self.vector_index.restore_document(snapshot)
                        except Exception:
                            raise CoordinatedMutationError(
                                "The document deletion failed and automatic rollback "
                                "was incomplete."
                            ) from exc
                        raise CoordinatedMutationError(
                            "The document deletion was rolled back in both local "
                            "stores."
                        ) from exc
                    return deleted
        except CoordinatedMutationError:
            raise
        except Exception as exc:
            raise CoordinatedMutationError(
                "THE DOCUMENT COULD NOT BE DELETED FROM BOTH LOCAL STORES."
            ) from exc

    @_mutmut_mutated(mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut)
    def _compensate_insert(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_orig(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_1(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = None
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_2(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = False
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_3(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(None)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_4(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = None
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_5(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = True
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_6(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(None)
        except Exception:
            completed = False
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_7(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = None
        return completed

    def xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_8(self, document_id: str) -> bool:
        """Remove a partial insert and report whether both stores were cleaned."""
        completed = True
        try:
            self.vector_index.delete_document(document_id)
        except Exception:
            completed = False
        try:
            with self.repository_factory() as repository:
                repository.delete_document(document_id)
        except Exception:
            completed = True
        return completed

mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['_mutmut_orig'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_1'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_2'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_3'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_4'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_5'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_6'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_7'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_8'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁcreate_manual__mutmut['xǁDocumentMutationPipelineǁcreate_manual__mutmut_9'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁcreate_manual__mutmut_9 # type: ignore # mutmut generated

mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['_mutmut_orig'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_1'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_2'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_3'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_4'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_5'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_6'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_7'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_8'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_9'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_10'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_11'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_12'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_13'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_14'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_15'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_16'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_17'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_18'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_19'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_20'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_21'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_22'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_23'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_24'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_25'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_26'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_27'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_28'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_29'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_30'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_31'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_32'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_33'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_34'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_35'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_36'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_37'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_38'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_39'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_40'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_41'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_42'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_43'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_44'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_45'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_46'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_47'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_48'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_49'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁconfirm__mutmut['xǁDocumentMutationPipelineǁconfirm__mutmut_50'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁconfirm__mutmut_50 # type: ignore # mutmut generated

mutants_xǁDocumentMutationPipelineǁupdate__mutmut['_mutmut_orig'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_1'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_2'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_3'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_4'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_5'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_6'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_7'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_8'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_9'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_10'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_11'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_12'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_13'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_14'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_15'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_16'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_17'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_18'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_19'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_20'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_21'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_22'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_23'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_24'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_25'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_26'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_27'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_28'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_29'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_30'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_31'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_32'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_33'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_34'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁupdate__mutmut['xǁDocumentMutationPipelineǁupdate__mutmut_35'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁupdate__mutmut_35 # type: ignore # mutmut generated

mutants_xǁDocumentMutationPipelineǁdelete__mutmut['_mutmut_orig'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_1'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_2'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_3'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_4'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_5'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_6'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_7'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_8'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_9'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_10'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_11'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_12'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_13'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_14'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_15'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_16'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_17'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_18'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_19'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_20'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_21'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_22'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_23'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁdelete__mutmut['xǁDocumentMutationPipelineǁdelete__mutmut_24'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁdelete__mutmut_24 # type: ignore # mutmut generated

mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['_mutmut_orig'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_1'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_2'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_3'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_4'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_5'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_6'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_7'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentMutationPipelineǁ_compensate_insert__mutmut['xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_8'] = DocumentMutationPipeline.xǁDocumentMutationPipelineǁ_compensate_insert__mutmut_8 # type: ignore # mutmut generated
