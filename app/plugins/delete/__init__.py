"""Delete Operation"""
import logging
import pandas as pd
from app.commands import Command

class DeleteHistoryCommand(Command):
    """Delete Operation using delete"""
    def execute(self):
        try:
            # Assuming your history file is in CSV format
            history_file_path = "./app/history.csv"
            # Load the history file into a pandas DataFrame
            logging.info("Retrieving current hsitory")
            history_df = pd.read_csv(history_file_path)
            print(history_df)
            try:
                index=int(input("Enter index to delete: "))
                logging.info(f"Performing deletion of index {index}...")
                history_df=history_df.drop(index=index)
                logging.info(f"Deleted: {index}")
                print(history_df)
                history_df.to_csv("./app/history.csv", mode="w", index=False)
                logging.info(f"updated history after deleting index {index}")
            except IndexError:
                logging.error(f"Invalid index: {index}")
        except:
            logging.error("Invalid input")
