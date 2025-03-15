import logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)  # Logger for tracking calculations

    def add(self, a, b):
        result = a + b
        self.logger.info(f"Adding {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.logger.info(f"Subtracting {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.logger.info(f"Multiplying {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self.logger.error("Attempted to divide by zero")
            return "Error: Cannot divide by zero"
        result = a / b
        self.logger.info(f"Dividing {a} / {b} = {result}")
        return result

