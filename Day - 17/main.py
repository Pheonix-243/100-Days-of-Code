
# ----------------------------
# Creating a Class in Python
# ----------------------------

# A class be like a blueprint (plan) for creating objects.
# Objects be instances of a class (they follow the structure of the class).
# Example: A "User" class fit be a template for creating different users.

class User:  # Define a class named "User"
    # The __init__ method is a constructor (it initializes attributes).
    # It runs automatically whenever a new object is created from the class.

    def __init__(self, user_id, user_name):
        # The 'self' parameter refers to the specific object being created.
        # 'user_id' be a parameter that we go pass when creating a user.

        self.id = user_id
        self.name = user_name
        self.followers = []
        self.following = []

    def follow(self,user_two):
        self.following.append(user_two)
    def unfollow(self, user_two):



user_1 = User(34, "Bright")
user_1 = User(35, "Elsi")


print(user_1)
print(user_1.id)
print(user_1.name)

