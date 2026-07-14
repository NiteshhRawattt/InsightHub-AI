"""
InsightHub AI — Chat API Endpoints
Placeholder — implementation in next phase.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", summary="Chat service ping")
async def chat_ping():
    """Simple ping to verify the chat service is wired up."""
    return {"message": "Chat service ready", "status": "stub"}


# TODO: Implement in next phase:
# POST /api/v1/chat/         — Send a message, receive streaming response
# GET  /api/v1/chat/history  — Retrieve chat history for a session
# DELETE /api/v1/chat/{id}   — Delete a chat session
