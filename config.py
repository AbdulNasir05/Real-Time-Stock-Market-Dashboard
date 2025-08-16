import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY = os.getenv("API_KEY")
    API_BASE = os.getenv("API_BASE", "https://www.alphavantage.co/query")
    REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", "60"))

settings = Settings()
