from logging import Logger

import interactions
from interactions import Extension, Client, Message

from exclamation_mark_charity.logger_factory import LoggerFactory


class Charity(Extension):
    def __init__(self, bot: Client):
        self.bot: Client = bot
        self.logger: Logger = LoggerFactory.get_logger(__name__)

    @interactions.extension_listener(name="on_message_create")
    async def on_message_create(self, message: Message):
        if int(message.author.id) != int(self.bot.me.id):
            if message.content.strip() == "!charity":
                message._client = self.bot.http
                channel = await message.get_channel()
                await channel.send("!charity")
                self.logger.info("!charity command fired!")


def setup(bot: Client):
    Charity(bot)
