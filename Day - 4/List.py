# Python Lists – A Comprehensive Guide
# Introduction
# A list in Python is a built-in data structure that allows you to store multiple items in a single variable. Lists are ordered, mutable, and allow duplicate values. They can contain elements of different data types, including integers, strings, floats, and even other lists.


# The order in which they are stored matters very much!
# List are mutable







# ==============================
# 🛠️ Python List Methods Reference 🛠️
# ==============================

# 📌 Creating a list
my_list = [1, 2, 3, 4, 5]

# ==============================
# 🔹 1. Adding Elements
# ==============================
my_list.append(6)        # Adds 6 to the end -> [1, 2, 3, 4, 5, 6]
my_list.insert(2, 99)    # Inserts 99 at index 2 -> [1, 2, 99, 3, 4, 5, 6]
my_list.extend([7, 8])   # Adds multiple elements -> [1, 2, 99, 3, 4, 5, 6, 7, 8]

# ==============================
# 🔹 2. Removing Elements
# ==============================
my_list.pop()            # Removes last item (8) -> [1, 2, 99, 3, 4, 5, 6, 7]
my_list.pop(2)           # Removes item at index 2 (99) -> [1, 2, 3, 4, 5, 6, 7]
my_list.remove(3)        # Removes first occurrence of 3 -> [1, 2, 4, 5, 6, 7]
my_list.clear()          # Removes all elements -> []

# ==============================
# 🔹 3. Searching & Counting
# ==============================
my_list = [10, 20, 30, 20, 40, 50]
index = my_list.index(20)  # Returns index of first occurrence of 20 (1)
count = my_list.count(20)  # Counts occurrences of 20 (2)

# ==============================
# 🔹 4. Sorting & Reversing
# ==============================
nums = [5, 3, 8, 1, 2]
nums.sort()             # Sorts in ascending order -> [1, 2, 3, 5, 8]
nums.sort(reverse=True) # Sorts in descending order -> [8, 5, 3, 2, 1]
nums.reverse()          # Reverses the order -> [1, 2, 3, 5, 8]

# ==============================
# 🔹 5. Copying Lists
# ==============================
original = [1, 2, 3]
copy_list = original.copy()  # Creates a copy of the list

# ==============================
# 🔹 6. List Comprehensions
# ==============================
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# ==============================
# 🔹 7. Joining & Splitting Strings
# ==============================
words = ["Hello", "World"]
sentence = " ".join(words)  # "Hello World"
split_list = "Python,Java,JavaScript".split(",")  # ['Python', 'Java', 'JavaScript']

# ==============================
# 🔹 8. Checking if an Item Exists
# ==============================
my_list = [10, 20, 30, 40]
exists = 20 in my_list   # True
not_exists = 50 not in my_list  # True

# ==============================
# 🔹 9. Getting the Length of a List
# ==============================
length = len(my_list)  # 4



states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)



states_of_america.append("Ghana")

print(states_of_america[-1])

states_of_america.extend(["Sola","Daka"])

print(states_of_america[-1])





# Nested List
# It is basically a list within a list ; a list of lists

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples"]
vegetables = ["Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits,vegetables]

print(dirty_dozen)