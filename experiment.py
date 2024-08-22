
class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, user, content):
        post = {
            'user': user,
            'content': content
        }
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            print(f"{post['user']}: {post['content']}")

# Create an instance of the SocialMediaPlatform class
social_media = SocialMediaPlatform()

while True:
    print("\n1. Create a post")
    print("2. Display posts")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user = input("Enter your username: ")
        content = input("Enter your post content: ")
        social_media.create_post(user, content)
        print("Post created successfully!")

    elif choice == '2':
        print("\nPosts:")
        social_media.display_posts()

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
