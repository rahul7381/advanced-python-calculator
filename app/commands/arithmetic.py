from app.commands import Command
from history_manager import HistoryManager

history = HistoryManager()

class AddCommand(Command):
    def execute(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"Result: {result}")
        history.add_entry("+", num1, num2, result)

class SubtractCommand(Command):
    def execute(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"Result: {result}")
        history.add_entry("-", num1, num2, result)

class MultiplyCommand(Command):
    def execute(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"Result: {result}")
        history.add_entry("*", num1, num2, result)

class DivideCommand(Command):
    def execute(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            result = num1 / num2
            print(f"Result: {result}")
            history.add_entry("/", num1, num2, result)

