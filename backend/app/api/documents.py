"""
InsightHub AI — Documents API Endpoints
Placeholder — implementation in next phase.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", summary="Documents service ping")
async def documents_ping():
    """Simple ping to verify the documents service is wired up."""
    return {"message": "Documents service ready", "status": "stub"}


# TODO: Implement in next phase:
# POST   /api/v1/documents/upload  — Upload PDF, DOCX, or TXT file
# GET    /api/v1/documents/        — List all uploaded documents
# DELETE /api/v1/documents/{id}    — Delete a document and its embeddings
