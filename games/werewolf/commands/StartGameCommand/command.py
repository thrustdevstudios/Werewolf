import discord
from discord.ext import commands

from games.werewolf import gamehandler
import lang


class StartGameCommand(commands.Cog, name='StartGameCommand'):
    def __init__(self, client: commands.Bot, handler: gamehandler.GameHandler):
        self.client = client
        self.handler = handler

    @commands.command(name='startgame',)
    @commands.guild_only()
    async def startgame(self, ctx: commands.Context):
        """A command which lets players start the game

        Usage:
        ```
        -startgame
        ```
        """

        await self.handler.start_game(ctx)

    @startgame
    async def startgame_error(self, ctx: commands.Context, error):
        await ctx.reply(f'error: {error}')


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(StartGameCommand(client=client, handler=handler))
