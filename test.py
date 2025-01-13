import os
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env файла

database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')  # Использует переменную окружения

print(f"Database URL: {database_url}")