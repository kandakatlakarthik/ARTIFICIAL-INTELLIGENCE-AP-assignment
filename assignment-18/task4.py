def print_students(students: list[str]) -> None:
    """
    Takes a list of student names and prints each name.
    
    Args:
        students: A list of student names.
    """
    print("Student List:")
    for student in students:
        print(student)

# Sample data
student_names = ["Alice", "Bob", "Charlie"]

# Test the function
print_students(student_names)
