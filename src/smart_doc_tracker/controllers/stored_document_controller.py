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
