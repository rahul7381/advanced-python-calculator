import pandas as pd
import os

class CalculationHistory:
    def __init__(self, filename="history.csv"):
        self.filename = filename
        self.columns = ["Operation", "Equation", "Operand1", "Operand2", "Result"]

        if os.path.exists(self.filename):
            self.load_history()
        else:
            self.history = pd.DataFrame(columns=self.columns)

    def add_record(self, operation, operand1, operand2, result):
        if operation == "expression":
            new_record = pd.DataFrame(
                [[operation, operand1, "", "", str(result)]],  # Store equation, leave operands empty
                columns=["Operation", "Equation", "Operand1", "Operand2", "Result"]
            )
        else:
            new_record = pd.DataFrame(
                [[operation, "", operand1, operand2, str(result)]],  # Store operands, leave equation empty
                columns=["Operation", "Equation", "Operand1", "Operand2", "Result"]
            )

        if self.history.empty:
            self.history = new_record
        else:
            self.history = pd.concat([self.history, new_record], ignore_index=True)

        self.save_history()
        self.load_history()  # Ensure history reloads properly

    def save_history(self):
        self.history.to_csv(self.filename, index=False)

    def load_history(self):
        try:
            self.history = pd.read_csv(self.filename, dtype=str)  # Store all values as string to avoid NaN issues
        except pd.errors.EmptyDataError:
            self.history = pd.DataFrame(columns=self.columns)

    def clear_history(self):
        self.history = pd.DataFrame(columns=self.columns)
        self.save_history()

    def delete_history_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            self.history = pd.DataFrame(columns=self.columns)

    def display_history(self):
        if self.history.empty:
            return "No history found."
        return self.history.fillna("-").to_string(index=False)

