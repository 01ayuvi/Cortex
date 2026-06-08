import sqlite3


def get_connection():

    return sqlite3.connect(
        "cortex.db",
        check_same_thread=False
    )


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    deadline TEXT,
    priority TEXT,
    category TEXT,
    status TEXT
    )
    """)

    conn.commit()
    conn.close()


initialize_database()


def save_task(
    task,
    deadline,
    priority,
    category,
    status="PENDING"
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO tasks (
        task,
        deadline,
        priority,
        category,
        status
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        task,
        deadline,
        priority,
        category,
        status
    )
)

    conn.commit()
    conn.close()


def get_tasks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks"
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def task_exists(task):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE task = ?",
        (task,)
    )

    exists = cursor.fetchone() is not None

    conn.close()

    return exists

def update_task_status(task_id, status):

    status = status.upper()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """,
        (status, task_id)
    )

    conn.commit()
    conn.close()