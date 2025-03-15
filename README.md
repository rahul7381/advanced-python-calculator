# Advanced Python Calculator

## 📌 Project Overview
This is a command-line calculator with a **dynamic plugin system** and **history tracking** using Pandas.

## 🔧 Features
- **Basic Arithmetic**: Supports `+`, `-`, `*`, `/`
- **History Management**: Saves all calculations in `history.csv`
- **Plugins Support**: Easily extendable with new commands
- **Logging**: Tracks all operations in `app.log`
- **Command Design Pattern**: Used for modularity
- **Facade Design Pattern**: Simplifies Pandas history management

## 🚀 Installation
```bash
git clone https://github.com/rahul7381/advanced-python-calculator.git
cd advanced-python-calculator
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
pip install -r requirements.txt

