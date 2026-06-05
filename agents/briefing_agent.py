import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
from database.db import get_tasks


def generate_briefing():

    tasks = get_tasks()

    print("\n")
    print("=" * 50)
    print("CORTEX DAILY BRIEFING")
    print("=" * 50)

    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:\n")

    for task in tasks:

        task_id = task[0]
        task_name = task[1]
        deadline = task[2]
        priority = task[3]

        print(f"[{priority}] {task_name}")

        if deadline:
            print(f"Deadline: {deadline}")

        print()


if __name__ == "__main__":
    generate_briefing()