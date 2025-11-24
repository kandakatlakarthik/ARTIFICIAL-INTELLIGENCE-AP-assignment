import math

def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

def calculate_square_area(side):
    """Calculates the area of a square."""
    return side * side

def calculate_circle_area(radius):
    """Calculates the area of a circle."""
    return math.pi * radius * radius

# Dictionary to dispatch to the correct function
AREA_CALCULATORS = {
    "rectangle": calculate_rectangle_area,
    "square": calculate_square_area,
    "circle": calculate_circle_area,
}

def calculate_area(shape, *args):
    """
    Calculates the area of a given shape using a dictionary-based dispatch.
    """
    calculator_func = AREA_CALCULATORS.get(shape)
    if not calculator_func:
        raise ValueError(f"Unsupported shape: '{shape}'. Supported shapes are {list(AREA_CALCULATORS.keys())}")
    
    return calculator_func(*args)


