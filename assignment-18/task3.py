def factorial(n):
  """
  Calculates the factorial of a non-negative integer using recursion.
  """
  # Base case: The factorial of 0 is 1.
  if n == 0:
    return 1
  # Recursive step: n * (n-1)!
  else:
    return n * factorial(n - 1)

# --- Function Calls ---

# Call the function with input 5
input_5 = 5
output_5 = factorial(input_5)
print(f"Input: {input_5} -> Output: Factorial = {output_5}")

# Call the function with input 0
input_0 = 0
output_0 = factorial(input_0)
print(f"Input: {input_0} -> Output: Factorial = {output_0}")
