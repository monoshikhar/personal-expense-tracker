from modules.storage import load_budgets, save_budgets


def set_budget(category, amount):
    if amount <= 0:
        raise ValueError("Budget must be greater than zero.")
    budgets = load_budgets()
    budgets[category] = amount
    save_budgets(budgets)


def show_budgets():
    budgets = load_budgets()
    if not budgets:
        print("No budgets set.")
    for category, amount in budgets.items():
        print(category, ": Rs. {:.2f}".format(amount))


def check_budgets(expenses):
    budgets = load_budgets()
    spent = {}
    month = __import__("datetime").date.today().strftime("%Y-%m")

    for expense in expenses:
        if expense["date"].startswith(month):
            category = expense["category"]
            spent[category] = spent.get(category, 0) + expense["amount"]

    if not budgets:
        print("Set a budget first.")
    for category, limit in budgets.items():
        total = spent.get(category, 0)
        print("{}: spent Rs. {:.2f} out of Rs. {:.2f}".format(category, total, limit))
        if total > limit:
            print("Budget exceeded!")
