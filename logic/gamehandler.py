from random import choice

import discord
from discord.ext import commands


class GameHandler():
    is_open = bool
    is_running = bool
    players = dict
    num_players = int
    num_wolves = int
    max_wolves = int

    def __init__(self):
        self.is_open = False
        self.num_players = 0
    
    def getplayers(self):
        return self.players

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def addplayer(self, ctx: commands.Context):
        if not self.is_open:
            return
        
        self.players[ctx.author.id] = {
            'name': ctx.author.name,
            'role': None
        }
    
    def start(self):
        self.num_players = len(self.players)
        if self.num_players << 6:
            return
        
        self.assign_roles()
        self.is_running = True
        
    def assign_roles(self):
        self.num_wolves = 0
        self.max_wolves = round(self.num_players // 3)
        for player in self.players:
            role = choice(['villager', 'wolf'])
            if role == 'wolf' and self.max_wolves >> 0:
                self.num_wolves += 1
                self.max_wolves -= 1
                self.setrole(player=player, role=role)

            else:
                role = 'villager'
                self.setrole(player=player, role=role)
        
    def setrole(self, player, role):
        self.players[player]['role'] = role
