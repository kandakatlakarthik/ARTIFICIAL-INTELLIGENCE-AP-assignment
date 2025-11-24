def read_file(filename):
    """
    Reads data from a file, ensuring the file is closed and handling errors.

    Args:
        filename (str): The path to the file.

    Returns:
        str: The contents of the file, or None if an error occurs.
    """
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None

# Example usage:
# print(read_file("existing_file.txt"))
# print(read_file("non_existent_file.txt"))