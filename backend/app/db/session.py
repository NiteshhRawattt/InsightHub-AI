"""
InsightHub AI — Database Session

Provides SQLAlchemy sessions for FastAPI dependencies.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.db.database import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    class_=Session,
)


def get_db() -> Generator[Session, None, None]:
    """
    Provide a database session and close it after the request completes.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()