import logging
import os

from dotenv import load_dotenv

# Setup
load_dotenv()

# Constants
BOT_TOKEN = os.environ.get("CHARITY_BOT_TOKEN")
BOT_PREFIX = "!"

# Set Up Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
