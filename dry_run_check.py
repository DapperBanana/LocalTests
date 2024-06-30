
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)

    def view_timeline(self):
        print(f"Timeline for {self.username}:")
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
    
    def create_user(self, username):
        user = User(username)
        self.users[username] = user
        print(f"User {username} has been created")
    
    def get_user(self, username):
        return self.users.get(username)

    def follow_user(self, follower, following):
        follower_user = self.get_user(follower)
        following_user = self.get_user(following)

        if follower_user and following_user:
            print(f"{follower} is now following {following}")
        else:
            print("User does not exist")

    def post_to_user(self, username, content):
        user = self.get_user(username)
        if user:
            user.create_post(content)
            print(f"Posted {content} to {username}'s timeline")
        else:
            print("User does not exist")

    def view_timeline(self, username):
        user = self.get_user(username)
        if user:
            user.view_timeline()
        else:
            print("User does not exist")


# Usage
social_media = SocialMediaPlatform()

social_media.create_user("Alice")
social_media.create_user("Bob")

social_media.post_to_user("Alice", "Hello world!")
social_media.post_to_user("Bob", "I am having a great day!")

social_media.follow_user("Alice", "Bob")

social_media.post_to_user("Bob", "Just posted a new photo!")
social_media.view_timeline("Alice")
social_media.view_timeline("Bob")
