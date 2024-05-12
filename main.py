from model import model_pipe
from fastapi import FastAPI

app = FastAPI()

@app.post("/ask")
def ask(context: str, question: str):
    answer = model_pipe(context, question)
    return {"answer": answer}