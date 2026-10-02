from dotenv import load_dotenv
import os
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
    model="gemini-3.5-flash-lite",
    model_provider="openai",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    # print("\n\n Inside chatbot node, state: ", state)
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
# START -> chatbot -> END


def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)


DB_URI = "mongodb://admin:admin@localhost:27017"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "vijay"}}

    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["Hi, What am i learning?"]}), config, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
