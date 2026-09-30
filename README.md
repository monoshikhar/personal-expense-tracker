# Expense Tracker

A small command-line program for keeping track of personal expenses. It was made as a beginner Python project.

## Features
- Add, view, edit and delete expenses
- Search expenses by category
- Show total spending and spending by category
- Save data in JSON files
- Set monthly budgets and check spending
- Export expenses to CSV

## Requirements
Python 3.9 or newer. No extra packages are needed.

## Run
Open a terminal in this folder and run:

```bash
python main.py
```

## Tests
Run:

```bash
python -m unittest discover -s tests -v
```

## Files
- `main.py`: menu and user input
- `modules/expense.py`: creates and checks expense entries
- `modules/manager.py`: add, edit, delete and search
- `modules/storage.py`: reads and writes JSON files
- `modules/budget.py`: budgets and budget checks
- `modules/reports.py`: summary and CSV export
