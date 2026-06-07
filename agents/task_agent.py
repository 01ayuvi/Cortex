import ollama
import json
import time


def extract_task(email_text):

    prompt = f"""
You are a JSON API.

Rules:
- Return ONLY valid JSON
- No explanation
- No markdown
- No comments
- No extra text

Schema:

{{
    "action_required": true,
    "task": "task description",
    "deadline": "deadline or null"
}}

Email:
{email_text}
"""

    try:

        start_time = time.time()

        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        elapsed = time.time() - start_time

        print(
            f"DEBUG: Ollama response received in {elapsed:.2f} seconds"
        )

        content = response["message"]["content"]

        start = content.find("{")
        end = content.rfind("}") + 1

        json_text = content[start:end]

        task_data = json.loads(json_text)

        print(
            f"DEBUG: Extracted task -> {task_data}"
        )

        return task_data

    except Exception as e:

        print(
            f"Task Extraction Error: {e}"
        )

        return {
            "action_required": False,
            "task": None,
            "deadline": None
        }


if __name__ == "__main__":

    sample_email = """
Hi Ayuvi,

Please submit the performance report by Friday.

Thanks
"""

    result = extract_task(
        sample_email
    )

    print(
        json.dumps(
            result,
            indent=4
        )
    )