import asyncio
import logging

import interactions
import table2ascii
from table2ascii import PresetStyle

from exclamation_mark_charity.constants import GUILD_ID, OWNER_IDS
from exclamation_mark_charity.database import Database
from exclamation_mark_charity.logger_factory import LoggerFactory


def create_button(style: interactions.ButtonStyle, label: str, custom_id: str) -> interactions.Button:
    return interactions.Button(style=style, label=label, custom_id=custom_id)


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
                name="create",
                description="Create a !charity tournament",
                type=interactions.OptionType.SUB_COMMAND,
                options=[
                    interactions.Option(
                        name="title",
                        description="Title of the tournament",
                        type=interactions.OptionType.STRING,
                        required=True,
                    )
                ]
            ),
            interactions.Option(
                name="all",
                description="View all existing tournaments",
                type=interactions.OptionType.SUB_COMMAND,
                options=[]
            ),
            interactions.Option(
                name="update",
                description="Update the tournament details",
                type=interactions.OptionType.SUB_COMMAND,
                options=[]
            ),
            interactions.Option(
                name="delete",
                description="Delete a tournament",
                type=interactions.OptionType.SUB_COMMAND,
                options=[]
            )
        ]
    )
    async def tournament_command(self, ctx: interactions.CommandContext, sub_command, title: str = None):
        # TODO: Remove when interactions.py implement application_command_permissions
        if int(ctx.author.id) not in OWNER_IDS:
            await ctx.send("**[ERROR 0069]** -> Not Allowed!")
            return

        # Check function to ensure inputs are from the original user who invoked slash command
        async def check(button_ctx):
            if int(button_ctx.author.user.id) == int(ctx.author.user.id):
                return True
            await button_ctx.send("I wasn't asking you!", ephemeral=True)
            return False

        if sub_command == "create":
            row = interactions.ActionRow(
                components=[
                    create_button(interactions.ButtonStyle.SUCCESS, "Yes", "success"),
                    create_button(interactions.ButtonStyle.DANGER, "Cancel", "cancel")
                ]
            )

            message: interactions.Message = await ctx.send(
                f"Create A Tournament With The Name **{title}**?", components=row)

            try:
                button_ctx: interactions.ComponentContext = await self.bot.wait_for_component(
                    components=row, check=check, timeout=25
                )
                if button_ctx.label == "Yes":
                    success, tournament_id = Database.create_tournament(title)
                    if success:
                        await message.edit(f"Tournament **{title}** Successfully Created!", components=None)
                        self.logger.info(f"Tournament '{title}' Created Successfully With ID '{tournament_id}'!")
                    else:
                        await message.edit("Tournament Creation Failed! **Check Logs!**", components=None)
                else:
                    await message.edit("Tournament Creation Aborted!", components=None)
            except asyncio.TimeoutError:
                await message.edit("You didn't click it :(", components=None)

        elif sub_command == "all":
            success, all_tournaments = Database.view_all_tournaments()
            if success:
                output = table2ascii.table2ascii(
                    header=all_tournaments[0],
                    body=all_tournaments[1:],
                    style=PresetStyle.thick_compact
                )
                await ctx.send(f"```\n{output}\n```")
                self.logger.info("All Tournaments Successfully Retrieved!")
            else:
                await ctx.send("Could Not List All Tournaments! **Check Logs!**")

        elif sub_command == "update":
            await ctx.send("**[INFO 0069]** Not Implemented Yet!")

        elif sub_command == "delete":
            success, all_tournaments = Database.view_all_tournaments()
            tables = [table[0] for table in all_tournaments[1:]]

            menu = interactions.SelectMenu(
                custom_id="tournament_deletes_menu",
                options=[interactions.SelectOption(label=table, value=table) for table in tables],
                placeholder="Select Row(s)",
                max_values=len(tables)
            )

            message: interactions.Message = await ctx.send(
                f"Select Tournaments To **DELETE FOREVER**", components=menu)

            try:
                menu_ctx: interactions.ComponentContext = await self.bot.wait_for_component(
                    components=menu, check=check, timeout=25
                )
                success = Database.delete_many_tournaments([tuple([row]) for row in menu_ctx.data.values])
                if success:
                    await message.edit("Chosen Table(s) Deleted", components=None)
                else:
                    await message.edit("Table(s) Could Not Be Deleted! **Check Logs!**", components=None)
            except asyncio.TimeoutError:
                await message.edit("You didn't choose anything :(", components=None)


def setup(bot):
    Tournament(bot)
