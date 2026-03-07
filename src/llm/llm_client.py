import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(question, context):
    """
    Generate natural language answer using LLM.
    """

    prompt = f"""
You are an AI research assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{question}

Provide a clear, concise, helpful answer.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

