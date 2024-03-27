from app.commands import Command
import logging
import pandas as pd
class ClearCommand(Command):
    def execute(self):
        f = open("./app/history.csv", "w")
        f.truncate()
        f.close()
        logging.info("History Deleted")
        df = pd.DataFrame(columns=["Expression", "num1", "num2","Result"])
        df.to_csv("./app/history.csv", index=False)
        logging.info("History Header updated")