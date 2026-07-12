import requests

BASE_URL = "http://127.0.0.1:8000"


def get_tasks():
    """Fetch all tasks."""
    response = requests.get(f"{BASE_URL}/tasks")
    response.raise_for_status()
    return response.json()


def run_cortex():
    """Run the Cortex pipeline."""
    response = requests.post(f"{BASE_URL}/run-cortex")
    response.raise_for_status()
    return response.json()


def complete_task(task_id):
    """Mark a task as completed."""
    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        params={"status": "COMPLETED"}
    )
    response.raise_for_status()
    return response.json()