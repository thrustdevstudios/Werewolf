import importlib
import os
from random import choice

import discord
from discord.ext import commands

from games.werewolf.cycle import cyclemanager
from games.werewolf.player import Player
import lang


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
        self.cyclemanager = cyclemanager

    async def __assign_roles(self, ctx: commands.Context):
        num_players = len(self.data['players'])
        num_werewolves = num_players // 3

        await ctx.send(lang.get('assigningwolves').format(num_werewolves))

        werewolves_assigned = 0
        players_list = list(self.data['players'])

        while werewolves_assigned < num_werewolves:
            for player in players_list:
                role = choice(['villager', 'werewolf'])
                self.data['players'][player].set_role(role)
                if role == 'werewolf':
                    werewolves_assigned += 1
                players_list.remove(player)

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
            await ctx.reply('game already open')
            return
        else:
            self.data['is_open'] = True
            await ctx.send(f'{ctx.author.mention} opened a game')
    
    async def close_game(self) -> bool:
        if not self.data['is_open']:
            return False
        else:
            self.data['is_open'] = False
            self.data['players'].clear()
            return True

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
            await self.__assign_roles(ctx=ctx)


async def register(client: commands.Bot):
    handler = GameHandler(client)
    client.add_cog(handler)

    for folder in os.listdir('games/werewolf/commands'):
        module = importlib.import_module(
            f'games.werewolf.commands.{folder}.command')
        module.register(client=client, handler=handler)
