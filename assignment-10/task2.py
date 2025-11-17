# Optimized version of find_common using Python sets

def find_common(a, b):
    """
    Returns the common elements between two lists using set intersection.
    Duplicate handling:
        - Result will contain each common element only once.
    """
    return list(set(a) & set(b))


# -------- SAMPLE INPUT --------
a = [1, 2, 3, 4, 4, 5]
b = [3, 4, 4, 6]

# -------- OUTPUT --------
result = find_common(a, b)
print("Common Elements:", result)
