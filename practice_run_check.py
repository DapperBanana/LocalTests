
class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
    
    def create_user(self, username):
        if username in self.users:
            print("Username already exists. Please choose another one.")
        else:
            self.users[username] = []
            print(f"User '{username}' created successfully!")
    
    def post_message(self, username, message):
        if username in self.users:
            self.users[username].append(message)
            print(f"Message posted by '{username}': {message}")
        else:
            print(f"User '{username}' not found. Please create a user first.")
    
    def view_messages(self, username):
        if username in self.users:
            messages = self.users[username]
            print(f"Messages posted by '{username}':")
            for message in messages:
                print(f"- {message}")
        else:
            print(f"User '{username}' not found. Please create a user first.")

# Main Program
social_media = SocialMediaPlatform()
while True:
    print("\n1. Create User\n2. Post Message\n3. View Messages\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        social_media.create_user(username)
    elif choice == "2":
        username = input("Enter username: ")
        message = input("Enter message: ")
        social_media.post_message(username, message)
    elif choice == "3":
        username = input("Enter username: ")
        social_media.view_messages(username)
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
