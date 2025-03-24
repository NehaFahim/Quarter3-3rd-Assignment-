"""
Assignment: Dictionary in Python

Task: Write Python programs to demonstrate the use of Dictionary in python.
"""

# Dictionary in Python

# Creating a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "course": "Computer Science"
}
print("Student Dictionary:", student)

# Accessing values using keys
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))

# Adding new key-value pairs
student["grade"] = "A"
print("Updated Dictionary:", student)

# Updating an existing key
student["age"] = 21
print("After Updating Age:", student)

# Removing a key-value pair
removed_value = student.pop("grade")
print("After Removing Grade:", student)
print("Removed Value:", removed_value)

# Iterating through a dictionary
print("\nIterating through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "course" in student:
    print("\nCourse key exists in dictionary.")

# Dictionary with mixed data types
mixed_dict = {
    "name": "Fatima",
    "marks": [85, 90, 78],
    "details": {"city": "Karachi", "country": "Pakistan"}
}
print("\nDictionary with mixed data types:", mixed_dict)

# Nested dictionary
students = {
    "student1": {"name": "Ahmed", "age": 22},
    "student2": {"name": "Sara", "age": 20}
}
print("\nNested Dictionary:", students)

# Using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\nDictionary Comprehension (Squares):", squares)
