
class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, user, content):
        post = {"user": user, "content": content}
        self.posts.append(post)

    def show_posts(self):
        for post in self.posts:
            print(f"{post['user']}: {post['content']}")

    def run(self):
        print("Welcome to our Social Media Platform!")
        while True:
            print("\nMenu:")
            print("1. Create a post")
            print("2. Show posts")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                user = input("Enter your username: ")
                content = input("Enter your post content: ")
                self.create_post(user, content)
            elif choice == "2":
                self.show_posts()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

social_media = SocialMediaPlatform()
social_media.run()
