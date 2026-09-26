from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in biology expert and only answer questions related to human biology also answer in few word and be polite. if the query is not related to biology just say Sorry, i can only answer questiosn related to Bio",
        },
        {"role": "user", "content": "Explain to me how AI works in few words"},
        # {"role": "user", "content": "Explain what a synapse is?"},
    ],
)

print(response.choices[0].message.content)
