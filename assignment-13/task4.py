# Original inefficient code
# nums = [1,2,3,4,5,6,7,8,9,10]
# squares = []
# for i in nums:
#     squares.append(i * i)

# Refactored using a list comprehension for better performance and readability
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [i * i for i in nums]
print(squares)