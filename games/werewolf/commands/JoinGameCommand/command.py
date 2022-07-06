import discord
from discord.ext import commands

from games.werewolf import gamehandler
import lang


@commands.guild_only()
class JoinGameCommand(commands.Cog, name='JoinGameCommand'):
    def __init__(self, client: commands.Bot, handler: gamehandler.GameHandler):
        self.client = client
        self.handler = handler

    @commands.command(name='joingame')
    @commands.guild_only()
    async def joingame(self, ctx: commands.Context):
        """A command which lets players join an open lobby

        Usage:
        ```
        -joingame
        ```
        """

        if await self.handler.add_player(ctx.author):
            num_players = len(await self.handler.get_players())
            await ctx.send(lang.get('joinlobby').format(ctx.author.mention, num_players))
        else:
            await ctx.reply(lang.get('alreadyin'))

    @joingame.error
    async def joingame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(lang.get('noprivatemessage'))
        else:
            await ctx.send(lang.get('error').format(error))


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(JoinGameCommand(client=client, handler=handler))
