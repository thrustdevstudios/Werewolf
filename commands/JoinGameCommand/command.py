import discord
from discord.ext import commands
from logic import gamehandler

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

        await self.handler.addplayer(ctx)
    
    @joingame.error
    async def joingame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'{ctx.message.author.mention} you have to be in a server to run this command')
        else:
            await ctx.send(f'{ctx.message.author.mention} something went wrong: {error}')


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(JoinGameCommand(client=client, handler=handler))