import unittest
from modules.expense import make_expense


class ExpenseTests(unittest.TestCase):
    def test_make_expense(self):
        expense = make_expense(1, "50", "food", "2025-01-01", "lunch")
        self.assertEqual(expense["amount"], 50.0)
        self.assertEqual(expense["category"], "Food")

    def test_bad_amount(self):
        with self.assertRaises(ValueError):
            make_expense(1, -5, "Food", "2025-01-01")

    def test_bad_category(self):
        with self.assertRaises(ValueError):
            make_expense(1, 5, "Games", "2025-01-01")


if __name__ == "__main__":
    unittest.main()
