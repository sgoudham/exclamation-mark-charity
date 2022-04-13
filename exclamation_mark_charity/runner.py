import discord
from discord.ext import commands
from discord.ext.commands import Context

from exclamation_mark_charity import BOT_PREFIX, BOT_TOKEN

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, description="idk", intents=intents)


@bot.command()
async def charity(ctx: Context):
    await ctx.send("!charity")


bot.run(BOT_TOKEN)
