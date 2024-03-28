"""Commands and Operations"""
from abc import ABC, abstractmethod
import logging

class Command(ABC):
    """Design Patterns to Execute"""
    @abstractmethod
    def execute(self):
        """Command Executed"""

class CommandHandler:
    """Registering and Executing Commands"""
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Commands Registered"""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Operations performed"""
        try:
            self.commands[command_name].execute()
            logging.info(f"{command_name} operation complete")
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error("Invalid input provided")
