
import jwt

def is_valid_jwt(token):
    try:
        decoded_token = jwt.decode(token, algorithms=["HS256"])
    except jwt.exceptions.InvalidTokenError:
        return False
    return True

# Example usage
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
if is_valid_jwt(jwt_token):
    print("Valid JWT")
else:
    print("Invalid JWT")
