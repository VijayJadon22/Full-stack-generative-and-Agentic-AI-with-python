from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return "Hello world!"


@app.get("/contact-us")
def contact_us():
    return "Thanks for reaching out, Hope you are doing well, email:'johndoe@gmail.com'"


@app.post("/chat")
def chat(message: str = Body(..., description="The Message")):
    response = client.chat(
        model="gemma:2b", messages=[{"role": "user", "content": message}]
    )

    return {"response": response.message.content}
