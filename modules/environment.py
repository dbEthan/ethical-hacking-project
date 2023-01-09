import os
from rich import print as rprint


def run(**args):
    rprint("[*] in the environment module.")
    output = os.environ

    rprint(f" :blue: {output}")
    return output