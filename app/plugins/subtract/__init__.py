from app.commands import Command

class SubtractCommand(Command):
    def execute(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result= num1-num2
        print(result) 