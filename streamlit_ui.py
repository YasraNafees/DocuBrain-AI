import streamlit as st
import time
from pathlib import Path
from indexing import build_or_load_index
from reterival import rerank
from llm_layer import generate_answer
from feedback import store_feedback

st.set_page_config(page_title="Enterprise chatbot", layout="wide")

st.title("📄 DocuBrain AI")

# ---------------------------
# Cache vectorstore
# ---------------------------
@st.cache_resource
def load_vectorstore():
    folder = Path("document")
    return build_or_load_index(folder)

vectorstore = load_vectorstore()

# ---------------------------
# Chat memory
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Show chat history
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# Streaming function
# ---------------------------
def stream_text(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.005)

# ---------------------------
# Chat input
# ---------------------------
q = st.chat_input("Ask something from your documents...")

if q:

    # show user message
    with st.chat_message("user"):
        st.markdown(q)

    st.session_state.messages.append(
        {"role": "user", "content": q}
    )

    # ---------------------------
    # Retrieval
    # ---------------------------
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    docs = retriever.invoke(q)

    selected_docs = rerank(q, docs)
    answer = generate_answer(q, selected_docs)

    # ---------------------------
    # Assistant response
    # ---------------------------
    with st.chat_message("assistant"):
        st.write_stream(stream_text(answer))

        col1, col2 = st.columns(2)

        if col1.button("👍", key=f"good_{len(st.session_state.messages)}"):
            store_feedback(q, answer, True)

        if col2.button("👎", key=f"bad_{len(st.session_state.messages)}"):
            store_feedback(q, answer, False)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
