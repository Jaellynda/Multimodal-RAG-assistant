# Multimodal-RAG-assistant
# Multimodal RAG Research Assistant

A **local AI research assistant** that reads research papers (PDFs) and answers questions using **Retrieval-Augmented Generation (RAG)** with a **local LLM (Llama 3 via Ollama)**.

No API billing. Fully local. Fast. Research-ready.

---

##  Quick Demo

![Demo](demo.gif)

Ask questions about research papers and receive grounded AI-generated explanations.

Example:

Question:
> How does predictive forgetting happen?

Answer:
> Predictive forgetting occurs when episodic details fade while conceptual knowledge is retained for better generalization.

---

##  Project Motivation

Large language models can generate fluent responses but often hallucinate when they lack grounding in real documents.

Retrieval-Augmented Generation (RAG) solves this by retrieving relevant knowledge from external documents before generating answers.

This project explores RAG as a research assistant for academic paper understanding.

---

## Research Inspiration

This project was inspired by:

**"Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation"**

The paper proposes that biological memory systems gradually forget episodic details while preserving semantic meaning to improve generalization.

This system mimics that behavior by:

1. Storing document knowledge as embeddings  
2. Retrieving relevant knowledge when needed  
3. Generating answers using retrieved context  

---

##  Architecture


The system follows a simple Retrieval-Augmented Generation pipeline.

1. A user submits a question through the web interface  
2. The FastAPI backend receives the request  
3. The RAG pipeline retrieves relevant document chunks from the vector store  
4. Retrieved context is passed to the language model  
5. The model generates a grounded answer based on the retrieved knowledge  

---

# System Flow

```text
User Question
     ↓
Web Interface (index.html)
     ↓
FastAPI Backend (src/api/server.py)
     ↓
RAG Pipeline (src/rag/rag_pipeline.py)
     ↓
Vector Store (FAISS embeddings)
     ↓
Local LLM (Llama 3 via Ollama)
     ↓
Answer Returned

---


```

---

# Tech Stack

## Backend

- Python  
- FastAPI  

## Vector Search

- FAISS  
- Sentence Transformers (`all-MiniLM-L6-v2`)

## Language Model

- Llama 3  
- Ollama (local inference)

## Frontend

- HTML  
- JavaScript  

## Document Processing

- pdfplumber  

---
## Project Structure


Multimodal-RAG-assistant
│
├── data/
│ └── raw/ # Research PDFs
│
├── src/
│ ├── api/
│ │ └── server.py # FastAPI backend
│ │
│ ├── rag/
│ │ └── rag_pipeline.py # RAG logic
│ │
│ ├── llm/
│ │ ├── llm_client.py
│ │ └── local_llm_client.py
│
├── web/
│ └── index.html # Web interface
│
├── requirements.txt
└── README.md


---

##  How Retrieval-Augmented Generation Works

RAG improves language model reliability by grounding responses in external knowledge sources.

This system works in three phases:

### 1. Document Processing
Research papers are loaded and split into smaller chunks.

### 2. Embedding & Storage
Each chunk is converted into vector embeddings using:

all-MiniLM-L6-v2

# Example Interaction

### Question

```
How does predictive forgetting happen?
```

### Answer

```
Predictive forgetting occurs when episodic details fade while
the conceptual gist of an experience is retained.
```

---

Embeddings are stored in a FAISS vector index.

### 3. Question Answering
When a user asks a question:

- The question is embedded
- FAISS retrieves the most relevant document passages
- The language model generates a grounded answer

This reduces hallucinations and improves factual accuracy.

---



# What I Learned

Through this project I learned:

- How Retrieval-Augmented Generation (RAG) systems work  
- How embeddings enable semantic search  
- How to build a FastAPI backend for AI applications  
- How to integrate a local LLM using Ollama  
- How to connect a web interface to an AI backend  

---

# Future Improvements

- Add chat memory for multi-turn conversations  
- Allow users to upload PDFs from the web interface  
- Implement streaming responses  
- Support reasoning across multiple papers  

---

## Research Context

This project was inspired by cognitive neuroscience research on memory consolidation and generalization efficiency.

Specifically:

- Predictive memory compression  
- Semantic abstraction of knowledge  



# Screenshots

## System Architecture

<img width="1113" height="597" alt="RAG architecture diagram" src="https://github.com/user-attachments/assets/3c2fb166-610e-46c6-ab14-eccf7606be11" />

## Example Interaction


<img width="1477" height="364" alt="Screenshot 2026-03-07 at 8 50 26 PM" src="https://github.com/user-attachments/assets/08d2c033-0baf-4fd1-864f-fbb0412b6bde" />

## API screenshot
<img width="946" height="760" alt="Screenshot 2026-03-07 at 8 51 26 PM" src="https://github.com/user-attachments/assets/f663232b-c570-472f-bdae-05a6bb699131" />

## License
MIT License

