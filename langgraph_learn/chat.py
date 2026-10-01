from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    print("\n\n Inside chatbot node, state: ", state)
    return {"messages": ["Hi, this is a message from chatbot node"]}


def samplenode(state: State):
    print("\n\n Inside sample node, state: ", state)
    return {"messages": ["Hi, this message is from sample node"]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)
# START -> chatbot -> samplenode -> END

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, my name is vijay jadon"]}))
print("\n\n Updated State: ", updated_state)
