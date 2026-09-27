# Chain of thought prompting automated with a loop

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

print("\n\n\n")

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    },
]

user_query = input("Hey Type Something: ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        response_format={"type": "json_object"},
        messages=message_history,
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    # Have to add this as gemini dosent expect the message history to system generated or role: assistant it needs the last message to be of user
    message_history.append({"role": "user", "content": "Continue to the next step."})
    parsed_result = json.loads(raw_result)

    if parsed_result["step"] == "START":
        print("Starting the LLM loop: ", parsed_result["content"])
        continue

    if parsed_result["step"] == "PLAN":
        print("Thinking..:", parsed_result["content"])
        continue

    if parsed_result["step"] == "OUTPUT":
        print("Result:", parsed_result["content"])
        break

print("\n\n\n")
