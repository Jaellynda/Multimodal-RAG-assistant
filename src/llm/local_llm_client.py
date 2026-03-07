import requests


def generate_answer(question, context):

    prompt = f"""
You are a research AI assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{question}

Provide a clear, simple answer.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

