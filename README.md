# 🚀 DocuBrain AI: Enterprise-Grade RAG Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![LangChain](https://img.shields.io/badge/LangChain-Enabled-green) ![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal) ![License](https://img.shields.io/badge/License-MIT-yellow)

### Hardware-Optimized | Local-First Privacy | Multi-Format Support

DocuBrain AI is a high-performance **Retrieval-Augmented Generation (RAG)** system designed to chat with enterprise documents (PDF, CSV, Docx). Unlike standard RAG implementations, this system is **hardware-optimized to run smoothly on just 4GB of RAM** without compromising accuracy.

---

## ✨ Key Features

- **SHA256 Document Fingerprinting:** Automatic deduplication — if the same document is uploaded twice, the system detects it instantly and skips redundant indexing, saving compute and storage.
- **4GB RAM Optimization:** Uses lightweight embeddings and in-memory indexing for high-speed performance on standard hardware.
- **Zero Hallucination:** Strict system prompting ensures the AI only answers based on provided context — never fabricates information.
- **Source Tracking:** Real-time citations including **File Name** and **Page Number** for every response.
- **Local-First Privacy:** Document indexing (FAISS) stays on your local infrastructure; no data is sent for external model training.
- **Multi-Format Ingestion:** Seamlessly parses unstructured PDFs, Word docs, and structured CSV files.

---

## 🛠️ Tech Stack & Design Decisions

| Component | Tool | Why |
|---|---|---|
| Vector Store | FAISS | Tiny memory footprint, superior retrieval speed in low-resource environments |
| Embeddings | all-MiniLM-L6-v2 | 80MB model — high semantic accuracy with minimal CPU/RAM usage |
| Orchestration | LangChain | Modular RAG pipeline and document splitting |
| Backend | FastAPI | Scalable, asynchronous real-time query handling |
| UI | Streamlit | Lightweight, professional document interaction interface |
| LLM | Llama-3.3 via OpenRouter | Enterprise-grade reasoning and grounded response generation |

---

## 🏗️ Architecture Flow
```
Document Upload
      ↓
PyMuPDF / Docx2txt (Ingestion)
      ↓
SHA256 Fingerprint Check (Deduplication)
      ↓
800-char Chunking with Overlap
      ↓
MiniLM-L6 Embedding (Local)
      ↓
FAISS Vector Index
      ↓
Top-K Retrieval → LLM → Cited Answer
```

---

## 🚀 Quick Start

**1. Clone the repo:**
```bash
git clone https://github.com/YasraNafees/DocuBrain-AI.git
cd DocuBrain-AI
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set environment variables:**

Create a `.env` file:
```
OPENROUTER_API_KEY=your_key_here
```

**4. Run the application:**
```bash
# Start the backend
uvicorn api:app --reload

# Start the UI (new terminal)
streamlit run streamlit_app.py
```

---

## 📸 Demo

> *output folder*

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.
