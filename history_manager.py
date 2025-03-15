import os
import pandas as pd
from config import HISTORY_FILE, logger

class HistoryManager:
    """Manages the history of calculations, including saving and loading."""

    def __init__(self):
        """Initialize history by loading existing data if available."""
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.load_history()

    def add_entry(self, operation, operand1, operand2, result):
        """Add a new calculation entry and save it."""
        new_entry = pd.DataFrame([{
            "operation": operation,
            "operand1": operand1,
            "operand2": operand2,
            "result": result
        }])

        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.save_history()
        logger.info(f"New entry added: {operation} {operand1} {operand2} = {result}")

    def save_history(self):
        """Save history to CSV."""
        self.history.to_csv(HISTORY_FILE, index=False)
        logger.info(f"History saved to {HISTORY_FILE}")

    def load_history(self):
        """Load history from CSV if available."""
        if os.path.exists(HISTORY_FILE):
            try:
                self.history = pd.read_csv(HISTORY_FILE)
                logger.info("History loaded successfully.")
            except pd.errors.EmptyDataError:
                logger.warning("History file exists but is empty.")

    def show_history(self):
        """Display calculation history in a readable format."""
        if self.history.empty:
            logger.info("No calculation history available.")
            return "No calculation history available."
        return self.history.to_string(index=False)

    def clear_history(self):
        """Clear the calculation history."""
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.save_history()
        logger.info("History cleared successfully.")

    def delete_history(self):
        """Delete the history file completely."""
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
            logger.info("History file deleted.")
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

history_manager = HistoryManager()  # Singleton instance

