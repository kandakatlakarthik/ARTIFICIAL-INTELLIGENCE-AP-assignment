# ...existing code...
def classify_age():
    try:
        age = int(input("Enter age (years): ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
        return

    # Outer check ensures age is non-negative, inner nested if-elif-else classifies groups
    if age >= 0:
        if age <= 12:
            group = "Child"
        elif age <= 17:
            group = "Teenager"
        elif age <= 24:
            group = "Young adult"
        elif age <= 64:
            group = "Adult"
        else:
            group = "Senior"
        print(f"Age {age}: {group}")
    else:
        print("Invalid age: age cannot be negative.")

if __name__ == "__main__":
    classify_age()
# ...existing code...