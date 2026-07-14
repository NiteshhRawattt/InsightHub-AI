"""
InsightHub AI — ChromaDB Service
Placeholder — full implementation in next phase.
"""

# TODO: Implement in next phase:
#
# class DBService:
#     def __init__(self):
#         import chromadb
#         from app.core.config import settings
#         self.client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIR)
#         self.collection = self.client.get_or_create_collection(
#             name=settings.CHROMA_COLLECTION_NAME,
#             metadata={"hnsw:space": "cosine"},
#         )
#
#     def add_chunks(self, chunks: list[str], metadata: list[dict], ids: list[str]) -> None:
#         """Add text chunks + embeddings to ChromaDB."""
#         ...
#
#     def query(self, query_text: str, n_results: int = 5) -> list[dict]:
#         """Semantic search — returns top-N relevant chunks with metadata."""
#         ...
#
#     def delete_document(self, document_id: str) -> None:
#         """Remove all chunks belonging to a document."""
#         ...
