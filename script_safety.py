
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, verify=False)
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

# Test the function
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.2vaMcW6e57i6dg9HYOW3-strinGToKEn_TpHITTadQw"
print(is_valid_jwt(token))
