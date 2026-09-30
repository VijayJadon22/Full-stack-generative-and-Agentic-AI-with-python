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


@app.get("/jib-status")
def check_status(job_id: str = Query(..., description="Enter the job id")):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()
    return {"result": result}
