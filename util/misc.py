from datetime import datetime
from util.config import BUILD, COMMIT, VERSION


class Colours:
    HEADER = '\033[95m'
    INFO = '\033[96m'
    DEBUG = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'


def get_time():
    """Returns current time in format [HH:MM:SS]

    Returns:
        str: Current time
    """
    return f"[{datetime.now().strftime('%H:%M:%S')}] "