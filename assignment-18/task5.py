class Car:
    """
    A class to represent a car with brand, model, and year.
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Initializes the Car object with brand, model, and year.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self) -> None:
        """
        Prints the details of the car.
        """
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Call the display_details method
my_car.display_details()