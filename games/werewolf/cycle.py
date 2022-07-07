import discord
from discord.ext import commands

from games.werewolf import exceptions
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

    def add_vote(self, target: Player) -> bool:
        target_id = target.get_id()
        if target_id in self.handler.get_players().keys():
            try:
                self.votes[target_id] += 1
            except:
                self.votes[target_id] = 1
            finally:
                return True
        else:
            raise exceptions.PlayerNotFoundError

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
