from app.commands import Command
import logging
import pandas as pd

class DivideCommand(Command):
    def execute(self):
        try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result= num1/num2
                logging.info(f"Performing division with {num1} and {num2}")
                print(result)
                df=pd.DataFrame(columns=['Division',f'{num1}',f'{num2}',f'{result}'])
                df.to_csv("./app/history.csv", mode="a", index=False)
                logging.info(f"History updated with {result}")
        except ZeroDivisionError:
                logging.error("Error: Cannot divide by zero.")
        except:
                logging.error("Invalid input. Enter only numbers")
