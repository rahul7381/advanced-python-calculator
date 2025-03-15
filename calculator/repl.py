import sys
from calculator.core import Calculator
from calculator.history import CalculationHistory
from calculator.logger import get_logger
from calculator.plugin_manager import PluginManager

class CalculatorREPL:
    def __init__(self):
        self.running = True
        self.calculator = Calculator()
        self.history = CalculationHistory()
        self.logger = get_logger(__name__)
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()

        self.command_map = {
            "add": "add", "+": "add",
            "subtract": "subtract", "sub": "subtract", "-": "subtract",
            "multiply": "multiply", "mul": "multiply", "*": "multiply",
            "divide": "divide", "div": "divide", "/": "divide",
            "history": "history",
            "clear": "clear",
            "delete": "delete",
        }

    def start(self):
        print("Welcome to the Advanced Python Calculator!")
        print("Commands: add 5 3 | history | clear | delete | exit")
        print("You can also enter an operation (+, -, *, /) and be prompted for numbers.")

        while self.running:
            try:
                command = input(">>> ").strip().lower()
                if command == "exit":
                    self.running = False
                else:
                    self.process_command(command)
            except KeyboardInterrupt:
                print("\nExiting calculator.")
                self.running = False
            except Exception as e:
                self.logger.error(f"Error: {e}")
                print(f"Error: {e}")

    def process_command(self, command):
        parts = command.split()

        if len(parts) == 1:
            if parts[0] == "history":
                self.show_history()
                return
            elif parts[0] == "clear":
                self.history.clear_history()
                print("Calculation history cleared.")
                return
            elif parts[0] == "delete":
                self.history.delete_history_file()
                print("History file deleted.")
                return
            elif parts[0] == "menu":
                self.list_plugins()
                return
            elif parts[0] in self.command_map:
                operation = self.command_map[parts[0]]
                num1, num2 = self.get_numbers()
                if num1 is not None and num2 is not None:
                    self.execute_operation(operation, num1, num2)
                return
            else:
                print("Unknown command.")
                return

    def get_numbers(self):
        """Prompts the user for two numbers and ensures they are valid floats."""
        while True:
            num1 = input("Enter first number: ").strip()
            if num1 == "":
                print("Input cannot be empty. Please enter a numeric value.")
                continue
            try:
                num1 = float(num1)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        while True:
            num2 = input("Enter second number: ").strip()
            if num2 == "":
                print("Input cannot be empty. Please enter a numeric value.")
                continue
            try:
                num2 = float(num2)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        return num1, num2

    def execute_operation(self, operation, num1, num2):
        if operation == "add":
            result = self.calculator.add(num1, num2)
        elif operation == "subtract":
            result = self.calculator.subtract(num1, num2)
        elif operation == "multiply":
            result = self.calculator.multiply(num1, num2)
        elif operation == "divide":
            result = self.calculator.divide(num1, num2)  # This will return "Error: Cannot divide by zero"
        else:
            print("Unknown operation.")
            return

        print(result)
        self.history.add_record(operation, num1, num2, result)  # Store result even if it's an error

    def show_history(self):
        history_output = self.history.display_history()
        print(history_output)

if __name__ == "__main__":
    CalculatorREPL().start()

