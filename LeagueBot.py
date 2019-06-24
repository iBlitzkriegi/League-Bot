from discord.ext import commands
from discord import Game
from commands import GeneralCommands, StaffCommands
import json

name = None
prefix = None
description = None
token = None
admins = []

for s in open('./ignore/config.yml'):
    line = s.split('=')
    key = line[0]
    value = line[1].replace('\'', '').strip()
    if 'name' in key:
        name = value
    elif 'prefix' in key:
        prefix = value
    elif 'desc' in key:
        description = value
    elif 'token' in key:
        token = value

bot = commands.Bot(command_prefix=prefix, description=description, activity=Game(name='Neeko is best decision'))
bot.add_cog(GeneralCommands.General(bot))
json_file = open('./jsonFiles/admins.json')
data = json.load(json_file)
for admin in data['admins']:
    admins.append(admin['id'])
bot.add_cog(StaffCommands.Staff(bot, admins))


@bot.event
async def on_ready():
    print(bot.user.name + ' is now online!')


if token is not None:
    bot.run(token)
    token = None
else:
    print('Error! Token wasn\'t parsed correctly! Was config corrupted?')
