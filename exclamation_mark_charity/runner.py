import os
from pathlib import Path

import interactions
from dotenv import load_dotenv
from interactions import Client, Intents, ClientPresence, PresenceActivity, PresenceActivityType
from interactions.ext import wait_for

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
            ],
            status=interactions.StatusType.ONLINE
        )
    )
    logger.debug("Finished Registering Client!")

    # Apply hooks to the class - wait_for(), wait_for_component()
    # setup(bot, add_method=True)
    wait_for.setup(bot, add_method=True)

    # Load cogs
    logger.debug("Loading Cogs...")
    for folder in os.listdir("exclamation_mark_charity/modules"):
        if os.path.exists(Path("exclamation_mark_charity/modules", folder, "cog.py")):
            bot.load(f"modules.{folder}.cog")
            logger.debug(f"Cog '{folder}' Successfully Loaded!")
    logger.debug("All Cogs Loaded!")

    # Run
    logger.info("Bot Online!")
    bot.start()


if __name__ == '__main__':
    main()
