import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22923037"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "dfb3666878b3851460a58461c5a50f5b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7463809159:AAG0WIc0l8BvwMKas4TrHfQCuMc43DMMFuo")

OWNER_ID = int(os.environ.get("OWNER_ID", "6554343173"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "6554343173").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002561871194"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002617599866")  # Optional here you'll get all logs
