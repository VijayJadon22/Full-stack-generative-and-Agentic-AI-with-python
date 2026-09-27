# Chain of thought prompting

from dotenv import load_dotenv
from openai import OpenAI
import os

import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first plan what needs to be done, The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an ouput.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START ( where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to be displayed to user).

    OUTPUT JSON Format:
    {"step":"START" | "PLAN" | "OUTPUT", "content":"string" }

    EXAMPLE:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: {"step":"PLAN","content":"Seems like user is interseted in a math problem"}
    PLAN: {"step":"PLAN","content":"Looking at the problem, we should solve it using BODMAS method"}
    PLAN: {"step":"PLAN","content":"Yes the BODMAS is the correct method here."}
    PLAN: {"step":"PLAN","content":"first we must multiple 3*5 which is 15"}
    PLAN: {"step":"PLAN","content":"Now the new equation is 2+15/10"}
    PLAN: {"step":"PLAN","content":"Now we must divide 15 by 10 which is 1.5"}
    PLAN: {"step":"PLAN","content":"Now the new equation is 2+1.5 which is 3.5"}
    PLAN: {"step":"PLAN","content":"Great! we have solved the equation and the answer is 3.5"}
    OUTPUT: {"step":"OUTPUT","content":"3.5"}

"""

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "Hey write a code to add n numbers in js",
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "PLAN",
                    "content": "The user wants a JavaScript function to add 'n' numbers.",
                }
            ),
        },
        {
            "role": "user",
            "content": "Now continue with the next step.",
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "PLAN",
                    "content": "I will use the rest parameter syntax (...) in JavaScript to accept an arbitrary number of arguments.",
                }
            ),
        },
        {
            "role": "user",
            "content": "Now continue with the next step.",
        },
    ],
)

print(response.choices[0].message.content)
