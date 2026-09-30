import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "expenses.json"
BUDGET_FILE = Path(__file__).resolve().parent.parent / "data" / "budgets.json"


def load_data():
    DATA_FILE.parent.mkdir(exist_ok=True)
    if not DATA_FILE.exists():
        return {"expenses": [], "next_id": 1}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with an empty list.")
        return {"expenses": [], "next_id": 1}


def save_data(data):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_budgets():
    if not BUDGET_FILE.exists():
        return {}
    try:
        with open(BUDGET_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_budgets(budgets):
    BUDGET_FILE.parent.mkdir(exist_ok=True)
    with open(BUDGET_FILE, "w", encoding="utf-8") as file:
        json.dump(budgets, file, indent=2)
