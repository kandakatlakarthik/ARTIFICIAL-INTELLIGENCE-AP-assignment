class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self):
        return self.average() >= 60

def main():
    # Get student information from user
    name = input("Enter student name: ")
    
    while True:
        try:
            age = int(input("Enter student age: "))
            if age > 0:
                break
            print("Age must be positive!")
        except ValueError:
            print("Please enter a valid number for age!")
    
    # Create student object
    student = Student(name, age)
    
    # Get grades from user
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                student.add_grade(grade)
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number for grade!")
    
    # Display student information
    print("\nStudent Information:")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Grades: {student.grades}")
    print(f"Average: {student.average():.2f}")
    print(f"Passing Status: {'Passed' if student.is_passing() else 'Failed'}")

if __name__ == "__main__":
    main()