"""
InsightHub AI — Database Engine

Creates the shared SQLAlchemy engine used by the application.
"""

from sqlalchemy import create_engine

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)