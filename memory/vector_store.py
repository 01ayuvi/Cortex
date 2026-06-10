from config import CHROMA_DB_PATH
import chromadb

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH
)

collection = client.get_or_create_collection(
    name="email_memory"
)

def save_email(email_id, email_content):

    try:

        collection.add(
            ids=[str(email_id)],
            documents=[email_content]
        )

    except Exception:

        pass