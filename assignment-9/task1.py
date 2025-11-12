def sum_even_odd(numbers):
    """Calculates the sum of even and odd numbers in a list.

    This function takes a list of integers, iterates through each number,
    and segregates them into even and odd groups. It then calculates the
    sum of each group.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        tuple[int, int]: A tuple containing two integers:
                         - The sum of all even numbers.
                         - The sum of all odd numbers.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_total, odd_total = sum_even_odd(my_list)

    print(f"Original list: {my_list}")
    print(f"Sum of even numbers: {even_total}")
    print(f"Sum of odd numbers: {odd_total}")