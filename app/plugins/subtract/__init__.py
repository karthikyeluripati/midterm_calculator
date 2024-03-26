from app.commands import Command
import logging
import pandas as pd

class SubtractCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result= num1-num2
        print(result)
        df=pd.DataFrame(columns=['Subtraction',f'{num1}',f'{num2}',f'{result}'])
        df.to_csv("./app/history.csv", mode="a", index=False)
        logging.info("Performed Subtraction") 