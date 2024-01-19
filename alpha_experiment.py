
import random
import string

def generate_password(length):
    # Define the possible characters to include in the password
    chars = string.ascii_letters + string.digits

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

# Prompt the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Random alphanumeric password:", password)
