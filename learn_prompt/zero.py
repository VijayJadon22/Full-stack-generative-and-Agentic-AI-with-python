# Zero shot prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#Example of zero shot prompting
SYSTEM_PROMPT = "You should only answer coding related questions. Do not answer anything else, if someone asks anything other than coding just say Sorry. Your name is Jarvis"

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {"role": "user", "content": "Explain to me how Python works in few words"},
    ],
)

print(response.choices[0].message.content)
