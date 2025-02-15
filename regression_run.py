
class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content

class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, author, content):
        post = Post(author, content)
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            print(f"{post.author}: {post.content}")

# Main program
social_media = SocialMediaPlatform()

while True:
    print("\n1. Create post\n2. Display posts\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        author = input("Enter your name: ")
        content = input("Enter your post content: ")
        social_media.create_post(author, content)
    elif choice == '2':
        social_media.display_posts()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the social media platform!")
