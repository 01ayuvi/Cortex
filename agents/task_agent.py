import ollama
import json


def extract_task(email_text):

    prompt = f"""
You are a JSON API.

Rules:
- Return ONLY JSON
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

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    try:
        start = content.find("{")
        end = content.rfind("}") + 1

        json_text = content[start:end]

        return json.loads(json_text)

    except Exception as e:

        print("JSON Parsing Error:", e)

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

    result = extract_task(sample_email)

    print(json.dumps(result, indent=4))