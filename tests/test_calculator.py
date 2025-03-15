import pytest
from app.app import App
from history_manager import HistoryManager
from config import HISTORY_FILE
import os
import pandas as pd

# Setup: Clear history before running tests
@pytest.fixture(scope="function")
def setup_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    return HistoryManager()

def test_addition(setup_history, monkeypatch):
    app = App()

    inputs = iter(["+", "4", "5", "exit"])  # Simulate user input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app.start()
    df = pd.read_csv(HISTORY_FILE)

    assert df.iloc[-1]["operation"] == "+"
    assert df.iloc[-1]["operand1"] == 4
    assert df.iloc[-1]["operand2"] == 5
    assert df.iloc[-1]["result"] == 9

def test_subtraction(setup_history, monkeypatch):
    app = App()

    inputs = iter(["-", "10", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app.start()
    df = pd.read_csv(HISTORY_FILE)

    assert df.iloc[-1]["operation"] == "-"
    assert df.iloc[-1]["operand1"] == 10
    assert df.iloc[-1]["operand2"] == 3
    assert df.iloc[-1]["result"] == 7

def test_multiplication(setup_history, monkeypatch):
    app = App()

    inputs = iter(["*", "3", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app.start()
    df = pd.read_csv(HISTORY_FILE)

    assert df.iloc[-1]["operation"] == "*"
    assert df.iloc[-1]["operand1"] == 3
    assert df.iloc[-1]["operand2"] == 3
    assert df.iloc[-1]["result"] == 9

def test_division(setup_history, monkeypatch):
    app = App()

    inputs = iter(["/", "8", "2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app.start()
    df = pd.read_csv(HISTORY_FILE)

    assert df.iloc[-1]["operation"] == "/"
    assert df.iloc[-1]["operand1"] == 8
    assert df.iloc[-1]["operand2"] == 2
    assert df.iloc[-1]["result"] == 4

def test_division_by_zero(setup_history, monkeypatch):
    app = App()

    inputs = iter(["/", "5", "0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app.start()
    df = pd.read_csv(HISTORY_FILE)

    assert df.iloc[-1]["operation"] == "/"
    assert df.iloc[-1]["operand1"] == 5
    assert df.iloc[-1]["operand2"] == 0
    assert df.iloc[-1]["result"] == "Error: Division by zero"

def test_history_loading(setup_history):
    setup_history.add_entry("+", 1, 1, 2)
    setup_history.load_history()
    df = pd.read_csv(HISTORY_FILE)

    assert df.iloc[-1]["operation"] == "+"
    assert df.iloc[-1]["operand1"] == 1
    assert df.iloc[-1]["operand2"] == 1
    assert df.iloc[-1]["result"] == 2

