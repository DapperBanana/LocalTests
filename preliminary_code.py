
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
    users = {}

    def create_user(self, username):
        self.users[username] = User(username)

    def get_user(self, username):
        return self.users.get(username)

# Main program
social_media_platform = SocialMediaPlatform()

while True:
    print("1. Create User")
    print("2. Create Post")
    print("3. View Posts")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        social_media_platform.create_user(username)
    elif choice == "2":
        username = input("Enter username: ")
        user = social_media_platform.get_user(username)
        if user:
            content = input("Enter post content: ")
            user.create_post(content)
        else:
            print("User not found.")
    elif choice == "3":
        username = input("Enter username: ")
        user = social_media_platform.get_user(username)
        if user:
            user.view_posts()
        else:
            print("User not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
