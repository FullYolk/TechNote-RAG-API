import shutil
from split_docs import split_documents
from langchain_chroma import Chroma
from pathlib import Path
from embedding import get_embeddings


current_dir = Path(__file__).parent
PERSIST_DIR = str(current_dir/"chroma_db")

def rebuild_vectorstore():
    persist_path = Path(PERSIST_DIR)
    if persist_path.exists():
        shutil.rmtree(PERSIST_DIR)
    chunks = split_documents()
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=PERSIST_DIR
    )
    return {"chunk_count":len(chunks), "message":"重建成功"}
