# ============================================================
#  InsightHub AI — Backend Dockerfile
#  Python 3.11 + FastAPI + Uvicorn
# ============================================================

FROM python:3.11-slim

# ── Labels ───────────────────────────────────────────────────
LABEL maintainer="InsightHub AI"
LABEL description="InsightHub AI FastAPI Backend"

# ── Environment ──────────────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# ── System Dependencies ──────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ── Working Directory ────────────────────────────────────────
WORKDIR /app

# ── Install Python Dependencies ──────────────────────────────
# Copy requirements first for Docker layer caching
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ── Copy Application Code ────────────────────────────────────
COPY . .

# ── Create Data Directories ──────────────────────────────────
RUN mkdir -p /app/data/chroma /app/data/uploads

# ── Expose Port ──────────────────────────────────────────────
EXPOSE 8000

# ── Health Check ─────────────────────────────────────────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# ── Start Server ─────────────────────────────────────────────
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
