import chromadb
from chromadb.config import Settings

# Create (or reuse) persistent ChromaDB vector store in ./chromadb/
client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chromadb"))
collection = client.get_or_create_collection(name="material_submittals")

def store_embeddings(text_chunks, embeddings):
    """
    Store list of embeddings for given text chunks in ChromaDB collection.
    """
    metadatas = [{"chunk": chunk} for chunk in text_chunks]
    ids = [str(i) for i in range(len(text_chunks))]

    # Convert embeddings from numpy array to list if needed
    embeddings_list = embeddings.tolist() if hasattr(embeddings, "tolist") else embeddings

    collection.add(ids=ids, embeddings=embeddings_list, metadatas=metadatas)

def query_vector_store(query_embedding, k=3):
    """
    Returns the k most relevant chunks (metadatas) by similarity to query embedding.
    """
    # Convert numpy array to list before querying
    query_embedding_list = query_embedding.tolist() if hasattr(query_embedding, "tolist") else query_embedding

    results = collection.query(query_embedding_list, n_results=k)
    return results['metadatas']

