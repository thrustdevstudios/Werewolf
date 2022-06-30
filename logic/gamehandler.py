from random import choice

import discord
from discord.ext import commands

data = {
    'is_open': False,
    'is_running': False,
    'min_players': 6,
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

async def assign_roles(ctx: commands.Context):
    global data

    num_players = len(data['players'])
    num_werewolves = round(num_players // 3)

    for player in data['players']:
        data['players'][player]['role'] = None
    
    await ctx.send(f'assigning {num_werewolves} werewolves.')

    werewolves_assigned = 0
    players_list = list(data['players'].keys())
    while werewolves_assigned < num_werewolves:
        for player in players_list:
            role = choice(['villager', 'werewolf'])
            data['players'][player]['role'] = role
            if role == 'werewolf':
                werewolves_assigned += 1
            players_list.remove(player)
    
    for player in list(data['players'].keys()):
        user = discord.Client.get_user(player)
        await user.send(f'you have been assigned the role {data["players"][player]["role"]}')

async def startgame(ctx: commands.Context):
    global data
    if data['is_running']:
        await ctx.send(f'{ctx.author.mention} is already running')
        return
    elif len(data['players']) << 6:
        ctx.reply('not enough players')
        return
    data['is_running'] = True
    await ctx.reply('started the game')
