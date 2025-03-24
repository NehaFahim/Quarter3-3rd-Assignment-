"""
Assignment: Set & Frozenset in Python

Task: Write Python programs to demonstrate the use of Set & Frozenset in python.
"""

# Creating a Set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding an element in Set
my_set.add(6)
print("After Adding 6:", my_set)

# Removing an element from Set
my_set.remove(3)  # Gives error if element not found
print("After Removing 3:", my_set)

# Discarding an element (does not give error if not found)
my_set.discard(10)  # No error even if 10 is not present
print("After Discarding 10:", my_set)

# Union of two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of two Sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference between two Sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

# Checking if an element exists in a Set
print("Is 2 in set1?", 2 in set1)

# Iterating through a Set
print("Iterating through set1:")
for item in set1:
    print(item)

# Creating a FrozenSet (Immutable Set)
frozen_set = frozenset([10, 20, 30, 40])
print("Frozen Set:", frozen_set)

# But we can perform union and intersection on frozenset
fs_union = frozen_set | {50, 60}
print("FrozenSet Union:", fs_union)

fs_intersection = frozen_set & {20, 40, 60}
print("FrozenSet Intersection:", fs_intersection)

