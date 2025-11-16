# test_date_converter.py

import unittest
from date_converter import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    """Test suite for the convert_date_format function."""

    def test_valid_date_conversion(self):
        """Test conversion of a standard valid date."""
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")

    def test_leap_year_date(self):
        """Test conversion of a leap day."""
        # 2024 is a leap year
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")

    def test_invalid_date_values(self):
        """Test inputs with invalid date values (e.g., month 13, day 32)."""
        invalid_dates = [
            "2023-13-01",  # Invalid month
            "2023-00-15",  # Invalid month (zero)
            "2023-04-31",  # Invalid day for April
            "2023-02-29",  # Invalid day (2023 is not a leap year)
            "1900-02-29",  # Invalid day (1900 is not a leap year)
        ]
        for date_str in invalid_dates:
            with self.subTest(date=date_str):
                with self.assertRaisesRegex(ValueError, "Invalid date or format"):
                    convert_date_format(date_str)

    def test_invalid_date_formats(self):
        """Test inputs with incorrect string formats."""
        invalid_formats = [
            "15-10-2023",      # Wrong format (DD-MM-YYYY)
            "2023/10/15",      # Wrong separator
            "23-10-15",        # Two-digit year
            "2023-Oct-15",     # Month as text
            "2023-10-15 10:00",# Extra time information
            "not-a-date",      # Gibberish
            "",                # Empty string
        ]
        for date_str in invalid_formats:
            with self.subTest(format=date_str):
                with self.assertRaisesRegex(ValueError, "Invalid date or format"):
                    convert_date_format(date_str)

    def test_invalid_input_types(self):
        """Test inputs that are not strings."""
        non_string_inputs = [
            None,
            12345,
            20231015.0,
            ["2023-10-15"],
            {"date": "2023-10-15"},
        ]
        for item in non_string_inputs:
            with self.subTest(type=type(item)):
                with self.assertRaises(TypeError):
                    convert_date_format(item)

if __name__ == '__main__':
    unittest.main(verbosity=2)
