
class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)

    def view_posts(self):
        for post in self.posts:
            print(post)

# Main program
platform = SocialMediaPlatform()

while True:
    print("\n1. Create Post")
    print("2. View Posts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        content = input("Enter your post content: ")
        platform.create_post(content)
        print("Post created successfully!")
    elif choice == "2":
        platform.view_posts()
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
