# ===================================
# PYTHON CONTROL STATEMENTS
# ===================================

# Control statements determine the flow of execution in a program.

# ===================================
# IF-ELSE STATEMENTS
# ===================================

# If-else statements allow conditional execution.

age = 18

if age >= 18:
    print("You are an adult.")  # Output: You are an adult.
else:
    print("You are a minor.")

# The `elif` keyword allows multiple conditions.
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Output: Grade: B
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# ===================================
# TERNARY OPERATOR
# ===================================

# A short-hand if-else statement (ternary operator)
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# ===================================
# LOOPS
# ===================================

# Loops help repeat a block of code multiple times.

# FOR LOOP
# Iterates over a sequence (list, tuple, string, range)

for i in range(5):  # Loops from 0 to 4
    print(i)  # Output: 0 1 2 3 4

# Looping over a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)  # Output: Apple, Banana, Cherry

# Looping over a string
word = "Python"
for letter in word:
    print(letter)  # Output: P y t h o n

# Looping with index (using enumerate)
for index, fruit in enumerate(fruits):
    print(index, fruit)  # Output: 0 Apple, 1 Banana, 2 Cherry

# WHILE LOOP
# Executes as long as the condition is True.

count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1  # Increments count

# ===================================
# BREAK, CONTINUE, PASS
# ===================================

# `break` stops the loop immediately.
for i in range(10):
    if i == 5:
        break  # Stops at 5
    print(i)  # Output: 0 1 2 3 4

# `continue` skips the current iteration.
for i in range(5):
    if i == 2:
        continue  # Skips 2
    print(i)  # Output: 0 1 3 4

# `pass` does nothing (used as a placeholder).
for i in range(3):
    pass  # No error, but does nothing

# ===================================
# NESTED LOOPS
# ===================================

# A loop inside another loop.
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
# Output: (0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)

# ===================================
# SUMMARY
# ===================================
# - If-else statements control decision-making.
# - Loops (for, while) help repeat code.
# - break (stops loop), continue (skips iteration), pass (placeholder).
# - Nested loops are loops inside loops.
