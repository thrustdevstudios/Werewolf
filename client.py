import os

import nextcord
from nextcord.ext import commands


intents = nextcord.Intents.default()
intents.members = True

if os.getenv('CLIENT') == 'production':
    prefix = '-'
else:
    prefix = '.'

client = commands.Bot(command_prefix=prefix, intents=intents)


client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_ready():
    for folder in os.listdir('commands'):
        if os.path.exists(os.path.join('commands', folder, 'cog.py')):
            client.load_extension(f'commands.{folder}.cog')


TOKEN = os.getenv('CLIENT_TOKEN')
client.run(TOKEN)
