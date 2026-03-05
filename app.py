from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from indexing import build_or_load_index
from reterival import rerank
from llm_layer import generate_answer
from feedback import store_feedback

app = FastAPI()
folder = Path("document")
vectorstore = build_or_load_index(folder)

class QuestionRequest(BaseModel):
    question: str

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    correct: bool

@app.post("/ask")
def ask_question(req: QuestionRequest):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    docs = retriever.invoke(req.question)
    reranked = rerank(req.question, docs)
    answer = generate_answer(req.question, reranked)
    return {"answer": answer}

@app.post("/feedback")
def feedback(req: FeedbackRequest):
    store_feedback(req.question, req.answer, req.correct)
    return {"status": "ok"}