import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "20567114"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "8a5b92106e45fc6637a65a67df060a65")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7640683389:AAH5tw6gXE3qZNKkyC5Q0wiZSfujT_GUpeA")

OWNER_ID = int(os.environ.get("OWNER_ID", "8036182138"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "8036182138").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002373143402")  # Optional here you'll get all logs
