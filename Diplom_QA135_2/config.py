import os
from dotenv import load_dotenv

# Загружаем данные из файла .env
load_dotenv()

BASE_URL_API: str = os.getenv("BASE_URL_API")
BASE_URL_UI: str = os.getenv("BASE_URL_UI")
API_KEY: str = os.getenv("API_KEY")
