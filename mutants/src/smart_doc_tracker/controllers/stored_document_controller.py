"""CLI presentation for direct stored-document queries."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from pydantic import ValidationError

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..db.database import (
    DatabaseConfigurationError,
    DatabaseError,
    MongoDocumentRepository,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStoredDocumentControllerǁget_stored__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut: MutantDict = {}  # type: ignore


@dataclass(slots=True)
class StoredDocumentController:
    """Read stored documents and render query results for the CLI."""

    dependencies: CliDependencies

    @_mutmut_mutated(mutants_xǁStoredDocumentControllerǁlist_stored__mutmut)
    def list_stored(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_orig(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_1(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = None
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_2(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                None,
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_3(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=None,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_4(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=None,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_5(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_6(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_7(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_8(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "XX[1/1] Reading stored documents from local MongoDB...XX",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_9(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] reading stored documents from local mongodb...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_10(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] READING STORED DOCUMENTS FROM LOCAL MONGODB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_11(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=False,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_12(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = None
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_13(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory and MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_14(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = None
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_15(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(None, file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_16(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=None)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_17(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_18(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", )
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_19(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 2

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_20(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            None,
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_21(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=None,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_22(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=None,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_23(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_24(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_25(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_26(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=False,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_27(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            None,
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_28(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            None,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_29(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_30(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_31(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(None) for item in documents],
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁlist_stored__mutmut_32(self) -> int:
        """Print every locally stored document as JSON."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading stored documents from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                documents = repository.get_all_documents()
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1

        print(
            f"[1/1] Database read completed ({len(documents)} document(s)).",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            [JsonResultSerializer.stored_document(item) for item in documents],
            dependencies.stdout,
        )
        return 1

    @_mutmut_mutated(mutants_xǁStoredDocumentControllerǁget_stored__mutmut)
    def get_stored(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_orig(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_1(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = None
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_2(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                None,
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_3(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=None,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_4(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=None,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_5(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_6(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_7(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_8(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "XX[1/1] Reading the stored document from local MongoDB...XX",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_9(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] reading the stored document from local mongodb...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_10(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] READING THE STORED DOCUMENT FROM LOCAL MONGODB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_11(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=False,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_12(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = None
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_13(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory and MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_14(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = None
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_15(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(None)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_16(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(None, file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_17(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=None)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_18(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_19(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", )
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_20(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 2
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_21(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is not None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_22(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print(None, file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_23(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=None)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_24(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print(file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_25(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", )
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_26(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("XXStored document not found.XX", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_27(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_28(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("STORED DOCUMENT NOT FOUND.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_29(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 2

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_30(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            None,
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_31(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=None,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_32(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=None,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_33(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_34(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_35(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_36(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "XX[1/1] Database read completed.XX",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_37(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_38(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] DATABASE READ COMPLETED.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_39(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=False,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_40(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            None,
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_41(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            None,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_42(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_43(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_44(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(None),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁget_stored__mutmut_45(self, document_id: str) -> int:
        """Print one locally stored document selected by identifier."""
        dependencies = self.dependencies
        try:
            print(
                "[1/1] Reading the stored document from local MongoDB...",
                file=dependencies.stderr,
                flush=True,
            )
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                document = repository.get_document_by_id(document_id)
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database read failed: {exc}", file=dependencies.stderr)
            return 1
        if document is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database read completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(document),
            dependencies.stdout,
        )
        return 1

    @_mutmut_mutated(mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut)
    def update_stored(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_orig(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_1(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = None
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_2(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = None
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_3(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "XXdocument_typeXX": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_4(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "DOCUMENT_TYPE": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_5(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "XXsummaryXX": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_6(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "SUMMARY": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_7(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "XXexpiry_dateXX": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_8(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "EXPIRY_DATE": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_9(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "XXissue_dateXX": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_10(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "ISSUE_DATE": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_11(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_12(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_13(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = None
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_14(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(None)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_15(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    None,
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_16(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=None,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_17(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_18(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_19(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "XXInput error: --extracted-data-json must contain valid JSON.XX",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_20(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "input error: --extracted-data-json must contain valid json.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_21(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "INPUT ERROR: --EXTRACTED-DATA-JSON MUST CONTAIN VALID JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_22(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 3
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_23(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_24(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    None,
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_25(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=None,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_26(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_27(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_28(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "XXInput error: --extracted-data-json must contain a JSON object.XX",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_29(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "input error: --extracted-data-json must contain a json object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_30(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "INPUT ERROR: --EXTRACTED-DATA-JSON MUST CONTAIN A JSON OBJECT.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_31(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 3
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_32(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = None
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_33(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["XXextracted_dataXX"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_34(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["EXTRACTED_DATA"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_35(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_36(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                None,
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_37(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=None,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_38(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_39(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_40(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "XXInput error: --update-stored requires at least one edit field.XX",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_41(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_42(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "INPUT ERROR: --UPDATE-STORED REQUIRES AT LEAST ONE EDIT FIELD.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_43(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 3

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_44(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = None
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_45(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory and MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_46(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = None
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_47(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(None)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_48(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is not None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_49(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print(None, file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_50(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=None)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_51(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print(file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_52(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", )
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_53(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("XXStored document not found.XX", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_54(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_55(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("STORED DOCUMENT NOT FOUND.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_56(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 2
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_57(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = None
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_58(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode=None)
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_59(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="XXpythonXX")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_60(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="PYTHON")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_61(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(None)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_62(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = None
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_63(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(None)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_64(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(None).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_65(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    None,
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_66(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=None,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_67(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=None,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_68(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_69(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_70(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_71(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "XX[1/1] Updating the stored document in local MongoDB...XX",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_72(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] updating the stored document in local mongodb...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_73(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] UPDATING THE STORED DOCUMENT IN LOCAL MONGODB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_74(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=False,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_75(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = None
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_76(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(None, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_77(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, None)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_78(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_79(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, )
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_80(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                None,
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_81(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=None,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_82(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_83(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_84(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "XXInput error: one or more document fields are invalid.XX",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_85(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_86(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "INPUT ERROR: ONE OR MORE DOCUMENT FIELDS ARE INVALID.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_87(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 3
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_88(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(None, file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_89(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=None)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_90(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_91(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", )
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_92(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 2
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_93(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is not None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_94(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print(None, file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_95(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=None)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_96(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print(file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_97(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", )
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_98(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("XXStored document not found.XX", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_99(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_100(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("STORED DOCUMENT NOT FOUND.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_101(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 2

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_102(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            None,
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_103(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=None,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_104(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=None,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_105(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_106(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_107(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_108(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "XX[1/1] Database update completed.XX",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_109(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_110(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] DATABASE UPDATE COMPLETED.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_111(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=False,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_112(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            None,
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_113(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            None,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_114(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_115(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_116(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(None),
            dependencies.stdout,
        )
        return 0

    def xǁStoredDocumentControllerǁupdate_stored__mutmut_117(
        self,
        document_id: str,
        *,
        document_type: str | None,
        summary: str | None,
        expiry_date: str | None,
        issue_date: str | None,
        extracted_data_json: str | None,
    ) -> int:
        """Validate and update selected fields of one stored document."""
        dependencies = self.dependencies
        changes: dict[str, Any] = {
            key: value
            for key, value in {
                "document_type": document_type,
                "summary": summary,
                "expiry_date": expiry_date,
                "issue_date": issue_date,
            }.items()
            if value is not None
        }
        if extracted_data_json is not None:
            try:
                extracted_data = json.loads(extracted_data_json)
            except json.JSONDecodeError:
                print(
                    "Input error: --extracted-data-json must contain valid JSON.",
                    file=dependencies.stderr,
                )
                return 2
            if not isinstance(extracted_data, dict):
                print(
                    "Input error: --extracted-data-json must contain a JSON object.",
                    file=dependencies.stderr,
                )
                return 2
            changes["extracted_data"] = extracted_data
        if not changes:
            print(
                "Input error: --update-stored requires at least one edit field.",
                file=dependencies.stderr,
            )
            return 2

        try:
            create_repository = (
                dependencies.repository_factory or MongoDocumentRepository.connect
            )
            with create_repository() as repository:
                current = repository.get_document_by_id(document_id)
                if current is None:
                    print("Stored document not found.", file=dependencies.stderr)
                    return 1
                updated_payload = current.document.model_dump(mode="python")
                updated_payload.update(changes)
                updated_data = type(current.document).model_validate(updated_payload)
                print(
                    "[1/1] Updating the stored document in local MongoDB...",
                    file=dependencies.stderr,
                    flush=True,
                )
                updated = repository.update_document(document_id, updated_data)
        except ValidationError:
            print(
                "Input error: one or more document fields are invalid.",
                file=dependencies.stderr,
            )
            return 2
        except (DatabaseConfigurationError, DatabaseError) as exc:
            print(f"Database update failed: {exc}", file=dependencies.stderr)
            return 1
        if updated is None:
            print("Stored document not found.", file=dependencies.stderr)
            return 1

        print(
            "[1/1] Database update completed.",
            file=dependencies.stderr,
            flush=True,
        )
        JsonResultSerializer.write(
            JsonResultSerializer.stored_document(updated),
            dependencies.stdout,
        )
        return 1

mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['_mutmut_orig'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_1'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_2'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_3'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_4'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_5'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_6'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_7'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_8'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_9'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_10'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_11'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_12'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_13'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_14'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_15'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_16'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_17'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_17 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_18'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_18 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_19'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_19 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_20'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_20 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_21'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_21 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_22'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_22 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_23'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_23 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_24'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_24 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_25'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_25 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_26'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_26 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_27'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_27 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_28'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_28 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_29'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_29 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_30'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_30 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_31'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_31 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁlist_stored__mutmut['xǁStoredDocumentControllerǁlist_stored__mutmut_32'] = StoredDocumentController.xǁStoredDocumentControllerǁlist_stored__mutmut_32 # type: ignore # mutmut generated

mutants_xǁStoredDocumentControllerǁget_stored__mutmut['_mutmut_orig'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_1'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_2'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_3'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_4'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_5'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_6'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_7'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_8'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_9'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_10'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_11'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_12'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_13'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_14'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_15'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_16'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_17'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_17 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_18'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_18 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_19'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_19 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_20'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_20 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_21'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_21 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_22'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_22 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_23'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_23 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_24'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_24 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_25'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_25 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_26'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_26 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_27'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_27 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_28'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_28 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_29'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_29 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_30'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_30 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_31'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_31 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_32'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_32 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_33'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_33 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_34'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_34 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_35'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_35 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_36'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_36 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_37'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_37 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_38'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_38 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_39'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_39 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_40'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_40 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_41'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_41 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_42'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_42 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_43'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_43 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_44'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_44 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁget_stored__mutmut['xǁStoredDocumentControllerǁget_stored__mutmut_45'] = StoredDocumentController.xǁStoredDocumentControllerǁget_stored__mutmut_45 # type: ignore # mutmut generated

mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['_mutmut_orig'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_1'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_2'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_3'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_4'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_5'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_6'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_7'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_8'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_9'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_10'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_11'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_12'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_13'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_14'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_15'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_16'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_17'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_17 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_18'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_18 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_19'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_19 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_20'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_20 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_21'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_21 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_22'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_22 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_23'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_23 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_24'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_24 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_25'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_25 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_26'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_26 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_27'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_27 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_28'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_28 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_29'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_29 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_30'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_30 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_31'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_31 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_32'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_32 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_33'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_33 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_34'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_34 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_35'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_35 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_36'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_36 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_37'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_37 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_38'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_38 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_39'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_39 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_40'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_40 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_41'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_41 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_42'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_42 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_43'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_43 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_44'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_44 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_45'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_45 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_46'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_46 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_47'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_47 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_48'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_48 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_49'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_49 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_50'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_50 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_51'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_51 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_52'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_52 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_53'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_53 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_54'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_54 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_55'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_55 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_56'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_56 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_57'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_57 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_58'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_58 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_59'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_59 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_60'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_60 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_61'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_61 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_62'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_62 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_63'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_63 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_64'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_64 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_65'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_65 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_66'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_66 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_67'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_67 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_68'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_68 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_69'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_69 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_70'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_70 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_71'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_71 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_72'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_72 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_73'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_73 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_74'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_74 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_75'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_75 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_76'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_76 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_77'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_77 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_78'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_78 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_79'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_79 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_80'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_80 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_81'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_81 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_82'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_82 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_83'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_83 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_84'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_84 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_85'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_85 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_86'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_86 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_87'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_87 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_88'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_88 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_89'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_89 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_90'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_90 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_91'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_91 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_92'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_92 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_93'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_93 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_94'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_94 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_95'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_95 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_96'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_96 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_97'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_97 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_98'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_98 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_99'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_99 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_100'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_100 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_101'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_101 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_102'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_102 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_103'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_103 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_104'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_104 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_105'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_105 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_106'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_106 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_107'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_107 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_108'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_108 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_109'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_109 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_110'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_110 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_111'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_111 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_112'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_112 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_113'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_113 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_114'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_114 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_115'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_115 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_116'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_116 # type: ignore # mutmut generated
mutants_xǁStoredDocumentControllerǁupdate_stored__mutmut['xǁStoredDocumentControllerǁupdate_stored__mutmut_117'] = StoredDocumentController.xǁStoredDocumentControllerǁupdate_stored__mutmut_117 # type: ignore # mutmut generated
