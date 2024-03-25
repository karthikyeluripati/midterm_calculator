from app.commands import Command
import logging

class DivideCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        try:
                result= num1/num2
                print(result)
                logging.info("Performed Division")
        except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
