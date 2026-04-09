from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

print("ENV PATH:", env_path)
print("API KEY:", os.getenv("GROQ_API_KEY"))