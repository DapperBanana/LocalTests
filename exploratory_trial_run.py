
class User:
    def __init__(self, username, bio):
        self.username = username
        self.bio = bio
        self.posts = []

    def create_post(self, post_content):
        self.posts.append(post_content)

    def view_posts(self):
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def create_user(self, username, bio):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            new_user = User(username, bio)
            self.users[username] = new_user

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            print("User not found.")

    def display_users(self):
        for username, user in self.users.items():
            print(f"Username: {username}, Bio: {user.bio}")

# Main code
social_media = SocialMediaPlatform()

while True:
    print("\n1. Create User")
    print("2. Create Post")
    print("3. View Posts")
    print("4. Display Users")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        bio = input("Enter bio: ")
        social_media.create_user(username, bio)
    elif choice == "2":
        username = input("Enter your username: ")
        user = social_media.get_user(username)
        if user:
            post_content = input("Enter post content: ")
            user.create_post(post_content)
    elif choice == "3":
        username = input("Enter your username: ")
        user = social_media.get_user(username)
        if user:
            user.view_posts()
    elif choice == "4":
        social_media.display_users()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting program.")
