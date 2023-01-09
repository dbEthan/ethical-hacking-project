import os

def run(**args):
    print("[*] in the dirlister module.")
    files = os.listdir('.')
    result=[]
    result.append("Dirlijster:")
    result.append(files)
    return result