
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

# Input token to check
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJKb2huIiwibmFtZSI6IkdvbGQifQ.DqdqFMK8anJ9FTbMvlmwF3Sh21-0HBl0Sai9B6Amxbg"

if is_valid_jwt(token):
    print("The token is a valid JSON Web Token (JWT).")
else:
    print("The token is not a valid JSON Web Token (JWT).")
