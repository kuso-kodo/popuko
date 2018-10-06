from os import path

import none


def init(config):
    none.init(config)
    bot = none.get_bot()
    none.load_builtin_plugins()
    none.load_plugins(path.join(path.dirname(__file__), 'plugins'),
                      'popuko.plugins')
    return bot
