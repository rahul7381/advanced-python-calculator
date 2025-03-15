import pytest
from calculator.repl import CalculatorREPL
from unittest.mock import patch

@pytest.fixture
def repl():
    return CalculatorREPL()

@patch("builtins.input", side_effect=["+ 3 4", "exit"])
@patch("builtins.print")
def test_repl_addition(mock_print, mock_input, repl):
    repl.start()
    output = [call[0][0].strip() for call in mock_print.call_args_list]  # Strip whitespace
    assert any("7.0" in line for line in output), f"Expected '7.0' in output: {output}"

@patch("builtins.input", side_effect=["history", "exit"])
@patch("builtins.print")
def test_repl_history(mock_print, mock_input, repl):
    repl.start()
    output = [call[0][0] for call in mock_print.call_args_list]
    assert any("No history found." in line for line in output)
@patch("builtins.input", side_effect=["clear", "exit"])
@patch("builtins.print")
def test_repl_clear_history(mock_print, mock_input, repl):
    repl.start()
    mock_print.assert_any_call("Calculation history cleared.")

@patch("builtins.input", side_effect=["delete", "exit"])
@patch("builtins.print")
def test_repl_delete_history(mock_print, mock_input, repl):
    repl.start()
    mock_print.assert_any_call("History file deleted.")

@patch("builtins.input", side_effect=["menu", "exit"])
@patch("builtins.print")
def test_repl_menu(mock_print, mock_input, repl):
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]  # Normalize text
    assert any("available plugins:" in line for line in output), f"Expected 'Available Plugins:' in output: {output}"

@patch("builtins.input", side_effect=["unknown_command", "exit"])
@patch("builtins.print")
def test_repl_unknown_command(mock_print, mock_input, repl):
    repl.start()
    output = [call[0][0].strip().lower() for call in mock_print.call_args_list]
    assert any("unknown command" in line for line in output), f"Expected 'Unknown command' in output: {output}"
@patch("builtins.input", side_effect=["", "exit"])
@patch("builtins.print")
def test_repl_empty_input(mock_print, mock_input, repl):
    repl.start()
    output = [call[0][0].strip() for call in mock_print.call_args_list]
    assert any("invalid command" in line for line in output), f"Expected 'Invalid command' in output: {output}"

