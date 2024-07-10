
class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.posts = []

    def add_user(self, username):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
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

    def view_timeline(self, username):
        if username not in self.users:
            print("User does not exist. Please create an account first.")
        else:
            timeline = self.users[username]
            for post in timeline:
                print(f"{post['username']}: {post['content']}")

# Main function to interact with the social media platform
def main():
    platform = SocialMediaPlatform()

    while True:
        print("\n1. Create a user\n2. Create a post\n3. View timeline\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            platform.add_user(username)
        elif choice == '2':
            username = input("Enter your username: ")
            post_content = input("Enter post content: ")
            platform.create_post(username, post_content)
        elif choice == '3':
            username = input("Enter your username: ")
            platform.view_timeline(username)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
