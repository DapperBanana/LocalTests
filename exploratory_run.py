
import jwt

def verify_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

# Test the function
token1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlN0ZXBoZW4gRm9yY2VsZXgiLCJpYXQiOjE1MTYyMzkwMjJ9.3pAKW-o6QglohhtHt56gQsN4tmnvseYNTSVkDzN2rM8"
token2 = "notavalidtoken"

if verify_jwt(token1):
    print("Token 1 is a valid JWT.")
else:
    print("Token 1 is not a valid JWT.")

if verify_jwt(token2):
    print("Token 2 is a valid JWT.")
else:
    print("Token 2 is not a valid JWT.")
