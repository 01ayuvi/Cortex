from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3"
)

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    "./chroma_db"
)

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "tasks.db"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)