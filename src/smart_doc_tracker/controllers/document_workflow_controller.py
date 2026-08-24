"""Dispatch CLI arguments to focused document workflow controllers."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from ..cli.dependencies import CliDependencies
from ..controllers.document_processing_controller import DocumentProcessingController
from ..controllers.expiration_workflow_controller import ExpirationWorkflowController
from ..controllers.inbox_workflow_controller import InboxWorkflowController
from ..controllers.stored_document_controller import StoredDocumentController


@dataclass(slots=True)
class DocumentWorkflowController:
    """Select the focused controller for one parsed CLI operation."""

    dependencies: CliDependencies

    def execute(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )

        days_threshold = args.days_threshold if args.days_threshold is not None else 30
        if args.check_expirations:
            return ExpirationWorkflowController(
                self.dependencies
            ).check_expirations(days_threshold)
        if args.monitor_expirations:
            return ExpirationWorkflowController(
                self.dependencies
            ).monitor_expirations(days_threshold, check_time=args.check_time)
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.image is None and args.days_threshold is not None:
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(args)
        if args.image is None:
            print("Input error: an image path is required.", file=self.dependencies.stderr)
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)
