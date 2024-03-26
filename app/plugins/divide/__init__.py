from app.commands import Command
import logging
import pandas as pd

class DivideCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        try:
                result= num1/num2
                print(result)
                df=pd.DataFrame(columns=['Divide',f'{num1}',f'{num2}',f'{result}'])
                df.to_csv("./app/history.csv", mode="a", index=False)
                logging.info("Performed Division")
        except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
