# Advanced Python Calculator

## Overview
This is a Python-based calculator with advanced features, including:
- Command-Line Interface (REPL)
- Plugin System for Extensions
- Calculation History Management using Pandas
- Professional Logging Practices
- Pytest-based Unit Testing with 90%+ Coverage
- GitHub Actions for CI/CD

## Features
### ✅ Arithmetic Operations
- Addition, Subtraction, Multiplication, Division
- Expression Parsing (`2+3*4` is supported)
- Division by zero is safely handled

### ✅ Calculation History
- View, clear, and delete history
- Stored in `history.csv` with Pandas

### ✅ Plugin System
- New features can be added via plugins
- Use the `menu` command to list available plugins

## Setup Instructions
### Install Dependencies
```sh
pip install -r requirements.txt

## Design Patterns
- **Facade Pattern**: Provides a simple interface for complex operations like calculation and history management.
- **Command Pattern**: Each operation (add, sub, mul, div) is encapsulated in a separate command object.
- **Factory Pattern**: Used for dynamically creating objects like calculation strategies or plugin objects.
- **Singleton Pattern**: Ensures only one instance of `CalculationHistory`.
- **Strategy Pattern**: Allows different strategies for handling different operations (e.g., addition, subtraction, etc.).

