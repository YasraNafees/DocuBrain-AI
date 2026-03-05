markdown
# 🚀 DocuBrain AI: Enterprise-Grade RAG Chatbot
### Hardware-Optimized | Local-First Privacy | Multi-Format Support

DocuBrain AI is a high-performance **Retrieval-Augmented Generation (RAG)** system designed to chat with enterprise documents (PDF, CSV, Docx). Unlike standard RAG implementations, this system is **Hardware-Optimized to run smoothly on just 4GB of RAM** without compromising accuracy.

---

## ✨ Key Features
- **4GB RAM Optimization:** Uses lightweight embeddings and in-memory indexing for high-speed performance on standard hardware.
- **Zero Hallucination:** Strict system prompting ensures the AI only answers based on provided context.
- **Source Tracking:** Real-time citations including **File Name** and **Page Number** for every response.
- **Local-First Privacy:** Document indexing (FAISS) stays on your local infrastructure; no data is used for external model training.
- **Multi-Format Ingestion:** Seamlessly parses unstructured PDFs, Word docs, and structured CSV files.

---

## 🛠️ The Tech Stack & Why I Chose It
- **FAISS (Vector Store):** Chosen over ChromaDB for its tiny memory footprint and superior retrieval speed in low-resource environments.
- **Sentence-Transformers (all-MiniLM-L6-v2):** A strategic 80MB model that delivers high semantic accuracy with minimal CPU/RAM usage.
- **LangChain:** Used for modular orchestration of the RAG pipeline and document splitting.
- **FastAPI:** Provides a scalable, asynchronous backend for real-time query handling.
- **Streamlit:** A lightweight, professional UI for document interaction and feedback.
- **Llama-3.3 (via OpenRouter):** Integrated for enterprise-grade reasoning and professional response generation.

---

## 🏗️ Architecture Flow
1. **Ingestion:** Documents are loaded using `PyMuPDF` and `Docx2txt`.
2. **Chunking:** Text is split into 800-character segments with overlap to maintain context.
3. **Embedding:** `MiniLM-L6` converts text into semantic vectors locally.
4. **Indexing:** `FAISS` stores and organizes vectors for lightning-fast retrieval.
5. **Generation:** Top relevant chunks are sent to the LLM to generate a cited, grounded answer.

---

## 🚀 How to Run

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/YasraNafees/DocuBrain-AI.git
   cd DocuBrain-AI
Use code with caution.

Install Dependencies:
bash
pip install -r requirements.txt
Use code with caution.

Set Environment Variables:
Create a .env file and add your OPENROUTER_API_KEY.
Run the Application:
bash
# Start the Backend
uvicorn api:app --reload

# Start the UI (In a new terminal)
streamlit run streamlit_app.py
Use code with caution.

💼 Remote Opportunities
I specialize in building cost-effective, private, and optimized AI solutions for businesses. If you are looking for an AI Developer who understands hardware constraints and data privacy, let's connect!
Contact:https://www.linkedin.com/in/yasranafees/


