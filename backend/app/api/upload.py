from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil

from app.rag.extractor import extract_text_from_pdf
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings

router = APIRouter(tags=["Upload"])

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        text = extract_text_from_pdf(str(file_path))

        print("=" * 50)
        print("Extracted Text:")
        print(text[:1000])
        print("=" * 50)


        chunks = chunk_text(text)

        print(f"\nTotal Chunks Created: {len(chunks)}")

        for i, chunk in enumerate(chunks[:3], start=1):
            print(f"\n------ Chunk {i} ------")
            print(chunk)

        embeddings = generate_embeddings(chunks)

        print("\n" + "=" * 50)
        print(f"Total Embeddings Generated: {len(embeddings)}")

        if embeddings:
                print(f"Vector Dimension: {len(embeddings[0])}")

        print("=" * 50)

    return {
        "message": "PDF uploaded successfully!",
            "filename": file.filename
    }