import faiss
import numpy as np


class VectorStore:

    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = []

    def add_embeddings(self, embeddings, texts):
        """
        Store embeddings + corresponding documents.
        """

        self.index.add(np.array(embeddings).astype("float32"))

        self.documents.extend(texts)

    def search(self, query_embedding, k=3):
        """
        Semantic search retrieval.
        """

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            k
        )

        results = [self.documents[i] for i in indices[0]]

        return results


if __name__ == "__main__":
    print("Vector store ready")

