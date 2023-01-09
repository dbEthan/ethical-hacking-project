# Source used: https://www.geeksforgeeks.org/python-get-list-of-running-processes/
# A module that will retrieve a list of active processes on Windows OS.
import os
from rich import print as rprint


def run(**args):
    rprint("[*] Listing processes.")

    message = os.popen('wmic process get description, processid').read()

    rprint(f" :blue: {message}")
    return message
