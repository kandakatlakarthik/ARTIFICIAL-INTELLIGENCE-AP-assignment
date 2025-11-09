# ...existing code...
import bisect

def classify_age():
    try:
        age = int(input("Enter age (years): ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return

    if age < 0:
        print("Invalid age: age cannot be negative.")
        return

    thresholds = [0, 13, 18, 25, 65]              # lower bounds for groups
    labels = ["Child", "Teenager", "Young adult", "Adult", "Senior"]

    idx = bisect.bisect_right(thresholds, age) - 1
    print(f"Age {age}: {labels[idx]}")

if __name__ == "__main__":
    classify_age()
# ...existing code...