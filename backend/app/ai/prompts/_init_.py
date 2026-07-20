from .qa import get_rag_prompt
from .summary import get_summary_prompt
from .quiz import get_quiz_prompt
from .notes import get_notes_prompt
from .flashcards import get_flashcards_prompt
from .mindmap import get_mindmap_prompt
from .translation import get_translation_prompt
from .rewrite import get_rewrite_prompt

PROMPT_BUILDERS = {
    "qa": get_rag_prompt,
    "summary": get_summary_prompt,
    "quiz": get_quiz_prompt,
    "notes": get_notes_prompt,
    "flashcards": get_flashcards_prompt,
    "mindmap": get_mindmap_prompt,
    "translation": get_translation_prompt,
    "rewrite": get_rewrite_prompt,
}