import logging
import os
from pathlib import Path

from dotenv import load_dotenv

# Setup
load_dotenv()

# Owner IDs
HAMMY = 154840866496839680
NUGGS = 337175192751308801
LUCA = 216625083186151425

# Constants
BOT_TOKEN = os.environ.get("CHARITY_BOT_TOKEN")
BOT_PREFIX = "!"
DB_FILE = Path("db", "charity.db")
DB_FILE.parent.mkdir(parents=True, exist_ok=True)
LOG_FILE = Path("logs", "discord.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

TWITCH_CHANNEL = "https://www.twitch.tv/exclamation_mark_charity"

# Set Up Logging
LOGGER = logging.getLogger("discord")
LOGGER.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=LOG_FILE, encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
LOGGER.addHandler(handler)
