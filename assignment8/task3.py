import re
import unittest

def is_sentence_palindrome(sentence: str) -> bool:
    """
    Checks if a sentence is a palindrome, ignoring case, punctuation, and spaces.

    Args:
        sentence: The string to check.

    Returns:
        True if the sentence is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")

    # Sanitize the string: convert to lowercase and remove non-alphanumeric characters.
    cleaned_sentence = re.sub(r'[^a-z0-9]', '', sentence.lower())

    # Check if the cleaned string is equal to its reverse.
    return cleaned_sentence == cleaned_sentence[::-1]


class TestIsSentencePalindrome(unittest.TestCase):
    """Test suite for the is_sentence_palindrome function."""

    def test_palindrome_sentences(self):
        """Test sentences that are palindromes, ignoring case, spaces, and punctuation."""
        palindromes = [
            "A man, a plan, a canal: Panama",
            "Was it a car or a cat I saw?",
            "No 'x' in 'Nixon'",
            "Madam, in Eden, I'm Adam.",
            "Go hang a salami, I'm a lasagna hog.",
            "Step on no pets.",
            "racecar",
            "level",
        ]
        for sentence in palindromes:
            with self.subTest(sentence=sentence):
                self.assertTrue(is_sentence_palindrome(sentence), f"Expected '{sentence}' to be a palindrome.")

    def test_non_palindrome_sentences(self):
        """Test sentences that are not palindromes."""
        non_palindromes = [
            "hello world",
            "python programming",
            "This is not a palindrome",
            "A man, a plan, a canal: Suez",
        ]
        for sentence in non_palindromes:
            with self.subTest(sentence=sentence):
                self.assertFalse(is_sentence_palindrome(sentence), f"Expected '{sentence}' not to be a palindrome.")

    def test_edge_cases(self):
        """Test edge cases like empty strings, single characters, and numbers."""
        edge_cases = {
            "": True,  # An empty string is technically a palindrome
            " ": True, # A string with only spaces is a palindrome
            "a": True,
            "12321": True,
            "12345": False,
            "A": True,
            ".,?!": True # A string with only punctuation is a palindrome
        }
        for sentence, expected in edge_cases.items():
            with self.subTest(sentence=sentence):
                self.assertEqual(is_sentence_palindrome(sentence), expected)

    def test_invalid_input_types(self):
        """Test that non-string inputs raise a TypeError."""
        invalid_inputs = [
            None,
            12321,
            123.45,
            ["A man, a plan, a canal: Panama"],
            {"sentence": "Was it a car or a cat I saw?"},
        ]
        for item in invalid_inputs:
            with self.subTest(item=item):
                with self.assertRaises(TypeError):
                    is_sentence_palindrome(item)


if __name__ == '__main__':
    # This allows running the tests directly from the command line
    # with detailed output.
    unittest.main(verbosity=2)