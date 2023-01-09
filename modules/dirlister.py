import os
from rich import print as rprint

def run(**args):
    rprint("[ :warning: ] in the dirlister module.")
    files = os.listdir('.')
    result=[]
    result.append("Dirlijster:")
    result.append(files)
    return result