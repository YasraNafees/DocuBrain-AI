import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

LLM_MODEL = "meta-llama/llama-3.3-70b-instruct:free"

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BSE_URL"),
    model=LLM_MODEL,
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Answer ONLY from context. If answer not in context say 'These provided context is not available'. "
     "Cite sources clearly."),
    ("human",
     "Question: {question}\n\nContext:\n{context}")
])

def generate_answer(question, docs):
    context = "\n\n".join(
        f"Source: {d.metadata.get('source')}\n{d.page_content}"
        for d in docs
    )

    response = llm.invoke(
        prompt.format(question=question, context=context)
    )

    return response.content