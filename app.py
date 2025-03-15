import logging
from app.commands import CommandHandler
from app.plugins import load_plugins
from history_manager import HistoryManager
from config import logger

class App:
    """
    Main application class that runs the calculator.
    """

    def __init__(self):
        """Initializes the application"""
        self.command_handler = CommandHandler()
        self.plugins = load_plugins()
        self.history_manager = HistoryManager()  # History Manager Instance

        # Register plugins
        for name, plugin in self.plugins.items():
            self.command_handler.register_command(name, plugin)

    def start(self):
        """Starts the REPL for the calculator"""
        logger.info("Application started!")
        print("Welcome to the Advanced Python Calculator (Type 'exit' to quit)")

        while True:
            command = input("Enter command (+, -, *, /, csv, menu, history, load_history, clear_history, exit): ").strip()

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "menu":
                print("Available commands:", ", ".join(self.command_handler.commands.keys()))

            elif command == "history":
                print(self.history_manager.show_history())  # Show history

            elif command == "load_history":
                self.history_manager.load_history()
                print("History loaded successfully!")

            elif command == "clear_history":
                self.history_manager.clear_history()
                print("History cleared.")

            elif command in ["+", "-", "*", "/"]:
                try:
                    operand1 = float(input("Enter first number: "))
                    operand2 = float(input("Enter second number: "))

                    if command == "+":
                        result = operand1 + operand2
                    elif command == "-":
                        result = operand1 - operand2
                    elif command == "*":
                        result = operand1 * operand2
                    elif command == "/":
                        if operand2 == 0:
                            result = "Error: Division by zero"
                        else:
                            result = operand1 / operand2

                    print(f"Result: {result}")

                    # 🔹 **Store ALL results, including error messages, in history**
                    self.history_manager.add_entry(command, operand1, operand2, str(result))  

                except ValueError:
                    print("Invalid input. Please enter a number.")

            elif command == "csv":
                if "csv" in self.plugins:
                    csv_command = self.plugins["csv"]
                    csv_command.execute(self.history_manager)
                else:
                    print("CSV export functionality is not available.")

            else:
                self.command_handler.execute_command(command)

