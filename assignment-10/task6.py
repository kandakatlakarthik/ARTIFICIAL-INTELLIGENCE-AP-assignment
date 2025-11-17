def grade_elif(score):
    # Input validation
    if not isinstance(score, (int, float)):
        return "Error: Score must be a number."
    if score < 0 or score > 100:
        return "Error: Score must be between 0 and 100."

    # Grade logic
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# -----------------------------
# Method 2: Cleaner logic using dictionary mapping
# -----------------------------
def grade_dict(score):
    # Input validation
    if not isinstance(score, (int, float)):
        return "Error: Score must be a number."
    if score < 0 or score > 100:
        return "Error: Score must be between 0 and 100."

    grade_map = {
        range(90, 101): "A",
        range(80, 90): "B",
        range(70, 80): "C",
        range(60, 70): "D",
        range(0, 60): "F"
    }

    for r, g in grade_map.items():
        if score in r:
            return g


# -----------------------------
# Testing both functions
# -----------------------------
test_scores = [95, 83, 72, 60, 49, -5, 105, "90"]

for s in test_scores:
    print(f"Input: {s} → elif method: {grade_elif(s)}  |  dict method: {grade_dict(s)}")
