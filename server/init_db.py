import sqlite3
from pathlib import Path
from config import DB_PATH

schema=Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
with sqlite3.connect(DB_PATH) as conn:
    conn.executescript(schema)
print(f"Initialized: {DB_PATH}")
