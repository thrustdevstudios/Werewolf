import discord
from discord.ext import commands

from games.werewolf import exceptions
from games.werewolf import gamehandler
import lang


class HuntCommand(commands.Cog, name='HuntCommand'):
    def __init__(self, client: commands.Bot, handler: gamehandler.GameHandler):
        self.client = client
        self.handler = handler
        self.cyclemanager = handler.cyclemanager

    @commands.command(name='hunt')
    @commands.guild_only()
    async def hunt(self, ctx: commands.Context, target: discord.User):
        """A command which lets werewolves vote on a target for the night

        Usage:
        ```
        -hunt
        ```
        """

        if self.cyclemanager.add_vote(target):
            await ctx.reply(lang.get('hunttarget').format(target.mention))

    @hunt.error
    async def hunt_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.reply(lang.get('noprivatemessage'))
        else:
            await ctx.reply(lang.get('error').format(error))


def register(client: commands.Bot, handler: gamehandler.GameHandler):
    client.add_cog(HuntCommand(client=client, handler=handler))
