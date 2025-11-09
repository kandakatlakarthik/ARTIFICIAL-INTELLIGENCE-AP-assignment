def format_name(full_name):
    """
    Format a full name as 'Last, First'
    
    Args:
        full_name (str): Full name as a string (e.g., 'John Doe')
    
    Returns:
        str: Formatted name as 'Last, First'
    """
    # Split the name into parts
    name_parts = full_name.split()
    
    # Handle edge cases
    if not name_parts:
        return ""
    if len(name_parts) == 1:
        return name_parts[0]
        
    # Extract last name (last part) and everything else
    last_name = name_parts[-1]
    first_names = " ".join(name_parts[:-1])
    
    # Return formatted string
    return f"{last_name}, {first_names}"

def main():
    while True:
        # Get user input
        user_input = input("Enter a full name (or 'quit' to exit): ").strip()
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            break
            
        # Format and display the result
        formatted_name = format_name(user_input)
        print(f"Formatted name: {formatted_name}")

if __name__ == "__main__":
    main()