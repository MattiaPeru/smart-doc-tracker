"""CLI presentation for direct stored-document queries."""

from __future__ import annotations

from dataclasses import dataclass

from ..cli.dependencies import CliDependencies
from ..cli.serializer import JsonResultSerializer
from ..db.database import DatabaseConfigurationError, DatabaseError, MongoDocumentRepository


@dataclass(slots=True)
class StoredDocumentController:
    """Read stored documents and render query results for the CLI."""

    dependencies: CliDependencies

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
