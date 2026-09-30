from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Status": "Server is up and running"}
