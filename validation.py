
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

# Example usage
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
if is_valid_jwt(token):
    print("Valid JWT")
else:
    print("Invalid JWT")
