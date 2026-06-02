import ollama

def classify_email(subject):

    prompt = f"""
You are Cortex, an AI executive assistant.

Classify email priority.

Rules:

HIGH:
- Job interviews
- Recruiter messages
- Security alerts
- Deadlines
- Urgent requests
- Meeting invitations

MEDIUM:
- Order updates
- Bank notifications
- Project updates

LOW:
- Marketing emails
- Promotions
- Newsletters
- Advertisements

Subject:
{subject}

Return ONLY one word:

HIGH
MEDIUM
LOW
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

    return response["message"]["content"].strip()


if __name__ == "__main__":

    test_subjects = [
        "Interview Invitation",
        "Security Alert",
        "Your Amazon Order Has Shipped",
        "Newsletter"
    ]

    for subject in test_subjects:
        priority = classify_email(subject)

        print("=" * 50)
        print("SUBJECT:", subject)
        print("PRIORITY:", priority)