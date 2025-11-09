# ...existing code...
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def main():
    while True:
        s = input("Enter a year (or 'q' to quit): ").strip()
        if s.lower() in ('q', 'quit', 'exit'):
            print("Exiting.")
            return
        try:
            year = int(s)
        except ValueError:
            print("Please enter a valid integer year.")
            continue
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
# filepath: c:\Users\LENOVO\Desktop\aiap\assignment-4\task1.py
# ...existing code...
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def main():
    while True:
        s = input("Enter a year (or 'q' to quit): ").strip()
        if s.lower() in ('q', 'quit', 'exit'):
            print("Exiting.")
            return
        try:
            year = int(s)
        except ValueError:
            print("Please enter a valid integer year.")
            continue
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()