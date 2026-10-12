"""JSON serialization for command-line results."""

from __future__ import annotations

import json
from typing import TextIO

from ..db.database import DocumentInsertResult, StoredDocument
from ..models.document import DocumentData
from ..pipeline import ExpirationCheckResult, InboxProcessingResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁJsonResultSerializerǁwrite__mutmut: MutantDict = {}  # type: ignore
mutants_xǁJsonResultSerializerǁdocument__mutmut: MutantDict = {}  # type: ignore
mutants_xǁJsonResultSerializerǁinsert_result__mutmut: MutantDict = {}  # type: ignore
mutants_xǁJsonResultSerializerǁstored_document__mutmut: MutantDict = {}  # type: ignore
mutants_xǁJsonResultSerializerǁexpiration_result__mutmut: MutantDict = {}  # type: ignore
mutants_xǁJsonResultSerializerǁinbox_result__mutmut: MutantDict = {}  # type: ignore


class JsonResultSerializer:
    """Convert domain and workflow results to stable CLI JSON payloads."""

    @staticmethod
    @_mutmut_mutated(mutants_xǁJsonResultSerializerǁwrite__mutmut)
    def write(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=2))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_orig(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=2))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_1(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(None)
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_2(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(None, indent=2))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_3(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=None))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_4(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(indent=2))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_5(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, ))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_6(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=3))
        stream.write("\n")

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_7(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=2))
        stream.write(None)

    @staticmethod
    def xǁJsonResultSerializerǁwrite__mutmut_8(payload: object, stream: TextIO) -> None:
        """Write one formatted JSON value followed by a newline."""
        stream.write(json.dumps(payload, indent=2))
        stream.write("XX\nXX")

    @staticmethod
    @_mutmut_mutated(mutants_xǁJsonResultSerializerǁdocument__mutmut)
    def document(document: DocumentData) -> dict[str, object]:
        """Serialize validated document data for JSON output."""
        return document.model_dump(mode="json")

    @staticmethod
    def xǁJsonResultSerializerǁdocument__mutmut_orig(document: DocumentData) -> dict[str, object]:
        """Serialize validated document data for JSON output."""
        return document.model_dump(mode="json")

    @staticmethod
    def xǁJsonResultSerializerǁdocument__mutmut_1(document: DocumentData) -> dict[str, object]:
        """Serialize validated document data for JSON output."""
        return document.model_dump(mode=None)

    @staticmethod
    def xǁJsonResultSerializerǁdocument__mutmut_2(document: DocumentData) -> dict[str, object]:
        """Serialize validated document data for JSON output."""
        return document.model_dump(mode="XXjsonXX")

    @staticmethod
    def xǁJsonResultSerializerǁdocument__mutmut_3(document: DocumentData) -> dict[str, object]:
        """Serialize validated document data for JSON output."""
        return document.model_dump(mode="JSON")

    @classmethod
    @_mutmut_mutated(mutants_xǁJsonResultSerializerǁinsert_result__mutmut, is_classmethod = True)
    def insert_result(cls, result: DocumentInsertResult) -> dict[str, object]:
        """Serialize a document insertion result."""
        return {"inserted": result.inserted, **cls.stored_document(result.record)}

    @classmethod
    def xǁJsonResultSerializerǁinsert_result__mutmut_orig(cls, result: DocumentInsertResult) -> dict[str, object]:
        """Serialize a document insertion result."""
        return {"inserted": result.inserted, **cls.stored_document(result.record)}

    @classmethod
    def xǁJsonResultSerializerǁinsert_result__mutmut_1(cls, result: DocumentInsertResult) -> dict[str, object]:
        """Serialize a document insertion result."""
        return {"XXinsertedXX": result.inserted, **cls.stored_document(result.record)}

    @classmethod
    def xǁJsonResultSerializerǁinsert_result__mutmut_2(cls, result: DocumentInsertResult) -> dict[str, object]:
        """Serialize a document insertion result."""
        return {"INSERTED": result.inserted, **cls.stored_document(result.record)}

    @classmethod
    def xǁJsonResultSerializerǁinsert_result__mutmut_3(cls, result: DocumentInsertResult) -> dict[str, object]:
        """Serialize a document insertion result."""
        return {"inserted": result.inserted, **cls.stored_document(None)}

    @staticmethod
    @_mutmut_mutated(mutants_xǁJsonResultSerializerǁstored_document__mutmut)
    def stored_document(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_orig(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_1(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "XXidXX": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_2(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "ID": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_3(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "XXfile_hashXX": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_4(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "FILE_HASH": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_5(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "XXcreated_atXX": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_6(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "CREATED_AT": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_7(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "XXdocumentXX": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_8(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "DOCUMENT": record.document.model_dump(mode="json"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_9(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode=None),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_10(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="XXjsonXX"),
        }

    @staticmethod
    def xǁJsonResultSerializerǁstored_document__mutmut_11(record: StoredDocument) -> dict[str, object]:
        """Serialize one stored document record."""
        return {
            "id": record.id,
            "file_hash": record.file_hash,
            "created_at": record.created_at.isoformat(),
            "document": record.document.model_dump(mode="JSON"),
        }

    @staticmethod
    @_mutmut_mutated(mutants_xǁJsonResultSerializerǁexpiration_result__mutmut)
    def expiration_result(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "documents_found": result.documents_found,
            "notifications_sent": result.notifications_sent,
        }

    @staticmethod
    def xǁJsonResultSerializerǁexpiration_result__mutmut_orig(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "documents_found": result.documents_found,
            "notifications_sent": result.notifications_sent,
        }

    @staticmethod
    def xǁJsonResultSerializerǁexpiration_result__mutmut_1(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "XXdocuments_foundXX": result.documents_found,
            "notifications_sent": result.notifications_sent,
        }

    @staticmethod
    def xǁJsonResultSerializerǁexpiration_result__mutmut_2(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "DOCUMENTS_FOUND": result.documents_found,
            "notifications_sent": result.notifications_sent,
        }

    @staticmethod
    def xǁJsonResultSerializerǁexpiration_result__mutmut_3(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "documents_found": result.documents_found,
            "XXnotifications_sentXX": result.notifications_sent,
        }

    @staticmethod
    def xǁJsonResultSerializerǁexpiration_result__mutmut_4(result: ExpirationCheckResult) -> dict[str, int]:
        """Serialize an expiration-check summary."""
        return {
            "documents_found": result.documents_found,
            "NOTIFICATIONS_SENT": result.notifications_sent,
        }

    @staticmethod
    @_mutmut_mutated(mutants_xǁJsonResultSerializerǁinbox_result__mutmut)
    def inbox_result(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_orig(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_1(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "XXdiscoveredXX": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_2(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "DISCOVERED": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_3(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "XXprocessedXX": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_4(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "PROCESSED": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_5(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "XXalready_presentXX": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_6(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "ALREADY_PRESENT": result.already_present,
            "failed": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_7(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "XXfailedXX": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_8(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "FAILED": result.failed,
            "skipped": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_9(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "XXskippedXX": result.skipped,
        }

    @staticmethod
    def xǁJsonResultSerializerǁinbox_result__mutmut_10(result: InboxProcessingResult) -> dict[str, int]:
        """Serialize an inbox-processing summary."""
        return {
            "discovered": result.discovered,
            "processed": result.processed,
            "already_present": result.already_present,
            "failed": result.failed,
            "SKIPPED": result.skipped,
        }

mutants_xǁJsonResultSerializerǁwrite__mutmut['_mutmut_orig'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_orig # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_1'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_1 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_2'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_2 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_3'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_3 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_4'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_4 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_5'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_5 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_6'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_6 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_7'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_7 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁwrite__mutmut['xǁJsonResultSerializerǁwrite__mutmut_8'] = JsonResultSerializer.xǁJsonResultSerializerǁwrite__mutmut_8 # type: ignore # mutmut generated

mutants_xǁJsonResultSerializerǁdocument__mutmut['_mutmut_orig'] = JsonResultSerializer.xǁJsonResultSerializerǁdocument__mutmut_orig # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁdocument__mutmut['xǁJsonResultSerializerǁdocument__mutmut_1'] = JsonResultSerializer.xǁJsonResultSerializerǁdocument__mutmut_1 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁdocument__mutmut['xǁJsonResultSerializerǁdocument__mutmut_2'] = JsonResultSerializer.xǁJsonResultSerializerǁdocument__mutmut_2 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁdocument__mutmut['xǁJsonResultSerializerǁdocument__mutmut_3'] = JsonResultSerializer.xǁJsonResultSerializerǁdocument__mutmut_3 # type: ignore # mutmut generated

mutants_xǁJsonResultSerializerǁinsert_result__mutmut['_mutmut_orig'] = JsonResultSerializer.xǁJsonResultSerializerǁinsert_result__mutmut_orig # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinsert_result__mutmut['xǁJsonResultSerializerǁinsert_result__mutmut_1'] = JsonResultSerializer.xǁJsonResultSerializerǁinsert_result__mutmut_1 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinsert_result__mutmut['xǁJsonResultSerializerǁinsert_result__mutmut_2'] = JsonResultSerializer.xǁJsonResultSerializerǁinsert_result__mutmut_2 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinsert_result__mutmut['xǁJsonResultSerializerǁinsert_result__mutmut_3'] = JsonResultSerializer.xǁJsonResultSerializerǁinsert_result__mutmut_3 # type: ignore # mutmut generated

mutants_xǁJsonResultSerializerǁstored_document__mutmut['_mutmut_orig'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_orig # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_1'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_1 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_2'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_2 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_3'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_3 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_4'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_4 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_5'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_5 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_6'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_6 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_7'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_7 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_8'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_8 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_9'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_9 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_10'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_10 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁstored_document__mutmut['xǁJsonResultSerializerǁstored_document__mutmut_11'] = JsonResultSerializer.xǁJsonResultSerializerǁstored_document__mutmut_11 # type: ignore # mutmut generated

mutants_xǁJsonResultSerializerǁexpiration_result__mutmut['_mutmut_orig'] = JsonResultSerializer.xǁJsonResultSerializerǁexpiration_result__mutmut_orig # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁexpiration_result__mutmut['xǁJsonResultSerializerǁexpiration_result__mutmut_1'] = JsonResultSerializer.xǁJsonResultSerializerǁexpiration_result__mutmut_1 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁexpiration_result__mutmut['xǁJsonResultSerializerǁexpiration_result__mutmut_2'] = JsonResultSerializer.xǁJsonResultSerializerǁexpiration_result__mutmut_2 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁexpiration_result__mutmut['xǁJsonResultSerializerǁexpiration_result__mutmut_3'] = JsonResultSerializer.xǁJsonResultSerializerǁexpiration_result__mutmut_3 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁexpiration_result__mutmut['xǁJsonResultSerializerǁexpiration_result__mutmut_4'] = JsonResultSerializer.xǁJsonResultSerializerǁexpiration_result__mutmut_4 # type: ignore # mutmut generated

mutants_xǁJsonResultSerializerǁinbox_result__mutmut['_mutmut_orig'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_orig # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_1'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_1 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_2'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_2 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_3'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_3 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_4'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_4 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_5'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_5 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_6'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_6 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_7'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_7 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_8'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_8 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_9'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_9 # type: ignore # mutmut generated
mutants_xǁJsonResultSerializerǁinbox_result__mutmut['xǁJsonResultSerializerǁinbox_result__mutmut_10'] = JsonResultSerializer.xǁJsonResultSerializerǁinbox_result__mutmut_10 # type: ignore # mutmut generated
