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

    async def __assign_roles(self):
        # TODO
        pass

    async def is_open(self) -> bool:
        return self.data['is_open']

    async def is_running(self) -> bool:
        return self.data['is_running']

    async def get_players(self) -> dict:
        return self.data['players']

    async def get_player(self, player: str) -> dict:
        return self.data['players'][player]

    async def add_player(self, user: discord.User) -> bool:
        if user.id in self.data['players'].keys():
            return False
        else:
            player = Player(user=user)
            self.data['players'][user.id] = player
            return True

    async def remove_player(self, user: discord.User) -> bool:
        if not user.id in self.data['players'].keys():
            return False
        else:
            del self.data['players'][user.id]
            return True

    async def open_game(self, ctx: commands.Context):
        if self.data['is_open']:
            ctx.reply('game already open')
            return
        else:
            self.data['is_open'] = True
            await ctx.send(f'{ctx.author.mention} opened a game')

    async def start_game(self, ctx: commands.Context) -> bool:
        if not ctx.author.id in self.data['players'].keys():
            await ctx.reply('you have to join the game to start it')
        elif not self.data['is_open']:
            await ctx.reply('no open game was found')
        elif self.data['is_running']:
            await ctx.reply('game already running')
        elif len(self.data['players']) < self.data['min_players']:
            await ctx.reply('not enough players to start a game')
        else:
            self.data['is_running'] = True
            await self.__assign_roles()


async def register(client: commands.Bot):
    handler = GameHandler(client)
    client.add_cog(handler)

    for folder in os.listdir('games/werewolf/commands'):
        module = importlib.import_module(
            f'games.werewolf.commands.{folder}.command')
        module.register(client=client, handler=handler)
