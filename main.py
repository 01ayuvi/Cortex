from integrations.gmail_client import get_unread_emails

def main():

    print("=" * 50)
    print("CORTEX STARTING...")
    print("=" * 50)

    get_unread_emails()

if __name__ == "__main__":
    main()