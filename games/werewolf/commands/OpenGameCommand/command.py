import discord
from discord.ext import commands
from games.werewolf import gamehandler


class OpenGameCommand(commands.Cog, name='OpenGameCommand'):
    def __init__(self, client: commands.Bot, handler: gamehandler.GameHandler):
        self.client = client
        self.handler = handler
    
    @commands.command(name='opengame')
    @commands.guild_only()
    async def opengame(self, ctx: commands.Context):
        """A command which opens a game lobby.
        Usage:
        ```
        -version
        ```
        """

        await self.handler.open_game(ctx)
    
    @opengame.error
    async def opengame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f'{ctx.message.author.mention} you have to be in a server to run this command')
        else:
            await ctx.send(f'{ctx.message.author.mention} something went wrong')


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(OpenGameCommand(client=client, handler=handler))