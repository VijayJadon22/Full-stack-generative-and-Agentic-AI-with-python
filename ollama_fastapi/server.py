from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello world!"


@app.get("/contact-us")
def contact_us():
    return "Thanks for reaching out, Hope you are doing well, email:'johndoe@gmail.com'"
