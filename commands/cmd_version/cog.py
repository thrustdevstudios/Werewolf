import os

import nextcord
from nextcord.ext import commands


class VersionCommand(commands.Cog, name='VersionCommand'):
    VERSION = os.environ.get('VERSION')
    COMMIT = os.environ.get('COMMIT')
    BUILD = os.environ.get('BUILD')

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name='version')
    async def version(self, ctx: commands.Context):
        """A command which returns the current version, commit hash and build number.
        Usage:
        ```
        -version
        ```
        """

        await ctx.send(f'Current version: {self.VERSION} ({self.COMMIT}) Build: {self.BUILD}')


def setup(client: commands.Bot):
    client.add_cog(VersionCommand(client))
