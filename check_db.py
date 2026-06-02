from langchain_chroma import Chroma
from embedding import get_embeddings
from pathlib import Path

PERSIST_DIR = str(Path(__file__).parent / "chroma_db")

def main():
    print("正在连接本地 Chroma 数据库...")
    db = Chroma(persist_directory=PERSIST_DIR, embedding_function=get_embeddings())
    
    # 获取库里所有的数据
    data = db.get()
    docs = data.get("documents", [])
    
    print(f"\n✅ 数据库中总共有 {len(docs)} 个 Chunk\n")
    
    print("--- 下面是库里所有 Chunk 的文本预览 ---")
    for i, text in enumerate(docs):
        # 把换行符换成空格，只截取前 80 个字看一眼
        preview = text.replace('\n', ' ')[:80]
        print(f"[{i+1}] {preview}...")
        if "全程Retrieval-Augmented" in text:
            print("    🎉 恭喜！找到 RAG 的定义文本了！")

if __name__ == "__main__":
    main()