from app.rag.rag_pipeline import generate_rag_response
from app.ai.gemini import generate_text

TASK_KEYWORDS = {
    "qa": [
        "what",
        "who",
        "when",
        "where",
        "why",
        "how",
        "explain",
    ],
    "summary": [
        "summarize",
        "summary",
        "brief",
    ],
    "quiz": [
        "quiz",
        "mcq",
        "multiple choice",
        "questions",
    ],
    "translation": [
        "translate",
        "translation",
    ],
    "notes": [
        "notes",
        "note",
    ],
    "flashcards": [
        "flashcard",
        "flashcards",
    ],
    "mindmap": [
        "mind map",
        "mindmap",
    ],
    "rewrite": [
        "rewrite",
        "rephrase",
    ],
}

class TaskEngine:

    @staticmethod
    def detect_task(message: str) -> str:

        message = message.lower()

        for task, keywords in TASK_KEYWORDS.items():

            for keyword in keywords:

                if keyword in message:
                    return task

        return "qa"

    @staticmethod
    def process(
        message: str,
        selected_document: str | None = None,
    ) -> str:
        
        task = TaskEngine.detect_task(message)

        print("Detected Task:", task)

        # If a document is selected → use RAG
        if selected_document:
            return generate_rag_response(
                question=message,
                selected_document=selected_document,
            )

        # Otherwise → General Chat
        return generate_text(message)