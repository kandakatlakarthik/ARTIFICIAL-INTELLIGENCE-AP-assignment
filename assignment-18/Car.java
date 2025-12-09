/**
 * A class to represent a car with brand, model, and year.
 */
public class Car {
    // Attributes
    private String brand;
    private String model;
    private int year;

    /**
     * Constructor to initialize the Car object.
     * @param brand The brand of the car.
     * @param model The model of the car.
     * @param year The manufacturing year of the car.
     */
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    /**
     * Prints the details of the car.
     */
    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + this.brand);
        System.out.println("Model: " + this.model);
        System.out.println("Year: " + this.year);
    }

    /**
     * The main method to create a Car object and display its details.
     */
    public static void main(String[] args) {
        // Create an object of the Car class
        Car myCar = new Car("Toyota", "Corolla", 2020);

        // Call the displayDetails method
        myCar.displayDetails();
    }
}