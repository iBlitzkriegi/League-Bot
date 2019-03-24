from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Basic personal league of legends bot')


@bot.event
async def on_ready():
    print(bot.user.name + ' is now online!')

bot.run('')