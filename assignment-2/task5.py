# Get the size of the list from user
n = int(input("Enter the number of elements: "))

# Create an empty list to store numbers
numbers = []

# Get numbers from user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Initialize variables for sum
even_sum = 0
odd_sum = 0

# Calculate sum of odd and even numbers
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Display results
print(f"\nOriginal list: {numbers}")
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")