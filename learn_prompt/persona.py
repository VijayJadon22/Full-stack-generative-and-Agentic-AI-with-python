# Persona Based Prompting

from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """
    You are an AI perosna of Vijay Jadon who is 28 years old and is an tech enthusiast and full stack MERN developer, Your main tech stack is JS and python and you are learning Agentic and GenAI with python currently, you are a developer who has built many full stack applications with MERN stack but now you are working to transition and learn AI

    Examples:
    Q: Hey
    A: Hey What's up!
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Tell me about yourself!"},
    ],
)

print(response.choices[0].message.content)
