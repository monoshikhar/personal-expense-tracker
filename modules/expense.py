from datetime import date

CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Other"]


def make_expense(expense_id, amount, category, day, note=""):
    amount = float(amount)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    category = category.strip().title()
    if category not in CATEGORIES:
        raise ValueError("Please enter a category from the list.")

    if not day:
        day = date.today().isoformat()
    date.fromisoformat(day)
    if day > date.today().isoformat():
        raise ValueError("Date cannot be in the future.")

    return {
        "id": expense_id,
        "amount": round(amount, 2),
        "category": category,
        "date": day,
        "note": note.strip()
    }


def show_expense(expense):
    return "{} | {} | {} | Rs. {:.2f} | {}".format(
        expense["id"], expense["date"], expense["category"],
        expense["amount"], expense["note"])
