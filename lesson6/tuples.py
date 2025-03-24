"""
Assignment: Tuples in Python

Task: Write Python programs to demonstrate the use of Tuples in python.
"""

# Tuples in Python
# A tuple is an `ordered`, `immutable` sequence of elements.
# Tuples are useful for fixed data collections.

# Creating Tuples
tuple1: tuple = tuple(["apple", "banana", "cherry"])  # Casting a list into a tuple
tuple2: tuple = (10, 20, 30)  # Simple tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True)  # Tuple with mixed data types

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)

# Accessing Elements in a Tuple
print("tuple1[0] =", tuple1[0])  # Accessing the first element

# Tuple Slicing
print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1

# Tuple Length
print("Length of tuple1:", len(tuple1))

# Iterating Through a Tuple
print("Iterating through tuple2:")
for item in tuple2:
    print(item)

# Checking if an Item Exists in a Tuple
print("Is 20 in tuple2?", 20 in tuple2)

# Concatenating Tuples
tuple3: tuple = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

# Repeating Tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)

# Nested Tuples
nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple)

# Unpacking Tuples
a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)

# Using Tuples as Keys in Dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)

# Immutable Nature of Tuples (Trying to Modify a Tuple Will Raise an Error)
# tuple1[0] = "watermelon"  # Uncommenting this line will cause an error

# Tuple Methods: count() and index()
print("tuple1.count('apple') =", tuple1.count("apple"))  # Count occurrences
print("tuple1.index('apple') =", tuple1.index("apple"))  # Find index

# Listing Methods Available for Tuples (Excluding Dunder Methods)
tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]
print("Tuple Methods:", tuple_methods)  # Output: ['count', 'index']

# Example Usage of Tuple Methods
tuple_example: tuple = ("apple", "banana", "cherry", "apple")
print("Count of 'apple':", tuple_example.count("apple"))  # Output: 2
print("Index of 'banana':", tuple_example.index("banana"))  # Output: 1

# Type Hinting Example
a: int = input("Enter a number: ")  # Input is always a string
print(a, type(a))  # Will still print as <class 'str'> since input() returns a string
