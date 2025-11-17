def discount(price, category):
    if category.lower() == "student":
        if price > 1000:
            return price * 0.9
        else:
            return price * 0.95
    else:
        if price > 2000:
            return price * 0.85
        else:
            return price

# Sample input values
inputs = [
    (800, "student"),
    (1200, "student"),
    (999, "student"),
    (2000, "student"),
    (1500, "regular"),
    (2500, "regular"),
    (2100, "customer"),
    (1800, "other")
]

# Printing outputs
for price, category in inputs:
    result = discount(price, category)
    print(f"Price: {price}, Category: {category} → Discounted Price: {result}")
