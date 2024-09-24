import unittest
from budget_category import BudgetCategory  # Assuming your class is in a file named budget_category.py

class TestBudgetCategory(unittest.TestCase):
    
    def setUp(self):
        """Set up a default BudgetCategory object for use in tests."""
        self.budget = BudgetCategory("Entertainment", 300)
    
    def test_get_category_name(self):
        """Test getter for category name."""
        self.assertEqual(self.budget.get_category_name(), "Entertainment")
    
    def test_set_category_name(self):
        """Test setter for category name with valid input."""
        self.budget.set_category_name("Leisure")
        self.assertEqual(self.budget.get_category_name(), "Leisure")
    
    def test_invalid_set_category_name(self):
        """Test setter for category name with invalid input."""
        with self.assertRaises(ValueError):
            self.budget.set_category_name("")

    def test_get_allocated_budget(self):
        """Test getter for allocated budget."""
        self.assertEqual(self.budget.get_allocated_budget(), 300)

    def test_set_allocated_budget(self):
        """Test setter for allocated budget with valid input."""
        self.budget.set_allocated_budget(400)
        self.assertEqual(self.budget.get_allocated_budget(), 400)
    
    def test_invalid_set_allocated_budget(self):
        """Test setter for allocated budget with invalid input."""
        with self.assertRaises(ValueError):
            self.budget.set_allocated_budget(-100)
    
    def test_add_expense(self):
        """Test adding an expense with valid input."""
        self.budget.add_expense(50)
        self.assertEqual(self.budget.get_allocated_budget() - 50, self.budget._BudgetCategory__remaining_budget)

    def test_invalid_expense(self):
        """Test adding an invalid expense (more than remaining budget)."""
        with self.assertRaises(ValueError):
            self.budget.add_expense(500)
    
    def test_display_budget_details(self):
        """Test displaying budget details."""
        self.budget.display_budget_details()  # This will print, but we won't assert on print output

if __name__ == "__main__":
    unittest.main()
