
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, message):
        self.posts.append(message)

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        self.users[username] = User(username)

    def follow_user(self, follower_username, following_username):
        self.users[follower_username].following = self.users.get(follower_username, []).append(self.users[following_username])

    def view_timeline(self, username):
        following_users = self.users[username].following
        timeline_posts = []
        for user in following_users:
            timeline_posts.extend(user.posts)
        return timeline_posts

# Sample Usage
social_media = SocialMediaPlatform()

social_media.create_user("user1")
social_media.create_user("user2")
social_media.create_user("user3")

social_media.follow_user("user1", "user2")
social_media.follow_user("user1", "user3")

social_media.users["user1"].create_post("Hello from user1!")
social_media.users["user2"].create_post("Hello from user2!")
social_media.users["user3"].create_post("Hello from user3!")

print(social_media.view_timeline("user1"))
