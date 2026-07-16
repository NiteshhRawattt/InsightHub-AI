from google import genai
from typing import Generator
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)
# print("===== AVAILABLE MODELS =====")

# for model in client.models.list():
#     print(model.name)

# print("============================")

# print("Model:", settings.GEMINI_MODEL)


def generate_response(message: str) -> str:
    prompt = f"""
Answer in clean Markdown.

Rules:
- Use # and ## headings
- Use bullet points
- Use **bold**
- Keep paragraphs short
- Do not output raw markdown symbols unnecessarily.

Question:
{message}
"""

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt,
    )

    return response.text


def generate_response_stream(message: str) -> Generator[str, None, None]:

    print(">>> generate_response_stream START")

    prompt = f"""
Answer in clean Markdown.

Rules:
- Use # and ## headings
- Use bullet points
- Use **bold**
- Keep paragraphs short

Question:
{message}
"""

    try:
        print("Using model:", settings.GEMINI_MODEL)
        print("About to call generate_content_stream()")
        stream = client.models.generate_content_stream(
           model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        print(">>> Stream created")

        for chunk in stream:
            print(">>> Chunk object:", chunk)

            if hasattr(chunk, "text") and chunk.text:
                print(">>> Chunk text:", repr(chunk.text))
                yield chunk.text

        print(">>> Stream finished")

    except Exception as e:
        import traceback

        print("FULL ERROR:")
        traceback.print_exc()
