"""
Assignment: Control Flow and Decision Making in Python

Task: Write Python programs to demonstrate the concepts of control flow using if, elif, else, and logical operators.
"""

# 1. Using if statement
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

# 2. Using if-else statement
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. Using if-elif-else statement
grade = int(input("Enter your marks: "))
if grade >= 90:
    print("A Grade")
elif grade >= 80:
    print("B Grade")
elif grade >= 70:
    print("C Grade")
elif grade >= 60:
    print("D Grade")
else:
    print("Fail")

# 4. Using logical operators
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")

# 5. Nested if statement
num2 = int(input("Enter another number: "))
if num2 > 0:
    if num2 % 5 == 0:
        print("The number is positive and a multiple of 5.")
    else:
        print("The number is positive but not a multiple of 5.")
else:
    print("The number is not positive.")






    