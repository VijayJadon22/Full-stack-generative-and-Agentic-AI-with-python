from dotenv import load_dotenv
from mem0 import Memory
import os
from openai import OpenAI

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
        "config": {"host": "localhost", "port": 6333},
    },
}


mem_client = Memory.from_config(config)


while True:
    user_query = input("Enter your input: ")

    response = openai_client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages=[{"role": "user", "content": user_query}],
    )

    ai_response = response.choices[0].message.content
    print("AI Response: ", ai_response)

    mem_client.add(
        user_id="vijayjadon",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response},
        ],
    )

    print("Memory has been saved...")
