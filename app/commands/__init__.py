from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
            logging.info(f"{command_name} operation complete")
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error("Invalid input provided")
