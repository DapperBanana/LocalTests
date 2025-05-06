
class SocialMedia:
    def __init__(self):
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)

    def view_posts(self):
        for post in self.posts:
            print(post)

    def menu(self):
        while True:
            print("\nSocial Media Platform")
            print("1. Create a post")
            print("2. View posts")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                content = input("Enter your post: ")
                self.create_post(content)
            elif choice == '2':
                self.view_posts()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    social_media = SocialMedia()
    social_media.menu()
