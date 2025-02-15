
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, text):
        self.posts.append(text)
        print(f"{self.username} created a new post: {text}")

    def view_timeline(self):
        print(f"{self.username}'s Timeline:")
        for post in self.posts:
            print(post)

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        self.users[username] = User(username)
        print(f"Welcome, {username}!")

    def get_user(self, username):
        return self.users.get(username)

def main():
    social_media = SocialMediaPlatform()

    while True:
        print("\n1. Create User\n2. Create Post\n3. View Timeline\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            social_media.create_user(username)
        elif choice == "2":
            username = input("Enter your username: ")
            user = social_media.get_user(username)
            if user:
                text = input("Enter your post: ")
                user.create_post(text)
            else:
                print("User does not exist")
        elif choice == "3":
            username = input("Enter your username: ")
            user = social_media.get_user(username)
            if user:
                user.view_timeline()
            else:
                print("User does not exist")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
