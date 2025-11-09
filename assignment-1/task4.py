def factorial_recursive(n):
    """
    Calculate factorial using recursive approach
    Args:
        n (int): The number to calculate factorial for
    Returns:
        int: The factorial of n
    """
    # Base cases
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Calculate factorial using iterative approach
    Args:
        n (int): The number to calculate factorial for
    Returns:
        int: The factorial of n
    """
    # Check for negative numbers
    if n < 0:
        return None
    
    # Initialize result
    result = 1
    
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    
    return result

if __name__ == "__main__":
    # Get user input and convert to integer
    try:
        # Prompt user for input
        number = int(input("Enter a non-negative integer to calculate factorial: "))
        
        # Calculate factorial using both methods
        recursive_result = factorial_recursive(number)
        iterative_result = factorial_iterative(number)
        
        # Check if results are valid (not None)
        if recursive_result is not None and iterative_result is not None:
            print(f"\nResults for factorial of {number}:")
            print(f"Using recursive method: {recursive_result}")
            print(f"Using iterative method: {iterative_result}")
        else:
            print("Error: Factorial is not defined for negative numbers!")
            
    except ValueError:
        # Handle invalid input (non-integer values)
        print("Error: Please enter a valid integer!")