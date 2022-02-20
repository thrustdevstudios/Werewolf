import nextcord
from nextcord.ext import commands


class PingCommand(commands.Cog, name='PingCommand'):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        """A command which returns a ping response.
        Usage:
        ```
        -ping
        ```
        """

        await ctx.send('Pong!')


def setup(client: commands.Bot):
    client.add_cog(PingCommand(client))
