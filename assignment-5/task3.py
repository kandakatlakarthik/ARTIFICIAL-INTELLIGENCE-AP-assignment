def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: The position in the Fibonacci sequence (starting from 0)
    Returns:
        The nth Fibonacci number
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case: Fib(n) = Fib(n-1) + Fib(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_user_input():
    """Get and validate user input for fibonacci calculation"""
    while True:
        try:
            n = int(input("Enter a non-negative number for Fibonacci calculation: "))
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    # Get input from user
    n = get_user_input()
    result = fibonacci(n)
    print(f"F({n}) = {result}")