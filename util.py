import json
import os
from datetime import datetime


class Colours:
    HEADER = '\033[95m'
    INFO = '\033[96m'
    DEBUG = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'


VERSION = 'v0.2.0-a1'
config = {
    'lobby_channel': os.environ.get('LOBBY_CHANNEL'),
    'game_channel': os.environ.get('GAME_CHANNEL'),
    'werewolf_channel': os.environ.get('WEREWOLF_CHANNEL'),
    'game_control': os.environ.get('GAME_CONTROL_CHANNEL'),
    'game_master': os.environ.get('GAME_MASTER')
}


def get_config(key: str):
    return config[key]


def get_setting(key: str):
    with open('settings.json') as f:
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
