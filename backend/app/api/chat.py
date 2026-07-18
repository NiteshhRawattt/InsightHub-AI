"""
InsightHub AI — Chat API Endpoints
Placeholder — implementation in next phase.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.rag.rag_pipeline import generate_rag_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str


@router.get("/ping", summary="Chat service ping")
async def chat_ping():
    """Simple ping to verify the chat service is wired up."""
    return {"message": "Chat service ready", "status": "stub"}

@router.post("/")
async def chat(request: ChatRequest):

    print("Message received:", request.message)

    response = generate_rag_response(request.message)

    return JSONResponse(
    content={
        "reply": response
    }
)


# TODO: Implement in next phase:
# POST /api/v1/chat/         — Send a message, receive streaming response
# GET  /api/v1/chat/history  — Retrieve chat history for a session
# DELETE /api/v1/chat/{id}   — Delete a chat session
