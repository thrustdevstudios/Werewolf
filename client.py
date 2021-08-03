import json
import os
import random
from datetime import datetime, timedelta
from typing import OrderedDict

import discord
from discord.ext import commands
from discord.ext.commands.core import has_role

import util

intents = discord.Intents.default()
intents.members = True

VERSION = util.get_version()
LOBBY_CHANNEL = util.get_config('lobby_channel')
GAME_CHANNEL = util.get_config('game_channel')
WEREWOLF_CHANNEL = util.get_config('werewolf_channel')
GAME_CONTROL_CHANNEL = util.get_config('game_control')
GAME_MASTER = util.get_config('game_master')
LOG_LEVEL = 0

game_status = None
player_list = []
player_dict = {}
roles = ["villager", "werewolf", "witch", "hunter",
         "amor", "seer", "bodyguard", "wild_kid"]
session = {
    'is_playing': False,
    'players': OrderedDict(),
    'is_day': False,
    'time': {
        'night_elapsed': timedelta(0),
        'day_elapsed': timedelta(0)
    },
    'first_join': 0,
    'gamemode': 0
}
special_roles = ["witch", "hunter", "amor", "seer", "bodyguard", "wild_kid"]


def get_time():
    """Returns current time.

    Returns:
        str: Formatted time in HH:MM:SS format.
    """
    return f"[{datetime.now().strftime('%H:%M:%S')}] "


def log(level: int, message: str):
    """Logs input to console.

    Args:
        level (int): Log level (0: Debug, 1: Info, 2: Warning, 3: Error)
        message (str): The message that will be logged in console
    """
    prefix = {0: f'{util.Colours.DEBUG}[DEBUG] ',
              1: f'{util.Colours.INFO}[INFO] ',
              2: f'{util.Colours.WARNING}[WARNING] ',
              3: f'{util.Colours.ERROR}[ERROR] '
              }
    suffix = f'{util.Colours.END}'
    print(f'{prefix[level]}{get_time()}{message}{suffix}')


LANGUAGE = "de-DE"


async def load_language():
    global translations
    try:
        with open(f"lang/{LANGUAGE}.json") as f:
            translations = json.load(f)
            f.close()
    except FileNotFoundError:
        log(3, "Language file not found. Terminating.")
        exit()


client = commands.Bot(command_prefix="-", intents=intents)


async def game_board():
    """Sends game board into the game channel based on current game status
    """
    global sent_message
    global game_status
    if game_status == "waiting":
        message = await get_game_board()
        sent_message = await client.get_channel(LOBBY_CHANNEL).send(message)
    elif game_status == "closed":
        message = "**GAME OVER**\nThanks for playing!\n\n_powered by Luftways_"
        sent_message = await client.get_channel(LOBBY_CHANNEL).send(message)
        game_status = None


async def get_game_board():
    return f"**Werewolf**\nSpieler: {len(player_list)}"


async def get_token():
    with open("token.key") as f:
        return f.read()


async def get_msg(id:str):
    """Gets and returns a random message from the message file

    Args:
        id (str): ID can be found in the json language file

    Returns:
        str: Returns a randomly picked message based on given ID
    """
    return random.choice(translations[id])


async def dm(user:int, msg:str):
    """Sends a direct message to specified user.

    Args:
        user (int): Discord user-id of the user the message should be sent to
        msg (str): The message delivered to the user
    """
    try:
        await user.send(msg)
    except discord.Forbidden:
        log(2, f"Couldn't DM {user.name}. Error Code: Onion")


async def dm_all(msg:str):
    """Sends a direct message to all users on the player list

    Args:
        msg (str): The message delivered to all users
    """
    for player in player_list:
        await dm(player, msg)


async def assign(player:int, role:str):
    """Assigns chosen role to a player

    Args:
        player (int): Discord User-ID
        role (str): Role-ID found in roles file
    """
    log(0, f"Assigning {role} to {player}")
    player_dict[player]["role"] = role
    user = client.get_user(player)
    if role == "werewolf":
        wolves_list.append(user)
    elif role == "witch":
        witch = user
    elif role == "hunter":
        hunter = user
    elif role == "wild_kid":
        wild_kid = user
    await dm(user, f"You have been assigned the role **{role}**.")


@client.event
async def on_ready():
    log(1, "Logged in as:")
    log(1, f"{client.user.name}")
    log(1, f"{client.user.id}")
    log(1, f"--------------------")
    await client.change_presence(status=discord.Status.online)


@client.command()
async def version(ctx):
    await ctx.send(f"Current version: {VERSION}")


@client.command()
@has_role("Captain")
async def reload(ctx):
    log(1, "Reloading...")
    log(1, "Reloading language file.")
    await load_language()
    log(1, "Reload complete!")


@client.command()
@has_role("Captain")
async def closeclient(ctx):
    await client.change_presence(status=discord.Status.offline, activity=None)
    await client.close()


@client.command()
@has_role(GAME_MASTER)
async def opengame(ctx):
    global game_status
    game_status = "waiting"
    await game_board()


@client.command()
@has_role(GAME_MASTER)
async def closegame(ctx):
    global game_status
    global player_list
    game_status = "closed"
    await game_board()
    log(0, "Closing session...")
    await client.change_presence(status=discord.Status.online, activity=None)
    for player in player_list:
        user = client.get_user(player)
        await user.send(
            f"The game you were in was closed by the session host. Thanks for playing!\n\n_powered by Luftways_")
    log(1, "Session closed.")


@client.command()
async def join(ctx):
    global player_list
    global player_dict
    player = ctx.message.author

    if game_status == "waiting":
        if ctx.message.author.id in player_list:
            await ctx.send(f"{player.mention}, you are already on the list.")
            return
        player_list.append(player.id)
        log(0, f"Updated player list: {player_list}")

        player_dict[player.id] = {"name": f"{player.name}",
                                  "is_alive": True,
                                  "role": None,
                                  "primary": None,
                                  "secondary": None
                                  }

        log(0, f"Updated player dictionary: {player_dict}")
        await game_board()

        try:
            await player.send("You're in the queue for Werewolf. GLHF!")
        except discord.Forbidden:
            log(2, f"Couldn't DM {player}. Error code: EICHHÖRNCHEN")

    elif game_status == "running":
        await ctx.send(f"{player.mention}, a game is already in progress.")


@client.command()
async def leave(ctx):
    global player_list
    global player_dict
    if game_status == "waiting":
        if ctx.message.author.id not in player_list:
            ctx.send(f"{ctx.message.author.mention}, you aren't on the list.")
            return
        player_list.remove(ctx.message.author.id)
        log(0, f"Updated player list: {player_list}")

        player_dict.pop(ctx.message.author.id)
        log(0, f"Updated player dictionary: {player_dict}")

        await game_board()


@client.command()
@has_role(GAME_MASTER)
async def start(ctx):
    global game_phase
    global player_list
    global wolves_list
    global witch
    global hunter
    global idol
    global wild_kid

    game_phase = str
    wolves_list = list
    witch = str
    hunter = str
    idol = str
    wild_kid = str

    if len(player_list) <= util.get_setting('min_players'):
        await ctx.send(get_msg("shortqueue"))
        return
    log(1, "Assigning roles.")

    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Werewolf"))

    max_werewolves = round(len(player_list) // 3, 9)
    assigned_specials = []

    for player in player_list:
        if random.random() < 25:
            assigned_role = "werewolf"
            max_werewolves - 1
            await assign(player, assigned_role)
            continue
        elif random.random() < 60:
            while True:
                assigned_role = random.choice(special_roles)
                if assigned_role not in assigned_specials:
                    await assign(player, assigned_role)
                    assigned_specials.append(assigned_role)
                    break
                elif assigned_role in assigned_specials and len(assigned_specials) << len(special_roles):
                    continue
                else:
                    await assign(player, "villager")
                    break
        else:
            await assign(player, "villager")
    log(1, f"{len(player_list)} roles assigned. Special roles: {assigned_specials}")


@client.command()
@has_role(GAME_MASTER)
async def night(ctx):
    global game_phase
    if game_phase == "night":
        ctx.send(get_msg("alreadynight"))
        return
    await dm_all(get_msg("sunset"))
    game_phase = "night"


@client.command()
@has_role(GAME_MASTER)
async def day(ctx):
    global game_phase
    if game_phase == "day":
        ctx.send(get_msg("alreadyday"))
        return
    await dm_all(get_msg("sunrise"))
    game_phase = "day"


@client.command()
@has_role(GAME_MASTER)
async def eliminate(ctx, player):
    pass


@client.command()
@has_role(GAME_MASTER)
async def wolves(ctx):
    pass


client.run(util.get_config('token'))
