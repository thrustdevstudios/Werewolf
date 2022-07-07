import discord
from discord.ext import commands

from games.werewolf.gamehandler import GameHandler
from games.werewolf.player import Player
import lang


class CycleManager:
    data = {
        'is_night': False,
        'night_number': 0
    }
    votes = {}

    def __init__(self, client: commands.Bot, handler: GameHandler):
        self.client = client
        self.handler = handler
    
    def is_night(self) -> bool:
        return self.data['is_night']
    
    def add_vote(self, target: Player) -> None:
        # TODO
        pass

    def start_cycle(self) -> None:
        # TODO
        pass
    
    def start_night(self) -> None:
        # TODO
        pass
    
    def start_day(self) -> None:
        # TODO
        pass


cyclemanager = CycleManager()
