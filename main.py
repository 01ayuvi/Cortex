from integrations.gmail_client import get_unread_emails

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

if __name__ == "__main__":
    main()