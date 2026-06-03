import sqlite3

conn = sqlite3.connect("cortex.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    deadline TEXT,
    priority TEXT
)
""")

def save_task(task, deadline, priority):

    cursor.execute(
        """
        INSERT INTO tasks (
            task,
            deadline,
            priority
        )
        VALUES (?, ?, ?)
        """,
        (task, deadline, priority)
    )

    conn.commit()

def get_tasks():

    cursor.execute(
        "SELECT * FROM tasks"
    )

    return cursor.fetchall()