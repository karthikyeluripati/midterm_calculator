"""Multiply Operation"""
import logging
import pandas as pd
from app.commands import Command

class MultiplyCommand(Command):
    """Multiply Operation using multiply"""
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result= num1*num2
            logging.info(f"Performing Multiplication with {num1} and {num2}")
            print(result)
            df=pd.DataFrame(columns=['Multiply',f'{num1}',f'{num2}',f'{result}'])
            df.to_csv("./app/history.csv", mode="a", index=False)
            logging.info(f"History updated with {result}")
        except:
            logging.error("Invalid input. Enter only numbers")
