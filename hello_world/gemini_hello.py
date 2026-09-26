from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interactions = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="Explain what is LLM and what are transformers in a few word",
)

print(interactions.output_text)
