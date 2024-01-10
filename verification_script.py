
class User:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def display_name(self):
        print("Username: ", self.name)

    def display_friends(self):
        print("Friends: ")
        for friend in self.friends:
            print("-", friend.name)


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_post(self):
        print("Author: ", self.author.name)
        print("Content: ", self.content)
        print("Comments: ")
        for comment in self.comments:
            print("-", comment)


class Comment:
    def __init__(self, author, content):
        self.author = author
        self.content = content

    def display_comment(self):
        print("Author: ", self.author.name)
        print("Content: ", self.content)


if __name__ == "__main__":
    # Create users
    user1 = User("User1")
    user2 = User("User2")
    user3 = User("User3")

    # Connect friends
    user1.add_friend(user2)
    user1.add_friend(user3)

    # Create a post
    post = Post(user1, "Hello, friends!")

    # Add comments
    comment1 = Comment(user2, "Hi!")
    comment2 = Comment(user3, "Hey there!")
    post.add_comment(comment1)
    post.add_comment(comment2)

    # Display post and comments
    post.display_post()
    comment1.display_comment()
    comment2.display_comment()

    # Display user's friends
    user1.display_friends()
    user2.display_friends()
    user3.display_friends()
