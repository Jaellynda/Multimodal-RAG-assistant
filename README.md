# Multimodal-RAG-assistant
# This is a Multimodal RAG Research Assistant

A **local AI research assistant** that reads research papers (PDFs) and answers questions using **retrieval-augmented generation (RAG)** with a **local LLM (Llama 3 via Ollama)** — no API billing, fully local, fast, and research-ready.

---

## Project Overview

This project lets the user:

- Ingest research papers or PDFs  
- Convert text to embeddings and store in vector memory  
- Ask questions and retrieve answers in natural language  
- Interact via a clean web interface  

Inspired by the research paper:  
**“Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation”**  
[Zafeirios Fountas et al., 2024]

---

# Multimodal RAG Research Assistant

A lightweight Retrieval-Augmented Generation (RAG) system that allows users to ask questions about academic papers using a local large language model.

The system retrieves relevant document passages using semantic search and generates grounded answers using a locally hosted LLM.

---

# Motivation

Large language models can generate fluent answers but often hallucinate information when they lack grounding in real documents.

Retrieval-Augmented Generation (RAG) addresses this limitation by retrieving relevant knowledge from external documents before generating an answer.

This project explores how RAG systems can be used to build a research assistant capable of answering questions about academic papers.

---

# Research Inspiration

This project was inspired by the paper:

**"Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation"**

The paper proposes that the brain gradually forgets episodic details while retaining conceptual knowledge, allowing better generalization.

This RAG system simulates a similar process:

1. Documents are stored as embeddings  
2. Relevant knowledge is retrieved when needed  
3. The language model generates explanations using retrieved context  

In this way, the system behaves like a simplified artificial research assistant.

---

# Architecture

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

# Screenshots

## System Architecture

<img width="1113" height="597" alt="RAG architecture diagram" src="https://github.com/user-attachments/assets/3c2fb166-610e-46c6-ab14-eccf7606be11" />

## Example Interaction


<img width="1477" height="364" alt="Screenshot 2026-03-07 at 8 50 26 PM" src="https://github.com/user-attachments/assets/08d2c033-0baf-4fd1-864f-fbb0412b6bde" />

## API screenshot
<img width="946" height="760" alt="Screenshot 2026-03-07 at 8 51 26 PM" src="https://github.com/user-attachments/assets/f663232b-c570-472f-bdae-05a6bb699131" />


