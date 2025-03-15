import pytest
from calculator.core import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 5) == 8

def test_subtract(calculator):
    assert calculator.subtract(10, 4) == 6

def test_multiply(calculator):
    assert calculator.multiply(3, 3) == 9

def test_divide(calculator):
    assert calculator.divide(8, 2) == 4

def test_divide_by_zero(calculator):
    assert calculator.divide(8, 0) == "Error: Cannot divide by zero"

