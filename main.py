from pathlib import Path
from indexing import build_or_load_index
from reterival import rerank
from llm_layer import generate_answer
from feedback import store_feedback

folder = Path("document")
vectorstore = build_or_load_index(folder)

while True:
    q = input("Ask question (exit to quit): ")
    if q == "exit":
        break

    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    docs = retriever.invoke(q)

    reranked = rerank(q, docs)
    answer = generate_answer(q, reranked)

    print("\n", answer)
    # ---- Feedback Section ----
    fb = input("Was this answer correct? (y/n): ").lower()
    correct = True if fb == "y" else False
    store_feedback(q, answer, correct)