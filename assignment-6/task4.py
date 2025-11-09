# ...existing code...
def sum_to_n():
    try:
        n = int(input("Enter a non-negative integer n: ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return

    if n < 0:
        print("Invalid input: n cannot be negative.")
        return

    total = n * (n + 1) // 2  # arithmetic series formula
    print(f"Sum of first {n} numbers is {total}")
    return total

if __name__ == "__main__":
    sum_to_n()
# ...existing code...