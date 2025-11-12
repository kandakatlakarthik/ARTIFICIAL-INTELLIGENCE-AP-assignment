# Define the sru_student class to represent a student's record.
class sru_student:
    # The __init__ method is the constructor for the class.
    # It is automatically called when a new object (student) is created.
    def __init__(self, name, roll_no, hostel_status):
        # Assign the provided name to the 'name' attribute of the student object.
        self.name = name
        # Assign the provided roll number to the 'roll_no' attribute.
        self.roll_no = roll_no
        # Assign the provided hostel status (e.g., True/False) to the 'hostel_status' attribute.
        self.hostel_status = hostel_status
        # Initialize a 'fee' attribute with a default value, for example, 50000.
        self.fee = 50000

    # This method updates the student's fee.
    def fee_update(self, new_fee):
        # Assign the new_fee value to the object's 'fee' attribute.
        self.fee = new_fee
        # Print a confirmation message indicating the fee has been updated.
        print(f"Fee for {self.name} has been updated to {self.fee}.")

    # This method displays all the details of the student.
    def display_details(self):
        # Print a header for the student's details.
        print("\n--- Student Details ---")
        # Print the student's name.
        print(f"Name: {self.name}")
        # Print the student's roll number.
        print(f"Roll No: {self.roll_no}")
        # Print the student's hostel status.
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")
        # Print the student's current fee.
        print(f"Fee: {self.fee}")

# This block of code will only run when the script is executed directly.
if __name__ == "__main__":
    # Prompt the user to enter the student's name.
    name_input = input("Enter student's name: ")
    # Prompt the user to enter the student's roll number.
    roll_no_input = input("Enter student's roll number: ")
    # Prompt the user for hostel status and convert the input to lowercase.
    hostel_input = input("Does the student require a hostel? (yes/no): ").lower()
    # Convert the user's 'yes'/'no' answer to a boolean True/False.
    hostel_status_input = (hostel_input == 'yes')

    # Create a new student object using the details provided by the user.
    student1 = sru_student(name_input, roll_no_input, hostel_status_input)
    # Display the initial details of the newly created student.
    student1.display_details()

    # Prompt the user to enter a new fee amount and convert it to a float (number with decimals).
    new_fee_input = float(input("\nEnter the new fee amount to update: "))
    # Call the fee_update method to update the student's fee.
    student1.fee_update(new_fee_input)
    # Display the details again to show the updated fee.
    student1.display_details()