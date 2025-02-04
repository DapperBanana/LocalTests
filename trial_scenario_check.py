
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)

    def view_posts(self):
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def display_users(self):
        for user in self.users:
            print(user.name)

    def display_user_posts(self, user_name):
        for user in self.users:
            if user.name == user_name:
                user.view_posts()

# Create users
user1 = User("Alice", 25)
user2 = User("Bob", 30)

# Create social media platform
social_media = SocialMediaPlatform()

# Add users to the platform
social_media.add_user(user1)
social_media.add_user(user2)

# User 1 creates a post
user1.create_post("Hello, this is my first post!")

# User 2 creates a post
user2.create_post("Just chilling on a Saturday afternoon.")

# Display all users on the platform
social_media.display_users()

# Display posts of a specific user
social_media.display_user_posts("Alice")
