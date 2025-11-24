def func(x):
    """
    The function for which we want to find the minimum.
    f(x) = 2x^3 + 4x + 5
    """
    return 2 * x**3 + 4 * x + 5
    
def func_derivative(x):
    """
    The derivative of the function f(x).
    f'(x) = 6x^2 + 4
    """
    return 6 * x**2 + 4
    
def main():
    """
    Demonstrates that f(x) has no minimum using gradient descent.
    """
    print("--- Attempting to find minimum using Gradient Descent ---")
    print("This will demonstrate that the function does not converge to a minimum.\n")
    
    # --- Parameters for Gradient Descent ---
    learning_rate = 0.01  # How big of a step to take
    iterations = 20       # Number of steps
    x = 5.0               # Starting point for x
    
    print(f"Starting at x = {x:.2f}, f(x) = {func(x):.2f}")
    print("-" * 50)
    
    # --- Gradient Descent Loop ---
    for i in range(iterations):
        gradient = func_derivative(x)
        
        # Update x by moving in the opposite direction of the gradient
        x = x - learning_rate * gradient
        
        # Print progress every 5 iterations
        if (i + 1) % 5 == 0:
            print(f"Iteration {i+1:2}: x = {x:10.2f}, f(x) = {func(x):12.2f}")
            
    print("-" * 50)
    print("\n--- Analysis ---")
    print("As shown above, the value of x continuously decreases, heading towards -infinity.")
    print("This is because the function's derivative (the gradient) is always positive.")
    print("Therefore, the function is always increasing and has no minimum value.")
    
if __name__ == "__main__":
    main()