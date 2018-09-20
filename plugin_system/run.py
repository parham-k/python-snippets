from plugin_system import plugin_manager

if __name__ == '__main__':
    for plugin in plugin_manager.get_installed_plugins():
        print(plugin.main(n=10, words=['a', 'a', 'b', 'c', 'a', 'b', 'd', 'c']))
