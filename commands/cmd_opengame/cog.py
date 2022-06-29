import discord
from discord.ext import commands
from logic.gamehandler import GameHandler


class OpenGameCommand(commands.Cog, name='OpenGameCommand'):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(name='opengame')
    @commands.guild_only
    async def opengame(self, ctx: commands.Context):
        """A command which opens a game lobby.
        Usage:
        ```
        -version
        ```
        """

        handler = GameHandler()
        handler.open()
        await ctx.send(f'{ctx.message.author.mention} opened a game')
    
    @opengame.error
    async def opengame_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.GuildNotFound):
            await ctx.send(f'{ctx.message.author.mention} you have to be in a server to run this command')
        else:
            await ctx.send(f'{ctx.message.author.mention} something went wrong')
