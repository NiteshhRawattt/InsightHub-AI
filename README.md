#  InsightHub AI

> A production-quality, AI research assistant powered by Google Gemini.

![InsightHub AI](https://img.shields.io/badge/InsightHub-AI-6366f1?style=for-the-badge&logo=google&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge)

---

##  Overview

**InsightHub AI** is a full-stack, AI-powered research assistant that lets you upload documents (PDF, DOCX, TXT), chat with your content, receive source citations, and explore multi-document knowledge — all in a beautiful dark-themed interface.

---

##  Features (Planned)

-  **Document Upload** — PDF, DOCX, TXT support
-  **AI Chat** — Google Gemini-powered conversational AI with streaming
-  **Source Citations** — Pinpoint exactly where answers come from
-  **Multi-Document Support** — Query across multiple files simultaneously
-  **Chat History** — Persistent session memory
-  **Semantic Search** — ChromaDB vector store for intelligent retrieval
-  **Streaming Responses** — Real-time AI output via Server-Sent Events
-  **Server-Side API Key** — Your Gemini key never leaves the server

---

##  Project Structure

```
InsightHub-AI/
├── backend/                    # Python FastAPI backend
│   ├── app/
│   │   ├── api/                # Route handlers
│   │   │   ├── __init__.py
│   │   │   ├── chat.py         # Chat & streaming endpoints
│   │   │   └── documents.py    # Document upload endpoints
│   │   ├── core/               # Config, settings, startup
│   │   │   ├── __init__.py
│   │   │   └── config.py       # App configuration (Pydantic Settings)
│   │   ├── models/             # Pydantic data models
│   │   │   ├── __init__.py
│   │   │   ├── chat.py         # Chat request/response schemas
│   │   │   └── document.py     # Document schemas
│   │   ├── services/           # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py   # Gemini AI integration
│   │   │   ├── db_service.py   # ChromaDB operations
│   │   │   └── doc_service.py  # Document processing
│   │   └── main.py             # FastAPI app entry point
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/                   # React + Vite + Tailwind CSS
│   ├── src/
│   │   ├── api/                # Axios API client
│   │   │   └── client.js
│   │   ├── components/
│   │   │   ├── ui/             # Base UI components (Button, Input, etc.)
│   │   │   ├── chat/           # Chat interface components
│   │   │   ├── documents/      # Document upload & list components
│   │   │   └── layout/         # Sidebar, Header, Shell
│   │   ├── hooks/              # Custom React hooks
│   │   │   └── useStream.js    # SSE streaming hook
│   │   ├── pages/              # Page-level components
│   │   │   ├── HomePage.jsx
│   │   │   └── ChatPage.jsx
│   │   ├── store/              # Zustand global state
│   │   │   └── useAppStore.js
│   │   ├── styles/
│   │   │   └── globals.css     # Tailwind base + custom styles
│   │   └── utils/              # Utility functions
│   │       └── format.js
│   ├── public/
│   │   └── favicon.svg
│   ├── Dockerfile
│   ├── index.html
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── package.json
│
├── docs/
│   └── deployment.md           # AWS App Runner deployment guide
│
├── docker-compose.yml          # Multi-service orchestration
├── .env.example                # Environment variable template
├── .gitignore
└── README.md
```

---

##  Quick Start

### Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose v2+
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- Node.js 18+ (for local frontend dev)
- Python 3.11+ (for local backend dev)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/InsightHub-AI.git
cd InsightHub-AI
```

### 2. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env — add your GEMINI_API_KEY
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

### 4. Local Development (Without Docker)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

##  Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key | ✅ |
| `GEMINI_MODEL` | Gemini model name | ✅ |
| `CHROMA_PERSIST_DIR` | ChromaDB storage directory | ✅ |
| `BACKEND_CORS_ORIGINS` | Allowed CORS origins (JSON array) | ✅ |
| `APP_ENV` | `development` or `production` | ✅ |
| `LOG_LEVEL` | Logging verbosity | Optional |
| `MAX_UPLOAD_SIZE_MB` | Max file upload size in MB | Optional |

---

##  Docker Architecture

```
docker-compose
├── backend   → Python FastAPI   (port 8000)
├── frontend  → React + Nginx    (port 5173)
└── chromadb  → ChromaDB server  (port 8001)
```

---

##  AWS App Runner

Ready for AWS App Runner deployment. See [docs/deployment.md](docs/deployment.md).

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite 5, Tailwind CSS v3 |
| Backend | Python 3.11, FastAPI |
| AI | Google Gemini 1.5 Pro |
| Vector DB | ChromaDB |
| Containers | Docker, Docker Compose |
| Cloud | AWS App Runner |

---

##  License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">Built using Google Gemini, FastAPI & React</div>
