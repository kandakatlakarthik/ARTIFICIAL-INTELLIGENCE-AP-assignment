
from math import isqrt

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.

    Uses quick checks for small factors then tests 6k ± 1 candidates.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# ...existing code...
if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Invalid input — please enter an integer.")
    else:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")