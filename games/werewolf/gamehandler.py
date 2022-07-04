import discord
from discord.ext import commands

from player import Player


class GameHandler():
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
