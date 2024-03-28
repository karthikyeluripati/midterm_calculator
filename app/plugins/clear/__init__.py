"""Clear Operation"""
import logging
import pandas as pd
from app.commands import Command

class ClearCommand(Command):
    """Clear Operation using clear"""
    def execute(self):
        f = open("./app/history.csv", "w")
        f.truncate()
        f.close()
        logging.info("History Deleted")
        df = pd.DataFrame(columns=["Expression", "num1", "num2","Result"])
        df.to_csv("./app/history.csv", index=False)
        logging.info("History Header updated")
