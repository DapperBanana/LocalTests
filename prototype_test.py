
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)

    def view_feed(self):
        print("Feed for", self.username)
        for post in self.posts:
            print(post)


def main():
    users = {}

    while True:
        print("\n1. Create a new user")
        print("2. Create a post")
        print("3. View feed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            users[username] = User(username)
            print(f"User {username} created successfully!")

        elif choice == "2":
            username = input("Enter your username: ")
            if username in users:
                content = input("Enter post content: ")
                users[username].create_post(content)
                print("Post created successfully!")
            else:
                print("User not found")

        elif choice == "3":
            username = input("Enter your username: ")
            if username in users:
                users[username].view_feed()
            else:
                print("User not found")

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
