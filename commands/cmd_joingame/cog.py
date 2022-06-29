from calendar import c
import discord
from discord.ext import commands
from logic.gamehandler import GameHandler


class JoinGameCommand(commands.Cog, name='JoinGameCommand'):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(name='joingame')
    @commands.guild_only()
    async def joingame(self, ctx: commands.Context):
        handler = GameHandler()
        try:
            handler.addplayer(ctx)
        except:
            await ctx.send(f'{ctx.message.author.mention} there was an error trying to join the game')
        else:
            await ctx.send(f'{ctx.message.author.mention} joined the game')
    
    @joingame.error
    async def joingame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'{ctx.message.author.mention} you have to be in a server to run this command')
        else:
            await ctx.send(f'{ctx.message.author.mention} something went wrong: {error}')


def setup(client: commands.Bot):
    client.add_cog(JoinGameCommand(client))