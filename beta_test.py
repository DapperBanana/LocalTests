
import random
import string

def generate_password(length):
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the length of the password: "))
print(f"Generated password: {generate_password(length)}")
