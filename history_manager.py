import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename="history.csv"):
        self.filename = filename
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.load_history()

    def load_history(self):
        """Loads history from CSV if it exists and ensures correct columns"""
        if os.path.exists(self.filename):
            self.history = pd.read_csv(self.filename)
            
            # Keep only necessary columns and remove unwanted data
            expected_columns = ["operation", "operand1", "operand2", "result"]
            self.history = self.history[expected_columns]

    def save_history(self):
        """Saves history to CSV only if it contains data"""
        if not self.history.empty:
            self.history.to_csv(self.filename, index=False)

    def add_entry(self, operation, operand1, operand2, result):
        """Adds a calculation entry to history using pd.concat()"""
        new_entry = pd.DataFrame([{
            "operation": operation, 
            "operand1": operand1, 
            "operand2": operand2, 
            "result": result
        }])
        
        self.history = pd.concat([self.history, new_entry], ignore_index=True)  # ✅ Fix for Pandas 2.0+
        self.save_history()

    def clear_history(self):
        """Clears the history"""
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.save_history()

    def show_history(self):
        """Displays history cleanly"""
        if self.history.empty:
            print("No calculation history available.")
        else:
            print(self.history.to_string(index=False))

