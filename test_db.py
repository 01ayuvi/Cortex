from database.db import save_task, get_tasks

save_task(
    "Submit performance report",
    "Friday",
    "HIGH"
)

tasks = get_tasks()

for task in tasks:
    print(task)