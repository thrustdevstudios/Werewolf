import importlib
import os

import discord
from discord.ext import commands

from logic.gamehandler import GameHandler

intents = discord.Intents.default()
intents.members = True

if os.getenv('CLIENT') == 'production':
    prefix = '-'
else:
    prefix = '.'

client = commands.Bot(command_prefix=prefix, intents=intents)
handler = GameHandler(client=client)

async def register_commands():
    for folder in os.listdir('commands'):
        module = importlib.import_module(f'commands.{folder}.command')
        command_class = getattr(module, f'{folder}')
        await module.register(client=client, handler=handler)

@client.event
async def on_ready():
    register_commands()


TOKEN = os.getenv('CLIENT_TOKEN')
client.run(TOKEN)
