# division_plugin.py
class DivisionPlugin:
    @staticmethod
    def perform_operation(x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
