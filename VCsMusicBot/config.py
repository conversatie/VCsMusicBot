import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BAC1roB8z8C3Tjaj5HKohpJvVl0q7COw_5fYS4Df5zSsCzymEO-E7XHUDn7V7aDxqkyTsyAzoYFmLSqpteERvvMRMw7ItcLb9AzeXTyS6ZgdzS4hm1rHoyWQlmUdCGTd4oo5x5pArk50xymUEuflZ9h7PFidptMsfC4Sp6b8yLqTlILAEN1ZEzWStp3U0XHyzkcAUbCTyGjB5s6RV1uQdvQvNxWMj-w5dbq9x-qfF2O3czAVICJo2gGd29KvNaJ6kzX46nbayw4l5HIlEj0Aiply5PvShcysFzVVO9MdPSEzAyHyktdvCMAZkK2RYLATlB9hSuUQEZmKKdHNfjBcp7OqaFaYTQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1920790228:AAF0PFC4_HrbaMuPgUWrFD20GEpi0xwPsjg")
BOT_NAME = getenv("BOT_NAME", "Durex")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "7378520"))
API_HASH = getenv("API_HASH", "6e04739d66a87f305207247d39875887")
BOT_USERNAME = getenv("BOT_USERNAME", "@Durexbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "JBKQDX-HJDFUB-ZFZUWV-EOANGW-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "973861411").split()))
