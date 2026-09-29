from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


embedding_model = OpenAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    check_embedding_ctx_length=False,
    encoding_format="float",
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)


# Take user input
user_query = input("Ask Something: ")

search_results = vector_db.similarity_search(query=user_query)
# This search returns the relevant chunks from the vector db

context = "\n\n\n".join(
    [
        f"Page Content: {result.page_content}\n Page Number: {result.metadata['page_label']}\n File Location: {result.metadata['source']}"
        for result in search_results
    ]
)

SYSTEM_PROMPT = f"""
    You're an helpful assistant who answers users query based on the available context retrieved from a PDF file along with the page_contents and page number.

    You should only answer the user based on the following context and navigate the user to open the right page number to know more.

    Context:{context}
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)

print(response.choices[0].message.content)
