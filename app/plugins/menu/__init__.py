from app.commands import Command
import os
import logging

class MenuCommand(Command):
    def execute(self):
        print("Available Plugins:")
        plugin_files=[f for f in os.listdir("./app/plugins") if f != '__init__.py' and f != '__pycache__']
        logging.info("All plugins Collected")
        for plugin_file in plugin_files:
                print(f"- {plugin_file}")
        logging.info("Displayed All plugins")