import pytest
from unittest.mock import patch
import os
import logging
from calculator.repl import CalculatorREPL


@pytest.fixture
def repl():
    return CalculatorREPL()

# Test Cases for Operations and Error Handling

@patch("builtins.input", side_effect=["+", "3", "4", "exit"])
@patch("builtins.print")
def test_repl_addition(mock_print, mock_input, repl):
    """Test addition operation in REPL"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]

    # Filter out the welcome message and focus on calculation results
    relevant_output = [line for line in output if line.replace('.', '', 1).isdigit()]
    assert any("7.0" in line for line in relevant_output), f"Expected '7.0' in output: {relevant_output}"

@patch("builtins.input", side_effect=["*", "6", "7", "exit"])
@patch("builtins.print")
def test_repl_multiplication(mock_print, mock_input, repl):
    """Test multiplication operation in REPL"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]

    # Filter out the welcome message and focus on calculation results
    relevant_output = [line for line in output if line.replace('.', '', 1).isdigit()]
    assert any("42.0" in line for line in relevant_output), f"Expected '42.0' in output: {relevant_output}"

@patch("builtins.input", side_effect=["/", "10", "0", "exit"])
@patch("builtins.print")
def test_repl_divide_by_zero(mock_print, mock_input, repl):
    """Test division by zero handling in REPL"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]

    # Focus on the error message and filter out the welcome message
    relevant_output = [line for line in output if "error" in line.lower()]
    assert any("Error: Cannot divide by zero" in line for line in relevant_output), f"Expected 'Error: Cannot divide by zero' in output: {relevant_output}"

@patch("builtins.input", side_effect=["5+3*2", "history", "exit"])
@patch("builtins.print")
def test_repl_equation_input(mock_print, mock_input, repl):
    """Test REPL correctly evaluates an equation and stores it in history"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]

    # Filter out irrelevant messages and check the output
    relevant_output = [line for line in output if line.replace('.', '', 1).isdigit()]

    # Ensure the correct result is printed (5 + (3 * 2) = 11)
    assert any("11" in line for line in relevant_output), f"Expected '11.0' in output: {relevant_output}"

    # Ensure history stores the equation correctly
    history_output = [line for line in output if "expression" in line]
    assert any("5+3*2" in line for line in history_output), f"Expected '5+3*2' in history: {history_output}"

# Additional Test Cases for History, Clear, Delete, and Menu

@patch("builtins.input", side_effect=["exit"])
@patch("builtins.print")
def test_repl_exit(mock_print, mock_input, repl):
    """Test REPL exit"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "Exiting..." in output

@patch("builtins.input", side_effect=["history", "exit"])
@patch("builtins.print")
def test_repl_history(mock_print, mock_input, repl):
    """Test history functionality"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "No history found" in output or "history" in output

@patch("builtins.input", side_effect=["clear", "exit"])
@patch("builtins.print")
def test_repl_clear_history(mock_print, mock_input, repl):
    """Test clearing history"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "Calculation history cleared" in output

@patch("builtins.input", side_effect=["delete", "exit"])
@patch("builtins.print")
def test_repl_delete_history(mock_print, mock_input, repl):
    """Test deleting history file"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "History file deleted" in output

@patch("builtins.input", side_effect=["menu", "exit"])
@patch("builtins.print")
def test_repl_menu(mock_print, mock_input, repl):
    """Test menu command to list available plugins"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "available plugins" in output

@patch("builtins.input", side_effect=["invalid_command", "exit"])
@patch("builtins.print")
def test_repl_invalid_command(mock_print, mock_input, repl):
    """Test unknown command"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "Unknown command" in output

@patch("builtins.input", side_effect=["", "exit"])
@patch("builtins.print")
def test_repl_empty_input(mock_print, mock_input, repl):
    """Test empty input"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "Unknown command" in output

# More test cases to cover other missing parts

@patch("builtins.input", side_effect=["add 2 3", "exit"])
@patch("builtins.print")
def test_repl_addition_edge_case(mock_print, mock_input, repl):
    """Test addition operation edge case"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "5.0" in output

@patch("builtins.input", side_effect=["sub 5 3", "exit"])
@patch("builtins.print")
def test_repl_subtraction_edge_case(mock_print, mock_input, repl):
    """Test subtraction operation edge case"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "2.0" in output

@patch("builtins.input", side_effect=["mul 5 0", "exit"])
@patch("builtins.print")
def test_repl_multiplication_zero(mock_print, mock_input, repl):
    """Test multiplication with zero"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "0.0" in output

@patch("builtins.input", side_effect=["div 100 10", "exit"])
@patch("builtins.print")
def test_repl_divide_edge_case(mock_print, mock_input, repl):
    """Test division edge case"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "10.0" in output

@patch("builtins.input", side_effect=["div 100 0", "exit"])
@patch("builtins.print")
def test_repl_divide_by_zero_edge_case(mock_print, mock_input, repl):
    """Test divide by zero edge case"""
    repl.start()
    output = [str(call[0][0]).strip() for call in mock_print.call_args_list]
    assert "Error: Cannot divide by zero" in output

