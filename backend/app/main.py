"""
InsightHub AI — FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings

# ── App Instance ─────────────────────────────────────────────
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="InsightHub AI — NotebookLM-inspired research assistant powered by Google Gemini",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# ── CORS Middleware ───────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Root Endpoint ────────────────────────────────────────────
@app.get("/", tags=["Root"])
async def root():
    """API root — returns service info."""
    return {
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "environment": settings.APP_ENV,
        "docs": "/docs",
    }


# ── Health Check ─────────────────────────────────────────────
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for Docker & AWS App Runner."""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "service": settings.APP_NAME},
    )


# ── TODO: Register Routers Here (added in future steps) ──────
# from app.api import chat, documents
# app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
# app.include_router(documents.router, prefix="/api/v1/documents", tags=["Documents"])
