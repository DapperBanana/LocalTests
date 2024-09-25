
class User:
    def __init__(self, username):
        self.username = username
        self.following = []
        self.posts = []

    def follow(self, user):
        self.following.append(user)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)

    def post(self, message):
        self.posts.append(message)

    def timeline(self):
        timeline_posts = []
        for user in self.following:
            timeline_posts.extend(user.posts)
        return timeline_posts

# Create users
user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")

# Alice follows Bob and Charlie
user1.follow(user2)
user1.follow(user3)

# Bob posts a message
user2.post("Hello from Bob!")

# Charlie posts a message
user3.post("Hi there from Charlie!")

# Alice posts a message
user1.post("Hey everyone, it's Alice!")

# Alice can see posts from users she follows
timeline = user1.timeline()
for post in timeline:
    print(post)
