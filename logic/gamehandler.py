import discord
from discord.ext import commands


class GameHandler():
    is_open = bool
    players = dict

    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def addplayer(self, ctx: commands.Context):
        if not self.is_open:
            return
        
        self.players[ctx.author.id] = {
            'name': ctx.author.name
        }