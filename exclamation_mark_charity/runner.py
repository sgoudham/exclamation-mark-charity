from discord import Intents, Streaming
from discord.ext.commands import Context, Bot

from exclamation_mark_charity import BOT_PREFIX, BOT_TOKEN, HAMMY, NUGGS, LUCA

bot = Bot(
    command_prefix=BOT_PREFIX,
    intents=Intents.all(),
    help_command=None,
    owner_ids=(HAMMY, NUGGS, LUCA)
)
bot.activity = Streaming(name="!charity", url="https://www.twitch.tv/exclamation_mark_charity")


@bot.command()
async def charity(ctx: Context):
    await ctx.send("!charity")


if __name__ == '__main__':
    bot.run(BOT_TOKEN)
