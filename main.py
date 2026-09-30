from modules.manager import ExpenseManager
from modules.reports import show_summary, export_csv
from modules.budget import set_budget, show_budgets, check_budgets


def main():
    manager = ExpenseManager()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Edit expense")
        print("4. Delete expense")
        print("5. Search by category")
        print("6. Show summary")
        print("7. Export to CSV")
        print("8. Set budget")
        print("9. View budgets")
        print("10. Check budgets")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category (Food, Travel, Bills, Shopping, Other): ")
            date = input("Date (YYYY-MM-DD, blank for today): ").strip()
            note = input("Note: ")
            try:
                manager.add(amount, category, date, note)
                print("Expense added.")
            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            expenses = manager.get_all()
            if not expenses:
                print("No expenses yet.")
            for expense in expenses:
                print(expense)

        elif choice == "3":
            try:
                expense_id = int(input("ID to edit: "))
                amount = input("New amount (blank to keep): ").strip()
                category = input("New category (blank to keep): ").strip()
                note = input("New note (blank to keep): ").strip()
                changes = {}
                if amount:
                    changes["amount"] = amount
                if category:
                    changes["category"] = category
                if note:
                    changes["note"] = note
                manager.edit(expense_id, changes)
                print("Expense updated.")
            except (ValueError, KeyError) as error:
                print("Error:", error)

        elif choice == "4":
            try:
                expense_id = int(input("ID to delete: "))
                manager.delete(expense_id)
                print("Expense deleted.")
            except (ValueError, KeyError) as error:
                print("Error:", error)

        elif choice == "5":
            category = input("Category: ").strip()
            results = manager.search(category)
            if not results:
                print("No matching expenses.")
            for expense in results:
                print(expense)

        elif choice == "6":
            show_summary(manager.get_all())

        elif choice == "7":
            print("CSV saved to", export_csv(manager.get_all()))

        elif choice == "8":
            try:
                category = input("Category: ").strip().title()
                amount = float(input("Monthly budget: "))
                set_budget(category, amount)
                print("Budget saved.")
            except ValueError as error:
                print("Error:", error)

        elif choice == "9":
            show_budgets()

        elif choice == "10":
            check_budgets(manager.get_all())

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
