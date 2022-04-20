from pathlib import Path

# Guild ID
GUILD_ID = 903322680034492416

# Owner IDs
HAMMY = 154840866496839680
NUGGS = 337175192751308801
LUCA = 216625083186151425
OWNER_IDS = (HAMMY, NUGGS, LUCA)

# Database & Logging Paths
DB_FILE = Path("db", "charity.db")
DB_FILE.parent.mkdir(parents=True, exist_ok=True)
LOG_FILE = Path("logs", "discord.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Socials
TWITCH_CHANNEL = "https://www.twitch.tv/exclamation_mark_charity"
