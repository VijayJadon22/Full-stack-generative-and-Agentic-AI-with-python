from dotenv import load_dotenv
from openai import OpenAI
import os
from mem0 import Memory
import json

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "gemini-embedding-2-preview",
            "api_key": os.getenv("GEMINI_API_KEY"),
        },
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "model": "gemini-3.5-flash-lite",
            "api_key": os.getenv("GEMINI_API_KEY"),
        },
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "embedding_model_dims": 768,
        },
    },
}

mem_client = Memory.from_config(config)

while True:
    user_query = input("Enter your input: ")

    search_memory = mem_client.search(
        query=user_query, filters={"user_id": "vijayjadon"}, limit=1
    )

    memories = [
        f"ID: {memory.get('id')}\nMemory: {memory.get('memory')}"
        for memory in search_memory.get("results", [])
    ]

    SYSTEM_PROMPT = f"""
        Here is the context about the user
        {json.dumps(memories)}
    """

    response = openai_client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ],
    )

    ai_response = response.choices[0].message.content
    print("AI Response: ", ai_response)

    result = mem_client.add(
        user_id="vijayjadon",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response},
        ],
    )

    print("Memory result:", result)

    print("Memory has been saved...")
