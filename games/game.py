import discord
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, client = commands.Bot()):
        self.client = client
    

