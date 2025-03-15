"""
This module defines basic arithmetic operations for the Advanced Python Calculator.
"""
from app.commands import Command
from history_manager import HistoryManager

history = HistoryManager()

class AdditionCommand:
    def execute(self, operand1, operand2):
        return operand1 + operand2

class SubtractionCommand:
    def execute(self, operand1, operand2):
        return operand1 - operand2

class MultiplicationCommand:
    def execute(self, operand1, operand2):
        return operand1 * operand2

class DivisionCommand:
    def execute(self, operand1, operand2):
        if operand2 == 0:
            return "Error: Division by zero"
        return operand1 / operand2

