import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(
    path="app/chroma_db",
    settings=Settings(
        anonymized_telemetry=False
    )
)
# Create (or get existing) collection
collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(
    filename: str,
    chunks: list[str],
    embeddings: list[list[float]]
):
    """
    Store chunks and embeddings into ChromaDB.
    """

    ids = []
    metadatas = []

    for i in range(len(chunks)):
        ids.append(f"{filename}_{i}")

        metadatas.append({
            "filename": filename,
            "chunk": i
        })

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )