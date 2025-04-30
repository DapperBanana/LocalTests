
class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, content):
        self.posts.append(content)
        
    def display_posts(self):
        if len(self.posts) == 0:
            print("No posts available.")
        else:
            for post in self.posts:
                print(post)

# Creating an instance of SocialMediaPlatform
social_media = SocialMediaPlatform()

# Main loop for the social media platform
while True:
    print("\n1. Create a new post")
    print("2. Display posts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        content = input("Enter your post content: ")
        social_media.create_post(content)
        print("Post created successfully.")
        
    elif choice == "2":
        print("\nPosts:")
        social_media.display_posts()
        
    elif choice == "3":
        print("Exiting social media platform.")
        break
    
    else:
        print("Invalid choice. Please try again.")
