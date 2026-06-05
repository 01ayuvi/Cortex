from integrations.gmail_client import get_unread_emails
from agents.task_agent import extract_task
from database.db import save_task


def main():

    print("=" * 50)
    print("CORTEX DAILY BRIEFING")
    print("=" * 50)

    emails = get_unread_emails()

    print(f"\nUnread Emails: {len(emails)}\n")

    for email in emails:

        print("-" * 50)
        print("FROM:", email["sender"])
        print("SUBJECT:", email["subject"])
        print("PRIORITY:", email["priority"])
        print("SNIPPET:", email["snippet"])

        task_data = extract_task(email["snippet"])

        print("\nTASK DATA:")
        print(task_data)

        if task_data["action_required"]:

            save_task(
                task_data["task"],
                task_data["deadline"],
                email["priority"]
            )

            print("Task saved to database.")


if __name__ == "__main__":
    main()