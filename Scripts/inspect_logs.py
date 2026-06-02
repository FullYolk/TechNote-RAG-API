import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "app.db"

def main():
    if not DB_PATH.exists():
        print("❌ 数据库文件不存在！")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, query, latency_ms, created_at 
    FROM query_logs 
    ORDER BY id DESC LIMIT 5
    """)
    rows = cursor.fetchall()
    
    print("\n✅ 最近 5 条 RAG 访问日志：")
    for row in rows:
        print(f"[{row[3]}] ID:{row[0]} | 耗时:{row[2]}ms | 问题: {row[1]}")
    conn.close()

if __name__ == "__main__":
    main()