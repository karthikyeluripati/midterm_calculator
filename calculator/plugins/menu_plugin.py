# plugins/menu_plugin.py

import os

def list_plugins():
    print("Available plugins:")
    plugin_files = [f for f in os.listdir('plugins') if f.endswith('.py') and f != '__init__.py']
    for plugin_file in plugin_files:
        plugin_name = plugin_file[:-3]  # Remove the '.py' extension
        print(f"- {plugin_name}")
