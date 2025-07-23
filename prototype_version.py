
class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.posts = []

    def create_user(self, username):
        if username in self.users:
            print("Username already exists. Please choose another one.")
        else:
            self.users[username] = []

    def create_post(self, username, post_content):
        if username not in self.users:
            print("User not found.")
        else:
            post = {"username": username, "content": post_content}
            self.posts.append(post)
            self.users[username].append(post)

    def view_timeline(self, username):
        if username not in self.users:
            print("User not found.")
        else:
            timeline = self.users[username]
            for post in timeline:
                print(f"{post['username']} said: {post['content']}")

if __name__ == "__main__":
    social_media_platform = SocialMediaPlatform()

    while True:
        print("\n1. Create user")
        print("2. Create post")
        print("3. View timeline")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            social_media_platform.create_user(username)
        elif choice == "2":
            username = input("Enter username: ")
            post_content = input("Enter post content: ")
            social_media_platform.create_post(username, post_content)
        elif choice == "3":
            username = input("Enter username: ")
            social_media_platform.view_timeline(username)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
