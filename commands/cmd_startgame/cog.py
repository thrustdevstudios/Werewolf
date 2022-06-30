import discord
from discord.ext import commands
from logic import gamehandler as handler


class StartGameCommand(commands.Cog, name='StartGameCommand'):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(name='startgame',)
    @commands.guild_only()
    async def startgame(self, ctx: commands.Context):
        """A command which lets players start the game
        
        Usage:
        ```
        -startgame
        ```
        """

        await handler.startgame(ctx)
    
    @startgame
    async def startgame_error(self, ctx: commands.Context, error: commands.Error):
        await ctx.reply(f'error: {error.message}')


def setup(client: commands.Bot):
    client.add_cog(StartGameCommand(client))