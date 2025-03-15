import sys
from calculator.core import Calculator

class CalculatorREPL:
    def __init__(self):
        self.running = True
        self.calculator = Calculator()
        self.command_map = {
            "add": "add",
            "subtract": "subtract",
            "sub": "subtract",
            "multiply": "multiply",
            "mul": "multiply",
            "divide": "divide",
            "div": "divide"
        }

    def start(self):
        print("Welcome to the Advanced Python Calculator!")
        print("Enter calculations in the format: add 5 3")
        print("Type 'exit' to quit.")

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
                print(f"Error: {e}")

    def process_command(self, command):
        parts = command.split()
        if len(parts) != 3:
            print("Invalid input. Format: add 5 3")
            return

        operation, num1, num2 = parts
        operation = self.command_map.get(operation, None)  # Convert shortcut to full command
        
        try:
            num1, num2 = float(num1), float(num2)
            if operation == "add":
                print(self.calculator.add(num1, num2))
            elif operation == "subtract":
                print(self.calculator.subtract(num1, num2))
            elif operation == "multiply":
                print(self.calculator.multiply(num1, num2))
            elif operation == "divide":
                print(self.calculator.divide(num1, num2))
            else:
                print("Unknown operation.")
        except ValueError:
            print("Invalid numbers.")

if __name__ == "__main__":
    CalculatorREPL().start()

