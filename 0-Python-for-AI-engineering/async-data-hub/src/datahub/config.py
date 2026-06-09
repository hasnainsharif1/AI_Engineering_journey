import os
from pathlib import Path
from dotenv import load_dotenv

# load .env from the project root (two levels up from this file)
load_dotenv(Path(__file__).parent.parent.parent / ".env")

# URLs
WEATHER_BASE_URL  = os.getenv("WEATHER_BASE_URL",  "https://api.open-meteo.com/v1/forecast")
COUNTRIES_BASE_URL = os.getenv("COUNTRIES_BASE_URL", "https://restcountries.com/v3.1")
POSTS_BASE_URL    = os.getenv("POSTS_BASE_URL",    "https://jsonplaceholder.typicode.com")

# App settings
LOG_LEVEL          = os.getenv("LOG_LEVEL",         "INFO")
HTTP_TIMEOUT       = int(os.getenv("HTTP_TIMEOUT",  "10"))
MAX_RETRIES        = int(os.getenv("MAX_RETRIES",   "3"))
RETRY_WAIT_SECONDS = int(os.getenv("RETRY_WAIT_SECONDS", "2"))
