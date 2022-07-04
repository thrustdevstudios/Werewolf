import importlib
import os

import discord
from discord.ext import commands

from games.werewolf.player import Player


class GameHandler(commands.Cog, name='Werewolf'):
    data = {
        'is_open': False,
        'is_running': False,
        'min_players': 6,
        'players': {
        }
    }

    def __init__(self, client: commands.Bot):
        self.client = client

    async def is_open(self) -> bool:
        return self.data['is_open']
    
    async def is_running(self) -> bool:
        return self.data['is_running']

    async def get_players(self) -> dict:
        return self.data['players']

    async def get_player(self, player: str) -> dict:
        return self.data['players'][player]
    
    async def add_player(self, player: str):
        user = self.client.fetch_user(int(player))
        player = Player(user=user)
        self.data['players'][user.id] = player

async def register(client: commands.Bot):
    handler = GameHandler(client)
    client.add_cog(handler)
    
    for folder in os.listdir('games/werewolf/commands'):
        module = importlib.import_module(f'games.werewolf.commands.{folder}.command')
        module.register(client=client, handler=handler)
