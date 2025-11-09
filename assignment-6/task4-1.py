# ...existing code...
def sum_to_n_for():
    try:
        n = int(input("Enter a non-negative integer n: ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return
    if n < 0:
        print("Invalid input: n cannot be negative.")
        return
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"(for) Sum of first {n} numbers is {total}")
    return total

def sum_to_n_while():
    try:
        n = int(input("Enter a non-negative integer n: ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return
    if n < 0:
        print("Invalid input: n cannot be negative.")
        return
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print(f"(while) Sum of first {n} numbers is {total}")
    return total

def sum_to_n_do_while():
    try:
        n = int(input("Enter a non-negative integer n: ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return
    if n < 0:
        print("Invalid input: n cannot be negative.")
        return
    # Emulate do-while: body runs at least once when n >= 1
    total = 0
    i = 1
    if n == 0:
        print(f"(do-while) Sum of first 0 numbers is 0")
        return 0
    while True:
        total += i
        i += 1
        if i > n:
            break
    print(f"(do-while) Sum of first {n} numbers is {total}")
    return total

def sum_to_n_builtin():
    try:
        n = int(input("Enter a non-negative integer n: ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return
    if n < 0:
        print("Invalid input: n cannot be negative.")
        return
    total = sum(range(1, n + 1))
    print(f"(builtin sum) Sum of first {n} numbers is {total}")
    return total

if __name__ == "__main__":
    method = input("Choose method (for/while/do/builtin): ").strip().lower()
    if method == "for":
        sum_to_n_for()
    elif method == "while":
        sum_to_n_while()
    elif method == "do":
        sum_to_n_do_while()
    else:
        sum_to_n_builtin()
# ...existing code...