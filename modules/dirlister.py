import os

def run(**args):
    print("[*] in the dirlister module.")
    files = os.listdir('.')
    return str(files)