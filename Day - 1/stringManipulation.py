# ===================================
# PYTHON STRING MANIPULATION
# ===================================

# Strings in Python are sequences of characters enclosed in quotes.
text = "Hello, World!"

# ===================================
# STRING INDEXING & SLICING
# ===================================

# Strings are indexed, meaning each character has a position (starting from 0).
print(text[0])   # Output: H
print(text[-1])  # Output: ! (Negative indexing starts from the end)

# Slicing allows extracting parts of a string.
print(text[0:5])   # Output: Hello (characters from index 0 to 4)
print(text[:5])    # Output: Hello (same as above)
print(text[7:])    # Output: World! (from index 7 to the end)
print(text[::2])   # Output: Hlo ol! (every second character)

# ===================================
# STRING METHODS
# ===================================

# Changing case
print(text.upper())    # HELLO, WORLD!
print(text.lower())    # hello, world!
print(text.title())    # Hello, World!
print(text.capitalize())  # Hello, world!

# Removing whitespace
trimmed = "  Hello  ".strip()  # Removes leading and trailing spaces
print(trimmed)  # Output: Hello

# Replacing characters
new_text = text.replace("World", "Python")
print(new_text)  # Output: Hello, Python!

# Splitting and joining
words = "apple,banana,orange".split(",")  # Converts string to list
print(words)  # Output: ['apple', 'banana', 'orange']

joined = "-".join(words)  # Joins list into a string
print(joined)  # Output: apple-banana-orange

# Finding substrings
print(text.find("World"))  # Output: 7 (index where "World" starts)
print("Hello" in text)     # Output: True (checks if "Hello" exists)
print("Python" not in text)  # Output: True (checks if "Python" is absent)

# ===================================
# STRING FORMATTING
# ===================================

# f-strings (recommended)
name = "Bright"
age = 22
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Bright and I am 22 years old.

# format() method
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Bright and I am 22 years old.

# Old-style formatting
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Bright and I am 22 years old.

# ===================================
# ESCAPE SEQUENCES
# ===================================

# Escape sequences allow special characters inside strings.
print("He said, \"Hello!\"")  # Output: He said, "Hello!"
print("Line 1\nLine 2")       # Output: Line 1 (new line) Line 2
print("Tab\tSpace")           # Output: Tab    Space
print("Backslash: \\")        # Output: Backslash: \

# ===================================
# STRING CONCATENATION & REPLICATION
# ===================================

# Joining strings
greeting = "Hello" + " " + "Bright!"
print(greeting)  # Output: Hello Bright!

# Repeating strings
laugh = "Ha" * 3
print(laugh)  # Output: HaHaHa

# ===================================
# SUMMARY
# ===================================
# - Strings are indexed and can be sliced.
# - Useful methods: upper(), lower(), replace(), strip(), split(), join().
# - Use f-strings or format() for string formatting.
# - Escape sequences help include special characters.
# - Strings can be concatenated (+) and repeated (*).
