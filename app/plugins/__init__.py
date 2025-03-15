import logging
from app.plugins.csv import CsvCommand  # Importing the CSV Plugin

def load_plugins(history_manager):
    """
    Dynamically load plugins and return a dictionary of available plugin commands.
    Now, accepting history_manager to pass it to the plugins.
    """
    logging.info("Loading plugins...")

    plugins = {
        "csv": CsvCommand(history_manager),  # Pass history_manager to the CsvCommand plugin
    }

    logging.info(f"Plugins loaded: {list(plugins.keys())}")  # Log the loaded plugins
    return plugins

