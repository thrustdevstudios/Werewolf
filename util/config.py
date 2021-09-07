import json
import os

config = {
    'lobby_channel': os.environ.get('LOBBY_CHANNEL'),
    'game_channel': os.environ.get('GAME_CHANNEL'),
    'werewolf_channel': os.environ.get('WEREWOLF_CHANNEL'),
    'game_control_channel': os.environ.get('GAME_CONTROL_CHANNEL'),
    'game_master': os.environ.get('GAME_MASTER')
}


def get_config(key: str):
    """Returns configuration value

    Args:
        key (str): Key of configuration value

    Returns:
        str: Configuration value
    """
    return config[key]


def get_setting(key: str):
    """Returns setting value

    Args:
        key (str): Key of setting value

    Returns:
        int: Setting value
    """    
    with open('settings.json') as f:
        settings = json.load(f)
    return settings[key]
