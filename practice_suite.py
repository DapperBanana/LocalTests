
import jwt

def is_valid_jwt(token):
    try:
        jwt.decode(token, options={'verify_signature': False})
        return True
    except jwt.InvalidTokenError:
        return False

# Test the program
token = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJzdWIiOiAiYWRtaW4iLCAiaWF0IjogMTUxNjIzOTAyMn0."
print(is_valid_jwt(token))  # Output: True

invalid_token = "invalid_token"
print(is_valid_jwt(invalid_token))  # Output: False
