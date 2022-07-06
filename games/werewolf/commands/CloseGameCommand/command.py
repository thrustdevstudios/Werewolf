import discord
from discord.ext import commands

from games.werewolf import gamehandler
import lang


class CloseGameCommand(commands.Cog, name='CloseGameCommand'):
    def __init__(self, client: commands.Bot, handler: gamehandler.GameHandler):
        self.client = client
        self.handler = handler

    @commands.command(name='closegame')
    @commands.guild_only()
    async def closegame(self, ctx: commands.Context):
        """A command which lets players close the game lobby.

        Usage:
        ```
        -joingame
        ```
        """

        if await self.handler.close_game():
            await ctx.reply(lang.get('gameclosed'))
        else:
            await ctx.reply(lang.get('error').format('unknown error'))

    @closegame.error
    async def closegame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.reply(lang.get('noprivatemessage'))
        else:
            await ctx.reply(lang.get('error').format(error))


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(CloseGameCommand(client=client, handler=handler))
