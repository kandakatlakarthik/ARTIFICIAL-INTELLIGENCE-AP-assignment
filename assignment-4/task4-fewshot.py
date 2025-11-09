# ...existing code...
def count_vowels(s: str) -> int:
    """Count vowels a, e, i, o, u in the given string (case-insensitive)."""
    return sum(1 for ch in s.lower() if ch in "aeiou")

def get_vowel_count_from_input(prompt: str = "") -> int:
    """Read a string from the user and return the vowel count."""
    s = input(prompt)
    return count_vowels(s)

if __name__ == "__main__":
    # Example: prints the count for a user-provided string
    print(get_vowel_count_from_input())
# ...existing code...
# filepath: c:\Users\LENOVO\Desktop\aiap\assignment-4\task4-fewshot.py
# ...existing code...
def count_vowels(s: str) -> int:
    """Count vowels a, e, i, o, u in the given string (case-insensitive)."""
    return sum(1 for ch in s.lower() if ch in "aeiou")

def get_vowel_count_from_input(prompt: str = "") -> int:
    """Read a string from the user and return the vowel count."""
    s = input(prompt)
    return count_vowels(s)

if __name__ == "__main__":
    # Example: prints the count for a user-provided string
    print(get_vowel_count_from_input())
# ...existing code...