import sys
from app.commands import Command
import logging


class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")
        logging.info("Application exit.")