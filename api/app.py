from fastapi import FastAPI
from main import main
from database.db import get_tasks
from agents.briefing_agent import generate_briefing

app = FastAPI(
    title="Cortex API",
    description="AI-Powered Email Intelligence Backend",
    version="1.0"
)


@app.get("/")
def root():

    return {
        "message": "Cortex API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/run-cortex")
def run_cortex():

    result = main()

    return result


@app.get("/tasks")
def tasks():

    tasks = get_tasks()

    task_list = []

    for task in tasks:

        task_list.append({
            "id": task[0],
            "task": task[1],
            "deadline": task[2],
            "priority": task[3]
        })

    return task_list

@app.get("/briefing")
def briefing():

    return {
        "briefing": generate_briefing()
    }