"""
InsightHub AI — AI Service (Google Gemini)
Placeholder — full implementation in next phase.
"""

# TODO: Implement in next phase:
#
# class AIService:
#     def __init__(self):
#         import google.generativeai as genai
#         from app.core.config import settings
#         genai.configure(api_key=settings.GEMINI_API_KEY)
#         self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
#
#     async def stream_chat(self, message: str, context: str = "") -> AsyncGenerator[str, None]:
#         """Stream a Gemini response token by token via SSE."""
#         ...
#
#     async def generate_response(self, message: str, context: str = "") -> str:
#         """Generate a full (non-streaming) Gemini response."""
#         ...
