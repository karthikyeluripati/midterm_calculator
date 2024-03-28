"""Exit Operation"""
import sys
import logging
from app.commands import Command


class ExitCommand(Command):
    """Exit Operation using exit"""
    def execute(self):
        logging.info("Application exit.")
        sys.exit("Exiting...")
