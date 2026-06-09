from integrations.gmail_client import get_unread_emails
from agents.task_agent import extract_task
from agents.briefing_agent import generate_briefing
from database.db import save_task, task_exists
from memory.vector_store import save_email


def main():

    print("DEBUG: Starting Cortex")

    emails = get_unread_emails()

    print(f"DEBUG: Found {len(emails)} emails")

    processed_tasks = 0

    for email in emails:
        print(email)

        print(
            f"DEBUG: Processing -> {email['subject']}"
        )

        # Create richer email content for memory storage
        email_text = f"""
Subject: {email['subject']}

Content:
{email['snippet']}
"""

        # Save email into ChromaDB memory
        save_email(
            str(hash(email_text)),
            email_text
        )

        print(
            "DEBUG: Email stored in memory"
        )

        task_data = extract_task(
            email["snippet"]
        )

        print(
            f"DEBUG: Extracted -> {task_data}"
        )

        if task_data["action_required"]:

            if not task_exists(
                task_data["task"]
            ):

                save_task(
                    task_data["task"],
                    task_data["deadline"],
                    email["priority"],
                    task_data["category"]
                )

                processed_tasks += 1

                print(
                    "DEBUG: Task saved"
                )

            else:

                print(
                    "DEBUG: Task already exists"
                )

    result = {
        "emails_processed": len(emails),
        "new_tasks": processed_tasks
    }

    print(
        f"DEBUG: Completed -> {result}"
    )

    return result


if __name__ == "__main__":

    result = main()

    print("\n")
    print("=" * 50)
    print("CORTEX DAILY BRIEFING")
    print("=" * 50)

    print(
        f"Emails Processed: {result['emails_processed']}"
    )

    print(
        f"New Tasks Added: {result['new_tasks']}"
    )

    print("\nGenerating briefing...\n")

    generate_briefing()