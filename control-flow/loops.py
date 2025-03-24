"""
Assignment: Loops and Iteration in Python

Task: Write Python programs to demonstrate the use of for loops and while loops.
"""

# 1. Using a for loop to iterate over a list of student scores and calculate the average
students_scores = [85, 90, 78, 92, 88]
total = 0
for score in students_scores:
    total += score
average = total / len(students_scores)
print("The average score of students is:", average)

# 2. Using a for loop with a range to simulate a washing machine's spinning cycles
for spin in range(1, 6):  # 5 spins
    print(f"Washing machine spinning... Cycle {spin}")

# 3. Using a while loop to fill a gas tank
fuel_level = 0
while fuel_level < 100:
    print(f"Filling fuel... Current level: {fuel_level}%")
    fuel_level += 20  # Filling fuel in increments of 20%
print("Gas tank is full!")

# 4. Using while loop to simulate a refrigerator cooling until the temperature is reached
temp = 30  # Initial temperature
while temp > 4:
    print(f"Cooling... Current temperature: {temp}°C")
    temp -= 2  # Cooling down step
print("Refrigerator is at optimal temperature!")

# 5. Using for loop with else in Python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
else:
    print("Loop completed successfully without break.")
