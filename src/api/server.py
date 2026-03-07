
from fastapi import FastAPI  
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.rag.rag_pipeline import RAGPipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
rag = RAGPipeline()
rag.build_knowledge_base()


class Question(BaseModel):
    question: str


@app.get("/")
def read_root():
    return {"message": "RAG AI Assistant Running"}


@app.post("/ask")
def ask_question(q: Question):

    answer = rag.ask(q.question)

    return {
        "question": q.question,
        "answer": answer
    }

