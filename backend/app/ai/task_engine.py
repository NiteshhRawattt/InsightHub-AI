from app.rag.rag_pipeline import get_document_context
from app.ai.prompt_manager import get_rag_prompt
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

        if selected_document:

            context = get_document_context(
                question=message,
                selected_document=selected_document,
            )

            if context is None:
                return "No relevant information found."

            prompt = get_rag_prompt(
                context=context,
                question=message,
            )

            return generate_text(prompt)

# Otherwise → General Chat
        return generate_text(message)