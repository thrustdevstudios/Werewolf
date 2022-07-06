import json
import random


def get(message_id: str) -> str:
    with open('lang/de-DE.json') as f:
        language = json.load(f)
        if message_id in language.keys():
            message = random.choice(language[message_id])
            return message
        else:
            return None
