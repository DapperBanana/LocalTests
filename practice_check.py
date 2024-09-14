
class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content

class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, username, content):
        post = Post(username, content)
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            print(f"{post.username}: {post.content}")

def main():
    social_media_platform = SocialMediaPlatform()

    while True:
        print("\n1. Create a post")
        print("2. Display posts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            content = input("Enter post content: ")
            social_media_platform.create_post(username, content)
            print("Post created!")
        elif choice == '2':
            social_media_platform.display_posts()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
