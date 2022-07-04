import discord
from discord.ext import commands

class Player():
    id = int
    name = str
    role = str
    is_alive = bool

    def __init__(self, user: discord.User):
        self.id = user.id
        self.name = user.name
    
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def get_role(self) -> str:
        return self.role

    def get_alive(self) -> bool:
        return self.is_alive