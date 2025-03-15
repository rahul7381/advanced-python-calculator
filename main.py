import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def main():
    """Main entry point for the calculator application."""
    try:
        from app.main import App  # Importing App class from the new location
        app = App().start()  # Instantiate and start the App
    except Exception as e:
        logger.error(f"An error occurred while running the application: {str(e)}")

if __name__ == "__main__":
    main()

