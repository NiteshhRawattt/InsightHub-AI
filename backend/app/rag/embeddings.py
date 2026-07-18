from google import genai

from app.core.config import settings


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_embeddings(texts: list[str]) -> list:
    """
    Generate embeddings for a list of text chunks using Gemini.
    """

    embeddings = []

    for text in texts:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
        )

        embeddings.append(response.embeddings[0].values)

    return embeddings