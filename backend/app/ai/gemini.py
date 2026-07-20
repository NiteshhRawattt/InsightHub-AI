from app.rag.embeddings import client
from app.core.config import settings


def generate_text(prompt: str) -> str:
    """
    Generate a text response using the configured Gemini model.
    """

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt,
    )

    return response.text