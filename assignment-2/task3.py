def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    import math
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle"""
    return 0.5 * base * height

def calculate_square_area(side):
    """Calculate the area of a square"""
    return side ** 2

def main():
    while True:
        print("\n=== Area Calculator ===")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the Area Calculator!")
            break
            
        try:
            if choice == '1':
                radius = float(input("Enter the radius of the circle: "))
                area = calculate_circle_area(radius)
                print(f"Area of the circle is: {area:.2f} square units")
                
            elif choice == '2':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = calculate_rectangle_area(length, width)
                print(f"Area of the rectangle is: {area:.2f} square units")
                
            elif choice == '3':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = calculate_triangle_area(base, height)
                print(f"Area of the triangle is: {area:.2f} square units")
                
            elif choice == '4':
                side = float(input("Enter the side length of the square: "))
                area = calculate_square_area(side)
                print(f"Area of the square is: {area:.2f} square units")
                
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Invalid input! Please enter numerical values only.")

if __name__ == "__main__":
    main()