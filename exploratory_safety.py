
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

class SocialMediaPlatform:
    def __init__(self):
        self.users = []

    def create_user(self, username):
        user = User(username)
        self.users.append(user)

    def create_post(self, username, content):
        for user in self.users:
            if user.username == username:
                user.posts.append(content)
                print(f"{username} posted: {content}")
                return
        print(f"User {username} not found.")

    def view_timeline(self, username):
        for user in self.users:
            if user.username == username:
                print(f"{username}'s timeline:")
                for post in user.posts:
                    print(post)
                return
        print(f"User {username} not found.")

if __name__ == "__main__":
    social_media = SocialMediaPlatform()

    social_media.create_user("Alice")
    social_media.create_user("Bob")

    social_media.create_post("Alice", "Hello, world!")
    social_media.create_post("Bob", "Python is awesome!")

    social_media.view_timeline("Alice")
    social_media.view_timeline("Bob")
    social_media.view_timeline("Charlie")  # User not found
