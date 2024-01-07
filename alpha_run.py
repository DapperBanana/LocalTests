
import random
import string

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and print the random alphanumeric password
password = generate_password(length)
print("Random Alphanumeric Password:", password)
