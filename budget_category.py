'''
1. Encapsulation in Personal Budget Management
Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
focusing on the use of private attributes and getters and setters.

Problem Statement: You are required to build a Personal Budget Management application. 
The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private 
and are accessed or modified through public methods.

Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
- Initialize these attributes in the constructor.

- Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. 
- Ensure that the setter methods include validation (e.g., budget should be a positive number).

- Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. 
- Validate the expense amount before making deductions from the budget.

Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

Task 4: Display Budget Details Create a method to display the details of a budget category, 
including the name, allocated budget, and remaining budget after expenses.
'''


class BudgetCategory:
    
    def __init__(self, category_name, allocated_budget):
        """Initialize the budget category with a name and an allocated budget."""
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget
    
    # Task 2: Getters and Setters with validation
    def get_category_name(self):
        """Return the category name."""
        return self.__category_name

    def set_category_name(self, new_name):
        """Set a new category name."""
        if isinstance(new_name, str) and new_name.strip():
            self.__category_name = new_name
        else:
            raise ValueError("Category name must be a non-empty string.")
    
    def get_allocated_budget(self):
        """Return the allocated budget."""
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_budget):
        """Set a new allocated budget with validation (positive number)."""
        if isinstance(new_budget, (int, float)) and new_budget > 0:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget  # Reset remaining budget to new allocation
        else:
            raise ValueError("Budget must be a positive number.")
    
    # Task 3: Add Budget Functionality
    def add_expense(self, expense_amount):
        """Deduct expense from the remaining budget with validation."""
        if isinstance(expense_amount, (int, float)) and expense_amount > 0:
            if expense_amount <= self.__remaining_budget:
                self.__remaining_budget -= expense_amount
            else:
                raise ValueError("Expense exceeds remaining budget!")
        else:
            raise ValueError("Expense amount must be a positive number.")
    
    # Task 4: Display Budget Details
    def display_budget_details(self):
        """Display the budget category details."""
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")

# Example Usage (which can be split into tests in another module):
if __name__ == "__main__":
    # Creating a BudgetCategory object
    food_budget = BudgetCategory("Food", 500)

    # Displaying the budget details
    food_budget.display_budget_details()

    # Adding an expense
    food_budget.add_expense(50)

    # Displaying updated budget details
    food_budget.display_budget_details()

    # Trying to set a new budget
    food_budget.set_allocated_budget(600)
    food_budget.display_budget_details()
