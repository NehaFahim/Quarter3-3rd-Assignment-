"""
Assignment: Lists in python 

Task: Write Python programs to demonstrate the use of List in python.
"""

# Working with Lists and Tuples

# 1. Creating a List
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["hello", 42, 3.14, True]

print("fruits  =", fruits)
print("numbers =", numbers)
print("mixed   =", mixed)

# 2. Accessing List Elements
print(fruits[0])   # Output: apple
print(fruits[-3])  # Output: apple

# 3. Modifying Lists
fruits[-3] = "watermelon"  # Replacing "apple" with "watermelon"
print(fruits)

# 4. List Slicing
print(fruits[0:2])  # Output: ['watermelon', 'banana']

# 5. Appending and Extending Lists
fruits.append("mango")  # Adds 'mango'
print(fruits)

fruits.extend(["grape", "kiwi"])  # Adds multiple elements
print(fruits)

# 6. Removing Elements
fruits.remove("banana")  # Removes 'banana'
print(fruits)

# 7. Pop Method
deleted = fruits.pop(1)  # Removes element at index 1
print("Deleted element =", deleted)
print(fruits)

# 8. Sorting a List
numbers = [3, 1, 4, 1, 5, 9]  # Unsorted list
numbers.sort()
print(numbers)  # Ascending order

numbers.sort(reverse=True)
print(numbers)  # Descending order

# Sorting by String Length
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words)

# Sorting by Last Character
words.sort(key=lambda word: word[-1])
print(words)

# Reverse Sorting
numbers = [1, 2, 5, 7, 10]
numbers.reverse()
print(numbers)

# 9. Iterating Over Lists
for fruit in fruits:
    print(fruit)

# 10. List Comprehension
squared = [x**2 for x in [1, 2, 3, 4, 5]]
print(squared, ":", type(squared))

squared = [x**2 for x in [1, 2, 3, 4, 5] if x > 3]
print(squared, ":", type(squared))
