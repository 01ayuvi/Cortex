import ollama
import json
import time
from memory.retrieval import retrieve_context
from config import OLLAMA_MODEL
from logging_config import logger

def normalize_task(task):

    if not task:
        return task

    task_lower = task.lower()

    if "recovery email" in task_lower:
        return "Verify account security"

    if "account change" in task_lower:
        return "Verify account security"

    if "security" in task_lower:
        return "Verify account security"

    if "account activity" in task_lower:
        return "Verify account security"

    return task.title()



def extract_task(email_text):

    context = retrieve_context(email_text)
    logger.info("Retrieved RAG context")

    prompt = f"""
You are Cortex AI.

You have access to previous related emails.

Related historical emails:

{context}

Current email:

{email_text}

Instructions:

- Determine if action is required.
- Extract the main task.
- Extract any deadline if present.
- Determine the most appropriate category.
- Use historical context only if relevant.
- Return ONLY valid JSON.
- No markdown.
- No explanations.
- No comments.

Schema:

{{
    "action_required": true,
    "task": "task description",
    "deadline": "deadline or null"
}}
"""

    try:

        start_time = time.time()

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        elapsed = time.time() - start_time

        logger.info(
    f"Ollama response received in {elapsed:.2f} seconds"
)

        content = response["message"]["content"]

        start = content.find("{")
        end = content.rfind("}") + 1
        if start == -1 or end == 0:
            raise ValueError("No JSON found in LLM response")
        json_text = content[start:end]

        task_data = json.loads(json_text)

        if task_data["task"]:

            task_data["task"] = normalize_task(
                task_data["task"]
            )

            task_data["category"] = detect_category(
                task_data["task"]
            )

        print(
            f"DEBUG: Retrieved Context -> {context[:200]}"
        )

        print(
            f"DEBUG: Extracted task -> {task_data}"
        )

        return task_data

    except Exception as e:

        logger.error(
    f"Task Extraction Error: {e}"
)

        return {
            "action_required": False,
            "task": None,
            "deadline": None,
            "category": "Other"
        }
    

def detect_category(task):

    task = task.lower()

    if "security" in task:
        return "Security"

    if "report" in task:
        return "Work"

    if "interview" in task:
        return "Recruitment"

    if "meeting" in task:
        return "Meetings"

    return "General"