
class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)
        print("Post created successfully!")
    
    def view_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                print(post)

    def menu(self):
        while True:
            print("\n1. Create a post")
            print("2. View posts")
            print("3. Quit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                content = input("Enter your post content: ")
                self.create_post(content)
            elif choice == "2":
                self.view_posts()
            elif choice == "3":
                print("Exiting the social media platform. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

social_media = SocialMediaPlatform()
social_media.menu()
