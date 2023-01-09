import os
from rich import print as rprint


def run(**args):
    rprint("[*] in the dirlister module.")
    files = os.listdir('.')
    result = ["Dirlijster:", files]

    rprint(f" :blue: {result}")
    return result
