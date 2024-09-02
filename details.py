import os
from os import getenv


API_ID = int(getenv("API_ID", 23031620))
API_HASH = getenv("API_HASH", "31cb00c1cbe580394778b43105864bca")
BOT_TOKEN = getenv("BOT_TOKEN", "6865731231:AAEDdXn48VOzOf0jRo0CvxkU0VxIFsikTvg")
OWNER_ID = int(getenv("OWNER_ID", "502980590"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590  20000898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://altafpathan65012:<password>@cluster0.aztmome.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002155787742"))
