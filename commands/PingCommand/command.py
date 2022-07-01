import discord
from discord.ext import commands
from logic import gamehandler


class PingCommand(commands.Cog, name='PingCommand'):
    def __init__(self, client: commands.Bot, handler: gamehandler.GameHandler):
        self.client = client
        self.handler = handler

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        """A command which returns a ping response.
        
        Usage:
        ```
        -ping
        ```
        """

        await ctx.reply('Pong!')


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(PingCommand(client=client, handler=handler))