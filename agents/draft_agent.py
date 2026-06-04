import ollama

def generate_reply(email_text):

    prompt = f"""
You are Cortex, an AI executive assistant.

Write a professional email reply.

Sign the email as:
Ayuvi

Email:
{email_text}

Return only the email reply.
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

    sample_email = """
Hi Ayuvi,

Are you available for an interview on Thursday at 2 PM?

Best Regards,
Recruiter
"""

    reply = generate_reply(sample_email)

    print(reply)