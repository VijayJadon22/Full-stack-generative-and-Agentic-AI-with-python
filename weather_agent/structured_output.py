from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
import requests
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def run_command(cmd: str):
    result = os.system(cmd)

    if result == 0:
        return f"Command executed successfully. Exit code: {result}"

    return f"Command failed. Exit code: {result}"


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"


available_tools = {"get_weather": get_weather, "run_command": run_command}


SYSTEM_PROMPT = """
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first plan what needs to be done, The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an ouput.
    You can also call a tool if required from the list of available tools.
    For every tool call wait for the observe step which is the output from the called tool.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START ( where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to be displayed to user).

    OUTPUT JSON Format:
    {"step":"START" | "PLAN" | "OUTPUT" | "TOOL", "content":"string", "tool":"string","input":"string" }

    Available Tools:
    - get_weather(city:str): Takes city name as input and return the weather information about the city.
    - run_command(cmd:str): Takes a system linux command as string and executes the command on the user's system and returns the output from that command

    The user is running Windows.
    For run_command:
    - Use Windows-compatible commands.
    - Do not use Linux commands such as mkdir -p, touch, pwd, or rm.
    - Exit code 0 means the command succeeded.
    - A non-zero exit code means the command failed.
    - Never tell the user that a command succeeded if the tool returned a non-zero exit code.
    - If a command fails, analyze the failure and try another appropriate Windows command.

    EXAMPLE 1:
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

    EXAMPLE 2:
    START: What is the weather of gwalior?
    PLAN: {"step":"PLAN","content":"User wants to know the weather information of gwalior in india"}
    PLAN: {"step":"PLAN","content":"Lets see if we have any available tool from the list of available tools to fetch weather of gwalior"}
    PLAN: {"step":"PLAN","content":"Great! we have get_weather tool available for this query."}
    PLAN: {"step":"PLAN","content":"I need to call get_weather tool for gwalior as input for city."}
    PLAN: {"step":"TOOL", "tool":"get_weather", "input":"gwalior"}
    PLAN: {"step":"OBSERVE","tool":"get_weather", "output":"The weather of gwalior is cloudy with 20C"}
    PLAN: {"step":"PLAN","content":"Great! I got the weather info about gwalior"}
    OUTPUT: {"step":"OUTPUT","content":"The current weather in gwalior is 20 C with some cloudy sky."}

"""

print("\n\n\n")


class MyOutputFormat(BaseModel):
    step: str = Field(
        ...,
        description="The ID of the step. Example: It can be START, PLAN, OUTPUT, TOOL etc",
    )
    content: Optional[str] = Field(
        None, description="The optional string content for the step"
    )
    tool: Optional[str] = Field(None, description="The ID of the tool to call")
    input: Optional[str] = Field(None, description="The input params for the tool")


message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    },
]

while True:
    user_query = input("Hey what can i do for you? ")
    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.parse(
            model="gemini-3.5-flash-lite",
            response_format=MyOutputFormat,
            messages=message_history,
        )

        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})

        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("Starting the LLM loop: ", parsed_result.content)
            # Have to add this as gemini dosent expect the message history to system generated or role: assistant it needs the last message to be of user
            message_history.append(
                {"role": "user", "content": "Continue to the next step."}
            )
            continue

        if parsed_result.step == "PLAN":
            print("Thinking..:", parsed_result.content)
            # Have to add this as gemini dosent expect the message history to system generated or role: assistant it needs the last message to be of user
            message_history.append(
                {"role": "user", "content": "Continue to the next step."}
            )
            continue

        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"Tool Call: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"Tool Call: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append(
                {
                    "role": "user",
                    "content": json.dumps(
                        {
                            "step": "OBSERVE",
                            "tool": tool_to_call,
                            "input": tool_input,
                            "output": tool_response,
                        }
                    ),
                }
            )
            continue

        if parsed_result.step == "OUTPUT":
            print("Result:", parsed_result.content)
            break

    print("\n\n\n")
