import pytest
from calculator.repl import CalculatorREPL
from unittest.mock import patch
from calculator.core import Calculator
import logging

# Create a test calculator instance
@pytest.fixture
def calculator():
    return Calculator()

# Test add method
def test_add(calculator):
    result = calculator.add(5, 3)
    assert result == 8, f"Expected 8, but got {result}"

# Test subtract method
def test_subtract(calculator):
    result = calculator.subtract(5, 3)
    assert result == 2, f"Expected 2, but got {result}"

# Test multiply method
def test_multiply(calculator):
    result = calculator.multiply(5, 3)
    assert result == 15, f"Expected 15, but got {result}"

# Test divide method
def test_divide(calculator):
    result = calculator.divide(6, 3)
    assert result == 2.0, f"Expected 2.0, but got {result}"

# Test divide by zero scenario
def test_divide_by_zero(calculator):
    result = calculator.divide(6, 0)
    assert result == "Error: Cannot divide by zero", f"Expected 'Error: Cannot divide by zero', but got {result}"

# Test logging for add method (We can use a caplog fixture to capture logs)
def test_add_logging(calculator, caplog):
    with caplog.at_level(logging.INFO):
        calculator.add(5, 3)
    assert "Adding 5 + 3 = 8" in caplog.text

# Test logging for subtract method
def test_subtract_logging(calculator, caplog):
    with caplog.at_level(logging.INFO):
        calculator.subtract(5, 3)
    assert "Subtracting 5 - 3 = 2" in caplog.text

# Test logging for multiply method
def test_multiply_logging(calculator, caplog):
    with caplog.at_level(logging.INFO):
        calculator.multiply(5, 3)
    assert "Multiplying 5 * 3 = 15" in caplog.text

# Test logging for divide method
def test_divide_logging(calculator, caplog):
    with caplog.at_level(logging.INFO):
        calculator.divide(6, 3)
    assert "Dividing 6 / 3 = 2.0" in caplog.text

# Test logging for divide by zero
def test_divide_by_zero_logging(calculator, caplog):
    with caplog.at_level(logging.ERROR):
        calculator.divide(6, 0)
    assert "Attempted to divide by zero" in caplog.text
@pytest.fixture
def repl():
    return CalculatorREPL()

@patch("builtins.input", side_effect=["add 3 4", "exit"])
@patch("builtins.print")
def test_repl_addition(mock_print, mock_input, repl):
    """Test addition operation in REPL"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Addition):", output)  # Debugging step
    assert any("7.0" in line for line in output), f"Expected '7.0' in output, got: {output}"

@patch("builtins.input", side_effect=["menu", "exit"])
@patch("builtins.print")
def test_repl_menu(mock_print, mock_input, repl):
    """Test 'menu' command to list available plugins"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Menu):", output)  # Debugging step
    assert any("available plugins:" in line for line in output), f"Expected 'Available Plugins:' in output: {output}"

@patch("builtins.input", side_effect=["", "exit"])
@patch("builtins.print")
def test_repl_empty_input(mock_print, mock_input, repl):
    """Test handling of empty input"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Empty Input):", output)  # Debugging step
    assert any("unknown command" in line or "invalid command" in line for line in output), f"Expected 'Unknown command' or 'Invalid command' in output: {output}"

@patch("builtins.input", side_effect=["/ 4 0", "exit"])
@patch("builtins.print")
def test_repl_divide_by_zero(mock_print, mock_input, repl):
    """Test division by zero handling in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Divide by Zero):", output)  # Debugging step
    assert any("error: cannot divide by zero" in line for line in output), f"Expected 'Error: Cannot divide by zero' in output: {output}"

@patch("builtins.input", side_effect=["+ 2 3", "history", "exit"])
@patch("builtins.print")
def test_repl_history_after_calculation(mock_print, mock_input, repl):
    """Test history command after performing calculations"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (History):", output)  # Debugging step
    assert any("add" in line for line in output), f"Expected 'add' operation in history output: {output}"

@patch("builtins.input", side_effect=["clear", "history", "exit"])
@patch("builtins.print")
def test_repl_clear_history(mock_print, mock_input, repl):
    """Test clearing calculation history in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Clear History):", output)  # Debugging step
    assert any("no history found" in line for line in output), f"Expected 'No history found.' in output: {output}"

@patch("builtins.input", side_effect=["delete", "history", "exit"])
@patch("builtins.print")
def test_repl_delete_history(mock_print, mock_input, repl):
    """Test deleting history file in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Delete History):", output)  # Debugging step
    assert any("history file deleted" in line for line in output), f"Expected 'History file deleted' in output: {output}"

@patch("builtins.input", side_effect=["unknown_command", "exit"])
@patch("builtins.print")
def test_repl_unknown_command(mock_print, mock_input, repl):
    """Test handling of unknown commands"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Unknown Command):", output)  # Debugging step
    assert any("unknown command" in line for line in output), f"Expected 'Unknown command' in output: {output}"

@patch("builtins.input", side_effect=["- 9 4", "exit"])
@patch("builtins.print")
def test_repl_subtraction(mock_print, mock_input, repl):
    """Test subtraction operation in REPL"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Subtraction):", output)  # Debugging step
    assert any("5.0" in line for line in output), f"Expected '5.0' in output, got: {output}"
