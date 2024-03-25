# File: app/plugins/delete_history_plugin.py

from app.commands import Command
import pandas as pd
import os

class DeleteHistoryCommand(Command):
    def execute(self):
        history_file = './app/history.csv'
        if not os.path.exists(history_file) or os.path.getsize(history_file) == 0:
            print("History is empty.")
            return

        try:
            index = int(input("Enter the index of the entry to delete: "))
            history_df = pd.read_csv(history_file)
            history_df = history_df.drop(index)
            history_df = history_df.reset_index(drop=True)  # Reset index after dropping row
            history_df.to_csv(history_file, index=False)
            print(f"Entry at index {index} deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting the entry: {e}")
