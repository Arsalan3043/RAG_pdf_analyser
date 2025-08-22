from .embedding import embedding_model
from .vector_store import query_vector_store

def retrieve_relevant_chunks(query: str, top_k: int = 3):
    """
    Encode query and fetch the top-k relevant document chunks.
    Handles dicts, lists, and strings for robust compatibility.
    """
    query_emb = embedding_model.encode([query])
    results = query_vector_store(query_emb, k=top_k)

    chunks = []
    for meta in results:
        if isinstance(meta, str):
            # Already a string
            chunks.append(meta)
        elif isinstance(meta, dict) and 'chunk' in meta:
            chunks.append(meta['chunk'])
        elif isinstance(meta, (list, tuple)):
            # Take first string if it's a list
            for item in meta:
                if isinstance(item, str):
                    chunks.append(item)
                elif isinstance(item, dict) and 'chunk' in item:
                    chunks.append(item['chunk'])
    return chunks
