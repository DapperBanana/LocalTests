
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get password length from user
length = int(input("Enter the length of the password: "))

# Generate password
password = generate_password(length)
print("Random alphanumeric password:", password)
