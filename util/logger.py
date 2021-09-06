from util.misc import Colours, get_time


def log(level: int, message: str):
    prefix = {0: f'{Colours.DEBUG}[DEBUG] ',
              1: f'{Colours.INFO}[INFO] ',
              2: f'{Colours.WARNING}[WARNING] ',
              3: f'{Colours.ERROR}[ERROR] '
              }
    suffix = f'{Colours.END}'
    print(f'{prefix[level]}{get_time()}{message}{suffix}')
