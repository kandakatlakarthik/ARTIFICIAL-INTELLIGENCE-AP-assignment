"""A simple calculator module.

This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division. Each function takes two numerical inputs
and returns the result of the operation.
"""

def add(a, b):
    """Calculates the sum of two numbers.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """Calculates the difference between two numbers.

    Args:
        a (int | float): The number to be subtracted from.
        b (int | float): The number to subtract.

    Returns:
        int | float: The result of a minus b.
    """
    return a - b

def multiply(a, b):
    """Calculates the product of two numbers.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """Divides the first number by the second.

    Args:
        a (int | float): The numerator.
        b (int | float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the denominator (b) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Example usage of the calculator functions.
if __name__ == "__main__":
    num1 = 20
    num2 = 5

    print(f"Using numbers: {num1} and {num2}")
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")

    try:
        print(f"Division: {divide(num1, num2)}")
        # This will raise an error
        print(f"Division by zero: {divide(num1, 0)}")
    except ValueError as e:
        print(f"Error: {e}")