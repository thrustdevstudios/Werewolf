import discord
from discord.ext import commands
from logic import gamehandler as handler


class JoinGameCommand(commands.Cog, name='JoinGameCommand'):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(name='joingame')
    @commands.guild_only()
    async def joingame(self, ctx: commands.Context):
        """A command which lets players join an open lobby

        Usage:
        ```
        -joingame
        ```
        """

        await handler.addplayer(ctx)
    
    @joingame.error
    async def joingame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'{ctx.message.author.mention} you have to be in a server to run this command')
        else:
            await ctx.send(f'{ctx.message.author.mention} something went wrong: {error}')


def setup(client: commands.Bot):
    client.add_cog(JoinGameCommand(client))