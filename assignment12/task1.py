def linear_search(data_list, search_value):
    """
    Performs a linear search to find the index of a value in a list.

    This function iterates through each element of the list one by one
    to check if it matches the search value.

    Args:
        data_list: The list of elements to search through.
        search_value: The value to search for.

    Returns:
        The index of the first occurrence of the search_value if found,
        otherwise returns -1.
    """
    for index, value in enumerate(data_list):
        if value == search_value:
            return index  # Return the index when the value is found
    return -1  # Return -1 if the loop completes without finding the value

# --- Example Usage ---
if __name__ == "__main__":
    my_numbers = [10, 23, 45, 70, 11, 15, 88, 62]
    target_value = 70

    # Search for the target value in the list
    result_index = linear_search(my_numbers, target_value)

    if result_index != -1:
        print(f"Value '{target_value}' found at index: {result_index}")
    else:
        print(f"Value '{target_value}' not found in the list.")