from typing import Optional

def divide_numbers(numerator: float, denominator: float) -> Optional[float]:
    """
    Divides the numerator by the denominator with error handling for division by zero.

    Args:
        numerator (float): The number to be divided.
        denominator (float): The number to divide by.

    Returns:
        Optional[float]: The result of the division as a float, or None if
                         the denominator is zero.
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# --- Example Usage ---

# Successful division
result1 = divide_numbers(10, 2)
if result1 is not None:
    print(f"Result of 10 / 2 is: {result1}")

print("-" * 20)

# Division by zero
result2 = divide_numbers(10, 0)
if result2 is None:
    print("The division by zero was handled gracefully.")

