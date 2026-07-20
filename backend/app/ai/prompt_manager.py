def get_rag_prompt(context: str, question: str) -> str:
    """
    Build the prompt for document-based question answering.
    """

    return f"""
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