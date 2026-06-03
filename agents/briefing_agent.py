import ollama

def generate_briefing(tasks_json):

    prompt = f"""
You are Cortex.

Create a professional morning briefing.

Tasks:
{tasks_json}

Format:

Good Morning

High Priority Items:
...

Tasks:
...

Deadlines:
...
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    sample_tasks = [
        {
            "priority": "HIGH",
            "task": "Submit performance report",
            "deadline": "Friday"
        },
        {
            "priority": "HIGH",
            "task": "Reply to recruiter",
            "deadline": None
        }
    ]

    briefing = generate_briefing(sample_tasks)

    print(briefing)