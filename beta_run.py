
import jwt

# Function to check if a given string is a valid JWT
def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.exceptions.DecodeError:
        return False

# Input string to check
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Check if the input string is a valid JWT
if is_valid_jwt(token):
    print("The input string is a valid JWT.")
else:
    print("The input string is not a valid JWT.")
