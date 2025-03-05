# ---------------- Day 9: Dictionaries and Nesting ----------------

# Dictionaries store key-value pairs
student_scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}

# Accessing values
print(student_scores["Alice"])  # Output: 90

# Adding new key-value pairs
student_scores["David"] = 88

# Modifying values
student_scores["Bob"] = 89

# Looping through a dictionary
for student in student_scores:
    print(f"{student}: {student_scores[student]}")

# ---------------- Nesting ----------------

# Dictionary inside a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon", "Nice"], "total_visits": 5},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 3}
}

# Accessing nested values
print(travel_log["France"]["cities_visited"])  # Output: ['Paris', 'Lyon', 'Nice']
print(travel_log["Germany"]["cities_visited"][1])

# Dictionary inside a list
travel_log_list = [
    {"country": "France", "cities_visited": ["Paris", "Lyon", "Nice"], "total_visits": 5},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg"], "total_visits": 3}
]

# Accessing data inside a list of dictionaries
print(travel_log_list[0]["country"])
print(travel_log_list[1]["total_visits"])
