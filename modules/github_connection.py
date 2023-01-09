import github3

username = 'dbEthan'
repository = 'ethical-hacking-project'


def github_connect():
    with open('mytoken.txt') as f:
        token = f.read()
    sess = github3.login(token=token)
    return sess.repository(username, repository)


def get_file_contents(dir_name, module_name, repo):
    return repo.file_contents(f'{dir_name}/{module_name}').content