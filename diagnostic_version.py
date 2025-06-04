
class User:
    def __init__(self, name):
        self.name = name
        self.posts = []
    
    def create_post(self, content):
        self.posts.append(content)
    
    def view_timeline(self):
        print("Timeline for " + self.name)
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = []
    
    def create_user(self, name):
        new_user = User(name)
        self.users.append(new_user)
    
    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

# Create a social media platform
platform = SocialMediaPlatform()

# Create users
platform.create_user("Alice")
platform.create_user("Bob")

# Alice creates a post
alice = platform.get_user("Alice")
alice.create_post("Hello, I'm Alice!")

# Bob creates a post
bob = platform.get_user("Bob")
bob.create_post("Hi there, I'm Bob!")

# View Alice's timeline
alice.view_timeline()

# View Bob's timeline
bob.view_timeline()
