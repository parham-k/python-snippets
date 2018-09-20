import os
import importlib


def get_installed_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    print(plugins_dir)
    plugins = []
    for f in os.listdir(plugins_dir):
        try:
            plugins.append(importlib.import_module(f'.{f}.main', 'plugins'))
        except ModuleNotFoundError:
            pass
    return plugins
