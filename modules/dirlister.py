import os

def run():
    print("[*] in the dirlister module.")
    files = os.listdir('.')
    return str(files)