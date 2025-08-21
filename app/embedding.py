from sentence_transformers import SentenceTransformer

# Instantiate globally so model loads only once
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # free, fast, effective model

def get_embeddings(text_chunks):
    """
    Generates embeddings for a list of texts using a transformer model.
    """
    return embedding_model.encode(text_chunks, show_progress_bar=True)
