from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
submissions = []                       # in-memory store, "for now"

class Submission(BaseModel):
    name: str
    age: int
    agree: bool
    flavor: str

@app.post("/submit")
def submit(s: Submission):
    submissions.append(s.model_dump())
    return {"stored": len(submissions)}

@app.get("/submissions")
def get_submissions():
    return submissions