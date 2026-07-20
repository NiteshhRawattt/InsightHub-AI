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

    from app.ai.prompt_manager import get_rag_prompt

    prompt = get_rag_prompt(
        context=context,
        question=question,
    )

    from app.ai.gemini import generate_text

    ...

    return generate_text(prompt)