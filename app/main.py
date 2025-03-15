import logging
from app.commands import CommandHandler
from app.plugins import load_plugins
from history_manager import HistoryManager  # Import the HistoryManager class

logger = logging.getLogger(__name__)

class App:
    def __init__(self):
        """Initializes the application"""
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()  # Create an instance of HistoryManager
        self.plugins = load_plugins(self.history_manager)  # Pass history_manager to load_plugins

        # Register plugins
        for name, plugin in self.plugins.items():
            self.command_handler.register_command(name, plugin)

    def start(self):
        """Starts the REPL for the calculator"""
        print("Welcome to the Advanced Python Calculator (Type 'exit' to quit)")
        while True:
            command = input("Enter command (+, -, *, /, csv, menu, history, exit): ").strip()
            if command == "exit":
                print("Goodbye!")
                break
            elif command == "menu":
                print("Available commands:", ", ".join(self.command_handler.commands.keys()))
            elif command == "history":
                self.history_manager.show_history()  # Show history
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
                        result = operand1 / operand2 if operand2 != 0 else "Error: Division by zero"
    
                    print(f"Result: {result}")  
                    self.history_manager.add_entry(command, operand1, operand2, result)  # Save to history
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                self.command_handler.execute_command(command)

