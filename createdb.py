import sqlite3

conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    dept TEXT
)
""")
conn.commit()
conn.close()
