def validate_input(prompt, valid_options=None):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
            continue
        if valid_options and value.upper() not in valid_options:
            print(f"Invalid input. Please enter one of: {valid_options}")
            continue
        return value

def get_applicant_info():
    print("\n=== Applicant Information ===")
    name = validate_input("Enter applicant's name: ")
    gender = validate_input("Enter applicant's gender (M/F): ", ['M', 'F']).upper()
    
    # Additional loan information
    try:
        loan_amount = float(validate_input("Enter loan amount requested: $"))
        years = int(validate_input("Enter loan term (in years): "))
    except ValueError:
        print("Invalid number format. Please enter numeric values.")
        return None, None, None, None
    
    return name, gender, loan_amount, years

def calculate_loan(loan_amount, years):
    # Simple interest rate calculation
    # Assume 5% interest rate for males and 4.5% for females (example purposes only)
    monthly_payment = (loan_amount * (1 + 0.05 * years)) / (years * 12)
    return monthly_payment

def approve_loan(name, gender, loan_amount, years):
    if not all([name, gender, loan_amount, years]):
        print("Error: Missing or invalid information.")
        return

    title = "Mr." if gender == 'M' else "Ms."
    monthly_payment = calculate_loan(loan_amount, years)
    
    print("\n=== Loan Approval Summary ===")
    print(f"Applicant: {title} {name}")
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Loan Term: {years} years")
    print(f"Estimated Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Status: Loan approved for {title} {name}.")

def main():
    print("============================")
    print("=== Loan Approval System ===")
    print("============================")
    
    while True:
        name, gender, loan_amount, years = get_applicant_info()
        approve_loan(name, gender, loan_amount, years)
        
        if validate_input("\nProcess another application? (Y/N): ", ['Y', 'N']).upper() == 'N':
            break
    
    print("\nThank you for using the Loan Approval System!")

if __name__ == "__main__":
    main()