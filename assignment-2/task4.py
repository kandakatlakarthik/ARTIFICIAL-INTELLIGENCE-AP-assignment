def calculate_sum_of_squares():
    """Calculate the sum of squares for a list of numbers entered by user"""
    try:
        # Get the count of numbers from user
        n = int(input("How many numbers do you want to enter? "))
        
        if n <= 0:
            return "Please enter a positive number!"
        
        numbers = []
        # Get numbers from user
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        # Calculate sum of squares
        sum_squares = sum(num ** 2 for num in numbers)
        
        return f"Numbers entered: {numbers}\nSum of squares: {sum_squares:.2f}"
    
    except ValueError:
        return "Invalid input! Please enter numerical values only."

def main():
    while True:
        print("\n=== Sum of Squares Calculator ===")
        print("1. Calculate sum of squares")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '2':
            print("Thank you for using the Sum of Squares Calculator!")
            break
        elif choice == '1':
            result = calculate_sum_of_squares()
            print(result)
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()