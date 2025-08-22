
import jwt
import json

def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.InvalidTokenError:
        return False

# Test the function with some example JWTs
jwt_token1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
jwt_token2 = "notavalidjwt"

if is_valid_jwt(jwt_token1):
    print("JWT token 1 is valid")
else:
    print("JWT token 1 is invalid")

if is_valid_jwt(jwt_token2):
    print("JWT token 2 is valid")
else:
    print("JWT token 2 is invalid")
