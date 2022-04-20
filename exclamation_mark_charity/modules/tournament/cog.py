import logging

import interactions

from exclamation_mark_charity.constants import GUILD_ID, OWNER_IDS
from exclamation_mark_charity.database import Database
from exclamation_mark_charity.logger_factory import LoggerFactory


class Tournament(interactions.Extension):
    def __init__(self, bot: interactions.Client):
        self.bot: interactions.Client = bot
        self.logger: logging.Logger = LoggerFactory.get_logger(__name__)

    @interactions.extension_command(
        name="tournament",
        description="Tournament Command",
        scope=GUILD_ID,
        options=[
            interactions.Option(
                name="update",
                description="Update The Tournament Details",
                type=interactions.OptionType.SUB_COMMAND,
                options=[]
            ),
            interactions.Option(
                name="create",
                description="Create A !charity Tournament",
                type=interactions.OptionType.SUB_COMMAND,
                options=[
                    interactions.Option(
                        name="name",
                        description="The name of the tournament",
                        type=interactions.OptionType.STRING,
                        required=True,
                    )
                ]
            )
        ]
    )
    async def tournament_command(self, ctx: interactions.CommandContext, sub_command, name: str = None):
        # TODO: Remove when interactions.py implement application_command_permissions
        if int(ctx.author.id) not in OWNER_IDS:
            await ctx.send("**[ERROR 0069]** -> Not Allowed!")
            return

        await ctx.defer()

        if sub_command == "create":
            success, tournament_id = Database.create_tournament(name)
            if success:
                await ctx.send(f"Tournament **{name}** Successfully Created!")
                self.logger.info(f"Tournament '{name}' Created Successfully With ID '{tournament_id}'!")
            else:
                await ctx.send(f"Tournament Creation Failed! Check Logs!")
        elif sub_command == "update":
            await ctx.send("**[INFO 0069]** Not Implemented Yet!")


def setup(bot):
    Tournament(bot)
