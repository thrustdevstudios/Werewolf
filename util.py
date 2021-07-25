from datetime import datetime
import json

from discord.webhook import Webhook

class Colours:
    HEADER = '\033[95m'
    INFO = '\033[96m'
    DEBUG = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'

VERSION = 'v0.1.0-beta'
LOBBY_CHANNEL = 867108595672678411
GAME_CHANNEL = 867389512953626654
WEREWOLF_CHANNEL = 867126719994527765
GAME_CONTROL_CHANNEL = 867126554521894949
GAME_MASTER = 839828233285402634
LOG_LEVEL = 0

def get_config(key:str):
    with open('data/config.json') as f:
        config = json.load(f)
    return config[key]

def get_setting(key:str):
    with open('data/settings.json') as f:
        settings = json.load(f)
    return settings[key]

def get_time():
    return f"[{datetime.now().strftime('%H:%M:%S')}] "

def get_version():
    return VERSION

def log(level: int, message: str):
    prefix = {0: f'{Colours.DEBUG}[DEBUG] ',
              1: f'{Colours.INFO}[INFO] ',
              2: f'{Colours.WARNING}[WARNING] ',
              3: f'{Colours.ERROR}[ERROR] '
              }
    suffix = f'{Colours.END}'
    print(f'{prefix[level]}{get_time()}{message}{suffix}')
