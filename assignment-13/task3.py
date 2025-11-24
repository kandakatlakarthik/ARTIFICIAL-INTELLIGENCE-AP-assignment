class Student:
    """
    Represents a student with their personal information and academic marks.

    This class provides methods to store student details, display them,
    and calculate their total marks.
    """

    def __init__(self, name: str, age: int, marks: list[int]):
        """
        Initializes a new Student object.

        Args:
            name (str): The full name of the student.
            age (int): The age of the student in years.
            marks (list[int]): A list of integer marks obtained by the student
                               in various subjects.
        """
        # Improved naming for clarity
        self.name = name
        self.age = age
        # Storing marks as a list makes it more flexible and scalable
        self.marks = marks

    def display_details(self) -> None:
        """
        Prints the basic personal details of the student (name and age)
        in a human-readable format.
        """
        # Improved print readability using f-strings
        print(f"--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"-----------------------")

    def calculate_total_marks(self) -> int:
        """
        Calculates and returns the sum of all marks obtained by the student.

        Returns:
            int: The total sum of marks. Returns 0 if the marks list is empty.
        """
        # Using sum() for conciseness and readability
        return sum(self.marks)

    def display_marks(self) -> None:
        """
        Prints the individual marks of the student.
        """
        print(f"Marks obtained: {self.marks}")

    def calculate_average_marks(self) -> float:
        """
        Calculates and returns the average marks obtained by the student.

        Returns:
            float: The average of all marks. Returns 0.0 if no marks are present.
        """
        if not self.marks:
            return 0.0
        return self.calculate_total_marks() / len(self.marks)

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the Student object.
        This is useful for printing the object directly.
        """
        return (f"Student(Name='{self.name}', Age={self.age}, "
                f"Total Marks={self.calculate_total_marks()})")

# --- Example Usage ---
if __name__ == "__main__":
    # Creating a student instance
    student1 = Student("Alice Smith", 16, [85, 92, 78, 90])

    # Displaying details
    student1.display_details()
    # Output:
    # --- Student Details ---
    # Name: Alice Smith
    # Age: 16 years old
    # -----------------------

    # Displaying marks
    student1.display_marks()
    # Output:
    # Marks obtained: [85, 92, 78, 90]

    # Calculating and printing total marks
    total = student1.calculate_total_marks()
    print(f"Total Marks for {student1.name}: {total}")
    # Output:
    # Total Marks for Alice Smith: 345

    # Calculating and printing average marks
    average = student1.calculate_average_marks()
    print(f"Average Marks for {student1.name}: {average:.2f}")
    # Output:
    # Average Marks for Alice Smith: 86.25

    # Using the __str__ method
    print(student1)
    # Output:
    # Student(Name='Alice Smith', Age=16, Total Marks=345)

    # Another student with different number of marks
    student2 = Student("Bob Johnson", 17, [70, 65, 80])
    student2.display_details()
    print(f"Total Marks for {student2.name}: {student2.calculate_total_marks()}")
    print(f"Average Marks for {student2.name}: {student2.calculate_average_marks():.2f}")
