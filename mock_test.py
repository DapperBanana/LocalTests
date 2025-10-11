
class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = 0

    def like(self):
        self.likes += 1

    def display(self):
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")
        print(f"Likes: {self.likes}")


class SocialMediaPlatform:
    def __init__(self):
        self.posts = []

    def create_post(self, content, author):
        post = Post(content, author)
        self.posts.append(post)

    def display_posts(self):
        for post in self.posts:
            post.display()
            print()

    def like_post(self, author):
        for post in self.posts:
            if post.author == author:
                post.like()
                print(f"{author}'s post has been liked!")


# Create an instance of the social media platform
my_social_media = SocialMediaPlatform()

# Create some posts
my_social_media.create_post("Hello, world!", "Alice")
my_social_media.create_post("Python is awesome!", "Bob")
my_social_media.create_post("Looking for a coding partner.", "Alice")

# Display all posts
my_social_media.display_posts()

# Like a post
my_social_media.like_post("Alice")

# Display all posts after liking
my_social_media.display_posts()
