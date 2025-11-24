def bubble_sort(data_list):
    """
    Sorts a list of elements in ascending order using the Bubble Sort algorithm.

    This function iterates through the list multiple times, comparing adjacent
    elements and swapping them if they are in the wrong order. The process
    is repeated until the list is sorted.

    Args:
        data_list: The list of elements to be sorted. The list is sorted in-place.

    Returns:
        The sorted list.
    """
    n = len(data_list)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list

# --- Example Usage ---
if __name__ == "__main__":
    my_numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", my_numbers)

    # Sort the list using Bubble Sort and check the output
    bubble_sort(my_numbers)
    print("Sorted list:  ", my_numbers)