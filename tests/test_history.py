import pytest
import os
from calculator.history import CalculationHistory

@pytest.fixture
def history():
    hist = CalculationHistory("test_history.csv")
    hist.clear_history()  # Ensure fresh history
    return hist

def test_add_record(history):
    history.add_record("add", 2, 3, 5)
    assert not history.history.empty

def test_clear_history(history):
    history.add_record("add", 2, 3, 5)
    history.clear_history()
    assert history.history.empty

def test_delete_history_file(history):
    history.delete_history_file()
    assert not os.path.exists(history.filename)

def test_display_history(history):
    history.add_record("multiply", 4, 5, 20)
    assert "multiply" in history.display_history()

def test_load_history(history):
    history.add_record("divide", 8, 2, 4)
    history.load_history()
    assert "divide" in history.history.to_string()

