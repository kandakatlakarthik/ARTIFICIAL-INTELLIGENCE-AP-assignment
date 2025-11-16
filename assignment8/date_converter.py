# date_converter.py

import datetime

def convert_date_format(date_str: str) -> str:
    """
    Converts a date string from "YYYY-MM-DD" to "DD-MM-YYYY".

    Example: "2023-10-15" -> "15-10-2023"

    Args:
        date_str: The date string in "YYYY-MM-DD" format.

    Returns:
        The date string in "DD-MM-YYYY" format.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is not a valid date or not in the
                    correct "YYYY-MM-DD" format.
    """
    if not isinstance(date_str, str):
        raise TypeError("Input must be a string.")
    
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        raise ValueError(f"Invalid date or format for '{date_str}'. Expected 'YYYY-MM-DD'.")