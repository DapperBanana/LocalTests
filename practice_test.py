
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.InvalidTokenError:
        return False

# Test the function with a sample token
sample_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
result = is_valid_jwt(sample_token)

if result:
    print("The provided token is a valid JSON Web Token.")
else:
    print("The provided token is not a valid JSON Web Token.")
