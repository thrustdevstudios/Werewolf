import discord
from discord.ext import commands

data = {
    'is_open': False,
    'is_running': False,
    'players': {}
}

async def opengame(ctx: commands.Context):
    global data
    if data.get('is_open'):
        await ctx.send(f'{ctx.author.mention} game already open')
        return
    data['is_open'] = True
    await ctx.send(f'{ctx.author.mention} opened a game')
