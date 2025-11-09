def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in input_string if char in vowels)
    return count

# New function to get user input and count vowels
def main():
    user_input = input("Enter a string: ")  # Get user input
    vowel_count = count_vowels(user_input)    # Count vowels
    print(f"Number of vowels: {vowel_count}")  # Print the result

if __name__ == "__main__":
    main()  # Call the main function