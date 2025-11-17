"""
This script processes a list of scores to find the average, highest, and lowest values.
The main logic is modularized into smaller, reusable helper functions.
"""
from typing import List, Union

def calculate_average(scores: List[Union[int, float]]) -> float:
    """
    Calculates the average of a list of scores.
    Returns 0 if the list is empty.
    """
    if not scores:
        return 0.0
    # Use built-in sum() and len() for a more concise and efficient calculation
    return sum(scores) / len(scores)

def find_highest(scores: List[Union[int, float]]) -> Union[int, float, None]:
    """
    Finds the highest score in a list.
    Returns None if the list is empty.
    """
    if not scores:
        return None
    # Use the built-in max() function
    return max(scores)

def find_lowest(scores: List[Union[int, float]]) -> Union[int, float, None]:
    """
    Finds the lowest score in a list.
    Returns None if the list is empty.
    """
    if not scores:
        return None
    # Use the built-in min() function
    return min(scores)

def process_scores(scores: List[Union[int, float]]):
    """
    Processes a list of scores to calculate and display the average,
    highest, and lowest scores using helper functions.
    """
    if not scores:
        print("Score list is empty. Cannot process.")
        return

    # Call helper functions to get the values
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print(f"Scores: {scores}")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

# --- Main execution block with sample input ---
if __name__ == "__main__":
    sample_scores = [88, 92, 100, 75, 83, 95, 67]
    process_scores(sample_scores)
