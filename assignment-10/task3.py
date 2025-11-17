"""
This module defines the Employee class.
"""

class Employee:
    """
    Represents an employee with a name and a salary. This improved version
    uses descriptive names, follows encapsulation principles, and includes
    docstrings and type hints for better readability and maintainability.

    Attributes:
        name (str): The name of the employee.
        salary (float): The current salary of the employee.
    """

    def __init__(self, name: str, salary: float):
        """
        Initializes an Employee object.

        Args:
            name (str): The full name of the employee.
            salary (float): The initial salary of the employee.
        """
        self._name = name
        self._salary = salary

    def increase_salary(self, percentage: float):
        """
        Increases the employee's salary by a given percentage. The salary
        is only increased if the percentage is a positive value.

        Args:
            percentage (float): The percentage to increase the salary by.
        """
        if percentage > 0:
            self._salary *= (1 + percentage / 100) # Simplified calculation

    def display_info(self):
        """Displays the employee's information in a formatted string."""
        print(f"Employee: {self._name}, Salary: ${self._salary:,.2f}")

# Example usage:
emp1 = Employee("Alice", 50000)
emp1.display_info()
emp1.increase_salary(10)
emp1.display_info()