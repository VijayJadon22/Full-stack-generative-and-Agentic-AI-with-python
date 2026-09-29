from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400,
)

chunks = text_splitter.split_documents(documents=docs)

# Vector embeddings for these chunks
# Gemini embeddings through OpenAI-compatible API
embedding_model = OpenAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    check_embedding_ctx_length=False,
    encoding_format="float",
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag2",
)

print("Indexing of documents done.")
