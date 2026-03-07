from sentence_transformers import SentenceTransformer


def chunk_text(text, chunk_size=500):
    """
    Simple chunking by character length.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def generate_embeddings(text_list):
    """
    Generate embeddings for list of text chunks.
    """

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(text_list)

    return embeddings


if __name__ == "__main__":
    sample_text = "Test embedding pipeline"

    chunks = chunk_text(sample_text)

    emb = generate_embeddings(chunks)

    print("Chunks:", chunks)
    print("Embeddings shape:", emb.shape)

