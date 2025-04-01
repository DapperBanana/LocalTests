
import random
import string

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password:", generate_password(length))
