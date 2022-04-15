from discord import Intents
from discord.ext import commands
from discord.ext.commands import Context

from exclamation_mark_charity import BOT_PREFIX, BOT_TOKEN

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=Intents.all())


@bot.command()
async def charity(ctx: Context):
    await ctx.send("!charity")


if __name__ == '__main__':
    bot.run(BOT_TOKEN)
