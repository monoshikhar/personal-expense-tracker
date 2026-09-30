from modules.expense import make_expense, show_expense
from modules.storage import load_data, save_data


class ExpenseManager:
    def __init__(self):
        self.data = load_data()

    def add(self, amount, category, day, note):
        expense = make_expense(self.data["next_id"], amount, category, day, note)
        self.data["expenses"].append(expense)
        self.data["next_id"] += 1
        save_data(self.data)

    def get_all(self):
        return self.data["expenses"]

    def search(self, category):
        return [e for e in self.get_all()
                if e["category"].lower() == category.lower()]

    def edit(self, expense_id, changes):
        for expense in self.get_all():
            if expense["id"] == expense_id:
                new_amount = changes.get("amount", expense["amount"])
                new_category = changes.get("category", expense["category"])
                new_note = changes.get("note", expense["note"])
                updated = make_expense(expense_id, new_amount, new_category,
                                       expense["date"], new_note)
                expense.update(updated)
                save_data(self.data)
                return
        raise KeyError("Expense ID not found.")

    def delete(self, expense_id):
        for expense in self.get_all():
            if expense["id"] == expense_id:
                self.data["expenses"].remove(expense)
                save_data(self.data)
                return
        raise KeyError("Expense ID not found.")

    def print_all(self):
        for expense in self.get_all():
            print(show_expense(expense))
