from app.commands import Command
import pandas as pd
import os
import logging

class ClearHistoryCommand(Command):
    def execute(self):
        history_file = './app/history.csv'
        if not os.path.exists(history_file) or os.path.getsize(history_file) == 0:
            print("History is already empty.")
            return

        try:
            os.remove(history_file)
            print("History cleared successfully.")
        except Exception as e:
            print(f"An error occurred while clearing the history: {e}")
            logging.info("Cleared History")