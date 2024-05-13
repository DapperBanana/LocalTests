
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)

    def view_posts(self):
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        if username in self.users:
            print("Username already in use")
        else:
            self.users[username] = User(username)

    def get_user(self, username):
        return self.users.get(username)

# Create a social media platform instance
platform = SocialMediaPlatform()

# Create users
platform.create_user("Alice")
platform.create_user("Bob")

# Users create posts
alice = platform.get_user("Alice")
alice.create_post("Hello, this is my first post!")

bob = platform.get_user("Bob")
bob.create_post("Excited to join this social media platform!")

# View posts
alice.view_posts()
bob.view_posts()
