from pathlib import Path
import logging
from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader, # Yeh sahi loader hai docx ke liye
    CSVLoader,
    TextLoader
)

def load_documents(folder: Path):
    all_docs = []
    # Folder check karein agar exist karta hai
    if not folder.exists():
        logging.error(f"Folder not found: {folder}")
        return []

    for file in folder.glob("*"):
        suffix = file.suffix.lower()
        file_path = str(file) # Windows path ko string mein convert kiya

        try:
            if suffix == ".pdf":
                loader = PyMuPDFLoader(file_path)
            elif suffix == ".docx":
                # Docx ke liye TextLoader nahi chalta, Docx2txtLoader chahiye
                loader = Docx2txtLoader(file_path)
            elif suffix == ".csv":
                # CSV ke liye encoding 'utf-8' ya 'latin1' check karein
                loader = CSVLoader(file_path, encoding="utf-8")
            elif suffix == ".txt":
                # Windows ki files ke liye utf-8 safe hai
                loader = TextLoader(file_path, encoding="utf-8")
            else:
                continue

            docs = loader.load()

            for d in docs:
                d.metadata["file_name"] = file.name
                d.metadata["file_type"] = suffix
                
                if suffix == ".pdf":
                    page = d.metadata.get("page", 0)
                    d.metadata["source"] = f"{file.name} - page {page+1}"
                else:
                    d.metadata["source"] = file.name

            all_docs.extend(docs)
            logging.info(f"Successfully loaded: {file.name}")

        except Exception as e:
            # Agar utf-8 fail ho jaye (Windows specific error), toh latin1 try karein
            logging.error(f"Failed loading {file.name}: {e}")
            continue

    return all_docs
