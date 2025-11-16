import re
import unittest

def is_valid_email(email: str) -> bool:
    """
    Validates an email address based on common practical standards.

    This function checks for:
    1. The input being a string.
    2. The basic structure: local-part@domain-part.
    3. Allowed characters in the local and domain parts.
    4. The domain part having at least one dot.
    5. The top-level domain (TLD) being at least two characters long.
    6. No leading/trailing/consecutive dots in the local part.
    7. No leading/trailing hyphens in domain labels.

    Args:
        email: The email string to validate.

    Returns:
        True if the email is valid, False otherwise.
    """
    if not isinstance(email, str):
        return False

    # A practical regex for email validation that covers most common cases
    # but is not strictly RFC 5322 compliant.
    # - Local part: letters, numbers, and specific special characters.
    #   - Cannot start or end with a dot.
    #   - Cannot have consecutive dots.
    # - @ symbol separator.
    # - Domain part: letters, numbers, hyphens.
    #   - Domain labels cannot start or end with a hyphen.
    # - TLD: at least 2 letters.
    email_regex = re.compile(
        r"^(?![.])(?!.*[.]{2})[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+(?<![.])"  # Local part
        r"@"
        r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"  # Domain name
        r"[a-zA-Z]{2,63}$"  # TLD
    )

    return re.fullmatch(email_regex, email) is not None


class TestIsValidEmail(unittest.TestCase):
    """
    Test suite for the is_valid_email function.
    """

    def test_valid_emails(self):
        """Test that commonly valid email formats pass."""
        valid_emails = [
            "simple@example.com",
            "very.common@example.com",
            "disposable.style.email.with+symbol@example.com",
            "other.email-with-hyphen@example.com",
            "fully-qualified-domain@example.co.uk",
            "user.name+tag+sorting@example.com",
            "x@example.com",
            "example-indeed@strange-example.com",
            "admin@mailserver1.com", # Changed to be a valid FQDN
            "example@s.solutions",
            # "user@com", # This is not a valid FQDN, so it should fail.
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), f"Expected {email} to be valid")

    def test_invalid_emails(self):
        """Test that invalid email formats fail."""
        invalid_emails = [
            "Abc.example.com",  # No @ symbol
            "A@b@c@example.com",  # Multiple @ symbols
            'a"b(c)d,e:f;g<h>i[j\\k]l@example.com',  # Invalid characters
            'just"not"right@example.com',  # Invalid quotes
            'this is"not\\allowed@example.com',  # Spaces
            "example@.com", # Leading dot in domain
            "example@com.", # Trailing dot in domain
            ".example@com.com", # Leading dot in local part
            "example.@com.com", # Trailing dot in local part
            "example..test@com.com", # Consecutive dots in local part
            "example@-com.com", # Leading hyphen in domain part
            "example@com-.com", # Trailing hyphen in domain part
            "example@com.c", # TLD too short
            "admin@mailserver1", # Not a fully-qualified domain name
            "user@com", # Not a fully-qualified domain name
            "", # Empty string
            "  ", # Whitespace string
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"Expected {email} to be invalid")

    def test_non_string_inputs(self):
        """Test that non-string inputs are handled gracefully."""
        non_string_inputs = [
            None,
            123,
            123.45,
            ["email@example.com"],
            {"email": "email@example.com"},
        ]
        for item in non_string_inputs:
            with self.subTest(item=item):
                self.assertFalse(is_valid_email(item), f"Expected non-string {type(item)} to be invalid")

if __name__ == '__main__':
    unittest.main(verbosity=2)


