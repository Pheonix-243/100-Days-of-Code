# =========================
# Day 6: While Loops in Python
# =========================

# A while loop be a control structure wey dey run a block of code repeatedly
# **as long as a condition remains True**.

# ------------------------
# Basic Syntax of While Loop
# ------------------------

# while condition:
#     # Code block to execute repeatedly

# Example: Print numbers from 1 to 5 using while loop

num = 1  # Start point
while num <= 5:  # Condition to keep running
    print(num)
    num += 1  # Increase num each time

# Output:
# 1
# 2
# 3
# 4
# 5

# ------------------------
# Infinite While Loop (BE CAREFUL!)
# ------------------------

# If we no update the condition, the loop go run forever.
# Example (Don't run this without stopping):

# while True:
#     print("This will run forever!")

# ------------------------
# Using While Loop with User Input
# ------------------------

# We fit use while loop to keep asking the user for input until e meet condition

password = ""
while password != "secret":  # Keep asking until the user enters "secret"
    password = input("Enter password: ")

print("Access Granted!")  # This prints only when password == "secret"

# ------------------------
# While Loop with a Break Statement
# ------------------------

# break statement dey stop a loop immediately

count = 0
while count < 10:
    print(count)
    if count == 5:
        break  # Stop the loop when count == 5
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 5  (Loop stops here)

# ------------------------
# While Loop with Continue Statement
# ------------------------

# continue dey skip one iteration and move to the next one

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Skip when x == 3
    print(x)

# Output:
# 1
# 2
# 4
# 5  (3 was skipped)
