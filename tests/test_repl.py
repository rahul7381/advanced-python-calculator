import pytest
from calculator.repl import CalculatorREPL
from unittest.mock import patch

@pytest.fixture
def repl():
    return CalculatorREPL()

@patch("builtins.input", side_effect=["+", "3", "4", "exit"])
@patch("builtins.print")
def test_repl_addition(mock_print, mock_input, repl):
    """Test addition operation in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Addition):", output)  # Debugging step
    assert any("7" in line or "7.0" in line for line in output), f"Expected '7.0' in output, got: {output}"

@patch("builtins.input", side_effect=["menu", "exit"])
@patch("builtins.print")
def test_repl_menu(mock_print, mock_input, repl):
    """Test 'menu' command to list available plugins"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Menu):", output)  # Debugging step
    assert any("available plugins" in line or "list of available plugins" in line or "plugins available" in line for line in output), f"Expected 'Available Plugins:' in output: {output}"

@patch("builtins.input", side_effect=["", "exit"])
@patch("builtins.print")
def test_repl_empty_input(mock_print, mock_input, repl):
    """Test handling of empty input"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Empty Input):", output)  # Debugging step
    assert any("unknown command" in line or "invalid command" in line or "invalid input" in line or "command not recognized" in line for line in output), f"Expected 'Unknown command' or 'Invalid command' in output: {output}"

@patch("builtins.input", side_effect=["/", "4", "0", "exit"])
@patch("builtins.print")
def test_repl_divide_by_zero(mock_print, mock_input, repl):
    """Test division by zero handling in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Divide by Zero):", output)  # Debugging step
    assert any("error: cannot divide by zero" in line or "cannot divide by zero" in line or "division by zero is not allowed" in line for line in output), f"Expected 'Error: Cannot divide by zero' in output: {output}"

@patch("builtins.input", side_effect=["+", "2", "3", "history", "exit"])
@patch("builtins.print")
def test_repl_history_after_calculation(mock_print, mock_input, repl):
    """Test history command after performing calculations"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (History):", output)  # Debugging step
    assert any("add" in line or "addition" in line for line in output), f"Expected 'add' operation in history output: {output}"

@patch("builtins.input", side_effect=["clear", "history", "exit"])
@patch("builtins.print")
def test_repl_clear_history(mock_print, mock_input, repl):
    """Test clearing calculation history in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Clear History):", output)  # Debugging step
    assert any("no history found" in line or "history is empty" in line for line in output), f"Expected 'No history found.' in output: {output}"

@patch("builtins.input", side_effect=["delete", "history", "exit"])
@patch("builtins.print")
def test_repl_delete_history(mock_print, mock_input, repl):
    """Test deleting history file in REPL"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Delete History):", output)  # Debugging step
    assert any("history file deleted" in line or "history removed" in line for line in output), f"Expected 'History file deleted' in output: {output}"

@patch("builtins.input", side_effect=["unknown_command", "exit"])
@patch("builtins.print")
def test_repl_unknown_command(mock_print, mock_input, repl):
    """Test handling of unknown commands"""
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Unknown Command):", output)  # Debugging step
    assert any("unknown command" in line or "command not recognized" in line for line in output), f"Expected 'Unknown command' in output: {output}"

@patch("builtins.input", side_effect=["-", "9", "4", "exit"])
@patch("builtins.print")
def test_repl_subtraction(mock_print, mock_input, repl):
    """Test subtraction operation in REPL"""
    repl.start()
    output = [str(call[0][0]).strip().lower() for call in mock_print.call_args_list]
    print("\nCaptured REPL Output (Subtraction):", output)  # Debugging step
    assert any("5" in line or "5.0" in line for line in output), f"Expected '5.0' in output, got: {output}"

