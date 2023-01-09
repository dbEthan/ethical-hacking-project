# Source used: https://www.geeksforgeeks.org/python-get-list-of-running-processes/
# A module that will retrieve a list of active processes on Windows OS.
import wmi
from rich import print as rprint


def run(**args):
    rprint("[*] Listing processes.")

    f = wmi.WMI()
    message = "pid\tProcess name\n"
    for process in f.Win32_Process():
        message += f"{process.ProcessId:<10}\t{process.Name}\n"

    return message
