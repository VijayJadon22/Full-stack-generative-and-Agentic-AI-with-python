from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END

load_dotenv()

# Main LLM
llm = init_chat_model(
    model="gemini-3.5-flash-lite",
    model_provider="openai",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Judge LLM
judge_llm = init_chat_model(
    model="gemini-3.5-flash-lite",
    model_provider="openai",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Improvement LLM
improvement_llm = init_chat_model(
    model="gemini-3.5-flash-lite",
    model_provider="openai",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]


# --------------------------------------------------
# 1. Main Chatbot Node
# --------------------------------------------------
def chatbot(state: State):
    print("\n\n Chatbot Node: ", state)
    response = llm.invoke(state["user_query"])
    return {**state, "llm_output": response.content}


# --------------------------------------------------
# 2. Judge Node
# --------------------------------------------------
def judge_node(state: State):
    print("\n\n Judge Node: ", state)
    judge_prompt = f"""
    - You're an ai evaluator, your job is to evaluate the response given by the LLM to the user's query and evaluate if it is accurate or not

    User Question:
    {state["user_query"]}

    AI Generated Answer:
    {state["llm_output"]}

    Return ONLY one word:

    TRUE
    if the answer is correct and sufficiently answers the question.

    FALSE
    if the answer is incorrect, incomplete, irrelevant, or misleading.

    Do not provide any explanation.
    Return only TRUE or FALSE.
    """
    response = judge_llm.invoke(judge_prompt)
    judge_result = response.content.strip().upper()

    # Converting the LLM's text into a Python boolean
    is_good = judge_result == "TRUE"

    print("is_good:", is_good)

    return {**state, "is_good": is_good}


# --------------------------------------------------
# 3. Conditional Router
# --------------------------------------------------
def evaluate_response(state: State) -> Literal["endnode", "improvement_node"]:
    print("\n\n===== EVALUATE RESPONSE =====")
    print("is_good:", state["is_good"])

    if state["is_good"]:
        print("Answer is GOOD → Going to END")
        return "endnode"

    print("Answer is NOT GOOD → Going to IMPROVEMENT")
    return "improvement_node"


# --------------------------------------------------
# 4. Improvement Node
# --------------------------------------------------
def improvement_node(state: State):
    print("\n\n===== IMPROVEMENT NODE =====")

    improvement_prompt = f"""
        You need to provide a better answer to the user's question.

        User Question:
        {state["user_query"]}

        Previous AI Answer:
        {state["llm_output"]}

        The previous answer was judged incorrect or insufficient.

        Generate a corrected and better answer.

        Return only the final answer to the user.
        Do not mention the evaluation process.
        """

    response = improvement_llm.invoke(improvement_prompt)
    print("Improved Answer:", response.content)
    return {**state, "llm_output": response.content}


# --------------------------------------------------
# 5. End Node
# --------------------------------------------------
def endnode(state: State):
    print("\n\n===== END NODE =====")
    print("Final Answer:", state["llm_output"])

    return state


# --------------------------------------------------
# Build LangGraph
# --------------------------------------------------

graph_builder = StateGraph(State)

# Nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("judge_node", judge_node)
graph_builder.add_node("improvement_node", improvement_node)
graph_builder.add_node("endnode", endnode)

# edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "judge_node")
graph_builder.add_conditional_edges("judge_node", evaluate_response)
graph_builder.add_edge("improvement_node", "endnode")
graph_builder.add_edge("endnode", END)

# Compile graph
graph = graph_builder.compile()

user_input = input("Enter your query: ")
updated_state = graph.invoke(State({"user_query": user_input}))

print("\n\n Updated State: ", updated_state)
