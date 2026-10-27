"""Coordinate cancellation and in-memory history for local document chat."""

import json
import logging
import secrets
from collections import OrderedDict
from collections.abc import Iterator
from contextlib import contextmanager
from threading import Event, Lock

from fastapi import HTTPException

from ..core.parser import DocumentParsingError
from ..db.database import DatabaseError
from ..db.vector_database import VectorDatabaseError
from ..infrastructure.ollama import (
    OllamaConfigurationError,
    OllamaConnectionError,
    OllamaResponseError,
)
from ..interfaces.document_repository import DocumentRepository
from ..interfaces.document_vector_index import DocumentVectorIndex
from ..interfaces.text_generator import TextGenerator
from ..models.rag import ConversationTurn
from ..pipeline import DocumentQuestionPipeline
from .chat_memory import TemporaryChatMemory
from .pending import PendingDocumentService
from .schemas import ChatDocumentReference, ChatRequest, ChatResponse


class ChatCancellation:
    """Coordinate cancellation and conversation memory across chat worker threads."""

    def __init__(self, memory: TemporaryChatMemory) -> None:
        """Keep cancellation state tied to one process-local memory store."""
        self._memory = memory
        self._lock = Lock()
        self._active: dict[str, tuple[str | None, Event]] = {}
        self._cancelled: OrderedDict[str, None] = OrderedDict()

    @contextmanager
    def track(
        self, request_id: str | None, conversation_id: str | None
    ) -> Iterator[Event]:
        """Track one request, including a cancellation received before it starts."""
        cancelled = Event()
        if request_id is not None:
            with self._lock:
                if request_id in self._cancelled:
                    cancelled.set()
                    del self._cancelled[request_id]
                self._active[request_id] = (conversation_id, cancelled)
        try:
            yield cancelled
        finally:
            if request_id is not None:
                with self._lock:
                    self._active.pop(request_id, None)

    def cancel(self, request_id: str) -> None:
        """Cancel an active request or remember an early cancellation briefly."""
        with self._lock:
            active = self._active.get(request_id)
            if active is not None:
                active[1].set()
            else:
                self._cancelled[request_id] = None
                if len(self._cancelled) > 1000:
                    self._cancelled.popitem(last=False)

    def clear(self, conversation_id: str) -> None:
        """Cancel active requests and forget one conversation atomically."""
        with self._lock:
            for active_conversation_id, cancelled in self._active.values():
                if active_conversation_id == conversation_id:
                    cancelled.set()
            self._memory.clear(conversation_id)

    def remember(
        self,
        conversation_id: str,
        cancelled: Event,
        turn: ConversationTurn,
    ) -> None:
        """Keep a completed exchange only if cancellation has not won the race."""
        with self._lock:
            if cancelled.is_set():
                raise HTTPException(status_code=409, detail="Chat request cancelled.")
            self._memory.remember(conversation_id, turn)


_LOGGER = logging.getLogger("smart_doc_tracker.web.app")


class DocumentChatService:
    """Answer document questions with local retrieval and bounded memory."""

    def __init__(
        self,
        vector_index: DocumentVectorIndex | None,
        generator: TextGenerator | None,
        pending_documents: PendingDocumentService,
        memory: TemporaryChatMemory,
        cancellation: ChatCancellation,
        debug: bool,
    ) -> None:
        """Bind local generation, conversation memory, and cancellation."""
        self._vector_index = vector_index
        self._generator = generator
        self._pending_documents = pending_documents
        self._memory = memory
        self._cancellation = cancellation
        self._debug = debug

    def answer(
        self, request: ChatRequest, repository: DocumentRepository
    ) -> ChatResponse:
        """Return a grounded local answer and validated document references."""
        question = request.question.strip()
        if not question:
            raise HTTPException(status_code=422, detail="The question cannot be empty.")
        if self._pending_documents.insertion_ids():
            raise HTTPException(
                status_code=503,
                detail="A document is still being inserted. Please try again shortly.",
            )
        with self._cancellation.track(
            request.request_id, request.conversation_id
        ) as cancelled:
            trace_id = request.request_id or secrets.token_hex(8)

            def trace(stage: str, details: dict[str, object]) -> None:
                """Write an opt-in, request-scoped trace to the local terminal."""
                if stage in {"semantic_results", "selected_context"}:
                    fragments = details.get("fragments", [])
                    if isinstance(fragments, list):
                        for fragment in fragments:
                            if not isinstance(fragment, dict):
                                continue
                            document_id = fragment.get("document_id")
                            if isinstance(document_id, str):
                                try:
                                    record = repository.get_document_by_id(document_id)
                                except DatabaseError:
                                    record = None
                                fragment["file_name"] = (
                                    record.source_file_name if record else None
                                )
                _LOGGER.info(
                    "Chat trace [%s] %s\n%s",
                    trace_id,
                    stage,
                    json.dumps(details, ensure_ascii=False, indent=2, default=str),
                )

            if cancelled.is_set():
                if self._debug:
                    trace(
                        "cancelled", {"message": "Request cancelled before processing."}
                    )
                raise HTTPException(status_code=409, detail="Chat request cancelled.")
            if self._debug:
                _LOGGER.info(
                    "Chat request accepted with local terminal tracing enabled."
                )
            else:
                _LOGGER.info("Chat request accepted; document contents are not logged.")
            history = (
                self._memory.history(request.conversation_id)
                if request.conversation_id is not None
                else ()
            )
            if self._debug:
                trace(
                    "request",
                    {
                        "question": question,
                        "conversation_id": request.conversation_id,
                        "history": [
                            {
                                "question": turn.question,
                                "answer": turn.answer,
                                "document_ids": list(turn.document_ids),
                            }
                            for turn in history
                        ],
                    },
                )
            try:
                _LOGGER.info("Chat request is using semantic retrieval and Ollama.")
                if self._vector_index is None or self._generator is None:
                    raise HTTPException(
                        status_code=503,
                        detail="The local document assistant is unavailable.",
                    )
                answer = DocumentQuestionPipeline(
                    self._vector_index,
                    self._generator,
                    trace=trace if self._debug else None,
                ).ask(question, history=history)
            except (
                DocumentParsingError,
                OllamaConfigurationError,
                OllamaConnectionError,
                OllamaResponseError,
                VectorDatabaseError,
            ) as exc:
                _LOGGER.error("Chat request failed with %s.", type(exc).__name__)
                if self._debug:
                    trace(
                        "error",
                        {"error_type": type(exc).__name__, "message": str(exc)},
                    )
                raise HTTPException(
                    status_code=503,
                    detail=_chat_error_detail(exc),
                ) from exc
            if cancelled.is_set():
                if self._debug:
                    trace(
                        "cancelled", {"message": "Request cancelled after generation."}
                    )
                raise HTTPException(status_code=409, detail="Chat request cancelled.")

            documents: list[ChatDocumentReference] = []
            for document_id in dict.fromkeys(answer.document_ids):
                record = repository.get_document_by_id(document_id)
                if record is not None:
                    documents.append(ChatDocumentReference.from_record(record))
            _LOGGER.info(
                "Chat request completed successfully (%s supporting documents).",
                len(documents),
            )
            if self._debug:
                trace(
                    "completed",
                    {
                        "answer": answer.answer,
                        "files": [item.model_dump() for item in documents],
                    },
                )
            if request.conversation_id is not None:
                self._cancellation.remember(
                    request.conversation_id,
                    cancelled,
                    ConversationTurn(
                        question=question,
                        answer=answer.answer,
                        document_ids=tuple(answer.document_ids),
                    ),
                )
            return ChatResponse(
                answer=answer.answer,
                claims=answer.claims,
                documents=documents,
                insufficient_information=answer.insufficient_information,
            )


def _chat_error_detail(exc: Exception) -> str:
    """Return a safe, actionable browser message for one local chat failure."""
    if isinstance(exc, OllamaConnectionError):
        return "The local Ollama service or language model is unavailable."
    if isinstance(exc, OllamaResponseError):
        return "The local Ollama service returned an invalid response."
    if isinstance(exc, VectorDatabaseError):
        return "The local document search could not be completed."
    if isinstance(exc, DocumentParsingError):
        return "The local model returned an invalid grounded answer."
    return "The local document assistant is not configured correctly."
