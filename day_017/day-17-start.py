class User:
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"{self.username} is now following {user.username}")

user1 = User("001", "calau")

print(user1.username)
print(user1.followers)

user2 = User("002", "grifflau")

print(user2.username)

user3 = User("003", "curtlau")
print(user3.username)

print(f"{user1.username} has {user1.followers} followers")
print(f"{user3.username} has {user3.followers} followers")

user1.follow(user3)

print(f"{user1.username} has {user1.followers} followers")
print(f"{user3.username} has {user3.followers} followers")