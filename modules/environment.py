import os
from rich import print as rprint


def run(**args):
    rprint("[*] in the environment module.")
    return os.environ