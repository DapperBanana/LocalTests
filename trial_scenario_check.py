
import jwt

def is_valid_jwt(jwt_string, secret_key):
    try:
        decoded = jwt.decode(jwt_string, secret_key, algorithms=['HS256'])
        return True
    except (jwt.DecodeError, jwt.InvalidSignatureError):
        return False

# Example usage
jwt_string = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
secret_key = "my-secret-key"

if is_valid_jwt(jwt_string, secret_key):
    print("The JWT is valid!")
else:
    print("The JWT is not valid.")
