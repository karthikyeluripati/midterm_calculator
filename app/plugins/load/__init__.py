from app.commands import Command
import pandas as pd
import os
import logging

class LoadCommand(Command):
    def execute(self):
        self.history_file = './app/history.csv'
        try:
            self.history_df = pd.read_csv(self.history_file)
            print("History loaded successfully.")
            print("Loaded history:")
            print(self.history_df)
            logging.info("Loaded History")
        except FileNotFoundError:
            print("No history file found.")