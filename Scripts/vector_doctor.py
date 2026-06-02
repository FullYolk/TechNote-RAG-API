from embedding import get_embeddings
import numpy as np

def cos_sim(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

emb = get_embeddings()

# 准备3段文本：1是问题，2是真答案，3是完全无关的
q = "什么是RAG？"
correct_doc = "RAG，全程Retrieval-Augmented Generation(检索增强生成)。是一种结合了检索系统和生成式大模型的技术范式。"
unrelated_doc = "原神是由米哈游开发的一款开放世界冒险游戏"

print("正在调用 Embedding API...")
v_q = emb.embed_query(q)
v_correct = emb.embed_query(correct_doc)
v_unrelated = emb.embed_query(unrelated_doc)

print(f"\n✅ 向量维度: {len(v_q)}  (bge-m3 应该是 1024)")
print(f"✅ 向量模长: {np.linalg.norm(v_q):.4f}  (应该接近 1.0)")
print(f"✅ 前 3 个数字: {v_q[:3]}  (不应该全是 0)")

print("\n--- 关键诊断 (cosine similarity 越接近 1，相关性越高) ---")
print(f"问题 vs 正确答案 : {cos_sim(v_q, v_correct):.4f}  👉 应该 > 0.7")
print(f"问题 vs 原神描述 : {cos_sim(v_q, v_unrelated):.4f}  👉 应该 < 0.5")