from fastapi import FastAPI, UploadFile, File
import shutil
import os

from .pdf_extractor import extract_text_from_pdf
from .text_chunker import chunk_text
from .embedding import get_embeddings
from .vector_store import store_embeddings
from .retrieval import retrieve_relevant_chunks
from .openai_client import generate_comment

app = FastAPI()

@app.post("/upload_pdf/")
async def process_pdf(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Text extraction and preprocessing
    text = extract_text_from_pdf(file_location)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)
    store_embeddings(chunks, embeddings)

    # Retrieval query (can make this user-configurable if desired)
    query = "Check for missing specifications and compliance"
    relevant_chunks = retrieve_relevant_chunks(query)
    comment_sheet = generate_comment(relevant_chunks)

    os.remove(file_location)
    return {"comment_sheet": comment_sheet}
