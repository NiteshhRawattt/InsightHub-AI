# 🚀 InsightHub AI — Deployment Guide

## AWS App Runner

### Prerequisites
- AWS Account with App Runner access
- Docker image pushed to Amazon ECR (or direct GitHub connection)
- Your `GEMINI_API_KEY`

### Steps

#### 1. Push to ECR (Backend)
```bash
aws ecr create-repository --repository-name insighthub-backend
docker build -t insighthub-backend ./backend
docker tag insighthub-backend:latest <account>.dkr.ecr.<region>.amazonaws.com/insighthub-backend:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/insighthub-backend:latest
```

#### 2. Create App Runner Service
1. Go to **AWS App Runner** in the console
2. Click **Create service**
3. Source: **Container registry → Amazon ECR**
4. Select your `insighthub-backend` image
5. Port: `8000`

#### 3. Set Environment Variables
In the App Runner configuration, add:
| Key | Value |
|---|---|
| `GEMINI_API_KEY` | Your Gemini API key |
| `APP_ENV` | `production` |
| `BACKEND_CORS_ORIGINS` | `["https://your-frontend-domain.com"]` |
| `CHROMA_PERSIST_DIR` | `/app/data/chroma` |

#### 4. Deploy
Click **Create & deploy**. App Runner handles:
- Auto-scaling
- Load balancing
- HTTPS/SSL
- Health checks

---

## Docker Compose (Self-Hosted)

```bash
# Production deployment
docker-compose -f docker-compose.yml up -d --build

# View logs
docker-compose logs -f backend

# Stop
docker-compose down
```

---

## Environment Variables Reference

See [../.env.example](../.env.example) for the full list.
