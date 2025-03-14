import logging
import os
import pandas as pd
from app.commands import Command

class CsvCommand(Command):
    def execute(self):
        """Generate and save a CSV file with sample state data."""
        logging.info("Executing CsvCommand...")

        # Ensure 'data' directory exists
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"Created directory: {data_dir}")

        # Create a CSV file with sample data
        states_abbreviations = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois',
            'NY': 'New York'
        }

        df = pd.DataFrame(list(states_abbreviations.items()), columns=['Abbreviation', 'State'])
        csv_file_path = os.path.join(data_dir, 'states.csv')
        df.to_csv(csv_file_path, index=False)
        
        print(f"CSV file saved at: {csv_file_path}")
        logging.info(f"CSV file saved at: {csv_file_path}")

