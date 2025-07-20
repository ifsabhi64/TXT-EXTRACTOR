import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "20567114"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "8a5b92106e45fc6637a65a67df060a65")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7384733984:AAG8_yOMmBbtj_3JoZJQrkZC4iNKmXbaenk")

OWNER_ID = int(os.environ.get("OWNER_ID", "8036182138"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "8036182138").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002441127578"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
