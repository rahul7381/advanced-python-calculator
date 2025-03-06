import logging
import pandas as pd
import os

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        self.history_file = os.getenv("HISTORY_FILE", "history.csv")
        self.history = []

    def add(self, a, b):
        result = a + b
        self.save_to_history(a, b, "+", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.save_to_history(a, b, "-", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.save_to_history(a, b, "*", result)
        return result

    def divide(self, a, b):
        if b == 0:
            logger.error("Division by zero error.")
            return "Error: Division by zero"
        result = a / b
        self.save_to_history(a, b, "/", result)
        return result

    def save_to_history(self, a, b, operation, result):
        self.history.append([a, b, operation, result])
        df = pd.DataFrame(self.history, columns=["A", "B", "Operation", "Result"])
        df.to_csv(self.history_file, index=False)

    def show_history(self):
        try:
            df = pd.read_csv(self.history_file)
            print(df)
        except FileNotFoundError:
            print("No history found.")

def main():
    calculator = Calculator()
    print("Welcome to Advanced Python Calculator")
    while True:
        command = input("Enter command (add, sub, mul, div, history, exit): ").strip().lower()
        if command == "exit":
            break
        elif command in ["add", "sub", "mul", "div"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if command == "add":
                    print("Result:", calculator.add(a, b))
                elif command == "sub":
                    print("Result:", calculator.subtract(a, b))
                elif command == "mul":
                    print("Result:", calculator.multiply(a, b))
                elif command == "div":
                    print("Result:", calculator.divide(a, b))
            except ValueError:
                logger.error("Invalid input. Please enter numeric values.")
        elif command == "history":
            calculator.show_history()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

