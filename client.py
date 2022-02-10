import json
import os
import random
from datetime import datetime, timedelta
from typing import OrderedDict

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.core import has_role


intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="-", intents=intents)


for folder in os.listdir('cogs'):
    if os.path.exists(os.path.join('cogs', folder, 'cog.py')):
        client.load_extension(f'cogs.{folder}.cog')


TOKEN = os.getenv('CLIENT_TOKEN')
client.run(TOKEN)
