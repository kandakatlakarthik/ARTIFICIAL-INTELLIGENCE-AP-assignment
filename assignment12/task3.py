# We know:
# A uses: 1 Milk, 3 Choco
# B uses: 1 Milk, 2 Choco
# Total milk = 5
# Total choco = 12
# Profit: A = 6, B = 5

max_profit = 0
best_A = 0
best_B = 0

# Try all possible combinations of A and B
for A in range(0, 6):       # A cannot exceed 5 (milk constraint)
    for B in range(0, 6):   # B cannot exceed 5 (milk constraint)
        
        # Check constraints
        milk_used = A + B
        choco_used = 3*A + 2*B
        
        if milk_used <= 5 and choco_used <= 12:
            profit = 6*A + 5*B
            if profit > max_profit:
                max_profit = profit
                best_A = A
                best_B = B

# Print results
print("Optimal Units of A =", best_A)
print("Optimal Units of B =", best_B)
print("Maximum Profit =", max_profit)
