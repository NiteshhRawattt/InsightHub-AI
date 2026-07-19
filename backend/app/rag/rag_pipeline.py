from app.rag.embeddings import client
from app.rag.vector_store import collection
from app.core.config import settings


def retrieve_context(
    query: str,
    selected_document: str | None = None,
    n_results: int = 3,
):
    """
    Retrieve the most relevant chunks from ChromaDB.
    """

    # Generate embedding for the user's query
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
    )

    query_embedding = response.embeddings[0].values

    # Search ChromaDB
    if selected_document:
        results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where={"filename": selected_document},
    )
    else:
        results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

    print("\n===== RAW CHROMADB RESPONSE =====")
    print(results)
    print("=================================\n")

    return results

def generate_rag_response(
    question: str,
    selected_document: str | None = None,
):

    results = retrieve_context(
    question,
    selected_document,
)

    documents = results.get("documents", [])

    if not documents:
        return "No relevant information found."

    context = "\n\n".join(documents[0])

    prompt = f"""
You are an AI assistant answering questions ONLY from the provided document.

Document Context:
{context}

Question:
{question}

Rules:
- Answer only using the document context.
- If the answer is not present, reply:
  "The answer is not available in the uploaded document."
- Keep the answer clear and concise.
"""

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt,
    )
    return response.text