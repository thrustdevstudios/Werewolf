import discord
from discord.ext import commands

data = {
    'is_open': False,
    'is_running': False,
    'players': {}
}

async def opengame(ctx: commands.Context):
    global data
    if data['is_open']:
        await ctx.reply('game already open')
        return
    data['is_open'] = True
    await ctx.send(f'{ctx.author.mention} opened a game')

async def closegame(ctx: commands.Context):
    global data
    if not data['is_open']:
        await ctx.reply('there is no open game')
        return
    data['is_open'] = False
    await ctx.send(f'{ctx.author.mention} closed the game')

async def addplayer(ctx: commands.Context):
    global data
    if ctx.author.id in data['players']:
        await ctx.reply('player already exists')
        return
    
    data['players'][ctx.author.id] = {
        'name': ctx.author.name,
        'role': None
    }

    await ctx.send(f'{ctx.author.mention} joined the game')

async def removeplayer(ctx: commands.Context):
    global data
    try:
        del data['players'][ctx.author.id]
    except:
        await ctx.send(f'{ctx.author.mention} something went wrong')

async def startgame(ctx: commands.Context):
    global data
    if data['is_running']:
        await ctx.send(f'{ctx.author.mention} is already running')
        return
    data['is_running'] = True
    await ctx.reply('started the game')
