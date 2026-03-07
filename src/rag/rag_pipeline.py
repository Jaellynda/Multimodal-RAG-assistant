from src.llm.local_llm_client import generate_answer
from sentence_transformers import SentenceTransformer
from ..embeddings.vector_store import VectorStore
import numpy as np
import os
import pdfplumber


class RAGPipeline:

    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.vector_store = VectorStore(384)

    # ---------------------------
    # Document Processing
    # ---------------------------

    def load_pdfs_from_folder(self, folder="data/raw"):
        documents = []

        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                path = os.path.join(folder, file)

                with pdfplumber.open(path) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()

                        if text:
                            documents.append(text)

        return documents

    # ---------------------------
    # Build Knowledge Memory
    # ---------------------------

    def build_knowledge_base(self):

        docs = self.load_pdfs_from_folder()

        chunks = []

        for doc in docs:
            chunks.extend(self.chunk_text(doc))

        embeddings = self.embedder.encode(chunks)

        self.vector_store.add_embeddings(embeddings, chunks)

        print("Knowledge base built!")

    # ---------------------------
    # Query + Answer Generation ⭐
    # ---------------------------

    def ask(self, question):

        query_embedding = self.embedder.encode([question])[0]

        context_list = self.vector_store.search(query_embedding)

        context = "\n".join(context_list)

        answer = generate_answer(question, context)

        return answer

    # ---------------------------
    # Utilities
    # ---------------------------

    def chunk_text(self, text, chunk_size=500):
        return [
            text[i:i + chunk_size]
            for i in range(0, len(text), chunk_size)
        ]


if __name__ == "__main__":

    rag = RAGPipeline()
    rag.build_knowledge_base()

    while True:
        q = input("Ask a question: ")
        print(rag.ask(q))














      



