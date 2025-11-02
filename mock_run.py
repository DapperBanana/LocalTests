
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
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        self.users[username] = User(username)

    def get_user(self, username):
        return self.users.get(username)

    def display_menu(self):
        print("Welcome to the Social Media Platform!")
        print("1. Create User")
        print("2. Create Post")
        print("3. View Posts")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                self.create_user(username)
            elif choice == "2":
                username = input("Enter your username: ")
                user = self.get_user(username)
                if user:
                    content = input("Enter post content: ")
                    user.create_post(content)
                else:
                    print("User not found.")
            elif choice == "3":
                username = input("Enter username: ")
                user = self.get_user(username)
                if user:
                    print(f"Posts by {username}:")
                    user.view_posts()
                else:
                    print("User not found.")
            elif choice == "4":
                print("Thank you for using the Social Media Platform!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    platform = SocialMediaPlatform()
    platform.run()
