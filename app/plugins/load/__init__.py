from app.commands import Command
import logging
import pandas as pd
class LoadHistoryCommand(Command):
    def execute(self):
        try:
            # Assuming your history file is in CSV format
            history_file_path = "./app/history.csv"
            # Load the history file into a pandas DataFrame
            history_df = pd.read_csv(history_file_path)
            logging.info("Loading history...")
            print(history_df)
            logging.info("History Loaded")
        except:
            logging.error("Parsing data error")