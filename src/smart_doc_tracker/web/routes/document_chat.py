"""Local chat HTTP endpoints."""

import re
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import Response

from ...interfaces.document_repository import DocumentRepository
from ..schemas import ChatRequest, ChatResponse
from .context import WebRouteContext


def register_document_chat_routes(context: WebRouteContext) -> APIRouter:
    """Register the chat endpoints with explicit local services."""
    router = APIRouter()
    chat_service = context.chat_service
    chat_cancellation = context.chat_cancellation
    Repository = Annotated[DocumentRepository, Depends(context.repository)]

    @router.post("/api/chat", response_model=ChatResponse)
    def ask_documents(
        request: ChatRequest,
        repository: Repository,
    ) -> ChatResponse:
        """Answer from local document data and return validated citations."""
        return chat_service.answer(request, repository)

    @router.delete("/api/chat/requests/{request_id}", status_code=204)
    def cancel_chat_request(request_id: str) -> Response:
        """Discard an active or not-yet-started local chat answer."""
        if not re.fullmatch(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
            request_id,
        ):
            raise HTTPException(status_code=422, detail="Invalid request identifier.")
        chat_cancellation.cancel(request_id)
        return Response(status_code=204)

    @router.delete("/api/chat/conversations/{conversation_id}", status_code=204)
    def clear_chat_conversation(conversation_id: str) -> Response:
        """Forget one process-local chat conversation."""
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", conversation_id):
            raise HTTPException(
                status_code=422,
                detail="Invalid conversation identifier.",
            )
        chat_cancellation.clear(conversation_id)
        return Response(status_code=204)

    return router
