"""
InsightHub AI — Chat Pydantic Models
Placeholder schemas for request/response validation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid


class ChatMessage(BaseModel):
    """A single message in a chat conversation."""
    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message text content")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ChatRequest(BaseModel):
    """Request body for sending a chat message."""
    session_id: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Unique session identifier"
    )
    message: str = Field(..., min_length=1, description="User's message")
    document_ids: Optional[List[str]] = Field(
        default=None,
        description="List of document IDs to query against"
    )
    stream: bool = Field(default=True, description="Enable streaming response")


class ChatResponse(BaseModel):
    """Response from the chat endpoint (non-streaming)."""
    session_id: str
    message: str
    sources: Optional[List[dict]] = None
    model: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
