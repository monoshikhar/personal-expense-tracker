import csv
from pathlib import Path

EXPORT_DIR = Path(__file__).resolve().parent.parent / "exports"


def show_summary(expenses):
    total = 0
    by_category = {}

    for expense in expenses:
        total += expense["amount"]
        category = expense["category"]
        by_category[category] = by_category.get(category, 0) + expense["amount"]

    print("\n--- Expense Summary ---")
    print("Total spent: Rs. {:.2f}".format(total))
    for category, amount in by_category.items():
        print("{}: Rs. {:.2f}".format(category, amount))


def export_csv(expenses):
    EXPORT_DIR.mkdir(exist_ok=True)
    path = EXPORT_DIR / "expenses.csv"
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "date", "category", "amount", "note"])
        for expense in expenses:
            writer.writerow([expense["id"], expense["date"], expense["category"],
                             expense["amount"], expense["note"]])
    return path
