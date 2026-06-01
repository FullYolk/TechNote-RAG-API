import sqlite3
import json
from pathlib import Path
from datetime import datetime

current_dir = Path(__file__).parent
DB_PATH = current_dir / "app.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS query_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        answer TEXT NOT NULL,
        sources TEXT,
        latency_ms INTEGER,
        created_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def log_query(query:str, answer:str, sources:list, latency_ms:int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO query_logs(query, answer, sources, latency_ms, created_at)
        VALUES (?,?,?,?,?)
        """,
        (
            query,
            answer,
            json.dumps(sources, ensure_ascii=False),
            latency_ms,
            datetime.now().isoformat(timespec="seconds")
        )
    )
    conn.commit()
    conn.close()
