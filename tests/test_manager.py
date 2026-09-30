import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from modules.manager import ExpenseManager


class ManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.file = Path(self.temp.name) / "expenses.json"
        self.data = {"expenses": [], "next_id": 1}
        patcher = patch("modules.manager.load_data", return_value=self.data)
        self.addCleanup(patcher.stop)
        patcher.start()
        self.save_patcher = patch("modules.manager.save_data")
        self.save_patcher.start()
        self.addCleanup(self.save_patcher.stop)
        self.manager = ExpenseManager()

    def tearDown(self):
        self.temp.cleanup()

    def test_add_and_search(self):
        self.manager.add(10, "Food", "2025-01-01", "lunch")
        self.assertEqual(len(self.manager.search("food")), 1)

    def test_delete(self):
        self.manager.add(10, "Food", "2025-01-01", "lunch")
        self.manager.delete(1)
        self.assertEqual(self.manager.get_all(), [])


if __name__ == "__main__":
    unittest.main()
