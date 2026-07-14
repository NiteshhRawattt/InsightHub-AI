# ============================================================
#  InsightHub AI — Frontend Dockerfile
#  Node 20 Alpine — Dev server via Vite
# ============================================================

FROM node:20-alpine

# ── Labels ───────────────────────────────────────────────────
LABEL maintainer="InsightHub AI"
LABEL description="InsightHub AI React Frontend"

# ── Working Directory ────────────────────────────────────────
WORKDIR /app

# ── Install Dependencies ─────────────────────────────────────
# Copy package files first for Docker layer caching
COPY package.json package-lock.json* ./
RUN npm ci --prefer-offline

# ── Copy Source ──────────────────────────────────────────────
COPY . .

# ── Expose Port ──────────────────────────────────────────────
EXPOSE 5173

# ── Start Dev Server ─────────────────────────────────────────
CMD ["npm", "run", "dev"]

# ── Production Build (uncomment for prod image) ───────────────
# RUN npm run build
# FROM nginx:alpine
# COPY --from=0 /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
