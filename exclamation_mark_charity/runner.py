import os
from pathlib import Path

from dotenv import load_dotenv
from interactions import Client, Intents, ClientPresence, PresenceActivity, PresenceActivityType

from exclamation_mark_charity.constants import TWITCH_CHANNEL
from exclamation_mark_charity.logger_factory import LoggerFactory


def main():
    logger = LoggerFactory.get_logger(__name__)

    # Setup dotenv()
    logger.info("---------------------------------------------------------------")
    logger.debug("Loading Environment Variables...")
    load_dotenv()
    logger.debug("Finished Loading Environment Variables!")

    # Setup Bot
    logger.debug("Registering Client...")
    bot = Client(
        token=os.environ.get("CHARITY_BOT_TOKEN"),
        intents=Intents.ALL,
        presence=ClientPresence(
            activities=[
                PresenceActivity(
                    name="!charity",
                    type=PresenceActivityType.STREAMING,
                    url=TWITCH_CHANNEL
                )
            ]
        )
    )
    logger.debug("Finished Registering Client!")

    # Load cogs
    logger.debug("Loading Cogs...")
    for folder in os.listdir("modules"):
        if os.path.exists(Path("modules", folder, "cog.py")):
            bot.load(f"modules.{folder}.cog")
            logger.debug(f"Cog '{folder}' Successfully Loaded!")
    logger.debug("All Cogs Loaded!")

    # Run
    logger.info("Bot Online!")
    bot.start()


if __name__ == '__main__':
    main()
