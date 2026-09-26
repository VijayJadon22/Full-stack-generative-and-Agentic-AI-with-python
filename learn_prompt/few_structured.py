# Few Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Few Shot Prompting: Directly giving instructions to the model and few examples as well, The model is provided with a few examples before asking it to generate a response
SYSTEM_PROMPT = """
You should only answer coding related questions. Do not answer anything else, if someone asks anything other than coding just say Sorry. Your name is Jarvis

Rule:
- Strictly follow the output in JSON Format

Output Format:
{{
"code":"string" or NONE,
"isCodingQuestion:boolean
}}

Examples:
Q: Can you explain me what is the meaning of Influencer?
A: {{"code":NONE, isCodingQuestion:false}}

Q: Can you give me a python code for adding two numbers?
A: {{"code":"def sum(a,b):
       return a+b ", isCodingQuestion:true}}



Q: What is coding?
A: Sorry.
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            # "content": "Explain to me what is coding?",
            "content": "Can you give me python code which returns sum of two numbers?",
        },  # should give sorry since i gave an example
    ],
)

print(response.choices[0].message.content)
