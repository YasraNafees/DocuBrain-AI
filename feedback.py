import json
from pathlib import Path


FEEDBACK_FILE = Path("feedback.json")

def store_feedback(question: str, answer: str, correct: bool):
    
    if FEEDBACK_FILE.exists():
        feedback = json.loads(FEEDBACK_FILE.read_text())
    else:
        feedback = []
    feedback.append({
        "question": question,
        "answer": answer,
        "correct": correct
    })
    FEEDBACK_FILE.write_text(json.dumps(feedback, indent=2))