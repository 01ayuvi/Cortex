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

    briefing = []

    briefing.append("=" * 50)
    briefing.append("CORTEX DAILY BRIEFING")
    briefing.append("=" * 50)

    if not tasks:

        briefing.append("No tasks found.")

        briefing_text = "\n".join(briefing)

        return briefing_text

    briefing.append("")
    briefing.append("Tasks:")
    briefing.append("")

    for task in tasks:

        task_name = task[1]
        deadline = task[2]
        priority = task[3]

        briefing.append(
            f"[{priority}] {task_name}"
        )

        if deadline:

            briefing.append(
                f"Deadline: {deadline}"
            )

        briefing.append("")

    briefing_text = "\n".join(
        briefing
    )

    return briefing_text


if __name__ == "__main__":

    print(
        generate_briefing()
    )