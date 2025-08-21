from .embedding import embedding_model
from .vector_store import query_vector_store

def retrieve_relevant_chunks(query: str, top_k: int = 3):
    """
    Encode query and fetch the top-k relevant document chunks.
    """
    query_emb = embedding_model.encode([query])
    results = query_vector_store(query_emb, k=top_k)
    return [meta['chunk'] for meta in results]
