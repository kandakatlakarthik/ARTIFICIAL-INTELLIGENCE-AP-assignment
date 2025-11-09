# ...existing code...
def cm_to_inches(cm: float, decimals: int | None = 3) -> float:
    """
    Convert centimeters to inches.
    By default returns value rounded to `decimals` places (3).
    """
    inches = cm / 2.54
    return round(inches, decimals) if decimals is not None else inches


if __name__ == "__main__":
    # Read a number from stdin, convert and print with 3 decimal places
    try:
        value = float(input().strip())
    except Exception:
        raise SystemExit("Invalid input: please provide a numeric value in centimeters.")
    print(f"{cm_to_inches(value, 3):.3f}")
# ...existing code...