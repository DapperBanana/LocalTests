
import random
import string

def generate_password(length):
    # Define the possible characters
    characters = string.ascii_letters + string.digits
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get the desired password length from the user
length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Generated password:", password)
