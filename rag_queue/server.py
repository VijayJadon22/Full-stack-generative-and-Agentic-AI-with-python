from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query

app = FastAPI()


@app.get("/")
def root():
    return {"Status": "Server is up and running"}


@app.post("/chat")
def chat(query: str = Query(..., description="The chat message of the user")):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "JOB ID": {job.id}}
