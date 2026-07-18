from app.rag.embeddings import client
from app.rag.vector_store import collection


def retrieve_context(query: str, n_results: int = 3):
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
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    print("\n===== RAW CHROMADB RESPONSE =====")
    print(results)
    print("=================================\n")

    return results