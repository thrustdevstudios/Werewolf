import os

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.core import has_role


intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="-", intents=intents)


for folder in os.listdir('cmd'):
    if os.path.exists(os.path.join('cmd', folder, 'cog.py')):
        client.load_extension(f'cmd.{folder}.cog')


TOKEN = os.getenv('CLIENT_TOKEN')
client.run(TOKEN)
