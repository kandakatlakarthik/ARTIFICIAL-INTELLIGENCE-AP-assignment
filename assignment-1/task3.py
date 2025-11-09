# Function to reverse a string
def reverse_string(input_str):
    return input_str[::-1]

# Get input from user
user_string = input("Enter a string: ")

# Call the function and print result
reversed_string = reverse_string(user_string)
print("Reversed string:", reversed_string)