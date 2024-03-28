"""Subtract Operation"""
import logging
import pandas as pd
from app.commands import Command

class SubtractCommand(Command):
    """Subtract Operation using subtract """
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result= num1-num2
            logging.info(f"Performing Subtraction with {num1} and {num2}")
            print(result)
            df=pd.DataFrame(columns=['subtract',f'{num1}',f'{num2}',f'{result}'])
            df.to_csv("./app/history.csv", mode="a", index=False)
            logging.info(f"History updated with {result}")
        except:
            logging.error("Invalid input. Enter only numbers")
