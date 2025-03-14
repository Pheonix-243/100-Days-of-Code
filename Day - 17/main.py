class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = []
        self.following = []

    def follow(self, user_two):
        if user_two not in self.following:
            self.following.append(user_two)
            user_two.followers.append(self)

    def unfollow(self, user_two):
        if user_two in self.following:
            self.following.remove(user_two)
            user_two.followers.remove(self)

    def num_followers(self):
        return len(self.followers)

    def num_following(self):
        return len(self.following)


user_1 = User(34, "Brightoo")
user_2 = User(35, "Elsi")
user_3 = User(32,"Albert")

user_2.follow(user_1)
user_3.follow(user_1)
user_2.unfollow(user_1)

print(user_1.name, "is following", user_1.num_following(), "users.")
print(user_2.name, "has", user_2.num_followers(), "followers.")

print(user_1.num_followers())

print(user_1.followers)
