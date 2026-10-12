"""Dispatch CLI arguments to focused document workflow controllers."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from ..cli.dependencies import CliDependencies
from ..controllers.document_processing_controller import DocumentProcessingController
from ..controllers.expiration_workflow_controller import ExpirationWorkflowController
from ..controllers.inbox_workflow_controller import InboxWorkflowController
from ..controllers.rag_workflow_controller import RagWorkflowController
from ..controllers.stored_document_controller import StoredDocumentController


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut: MutantDict = {}  # type: ignore


@dataclass(slots=True)
class DocumentWorkflowController:
    """Select the focused controller for one parsed CLI operation."""

    dependencies: CliDependencies

    @_mutmut_mutated(mutants_xǁDocumentWorkflowControllerǁexecute__mutmut)
    def execute(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_orig(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_1(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(None).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_2(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_3(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                None
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_4(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(None).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_5(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_6(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                None,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_7(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=None,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_8(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=None,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_9(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=None,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_10(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=None,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_11(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=None,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_12(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_13(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_14(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_15(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_16(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_17(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_18(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(None).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_19(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            None
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_20(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_21(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                None,
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_22(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=None,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_23(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_24(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_25(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "XXInput error: document edit fields require --update-stored.XX",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_26(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_27(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "INPUT ERROR: DOCUMENT EDIT FIELDS REQUIRE --UPDATE-STORED.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_28(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 3
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_29(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_30(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(None)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_31(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(None).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_32(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = None
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_33(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                None
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_34(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(None).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_35(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                None, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_36(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=None
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_37(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_38(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_39(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(None).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_40(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(None)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_41(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(None).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_42(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline and (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_43(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None or args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_44(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is not None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_45(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_46(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                None
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_47(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(None).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_48(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is not None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_49(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                None, file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_50(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=None
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_51(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_52(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_53(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "XXInput error: an image path is required.XX", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_54(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_55(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "INPUT ERROR: AN IMAGE PATH IS REQUIRED.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_56(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 3
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_57(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store or not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_58(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_59(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                None,
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_60(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=None,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_61(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_62(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_63(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "XXInput error: --store requires --structured.XX",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_64(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_65(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "INPUT ERROR: --STORE REQUIRES --STRUCTURED.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_66(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 3
        return DocumentProcessingController(self.dependencies).process_document(args)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_67(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(self.dependencies).process_document(None)

    def xǁDocumentWorkflowControllerǁexecute__mutmut_68(self, args: argparse.Namespace) -> int:
        """Dispatch parsed arguments without implementing document operations."""
        if args.list_stored:
            return StoredDocumentController(self.dependencies).list_stored()
        if args.get_stored is not None:
            return StoredDocumentController(self.dependencies).get_stored(
                args.get_stored
            )
        if args.update_stored is not None:
            return StoredDocumentController(self.dependencies).update_stored(
                args.update_stored,
                document_type=args.document_type,
                summary=args.summary,
                expiry_date=args.expiry_date,
                issue_date=args.issue_date,
                extracted_data_json=args.extracted_data_json,
            )
        if any(
            value is not None
            for value in (
                args.document_type,
                args.summary,
                args.expiry_date,
                args.issue_date,
                args.extracted_data_json,
            )
        ):
            print(
                "Input error: document edit fields require --update-stored.",
                file=self.dependencies.stderr,
            )
            return 2
        if args.ask_documents is not None:
            return RagWorkflowController(self.dependencies).ask_documents(args)

        days_threshold = args.days_threshold
        if args.check_expirations:
            return ExpirationWorkflowController(self.dependencies).check_expirations(
                days_threshold
            )
        if args.monitor_expirations:
            return ExpirationWorkflowController(self.dependencies).monitor_expirations(
                days_threshold, check_time=args.check_time
            )
        if args.process_inbox:
            return InboxWorkflowController(self.dependencies).process_inbox(args)
        if args.complete_pipeline or (
            args.image is None and args.days_threshold is not None
        ):
            return InboxWorkflowController(self.dependencies).run_complete_pipeline(
                args
            )
        if args.image is None:
            print(
                "Input error: an image path is required.", file=self.dependencies.stderr
            )
            return 2
        if args.store and not args.structured:
            print(
                "Input error: --store requires --structured.",
                file=self.dependencies.stderr,
            )
            return 2
        return DocumentProcessingController(None).process_document(args)

mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['_mutmut_orig'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_1'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_2'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_3'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_4'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_5'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_6'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_7'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_8'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_9'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_10'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_11'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_12'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_13'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_14'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_15'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_16'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_17'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_18'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_19'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_20'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_21'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_22'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_23'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_24'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_25'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_26'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_27'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_28'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_29'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_30'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_31'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_32'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_33'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_34'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_35'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_36'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_37'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_38'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_39'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_40'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_41'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_42'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_43'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_44'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_45'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_46'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_47'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_48'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_49'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_50'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_51'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_52'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_53'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_54'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_55'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_56'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_57'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_58'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_59'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_60'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_61'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_62'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_63'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_64'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_65'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_66'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_67'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDocumentWorkflowControllerǁexecute__mutmut['xǁDocumentWorkflowControllerǁexecute__mutmut_68'] = DocumentWorkflowController.xǁDocumentWorkflowControllerǁexecute__mutmut_68 # type: ignore # mutmut generated
