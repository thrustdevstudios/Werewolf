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

async def closegame(ctx: commands.Context):
    global data
    if not data.get('is_open'):
        await ctx.send(f'{ctx.author.mention} there is no open game')
        return
    data['is_open'] = False
    await ctx.send(f'{ctx.author.mention} closed the game')

async def addplayer(ctx: commands.Context, user: discord.User):
    global data
    if not data.get('is_open'):
        await ctx.send(f'{ctx.author.mention} there is no open game')
        return
    elif not data['players'] == None:
        await ctx.send(f'{ctx.author.mention} is already in the game')
    data['players'][user.id] = {
        'name': user.name,
        'role': None
    }
    await ctx.send(f'{ctx.author.mention} joined the game')
