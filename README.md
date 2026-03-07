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

## Architecture

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
