import random

# Lists of characters to use in the password
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()-_=+[]{};:,.<>?/|'

# Convert strings into lists for random selection
letters = list(letters)
numbers = list(numbers)
symbols = list(symbols)

print("Welcome to the Python Password Generator!")

# User input for password length
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password components
password_letters = random.sample(letters, nr_letters)
password_symbols = random.sample(symbols, nr_symbols)
password_numbers = random.sample(numbers, nr_numbers)

# Combine all characters
password_list = password_letters + password_symbols + password_numbers

# Shuffle the password for randomness
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

# Output the final password
print(f"Your generated password is: {password}")
