"""
InsightHub AI — Document Pydantic Models
Placeholder schemas for document management.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import uuid


class DocumentMetadata(BaseModel):
    """Metadata attached to a processed document."""
    document_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str
    file_type: str = Field(..., description="pdf | docx | txt")
    file_size_bytes: int
    page_count: Optional[int] = None
    chunk_count: Optional[int] = None
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)


class DocumentUploadResponse(BaseModel):
    """Response returned after a successful document upload."""
    document_id: str
    filename: str
    message: str
    chunks_stored: Optional[int] = None


class DocumentListResponse(BaseModel):
    """List of all uploaded documents."""
    documents: List[DocumentMetadata]
    total: int
