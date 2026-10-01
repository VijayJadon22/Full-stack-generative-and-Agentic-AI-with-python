from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from openai import OpenAI

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Main LLM
llm = init_chat_model(
    model="gemini-3.5-flash-lite",
    model_provider="openai",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Judge LLM
judge_llm = init_chat_model(
    model="gemini-3.1-pro-preview",
    model_provider="openai",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]


def chatbot(state: State):
    print("\n\n Chabot Node: ", state)
    response = llm.invoke(state["user_query"])
    return {**state, "llm_output": response.content}


def evaluate_response(state: State) -> Literal["chatbot_gemini_pro_node", "endnode"]:
    print("\n\n evaluate_response Node: ", state)
    if True:
        return "endnode"

    return "chatbot_gemini_pro_node"


def chatbot_gemini_pro_node(state: State):
    print("\n\n chatbot_gemini_pro_node Node: ", state)
    response = judge_llm.invoke(state["user_query"])
    return {**state, "llm_output": response.content}


def endnode(state: State):
    print("\n\n endnode Node: ", state)

    return state


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini_pro_node", chatbot_gemini_pro_node)
graph_builder.add_node("endnode", endnode)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini_pro_node", "endnode")
graph_builder.add_edge("endnode", END)

graph = graph_builder.compile()

updated_state = result = graph.invoke(State({"user_query": "Hey, what is 2+2?"}))
print("\n\n Updated state: ", updated_state)
