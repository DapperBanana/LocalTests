
import random

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, post_content):
        self.posts.append(post_content)

    def view_timeline(self):
        print("\nTimeline for " + self.username + ":")
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = []

    def create_user(self, username):
        user = User(username)
        self.users.append(user)
        print("User " + username + " has been created.")

    def get_random_user(self):
        return random.choice(self.users)

    def run(self):
        while True:
            print("\n1. Create User")
            print("2. Create Post")
            print("3. View Timeline")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                self.create_user(username)
            elif choice == "2":
                user = self.get_random_user()
                post_content = input("Enter your post: ")
                user.create_post(post_content)
                print("Post created by " + user.username)
            elif choice == "3":
                user = self.get_random_user()
                user.view_timeline()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    social_media_platform = SocialMediaPlatform()
    social_media_platform.run()
