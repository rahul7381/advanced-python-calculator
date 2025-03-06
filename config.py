from dotenv import load_dotenv
import os

load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")

