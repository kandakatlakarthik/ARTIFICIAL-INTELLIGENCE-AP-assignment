def check_number(num):
    """
    Checks if a given number is positive, negative, or zero and prints the result.
    :param num: The number to check.
    """
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")

# --- Python Execution ---
print("--- Python Execution ---")

print("Input: -5 -> Output: ", end="")
check_number(-5)

print("Input: 0 -> Output: ", end="")
check_number(0)

print("Input: 7 -> Output: ", end="")
check_number(7)
