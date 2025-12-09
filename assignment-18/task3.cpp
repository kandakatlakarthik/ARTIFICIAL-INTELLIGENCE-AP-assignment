#include <iostream>

/**
 * @brief Calculates the factorial of a non-negative integer using recursion.
 * 
 * @param n The non-negative integer.
 * @return The factorial of n.
 */
int factorial(int n) {
    // Base case: The factorial of 0 is 1.
    if (n == 0) {
        return 1;
    }
    // Recursive step: n * (n-1)!
    else {
        return n * factorial(n - 1);
    }
}

// --- Function Calls ---
int main() {
    // Call the function with input 5
    int input_5 = 5;
    int output_5 = factorial(input_5);
    std::cout << "Input: " << input_5 << " -> Output: Factorial = " << output_5 << std::endl;

    // Call the function with input 0
    int input_0 = 0;
    int output_0 = factorial(input_0);
    std::cout << "Input: " << input_0 << " -> Output: Factorial = " << output_0 << std::endl;

    return 0;
}
