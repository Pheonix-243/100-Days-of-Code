# Basic for loop syntax

sequence = ["apple", "banana", "cherry"]
for variable in sequence:
    # Code to execute
    pass  # Replace with actual code

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() to loop through numbers
for i in range(1, 6):  # Loops from 1 to 5
    print(i)

for i in range(5):  # Loops from 0 to 4
    print(i)

for i in range(0, 10, 2):  # Loops from 0 to 8 (step of 2)
    print(i)

# Looping through a string
for letter in "Hello":
    print(letter)

# Looping through a dictionary
person = {"name": "Bright", "age": 22, "country": "Ghana"}

for key in person:  # Iterating over keys
    print(key)

for value in person.values():  # Iterating over values
    print(value)

for key, value in person.items():  # Iterating over key-value pairs
    print(key, ":", value)

# Using break in a loop
for num in range(1, 6):
    if num == 3:
        break  # Stops the loop at 3
    print(num)
print("Loop stopped!")

# Using continue to skip an iteration
for num in range(1, 6):
    if num == 3:
        continue  # Skips 3
    print(num)

# Using else in a for loop
for num in range(1, 4):
    print(num)
else:
    print("Loop finished successfully!")

# else does not run if break is used
for num in range(1, 4):
    if num == 2:
        break
    print(num)
else:
    print("Loop finished successfully!")  # This won't print

# Using enumerate() to get index and value
names = ["Bright", "Blessing", "Stanley"]
for index, name in enumerate(names):
    print(index, name)









##################################

student_scores = [
    98, 75, 88, 92, 67, 81, 95, 73, 89, 100, 56, 79, 84, 91, 68, 90, 77, 85, 93, 82,
    74, 96, 87, 99, 55, 76, 83, 70, 97, 72, 94, 78, 80, 86, 66, 65, 69, 60, 64, 58,
    59, 63, 57, 62, 54, 53, 52, 51, 50, 61, 71, 67, 88, 92, 95, 89, 100, 79, 84, 91,
    68, 90, 77, 85, 93, 82, 74, 96, 87, 99, 55, 76, 83, 70, 97, 72, 94, 78, 80, 86,
    66, 65, 69, 60, 64, 58, 59, 63, 57, 62, 54, 53, 52, 51, 50, 61, 71, 98, 75, 88,
    92, 67, 81, 95, 73, 89, 100, 56, 79, 84, 91, 68, 90, 77, 85, 93, 82, 74, 96, 87,
    99, 55, 76, 83, 70, 97, 72, 94, 78, 80, 86, 66, 65, 69, 60, 64, 58, 59, 63, 57,
    62, 54, 53, 52, 51, 50, 61, 71, 98, 75, 88, 92, 67, 81, 95, 73, 89, 100, 56, 79,
    84, 91, 68, 90, 77, 85, 93, 82, 74, 96, 87, 99, 55, 76, 83, 70, 97, 72, 94, 78,
    80, 86, 66, 65, 69, 60, 64, 58, 59, 63, 57, 62, 54, 53, 542, 51, 50, 61, 71
]


total_scores = sum(student_scores)
max_score = max(student_scores)


print(total_scores)
print(max_score)

sum = 0
max = 0

for score in student_scores:
    sum += score
    if score > max:
        max = score

print(f"This is the total sum of the scores done manually: {sum}")
print(f"This is the max of the scores done manually: {max}")


# For Loop with the range function
t = 0
for i in range(1,101):
    t += i
print(t)