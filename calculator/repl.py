import logging
import os
import csv
from calculator.core import Calculator
from calculator.history import CalculationHistory
from calculator.logger import get_logger
from calculator.plugin_manager import PluginManager


class CalculatorREPL:
    def __init__(self):
        self.logger = logging.getLogger("CalculatorREPL")
        logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO").upper())
        self.history = self.load_history()  # Load history from file on startup

        self.command_map = {
            "add": self.execute_operation,
            "sub": self.execute_operation,
            "mul": self.execute_operation,
            "div": self.execute_operation,
            "+": self.execute_operation,
            "-": self.execute_operation,
            "*": self.execute_operation,
            "/": self.execute_operation
        }

    def start(self):
        """Start the REPL (Read-Eval-Print Loop)"""
        print("Welcome to the Advanced Python Calculator!")
        print("Commands: add 5 3 | sub 5 3 | mul 5 3 | div 5 3 | history | clear | delete | exit")
        print("You can also enter an operation (+, -, *, /) and be prompted for numbers.")

        while True:
            try:
                command = input(">>> ").strip().lower()

                # Exit condition
                if command == "exit":
                    print("Exiting...")
                    break

                # If the command contains an operation, attempt to evaluate the equation directly
                if command in ['+', '-', '*', '/']:
                    self.get_numbers_and_execute(command)
                elif "=" in command:
                    self.evaluate_equation(command)  # Evaluate full equation (e.g., 5+3*2)
                # If the command is an equation (e.g., '3+3*3')
                elif self.is_equation(command):
                    self.evaluate_equation(command)
                elif command == "history":
                    self.show_history()  # Handle history command
                elif command == "clear":
                    self.clear_history()  # Clear history command
                    print("Calculation history cleared.")
                elif command == "delete":
                    self.delete_history()  # Delete history command
                    print("History file deleted.")
                elif any(op in command for op in self.command_map):
                    self.process_command(command)  # Process regular operations
                else:
                    print("Unknown command.")

            except KeyboardInterrupt:
                print("\nExiting calculator.")
                break
            except Exception as e:
                self.logger.error(f"Error: {e}")
                print(f"Error: {e}")

    def is_equation(self, command):
        """Check if the input is a mathematical equation"""
        return any(op in command for op in ['+', '-', '*', '/'])

    def process_command(self, command):
        """Process commands like 'add 5 3', 'history', 'clear', etc."""
        parts = command.split()

        if len(parts) == 1:
            if parts[0] in self.command_map:
                # Case where only the operator is entered like '+' or '-'
                self.get_numbers_and_execute(parts[0])
                return
            elif parts[0] == "exit":
                print("Exiting...")
                return
            else:
                print("Unknown command.")
                return
        elif len(parts) == 3 and parts[0] in self.command_map:
            # Command with two operands like 'add 4 5'
            operation = parts[0]
            try:
                num1 = float(parts[1])
                num2 = float(parts[2])
                self.execute_operation(operation, num1, num2)
            except ValueError:
                print("Invalid input. Please provide valid numbers.")
        else:
            print("Invalid command. Use: add 5 3")

    def execute_operation(self, operator, num1, num2):
        """Handles basic operations (+, -, *, /)."""
        result = None
        if operator == "add" or operator == "+":
            result = num1 + num2
        elif operator == "sub" or operator == "-":
            result = num1 - num2
        elif operator == "mul" or operator == "*":
            result = num1 * num2
        elif operator == "div" or operator == "/":
            if num2 == 0:
                result = "Error: Cannot divide by zero"
            else:
                result = num1 / num2

        # Store the result in history
        if isinstance(result, str) and "Error" in result:
            self.history.append({
                "operation": operator,
                "equation": "-",
                "operand1": num1,
                "operand2": num2,
                "result": result
            })
        else:
            self.history.append({
                "operation": operator,
                "equation": f"{num1} {operator} {num2}",
                "operand1": num1,
                "operand2": num2,
                "result": result
            })

        print(result)

        # Save history to file after operation
        self.save_history()

    def get_numbers_and_execute(self, operator):
        """Prompt for numbers and execute the operation."""
        try:
            num1 = float(input(f"Enter first number for '{operator}': "))
            num2 = float(input(f"Enter second number for '{operator}': "))
            self.execute_operation(operator, num1, num2)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    def show_history(self):
        """Show history in the desired format."""
        if not self.history:
            print("No history found.")
        else:
            print(f"{'Operation':<12} {'Equation':<20} {'Operand1':<10} {'Operand2':<10} {'Result':<10}")
            for record in self.history:
                print(f"{record['operation']:<12} {record['equation']:<20} {record['operand1']:<10} {record['operand2']:<10} {record['result']:<10}")

    def clear_history(self):
        """Clear history."""
        self.history = []
        self.save_history()
        print("Calculation history cleared.")

    def delete_history(self):
        """Delete history."""
        self.history = []
        if os.path.exists("history.csv"):
            os.remove("history.csv")
        print("History file deleted.")

    def save_history(self):
        """Save history to a CSV file."""
        with open("history.csv", "w", newline="") as csvfile:
            fieldnames = ["operation", "equation", "operand1", "operand2", "result"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for record in self.history:
                writer.writerow(record)

    def load_history(self):
        """Load history from the CSV file."""
        if os.path.exists("history.csv"):
            with open("history.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                history = []
                for row in reader:
                    operand1 = row["operand1"]
                    operand2 = row["operand2"]

                    # Handle empty strings and invalid float values
                    operand1 = float(operand1) if operand1 and operand1 != "-" else None
                    operand2 = float(operand2) if operand2 and operand2 != "-" else None
                    
                    history.append({
                        "operation": row["operation"],
                        "equation": row["equation"],
                        "operand1": operand1,
                        "operand2": operand2,
                        "result": row["result"]
                    })
                return history
        return []

    def show_menu(self):
        print("Available Plugins: ...")  # Add your plugin list here

    def evaluate_equation(self, equation):
        """Evaluate a full equation (e.g., 5+3*2)."""
        try:
            # Remove all spaces from the equation string and evaluate it
            result = eval(equation)
            print(result)
            # Save equation and result in history
            self.history.append({
                "operation": "expression",
                "equation": equation,
                "operand1": "-",
                "operand2": "-",
                "result": result
            })
            self.save_history()
        except Exception as e:
            print(f"Error evaluating equation: {e}")


if __name__ == "__main__":
    CalculatorREPL().start()
