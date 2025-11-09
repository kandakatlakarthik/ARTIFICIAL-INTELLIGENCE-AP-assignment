# to find a largest number in the list Then assess the code quality and efficiency.

from typing import Iterable, List, Union

Number = Union[int, float]

def parse_numbers(s: str) -> List[Number]:
    """Parse a string of numbers separated by commas/whitespace into a list of floats/ints."""
    parts = [p.strip() for p in s.replace(",", " ").split()]
    nums: List[Number] = []
    for p in parts:
        if not p:
            continue
        try:
            if "." in p or "e" in p.lower():
                nums.append(float(p))
            else:
                nums.append(int(p))
        except ValueError:
            raise ValueError(f"Invalid number: {p}")
    return nums

def max_in_list(nums: Iterable[Number]) -> Number:
    """Return the largest element from nums. Raises ValueError for empty iterable."""
    it = iter(nums)
    try:
        max_val = next(it)
    except StopIteration:
        raise ValueError("max_in_list() arg is an empty iterable")
    for x in it:
        if x > max_val:
            max_val = x
    return max_val

if __name__ == "__main__":
    try:
        raw = input("Enter numbers separated by spaces or commas: ").strip()
        numbers = parse_numbers(raw)
        largest = max_in_list(numbers)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Largest number: {largest}")