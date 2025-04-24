
class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.posts = []

    def create_user(self, username):
        if username in self.users:
            print("Username already exists. Please choose a different one.")
        else:
            self.users[username] = []
            print(f"User {username} created successfully.")

    def create_post(self, username, post_content):
        if username not in self.users:
            print("User does not exist. Please create an account first.")
        else:
            post = {"username": username, "content": post_content}
            self.posts.append(post)
            self.users[username].append(post)
            print("Post created successfully.")

    def view_feed(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                print(f"{post['username']}: {post['content']}")

def main():
    social_media = SocialMediaPlatform()

    while True:
        print("1. Create User")
        print("2. Create Post")
        print("3. View Feed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            social_media.create_user(username)
        elif choice == "2":
            username = input("Enter your username: ")
            post_content = input("Enter your post content: ")
            social_media.create_post(username, post_content)
        elif choice == "3":
            social_media.view_feed()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
