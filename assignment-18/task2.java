public class NumberChecker {

    /**
     * Checks if a given integer is positive, negative, or zero and prints the result.
     * @param num The integer to check.
     */
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println("The number is positive");
        } else if (num < 0) {
            System.out.println("The number is negative");
        } else {
            System.out.println("The number is zero");
        }
    }

    public static void main(String[] args) {
        System.out.println("--- Java Execution ---");

        System.out.print("Input: -5 -> Output: ");
        checkNumber(-5);

        System.out.print("Input: 0 -> Output: ");
        checkNumber(0);

        System.out.print("Input: 7 -> Output: ");
        checkNumber(7);
    }
}
