"""
InsightHub AI — Chat API Endpoints
Placeholder — implementation in next phase.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.rag.rag_pipeline import generate_rag_response
from app.ai.task_engine import TaskEngine

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    selected_document: str | None = None


@router.get("/ping", summary="Chat service ping")
async def chat_ping():
    """Simple ping to verify the chat service is wired up."""
    return {"message": "Chat service ready", "status": "stub"}

@router.post("/")
async def chat(request: ChatRequest):

    print("Message received:", request.message)
    print("Selected document:", request.selected_document)

    response = TaskEngine.process(
        message=request.message,
        selected_document=request.selected_document,
    )

    return JSONResponse(
    content={
        "reply": response
    }
)


# TODO: Implement in next phase:
# POST /api/v1/chat/         — Send a message, receive streaming response
# GET  /api/v1/chat/history  — Retrieve chat history for a session
# DELETE /api/v1/chat/{id}   — Delete a chat session
