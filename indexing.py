import hashlib
import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def folder_hash(folder: Path):
    meta = {}
    for f in sorted(folder.glob("*")):
        if f.is_file():
            meta[f.name] = f.stat().st_mtime
    return hashlib.sha256(json.dumps(meta).encode()).hexdigest()

def build_or_load_index(folder: Path):
    index_root = Path(".indices")
    index_root.mkdir(exist_ok=True)

    hash_key = folder_hash(folder)
    index_dir = index_root / hash_key

    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    if index_dir.exists():
        return FAISS.load_local(
            str(index_dir),
            embeddings,
            allow_dangerous_deserialization=True
        )

    from ingestion import load_documents
    docs = load_documents(folder)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    splits = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(splits, embeddings)

    index_dir.mkdir(parents=True)
    vectorstore.save_local(str(index_dir))

    return vectorstore