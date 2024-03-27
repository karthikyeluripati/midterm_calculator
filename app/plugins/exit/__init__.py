import sys
from app.commands import Command
import logging


class ExitCommand(Command):
    def execute(self):
        logging.info("Application exit.")
        sys.exit("Exiting...")
