# Basic Design

## Main parts
1. `main.py` shows the menu and asks for input.
2. `expense.py` checks expense details.
3. `manager.py` changes and searches the expense list.
4. `storage.py` saves and loads JSON data.
5. `budget.py` stores budgets and compares them with spending.
6. `reports.py` shows totals and exports a CSV file.

## Data storage
Expenses are stored in `data/expenses.json`. Budgets are stored in `data/budgets.json`. Each expense has an ID, amount, category, date and note.

## Basic workflow
Start program -> choose menu option -> enter details -> validate details -> save changes -> show result.

## Non-functional requirements
- Usability: menu options are shown in the terminal.
- Reliability: data is saved to a file so it remains after the program closes.
- Error handling: invalid amounts, categories and dates are rejected.
- Maintainability: different tasks are kept in separate files.
