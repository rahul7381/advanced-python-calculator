import logging
from app.plugins.csv import CsvCommand  # Importing the CSV Plugin

def load_plugins():
    """
    Dynamically load plugins and return a dictionary of available plugin commands.
    """
    logging.info("Loading plugins...")
    
    plugins = {
        "csv": CsvCommand(),  # Register CSV plugin
    }

    logging.info(f"Plugins loaded: {list(plugins.keys())}")  # Log the loaded plugins
    return plugins

