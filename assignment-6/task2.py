# ...existing code...
def print_first_10_multiples(n):
    """Print the first 10 multiples of n."""
    for i in range(1, 11):
        print(n * i)

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print_first_10_multiples(num)
# ...existing code...

# ...existing code...
def print_first_10_multiples(n):
    """Print the first 10 multiples of n."""
    for i in range(1, 11):
        print(n * i)

if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print_first_10_multiples(num)
# ...existing code...