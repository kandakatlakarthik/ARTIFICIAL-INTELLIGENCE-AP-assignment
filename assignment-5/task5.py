def greet_user(name, gender):
    if gender == 'M':
        return f"Hello, Mr. {name}!"
    elif gender == 'F':
        return f"Hello, Ms. {name}!"
    else:
        return f"Hello, {name}!"
name = input("Enter your name: ")
gender = input("Enter your gender (M/F): ")
print(greet_user(name, gender))