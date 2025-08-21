def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    """
    Splits text into overlapping chunks for processing.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks
