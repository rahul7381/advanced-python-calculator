import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class CsvCommand:
    def __init__(self, history_manager):
        """Initialize CSV export paths."""
        self.history_manager = history_manager  # Accepting history_manager here
        self.output_dir = "data"
        self.history_file = os.path.join(self.output_dir, "history.csv")
        self.states_file = os.path.join(self.output_dir, "states.csv")

        # Ensure the output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_history(self):
        """Exports calculation history to a CSV file."""
        try:
            if os.path.exists(self.history_manager.history_file):
                df = pd.read_csv(self.history_manager.history_file)

                if not df.empty:
                    df.to_csv(self.history_file, index=False)
                    logger.info("History CSV file saved at: %s", self.history_file)
                    print(f"History CSV file saved at: {self.history_file}")
                else:
                    logger.warning("No history data available to save.")
                    print("No history data available to save.")
            else:
                logger.warning("History file not found.")
                print("History file not found.")

        except Exception as e:
            logger.error("Error exporting history: %s", str(e))
            print(f"Error exporting history: {e}")

    def save_states(self):
        """Exports predefined states data to a CSV file."""
        try:
            states_data = {
                "State": ["California", "Texas", "New York", "Florida", "Illinois"],
                "Abbreviation": ["CA", "TX", "NY", "FL", "IL"],
                "Population (millions)": [39.24, 30.3, 19.5, 22.3, 12.8]
            }
            df = pd.DataFrame(states_data)

            df.to_csv(self.states_file, index=False)
            logger.info("States CSV file saved at: %s", self.states_file)
            print(f"States CSV file saved at: {self.states_file}")

        except Exception as e:
            logger.error("Error exporting states data: %s", str(e))
            print(f"Error exporting states data: {e}")

    def execute(self):
        """Executes the CSV export command."""
        self.save_history()
        self.save_states()

